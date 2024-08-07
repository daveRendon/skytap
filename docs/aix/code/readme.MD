# Deploy Skytap AIX Landing Zone 

The primary objective of this Skytap AIX Landing Zone is to set up all necessary components for migrating AIX on-premises systems to Skytap on Azure.

### 🚀 Prerequisites: ###

1. **Install Required Tooling:** [VS Code and Bicep](https://docs.microsoft.com/azure/azure-resource-manager/bicep/install?WT.mc_id=AZ-MVP-5000671).
2. **Create Your Skytap Account:** [Skytap on Azure](https://www.skytap.com/blog/creating-a-skytap-on-azure-account-from-the-azure-marketplace/).
3. **Set Up ExpressRoute Connection (Optional):** [Using the Skytap Portal](https://help.skytap.com/wan-create-self-managed-expressroute.html).
4. **Create Resource Group:** Name it `skytap-landing-zone`.

## 📝 Analysis of the Bicep template: ###

This Bicep creates a set of Azure resources, including a Virtual Network, Virtual Machines, and associated components. Here's a breakdown of the key components and their purpose:

### Parameters
 The `main.bicepparam` file defines the below:

- **Location, Resource Group Name, Storage Account Name**: Define essential values.
- **VM Settings**: Includes admin username, password, DNS label, VM size, and security type.
- **New or Existing Storage**: Determine if a new or existing storage account is used.

The template also includes settings for the virtual machine, such as the admin username, password, DNS label, VM size, and security type.

### Resources
 The `main.bicep` file defines the below:
   
   - **Virtual Network (vnet)**: Creates a virtual network with specified address space.
   - **Subnets**: Defines subnets within the virtual network, including a *GatewaySubnet* and another subnet with an associated network security group.
   - **Local Network Gateway**: Sets up a local network gateway with specified IP address and address space, typically used in hybrid network scenarios.
   - **Public IP (gatewayPublicIP, vmPublicIp)**: Configures public IP addresses for the VPN gateway and the virtual machine.
   - **Virtual Network Gateway (vnetGateway)**: Creates an ExpressRoute Gateway with specified SKU and configuration.
   - **Express Route connection**: If there's already an Express Route deployed, the Bicep template will configure the Express Route connection to Skytap.
   - **Storage Account**: This Bicep template create a new storage account or it can use an existing storage account.
   - **Private Endpoint**: Configures a private endpoint for secure access to the storage account.
   - **Network Security Group**: Sets security rules for network traffic control.
   - **Network Interface (nic)**: Configures the network interface for the virtual machine, including accelerated networking.
   - **Virtual Machine (vm)**: Creates a Windows VM with specified settings, including admin credentials, disk configuration, and security profile (TrustedLaunch if specified).
   - **VM Extension**: Adds a custom script extension to the VM to download and install the AzCopy tool.

### Outputs
   - `hostname`: The fully qualified domain name (FQDN) of the VM's public IP.
   - `storageAccountId`: The ID of the storage account, depending on whether a new or existing one is used.

This template sets up a complete environment in Azure to prepare for the AIX migration, including networking, storage, and a virtual machine, with options for secure and managed infrastructure configurations.



## 📦 Deployment Options: ##

### Option 1: Local Machine Deployment

Deploy application samples directly from your local machine using Windows Terminal and Azure PowerShell.

```powershell
$date = Get-Date -Format "MM-dd-yyyy"
$rand = Get-Random -Maximum 1000
$deploymentName = "SkytapDeployment-"+"$date"+"-"+"$rand"

New-AzResourceGroupDeployment -Name $deploymentName -ResourceGroupName skytap-landing-zone -TemplateFile .\main.bicep -TemplateParameterFile .\main.bicepparam -c
```

You can also utilize a Bicep parameters file for added flexibility.

### Option 2: Azure Portal Deployment

1. Open CloudShell(PowerShell) in the [Azure Portal](https://portal.azure.com) and clone the repository:

```powershell
git clone https://github.com/daveRendon/skytap.git
cd skytap/docs/aix/code/
```

2. Run the deployment script:

```powershell
./bicep-rg-deploy.ps1
```
Deployment takes up to 45 minutes. Example output:

![Deployment Output](/assets/images/aix-landing-zone-deployment-output.jpg)


## Post-Deployment Steps

Once the deployment completes, you can follow the below steps: 

1. **Replicate Data to Azure Blob Storage**: Transfer the mksysb backups to Azure Blob Storage using the JumpboxVM and AzCopy. Transfer the Mksysb from the blob storage to the JumpboxVM data disk(s).

1. **Setup Connectivity to Skytap**: Configure a VPN connection or ExpressRoute circuit from Azure to the Skytap environment.

1. **Deploy NIM Server in Skytap**: Deploy a NIM server in your Skytap environment. You can use the create-nim-server.py to deplooy the NIM Server in Skytap.

     The Python script provided is designed to authenticate to the Skytap API using your credentials (username and API token) and then make a request to create a new environment that includes a Network Installation Management (NIM) server, based on a specified template. 

     #### Preparing your python script to deploy NIM Server:
   1. **API Credentials**: You must have valid Skytap API credentials (username and API token). These are crucial for the authentication part of the script.
   2. **Template ID**: The script assumes you have a predefined template that includes a NIM server configuration. You need to replace `"your_template_id_with_nim_server"` with the actual ID of this template.
   
      To find the template ID of the NIM (Network Installation Management) server in the Skytap portal, you can follow these steps:

      1. **Log In to Skytap**: Sign in to your Skytap account.

      2. **Navigate to Templates**: Once logged in, look for the navigation bar or menu and select "Templates" or a similarly named section where your saved templates are listed.

      3. **Locate the NIM Server Template**: Search through your list of templates to find the one for the NIM server. You might need to use the search function if you have many templates.

      4. **View Template Details**: Click on the NIM server template to open its detailed view. The template ID is usually displayed in the details section, often in the URL or on the template information page.

      5. **Copy the Template ID**: Once you locate the template ID, copy it for use in your scripts or documentation.


   3. **Python Environment**: Ensure Python is installed on your system along with the `requests` library. If not, you can install Python from [python.org](https://www.python.org/downloads/) and install the `requests` library using pip:

      ```bash
      pip install requests
      ```

   #### Considerations:
   - **Security**: The script uses basic authentication, which involves sending your username and API token in the request headers.
   - **Permissions**: Your Skytap API user account needs to have the necessary permissions to create environments. If you encounter permissions errors, you may need to adjust your account settings or contact your Skytap administrator.

   #### Running the Script:
   To run the script:
   1. Open your text editor or Python IDE.
   2. Open the `create_nim_server.py` file.
   3. Replace `your_username` and `your_api_token` with your actual Skytap API credentials.
   4. Replace `your_template_id_with_nim_server` with the actual template ID that has a NIM server.
   5. Save the file.
   6. Open a command line or terminal.
   7. Navigate to the directory where the file is saved.
   8. Run the script by typing:
      ```bash
      python create_nim_server.py
      ```

   #### Expected Outcome:
   If all configurations are correct and you have sufficient permissions, the script will authenticate to Skytap, create a new environment based on the specified template, and print the details of the newly created environment. If there are any issues, it will print the error details provided by the Skytap API.




1. **Migrate the Mksysb Backups from Blob Storage to Skytap**: Copy the Mksysb files from the JumpboxVM data disks to the NIM server using SCP. (https://winscp.net/download/WinSCP-6.3.4-Setup.exe/download)

1. **Restore Mksysb Files**: Initiate the Mksysb restoration process on the target systems within Skytap.

1. **Add Filesystem to Restored LPARs**: Include necessary temporary space on the restored Logical Partitions (LPARs) for savevg and database files.

1. **Transfer Additional Backup Files (copy savevg and DB files to temporary disk on restore target)**: Copy savevg and database files to the temporary disk space allocated on the restoration targets.

1. **Restore Savevg and Database Files**: Complete the restoration of savevg and database files to ensure all system and application data is accurately reinstated.
