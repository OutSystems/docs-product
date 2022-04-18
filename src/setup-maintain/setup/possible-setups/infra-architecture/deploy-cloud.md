---
summary: An OutSystems Cloud infrastructure provides enterprise-class cloud computing without the hassle of managing physical software infrastructure. 
locale: en-us
guid: de7c085b-1c0b-4a1f-9d36-4a7e3f1c3ebc
app_type: traditional web apps, mobile apps, reactive web apps
---

# Deploy an infrastructure on OutSystems Cloud

An OutSystems Cloud infrastructure, also known as Platform as a Service (PaaS), provides enterprise-class cloud computing without the hassle of managing physical software infrastructure. 

The OutSystems Cloud provides you:

* a ready to use infrastructure
* high performance
* security and reliability
* high availability and scalability
* less time spent on maintenance
* database storage, backup and restore
* additional environments for elastic release management

OutSystems handles all server and database maintenance, server and system upgrades and  patches for you. 

In the OutSystems Cloud deployment, all servers, physical infrastructure, and data are hosted in the secure data centers of Amazon Web Services (AWS). AWS is the market leader and the most mature public cloud infrastructure as a service (IaaS). It has enterprise-grade availability with guaranteed service levels of 99.9%, and it is the IaaS technology that has been accredited by the largest number of security compliance standards.


OutSystems Cloud benefits from the multiple layers of operational and physical security implemented by AWS. OutSystems Cloud Infrastructure Security relies both on the AWS security controls and on the secure configuration standards that OutSystems applies to all infrastructure components: network, operating system, database, and application servers. These defend the integrity of customer data and protect systems against unauthorized access and malware.

Both OutSystems and AWS adopt a proactive approach to security, with carefully designed  Security Processes run by specialized security teams. These processes defend the OutSystems Cloud from rogue employees, enforce secure practices, and ensure that the OutSystems Cloud is ready to respond to any type of security event.


## Setting up your OutSystems Cloud

Upon subscribing to an infrastructure in the OutSystems Cloud, organisations choose the edition as well as any necessary addons for their needs. If you haven’t already, check the infrastructure architecture and some configuration examples [here](https://success.outsystems.com/Support/Enterprise_Customers/Infrastructure_architecture_and_deployment_options#Infrastructure_architecture).

The available add ons include:

* Additional non-production environment(s) for UAT, for example.
* Additional [pipelines](https://success.outsystems.com/Support/Enterprise_Customers/Infrastructure_architecture_and_deployment_options#Pipelines), a full set of environments to enable independent development and release.
* High availability add on that deploys a stand-by database replica and additional application servers in a distinct datacenter.
* [Sentry](https://www.outsystems.com/sentry/) add-on, the high compliance OutSystems Cloud.

But you won’t be locked in an initial configuration, as needs evolve, so can your infrastructure. And in every step of the way, OutSystems automatic provisioning takes care of the full setup.

Several deployment regions are available to adjust to needs such as data compliance, integration performance, and application performance for end users. Rather than choosing only one region, global organizations can choose a different region for each pipeline.
Pipelines in different regions have independent databases for each environment. 

OutSystems automatically deploys the infrastructure according to the specifications. This is achieved through and orchestrated provisioning based on infrastructure-as-code principles that ensure: 

* an up to date operating system and database management system
* hardened images that benefit from continuous improvement
* tested setups and quick recovery

## Maintenance and upgrades

OutSystems installs updates of the operating system and application server approximately every 60 days. OutSystems Cloud support reassesses the risk of vulnerabilities reported by the platform vendors (e.g. Microsoft) and presents a mitigation plan for any critical vulnerability within 7 days.

OutSystems’ Cloud host, AWS, automatically schedules security and durability related patches to the database, and OutSystems notifies customers on a timely basis. Such patching occurs infrequently (typically once every few months).
By default, customers are free to choose the timing of updates to OutSystems revisions. However, OutSystems may proactively update OutSystems software, when necessary to defend the security and/or availability of the OutSystems Cloud.
In the OutSystems Cloud, the overall upgrade process is managed by OutSystems, coordinating with you in every step of the way, to guarantee a successful and as effortless as possible procedure. Maintenance and upgrades are done under the same principles of infrastructure-as-code.

Upgrades of the OutSystems software are coordinated with you every step of the way to guarantee a successful and as effortless as possible procedure. You can read more about it [here](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/01_Upgrade_OutSystems_Platform).

## High availability

The OutSystems Cloud high-availability option allows customers to deploy Front-Ends across different availability zones, and to set up a database replica in a different availability zone than the primary database. Each availability zone is designed as an independent failure zone.
This means that availability zones are physically separated within a typical metropolitan region and are located in lower risk floodplains (specific flood zone categorization varies by region). In addition to utilizing discrete uninterruptible power supply (UPS) and onsite backup generators, they are each fed via different grids from independent utilities to further reduce single points of failure. Availability zones are all redundantly connected to multiple tier-1 transit providers.


AWS infrastructure has a high level of availability, enabling the deployment of resilient IT architectures. AWS has designed its systems to tolerate system or hardware failures with minimal customer impact.
Data centers are built in clusters in various global regions. All data centers are online and serving customers; no data center is “cold.” In case of failure, automated processes move customer data traffic away from the affected area. Core AWS applications are deployed in an N+1 configuration. In the event of a data center failure, there is sufficient capacity to enable traffic to be load-balanced to the remaining sites.



The OutSystems Cloud high-availability option provides the ability to remain resilient in the face of most failure scenarios, including natural disasters or system failures.
**OutSystems Sentry always includes the high-availability option.**
OutSystems doesn’t replicate customer data between regions, thus allowing customers to be compliant with their data placement and privacy requirements.

Read more about high availability and scalability strategies [here](https://success.outsystems.com/Support/Enterprise_Customers/High_availability_and_scalability_strategies).


## Built-in infrastructure security

OutSystems applies security best practices and manages security to allow customers to focus primarily on their business. OutSystems Cloud inherently protects customers from threats by making sure security controls are applied at every layer, while ensuring that customer applications and data are isolated.
OutSystems allows any customer to conduct security audits and penetration tests within the OutSystems Cloud, as long as they are limited to the customer’s own cloud infrastructure.


### Data security

OutSystems applies industry-standard procedures to safeguard the confidentiality of the data stored by the applications hosted in the OutSystems Cloud.We carefully control employee access to your data and applications based on the task being performed.
OutSystems keeps customer data in the region selected by the customer, enabling compliance with data residency regulations.

Within the OutSystems organization, access to customer data is restricted to the support team, and used only when necessary to provide services to the customer.
Even though OutSystems protects customer data, customers are still responsible for developing applications that follow best practices for data security.

OutSystems Cloud automatically backs up production databases. Customers can request a database restore to any point-in-time in the last 15 days. As an example, if a developer introduces a bug that corrupts or deletes data, by restoring to a point-in-time, the customer can avoid or minimize data loss. 

OutSystems encrypts data-at-rest in production databases. Encryption is always enabled with OutSystems Sentry, and activated upon request for other customers. Encrypted databases provide an additional layer of data protection, securing data in the event of unauthorized access to the underlying storage. Encryption increases data protection of applications deployed in the OutSystems Cloud, and can fulfill specific compliance requirements.

Encryption of data-at-rest includes the underlying storage for a DB instance and its automated backups. Encrypted databases use the industry standard AES-256 encryption algorithm to encrypt data on the server that hosts customer databases. Once the data is encrypted, authentication of access and decryption of the data is handled transparently with a minimal impact on performance. Customers don't need to modify their applications to use encryption. 

OutSystems recommends that customers configure their OutSystems Cloud environments to encrypt all data communication between OutSystems Cloud and third-party systems, to prevent eavesdropping. 
The data communication between the OutSystems application servers and the databases is encrypted by default.

### Access control

OutSystems follows a formal Logical Access Procedure to limit access to those employees who need it to perform their duties, and ensure that these employees are adequately vetted and trained. This procedure includes request, approval, and provisioning processes for authorizing and implementing user IDs. Employees are assigned a unique ID. Employee computers are registered in an internal Active Directory, and only these computers are authorized to access system components. Access is immediately revoked for any terminated/separated employees.

### Protection from malicious software

The OutSystems Cloud servers are provisioned automatically from malware-free virtual machine images, with strict access permissions that block any malware contamination attempts. The OutSystems Cloud virtual machine images are regularly patched and hardened (including the removal of unnecessary services). 

The OutSystems Cloud servers are managed from OutSystems employee computers with centrally managed and regularly updated antivirus software. Only OutSystems support engineers have operating system access to the OutSystems Cloud servers; malware protection at their computers effectively protects the OutSystems Cloud servers as well.
OutSystems Cloud is hosted on Amazon AWS, which implements additional malware defense mechanisms at the network layer.

### Network Security

The OutSystems Cloud dedicates a Virtual Private Cloud (VPC) to each Enterprise customer, ensuring complete isolation of each tenant’s environment from each other. Each tenant has a dedicated set of virtual machines and a dedicated database instance, both running on the dedicated Virtual Private Cloud.

The OutSystems design isolates the different product lifecycle environments (e.g. development, test, production, other non-production environments). Developers stage their applications in the various environments using the OutSystems console. The OutSystems console runs in its own separate environment, and communicates with the other environments using HTTPS only. 

Each customer has a dedicated set of virtual machines and database instances protected inside a dedicated Virtual Private Cloud (VPC), which is logically isolated from the internet and other virtual networks in the AWS cloud. OutSystems Cloud provides segregated environments for product lifecycle environments running on different virtual server instances. 
A layer of AWS Security Groups, acting as firewalls, control the traffic between the environments and the internet. Security Groups define a granular access control per environment and per asset.
OutSystems shields each environment using a Web Application Firewall (WAF), which blocks malicious traffic from reaching the running web applications. To ensure that OutSystems keeps full flexibility on the reaction to evolving security threats, maximum availability, and compatibility with OutSystems product evolution, the same WAF's policies apply to all customers.

Read [here](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/Possible_setups_for_an_OutSystems_infrastructure/OutSystems_Cloud_network_architecture) more about OutSystems Cloud network architecture.


#### Secure connection to your systems

To integrate with the existing ecosystems, there are several options to securely connect OutSystems Cloud to external databases, and other systems such as web services and identity management systems, for example:

* **VPN** - customers can set up an IPsec VPN connection between their data center and the OutSystems Cloud VPC. VPN connections use industry-standard IPsec tunnel mode (with IKEPSK, AES-128, HMAC-SHA-1, PFS) to authenticate the two sides of the VPN connection and to protect the data in transit from eavesdropping and tampering.
* **Transit gateway** - a service that enables you to connect your multiple AWS accounts, Virtual Private Clouds (VPCs), and your on-premises networks to a single gateway. For seamless integration with your corporate systems, OutSystems allows you to connect to your OutSystems Cloud VPC using your own AWS Transit Gateway. 
* **Direct connection** - For scenarios which require the use of high bandwidth and a steady connection without network congestion, you can use AWS Direct Connect to link your private AWS network to your OutSystems Cloud over a dedicated line.
