# Sktap AIX Landing Zone 

This Bicep file specifies the configuration of a set of Azure resources, including a Virtual Network, Virtual Machines, and associated components. Here's a breakdown of the key components and their purpose:

1. **Parameters**:
   - Define values like location, resource group name, storage account name, and more.
   - Parameters include `newOrExisting`, which determines whether a new or existing storage account is used.
   - The template also includes settings for the virtual machine, such as the admin username, password, DNS label, VM size, and security type.

2. **Resources**:
   - **Virtual Network (vnet)**: Creates a virtual network with specified address space.
   - **Subnets (subnet1, subnet2)**: Defines subnets within the virtual network, including a GatewaySubnet and another subnet with an associated network security group.
   - **Local Network Gateway**: Sets up a local network gateway with specified IP address and address space, typically used in hybrid network scenarios.
   - **Public IP (gatewayPublicIP, vmPublicIp)**: Configures public IP addresses for the VPN gateway and the virtual machine.
   - **Virtual Network Gateway (vnetGateway)**: Creates an ExpressRoute gateway with specified SKU and configuration.
   - **Storage Account**: Conditionally creates a new or uses an existing storage account.
   - **Private Endpoint**: Configures a private endpoint for secure access to the storage account.
   - **Network Security Group**: Sets security rules for network traffic control.
   - **Network Interface (nic)**: Configures the network interface for the virtual machine, including accelerated networking.
   - **Virtual Machine (vm)**: Creates a Windows VM with specified settings, including admin credentials, disk configuration, and security profile (TrustedLaunch if specified).
   - **VM Extension**: Adds a custom script extension to the VM to download and install the AzCopy tool.

3. **Outputs**:
   - `hostname`: The fully qualified domain name (FQDN) of the VM's public IP.
   - `storageAccountId`: The ID of the storage account, depending on whether a new or existing one is used.

This template sets up a complete environment in Azure to prepare for the AIX migration, including networking, storage, and a virtual machine, with options for secure and managed infrastructure configurations.

### 🚀 Prerequisites: ###

1. **Begin by [installing the necessary tooling](https://docs.microsoft.com/azure/azure-resource-manager/bicep/install?WT.mc_id=AZ-MVP-5000671).**

### 📦 Deployment Options: ###

**Option 1. Local Machine Deployment:**

Deploy application samples directly from your local machine using Windows Terminal and Azure PowerShell.

```powershell
$date = Get-Date -Format "MM-dd-yyyy"
$rand = Get-Random -Maximum 1000
$deploymentName = "SkytapDeployment-"+"$date"+"-"+"$rand"

New-AzResourceGroupDeployment -Name $deploymentName -ResourceGroupName skytap-landing-zone -TemplateFile .\main.bicep -TemplateParameterFile .\main.bicepparam -c
```

You can also utilize a Bicep parameters file for added flexibility.

**Option 2. Azure Portal Deployment:**

1. Access the Azure Portal, open CloudShell (using PowerShell), and clone this repository:

```shell
git clone https://github.com/daveRendon/skytap.git
cd docs/aix/code/
```

2. Once in the working directory of the sample application, execute the following command:

```powershell
$date = Get-Date -Format "MM-dd-yyyy"
$rand = Get-Random -Maximum 1000
$deploymentName = "SkytapDeployment-"+"$date"+"-"+"$rand"

New-AzResourceGroupDeployment -Name $deploymentName -ResourceGroupName skytap-landing-zone -TemplateFile .\main.bicep -TemplateParameterFile .\main.bicepparam -c
```



