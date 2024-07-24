param location string = 'eastus'
param resourceGroupName string = 'skytap-landing-zone'
param storageAccountName string = 'skytapsa0021'

@allowed([
  'new'
  'existing'
])
param newOrExisting string = 'existing'

param vnetName string = 'skytap-vnet'
param localNetworkGatewayName string = 'skytap-LocalNetworkGateway'
param vnetGatewayName string = 'skytap-virtualNetworkGateway'
param gatewayPublicIPName string = 'gtwyPublicIP'
param privateEndpointName string = 'storagePrivateEndpoint'
param vnetAddressPrefix string = '10.0.0.0/16'
param subnet1AddressPrefix string = '10.0.1.0/24'
param subnet2AddressPrefix string = '10.0.2.0/24'

@description('ExpressRoute Gateway SKU')
@allowed([
  'Standard'
  'HighPerformance'
  'UltraPerformance'
  'ErGw1AZ'
  'ErGw2AZ'
  'ErGw3AZ'
])
param gatewaySku string = 'Standard'

//params for the Virtual Machine
@description('Username for the Virtual Machine.')
param adminUsername string = 'azureuser'

@description('Password for the Virtual Machine.')
@minLength(12)
@secure()
param adminPassword string = 'Azuretest01!!'

@description('Unique DNS Name for the Public IP used to access the Virtual Machine.')
param dnsLabelPrefix string = toLower('${vmName}-${uniqueString(resourceGroup().id, vmName)}')

@description('Name for the Public IP used to access the Virtual Machine.')
param vmPublicIpName string = 'vmPublicIP'

@description('Allocation method for the Public IP used to access the Virtual Machine.')
@allowed([
  'Dynamic'
  'Static'
])
param vmPublicIPAllocationMethod string = 'Dynamic'

@description('SKU for the Public IP used to access the Virtual Machine.')
@allowed([
  'Basic'
  'Standard'
])
param vmPublicIpSku string = 'Basic'

@description('The Windows version for the VM. This will pick a fully patched image of this given Windows version.')
@allowed([
  '2022-datacenter-azure-edition'
  '2022-datacenter-azure-edition-core'
  '2022-datacenter-azure-edition-core-smalldisk'
  '2022-datacenter-azure-edition-smalldisk'
  '2022-datacenter-core-g2'
  '2022-datacenter-core-smalldisk-g2'
  '2022-datacenter-g2'
  '2022-datacenter-smalldisk-g2'
])
param OSVersion string = '2022-datacenter-azure-edition'
param osDiskType string = 'Premium_LRS'
param dataDiskSizeGB int = 10240
param dataDiskType string = 'Premium_LRS'

@description('Size of the virtual machine.')
param vmSize string = 'Standard_D16s_v5'

@description('Name of the virtual machine.')
param vmName string = 'jumpbox-vm'

@description('Security Type of the Virtual Machine.')
@allowed([
  'Standard'
  'TrustedLaunch'
])
param securityType string = 'TrustedLaunch'

var storageAccountNameBootDiagnostics = 'bootdiags${uniqueString(resourceGroup().id)}'
var nicName = 'vmNic'
var networkSecurityGroupName = 'default-NSG'
var securityProfileJson = {
  uefiSettings: {
    secureBootEnabled: true
    vTpmEnabled: true
  }
  securityType: securityType
}
var extensionName = 'AzCopyInstaller'
var extensionPublisher = 'Microsoft.Compute'
var extensionVersion = '1.0'

resource vnet 'Microsoft.Network/virtualNetworks@2021-02-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [
        vnetAddressPrefix
      ]
    }
  }
}

resource subnet1 'Microsoft.Network/virtualNetworks/subnets@2020-06-01' = {
  parent: vnet
  name: 'GatewaySubnet'
  properties: {
    addressPrefix: subnet1AddressPrefix
  }
}

resource subnet2 'Microsoft.Network/virtualNetworks/subnets@2020-06-01' = {
  parent: vnet
  name: 'subnet2'
  properties: {
    addressPrefix: subnet2AddressPrefix
    networkSecurityGroup: {
      id: networkSecurityGroup.id
    }
  }
}

resource localNetworkGateway 'Microsoft.Network/localNetworkGateways@2021-02-01' = {
  name: localNetworkGatewayName
  location: location
  properties: {
    localNetworkAddressSpace: {
      addressPrefixes: [
        '192.168.0.0/16'
      ]
    }
    gatewayIpAddress: '192.168.0.1'
  }
}

resource gatewayPublicIP 'Microsoft.Network/publicIPAddresses@2023-09-01' = {
  name: gatewayPublicIPName
  location: location
  sku: {
    name: 'Standard'
    tier: 'Regional'
  }
  properties: {
    publicIPAllocationMethod: 'Static'
  }
}

resource vnetGateway 'Microsoft.Network/virtualNetworkGateways@2023-09-01' = {
  name: vnetGatewayName
  location: location
  properties: {
    ipConfigurations: [
      {
        properties: {
          privateIPAllocationMethod: 'Dynamic'
          subnet: {
            id: resourceId('Microsoft.Network/virtualNetworks/subnets', vnetName, 'GatewaySubnet')
          }
          publicIPAddress: {
            id: gatewayPublicIP.id
          }
        }
        name: 'gwIPconf'
      }
    ]
    gatewayType: 'ExpressRoute'
    sku: {
      name: gatewaySku
      tier: gatewaySku
    }
    vpnType: 'RouteBased'
  }
  dependsOn: [
    subnet1
    gatewayPublicIP
    vm
  ]
}

// Storage account conditional creation
resource saNew 'Microsoft.Storage/storageAccounts@2022-09-01' = if (newOrExisting == 'new') {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

resource saExisting 'Microsoft.Storage/storageAccounts@2022-09-01' existing = if (newOrExisting == 'existing') {
  name: storageAccountName
}

resource privateEndpoint 'Microsoft.Network/privateEndpoints@2021-02-01' = {
  name: privateEndpointName
  location: location
  properties: {
    subnet: {
      id: subnet2.id
    }
    privateLinkServiceConnections: [
      {
        name: 'myPrivateLinkServiceConnection'
        properties: {
          privateLinkServiceId: (newOrExisting == 'new') ? saNew.id : saExisting.id
          groupIds: [
            'blob'
          ]
        }
      }
    ]
  }
  dependsOn: [
    saNew
  ]
}

resource storageAccountBootDiagnostics 'Microsoft.Storage/storageAccounts@2022-05-01' = {
  name: storageAccountNameBootDiagnostics
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'Storage'
}

resource vmPublicIp 'Microsoft.Network/publicIPAddresses@2022-05-01' = {
  name: vmPublicIpName
  location: location
  sku: {
    name: vmPublicIpSku
  }
  properties: {
    publicIPAllocationMethod: vmPublicIPAllocationMethod
    dnsSettings: {
      domainNameLabel: dnsLabelPrefix
    }
  }
}

resource networkSecurityGroup 'Microsoft.Network/networkSecurityGroups@2022-05-01' = {
  name: networkSecurityGroupName
  location: location
  properties: {
    securityRules: [
      {
        name: 'default-allow-3389'
        properties: {
          priority: 1000
          access: 'Allow'
          direction: 'Inbound'
          destinationPortRange: '3389'
          protocol: 'Tcp'
          sourcePortRange: '*'
          sourceAddressPrefix: '*'
          destinationAddressPrefix: '*'
        }
      }
    ]
  }
}

resource nic 'Microsoft.Network/networkInterfaces@2022-05-01' = {
  name: nicName
  location: location
  properties: {
    ipConfigurations: [
      {
        name: 'ipconfig1'
        properties: {
          privateIPAllocationMethod: 'Dynamic'
          publicIPAddress: {
            id: vmPublicIp.id
          }
          subnet: {
            id: subnet2.id   
              }
        }
      }
    ]
    enableAcceleratedNetworking: true
  }
  dependsOn: [
    subnet2
  ]
}

resource vm 'Microsoft.Compute/virtualMachines@2022-03-01' = {
  name: vmName
  location: location
  properties: {
    hardwareProfile: {
      vmSize: vmSize
    }
    osProfile: {
      computerName: vmName
      adminUsername: adminUsername
      adminPassword: adminPassword
    }
    storageProfile: {
      imageReference: {
        publisher: 'MicrosoftWindowsServer'
        offer: 'WindowsServer'
        sku: OSVersion
        version: 'latest'
      }
      osDisk: {
        createOption: 'FromImage'
        managedDisk: {
          storageAccountType: osDiskType
        }
      }
      dataDisks: [
        {
          lun: 0
          createOption: 'Empty'
          diskSizeGB: dataDiskSizeGB
          managedDisk: {
            storageAccountType: dataDiskType
          }
        }
      ]
    }
    networkProfile: {
      networkInterfaces: [
        {
          id: nic.id
        }
      ]
    }
    diagnosticsProfile: {
      bootDiagnostics: {
        enabled: true
        storageUri: storageAccountBootDiagnostics.properties.primaryEndpoints.blob
      }
    }
    securityProfile: ((securityType == 'TrustedLaunch') ? securityProfileJson : null)
  }
  dependsOn: [
    nic
    storageAccountBootDiagnostics
  ]
}

resource vmExtension 'Microsoft.Compute/virtualMachines/extensions@2022-03-01' =  {
  parent: vm
  name: extensionName
  location: location
  properties: {
    publisher: extensionPublisher
    type: 'CustomScriptExtension'
    typeHandlerVersion: extensionVersion
    autoUpgradeMinorVersion: false
    enableAutomaticUpgrade: false
    settings: {
      fileUris: [
        'https://aka.ms/downloadazcopy-v10-windows'
      ]
      commandToExecute: 'powershell -Command "Invoke-WebRequest -Uri https://aka.ms/downloadazcopy-v10-windows -OutFile azcopy.zip; Expand-Archive -Path azcopy.zip -DestinationPath .; Move-Item -Path .\\azcopy_windows_amd64_*/azcopy.exe -Destination C:\\Windows\\System32\\azcopy.exe; Remove-Item -Recurse -Force .\\azcopy_windows_amd64_*, azcopy.zip"'
    }
  }
}

output hostname string = vmPublicIp.properties.dnsSettings.fqdn
output storageAccountId string = ((newOrExisting == 'new') ? saNew.id : saExisting.id)
