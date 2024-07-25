# Skytap Landing Zones

Welcome to the repository for Skytap Landing Zones on Azure. This project is designed to provide a structured approach to deploying Skytap environments in Azure, facilitating the migration and management of AIX and IBM i to Skytap on Azure. 

🌟 Star this repository now to stay updated and show your support for the project

## Overview

Skytap on Azure provides a unique capability for running IBM Power and x86 workloads in the cloud, enabling lift-and-shift migrations without the need to modify the applications or architectures significantly. Skytap Landing Zones are pre-configured environments that follow best practices and guidelines to optimize the deployment of these workloads on Azure.

### Key Components of a Skytap Landing Zone

1. **Pre-configured Infrastructure**:
   - Includes all necessary virtual network settings, storage configurations, and computing resources needed to perform the migration of AIX or IBM i. This setup is tailored to meet the security, compliance, and operational requirements of the applications being migrated.

2. **Security and Compliance**:
   - Built with security controls and compliance guidelines in mind to ensure that the migrated applications adhere to organizational policies and regulatory standards.

3. **Connectivity**:
   - Ensures robust connectivity options, including VPNs and ExpressRoute connections, for secure and reliable communication between the Skytap environment and on-premises data centers or other cloud services.

4. **Scalability and Flexibility**:
   - Designed to be scalable and flexible to accommodate growth and changes in the workload requirements. This includes scalable storage options and dynamic allocation of computing resources.

5. **Automation and Orchestration**:
   - Incorporates automation tools and scripts to streamline the deployment, management, and scaling of applications. This might involve using Skytap APIs for automation and integration with existing CI/CD pipelines.

6. **Monitoring and Management Tools**:
   - Equipped with monitoring and management tools to provide visibility into application performance and resource utilization, facilitating proactive management and optimization.

### Purpose of a Skytap Landing Zone

- **Risk Mitigation**: Reduces the risk associated with cloud migrations by providing a controlled and secure environment to deploy applications.
- **Accelerate Migration**: Speeds up the migration process by offering a ready-to-use environment that reduces the setup time and complexity involved in configuring cloud resources from scratch.
- **Best Practices Integration**: Integrates best practices for cloud deployment, management, and security, ensuring a robust and efficient cloud environment.
- **Consistency and Standardization**: Provides a standardized approach to deploying workloads in the cloud, ensuring consistency across various projects and teams within an organization.

Skytap Landing Zones are part of a strategic approach to cloud adoption, ensuring that organizations can leverage the full benefits of the cloud while addressing the challenges of migration and ongoing cloud management effectively.

## Getting Started

To get started with Skytap Landing Zones, follow the steps below:

1. **Prerequisites**:
   - An active Azure subscription.
   - A basic understanding of Skytap and its functionalities.
   - Basic knowledge of Azure services like VNets, Blob Storage, and ExpressRoute.

2. **Select a Landing Zone (IBMi or AIX)**:
   - Utilize the provided Bicep templates and scripts to set up your initial Skytap environment in Azure.

| OS  | Description                                                                                                 |
|-----|-------------------------------------------------------------------------------------------------------------|
| AIX | Refer to the following document for the AIX Landing Zone: 👉 [AIX Landing Zone](docs/aix/aix-landing-zone.md) |
| IBM | Refer to the following document for the IBM i Landing Zone (work in progress)                                |


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
