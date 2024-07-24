# Skytap Landing Zones

Welcome to the repository for Skytap Landing Zones on Azure. This project is designed to provide a structured approach to deploying Skytap environments in Azure, facilitating the migration and management of traditional applications such as AIX, IBM i, and legacy Unix systems in Skytap on Azure. Our goal is to ensure that enterprises can seamlessly integrate their legacy applications into Azure while maintaining the high performance, reliability, and security standards that Skytap offers.

## Overview

Skytap on Azure provides a unique capability for running IBM Power and x86 workloads in the cloud. It replicates traditional data center environments in Azure, enabling lift-and-shift migrations without the need to modify the applications or architectures significantly. Skytap Landing Zones are pre-configured environments that follow best practices and guidelines to optimize the deployment of these workloads on Azure.

## Key Features

- **Pre-Configured Templates**: Skytap Landing Zones include a variety of templates that are pre-configured for different needs, helping to accelerate the deployment and integration of traditional environments into Azure.
- **Customizable and Scalable**: While offering out-of-the-box solutions, Skytap Landing Zones also provide the flexibility to be tailored according to specific enterprise needs, supporting scalability as business requirements grow.
- **Integrated Networking**: Fully integrated with Azure networking features including ExpressRoute, VNets, and VPN Gateways, ensuring secure and efficient connectivity between on-premises data centers and the Azure cloud.
- **Compliance and Security**: Built with security and compliance at its core, adhering to Azure’s compliance frameworks, ensuring that your critical workloads meet industry standards and regulations.

## Architecture

The architecture of Skytap Landing Zones focuses on creating a secure, scalable, and efficient environment for legacy applications. It includes:
- **ExpressRoute Integration**: For a direct, secure, and high-speed connection between on-premises environments and Azure.
- **Automated Data Migration Tools**: Tools like AzCopy integrated within the VMs to facilitate efficient data transfer processes.
- **Environment Templates**: Standardized templates for rapid deployment of IBM Power and legacy Unix systems.

## Getting Started

To get started with Skytap Landing Zones, follow the steps below:

1. **Prerequisites**:
   - An active Azure subscription.
   - An understanding of Skytap and its functionalities.
   - Basic knowledge of Azure services like VNets, Blob Storage, and ExpressRoute.

2. **Select a Landing Zone (IBMi or AIX)**:
   - Utilize the provided Bicep templates and scripts to set up your initial Skytap environment in Azure.

| OS | Description |
|----------|-------------|
| AIX      | Refer to the following document for the AIX Landing Zone: 👉 [AIX Landing Zone](docs\aix\aix-landing-zone.md)
 |
| IBM      | Refer to the following document for the IBM i Landing Zone (work in progress) |

3. **Configuration**:
   - Configure the network settings according to your organizational needs.
   - Set up the connection between your on-premises data center and Azure using ExpressRoute.

4. **Deployment**:
   - Deploy the Skytap Landing Zones using the guidelines provided in the deployment scripts.
   - Monitor the deployment process through Azure portal notifications and adjust configurations as needed.

## Contributing

Contributions to the Skytap Landing Zones project are welcome! Please consider the following ways you can contribute:
- **Feedback**: Provide feedback on templates and scripts.
- **Features**: Suggest and contribute new features or enhancements.
- **Documentation**: Improve existing documentation or create new guides to help users.

## License

This project is licensed under the terms of the MIT license.

## Support

For support and further assistance, please open an issue in this repository.
