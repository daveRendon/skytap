using './main.bicep'

param location = 'eastus'
param resourceGroupName = 'skytap-landing-zone'
param storageAccountName = 'skytapsa0021' //UPDATE THIS TO YOUR STORAGE ACCOUNT NAME
param newOrExisting = 'new' // allowed values: 'new', 'existing' for the Storage acccount that will host the Mksysb
param vnetName = 'skytap-vnet'
param localNetworkGatewayName = 'skytap-localNetGateway'
param vnetGatewayName = 'skytap-vnetGateway'
param gatewayPublicIPName = 'gtwyPublicIP'
param privateEndpointName = 'storagePrivateEndpoint'
param vnetAddressPrefix = '10.0.0.0/16'
param subnet1AddressPrefix = '10.0.1.0/24'
param subnet2AddressPrefix = '10.0.2.0/24'
param gatewaySku = 'Standard'
param adminUsername = 'azureuser'
param adminPassword = 'Azuretest01!!'
param vmPublicIpName = 'vmPublicIP'
param vmPublicIPAllocationMethod = 'Dynamic'
param vmPublicIpSku = 'Basic'
param OSVersion = '2022-datacenter-azure-edition'
param osDiskType = 'Premium_LRS'
param dataDiskSizeGB = 10240
param dataDiskType = 'Premium_LRS'
param vmSize = 'Standard_D16s_v5'
param vmName = 'jumpbox-vm'
param securityType = 'TrustedLaunch'

