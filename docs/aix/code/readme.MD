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

   [![Deploy To Azure](https://learn.microsoft.com/en-us/azure/templates/media/deploy-to-azure.svg)]()


This template sets up a complete environment in Azure to prepare for the AIX migration, including networking, storage, and a virtual machine, with options for secure and managed infrastructure configurations.

