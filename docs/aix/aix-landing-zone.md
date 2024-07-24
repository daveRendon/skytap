## Migrate AIX workloads to Skytap on Azure

Skytap on Azure streamlines the cloud migration process for applications operating on IBM Power Systems. This case study demonstrates the migration of AIX logical partitions (LPARs) to Skytap on Azure, drawing on proven strategies from recent customer implementations. A web application hosted on Microsoft Azure provides a contemporary interface to manage the resources in LPARs on Skytap on Azure.

## Architecture

![AIX Landing Zone Architecture](/assets/images/aix-landing-zone-architecture.jpg)


This architecture diagram illustrates the migration of AIX systems from an on-premises environment to Microsoft Azure and Skytap, leveraging Azure services for enhanced networking and storage solutions. Here's a detailed breakdown of the components and their functions within this migration process:

### On-premises Environment:
- **AIX Systems**: These are the IBM AIX (Advanced Interactive eXecutive) systems that are currently operating in an on-premises data center. AIX is an enterprise-class UNIX operating system that runs on IBM systems.

### Microsoft Azure Components:
- **ExpressRoute Gateway**: This component is used to establish a dedicated and private connection from the on-premises network to Microsoft Azure. It offers more reliability, faster speeds, and lower latencies than typical Internet-based connections.
- **Virtual Network (VNet)**: This is the fundamental building block for your private network in Azure. VNets allow many types of Azure resources, such as Azure Virtual Machines (VM), to securely communicate with each other, the internet, and on-premises networks.
- **Subnet**: A subnet is a range of IP addresses in the VNet. You can divide a VNet into multiple subnets for organizational and security purposes.
- **VNet Gateway**: This component is used to connect VNets to each other or with on-premises networks. It acts as a router or a gateway that routes traffic accordingly.
- **Local Network Gateway**: This logical object represents the on-premises network in Azure to facilitate the routing of data.
- **Storage Account**: Azure Storage Accounts provide a unique namespace to store and access your Azure storage data objects. Here it is used to store data from AIX systems.
- **Private Endpoint**: A private endpoint is a network interface that connects you privately and securely to a service powered by Azure Private Link. Here, it's used to ensure secure access to the Azure Storage Account.

### Migration Pathways:
- **Migration to Blob Storage using ExpressRoute**: Data from the AIX systems is migrated to Azure Blob Storage via ExpressRoute, ensuring a fast and secure data transfer.
- **Migration to Skytap using ExpressRoute**: Another pathway is directly migrating AIX systems to Skytap, an environment in Azure tailored for running traditional workloads like AIX.

### Skytap Environment:
- **Skytap WAN**: This component represents the wide area network configuration within Skytap, which supports connectivity back to Azure or on-premises environments.
- **Linux VM with AzCopy**: This Virtual Machine in Skytap runs Linux and uses AzCopy, a command-line utility designed to copy data to/from Azure Blob storage and between Azure Blob storage accounts.

### General Flow:
1. **Data Transfer**: Data from the on-premises AIX systems is transferred to Azure Blob Storage using ExpressRoute for speed and security.
2. **Networking Setup**: The entire transfer and subsequent communications are managed through a series of gateways and private endpoints that ensure the traffic is secure and efficient.
3. **Utilization in Skytap**: Post migration, AIX systems can be managed in Skytap or Azure, with specific configurations done through VNets and subnets in Azure.

This setup ensures a smooth transition of AIX systems to a cloud environment, leveraging Azure's robust networking capabilities for an efficient and secure migration process.
