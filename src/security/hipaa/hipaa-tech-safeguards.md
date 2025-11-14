---
summary: Explore how OutSystems 11 (O11) supports HIPAA compliance through technical safeguards, access control, and encryption features.
tags: hipaa compliance, technical safeguards, access control, data encryption, security compliance
locale: en-us
guid: 219da37e-3496-4cc3-b6e8-452dc531a608
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - full stack developers
  - platform administrators
  - architects
  - backend developers
  - tech leads
outsystems-tools:
  - none
coverage-type:
  - apply
---

# Checklist of HIPAA safeguards

The HIPAA requirements and controls are sometimes by numbers and letters.
The alphanumeric combinations refer to a specific HIPAA control. Capital letters refer to whether a control is (R) required or (A) addressable by a covered entity and their BA.

For example, (R)164.312(a)(2)(i) means this control is required and the numbers and letter that followed are the control number and section/subsection. More details on the various HIPAA technical safeguards, controls and their numbers system are addressed in this [US government publication](https://www.hhs.gov/sites/default/files/ocr/privacy/hipaa/administrative/securityrule/techsafeguards.pdf).

## Technical safeguards

There are several aspects involved in achieving HIPAA compliance for your OutSystems-developed applications, and we’ll cover the specifics in the following Technical safeguards required by HIPAA, and how OutSystems helps you achieve them.

Highlights of how OutSystems accelerates HIPAA Technical safeguards:

* Built in role-based access control for both IT users and end-users that allow for granular permissions and enable **access control policies and procedures**.
* Applications can use role checks on specific screens of your apps to control who can alter and destroy EPHI.
* Auditing trails of IT and end-users' actions.
* Session mechanism with a default timeout that can be customised.
* Extensive support for data encryption at rest and in transit.
* Emergency failover of data for all the supported databases.

### Access control { #access-control }

This HIPAA regulation requires the following controls to implement technical policies and procedures for electronic information systems that maintain electronic protected health information to allow access only to those persons or software programs that have been granted access rights as specified in 164.308(a)(4).

#### Develop access control policies and procedures

##### What you need to have and do

You have policies and procedures in place for access control procedures, covering joiners (people you are onboarding), movers (people changing roles) and leavers. You specify requirements for access control for your overall IT system and applications that store and process ePHI especially where users need to access such information. You implement a procedure to periodically review all user access and follow up on necessary access changes that were not made in real time (internal access audit/review).

##### How OutSystems can help you

###### For OutSystems IT users

OutSystems management console, LifeTime, makes it easy to manage IT team permissions. While OutSystems management consoles don’t contain EPHI themselves, they provide developer access to the application code in the OutSystems environments. LifeTime allows you to define the permissions of IT users using a [role-based permission model](../../manage-platform-app-lifecycle/manage-it-teams/about-permission-levels.md). This model enables you to set up the permissions of your IT users for simple to complex security policy needs.

###### For OutSystems end users

We provide a default module for end-user management with a set of capabilities. Considering OutSystems is a development platform the access control is dependent on the application development itself (its logic and data accessed). When developing an application, make sure to define the requirements correctly and clearly for access control so they can be easily implemented.

You can restrict or allow end users access to specific screens and operations of OutSystems applications using OutSystems own custom roles. The default user module provides the capability of user and group management, assigning any role (default or custom) to each of these entities. Groups allow you to manage the permissions of many users over all OutSystems applications.

OutSystems also offers the [Users API](../../ref/apis/auto/users-api.final.md) to perform end user management programmatically. Use the API to write your own applications for managing registered users or for exposing APIs to external systems through Web Services.

#### Assign unique identifiers (R)164.312(a)(2)(i)

##### What you need to have and do

Ensure unique user credentials are assigned for each user of applications that you develop using OutSystems. This is to trace user activity. You ensure that all application activity can be traced to a specific user. Likewise ensure that the necessary data is available in the system logs, to support audit and other related business functions.

##### How OutSystems can help you

###### For OutSystems IT users

OutSystems management console (LifeTime) automatically ensures that each IT user has a unique username and UserID. You can also populate IT users with further distinguishable data such as name and email address. LifeTime also includes [built in auditing](../../app-architecture/data/audit-trails.md) of IT users' actions.

IT user authentication can also be extended to use an [external authentication provider](../../manage-platform-app-lifecycle/manage-it-teams/use-an-external-authentication-provider.md).

###### For OutSystems end users

When developing custom applications, implement a unique identifier for any entity that identifies a user. The default [Users](../../user-management/intro.md) management app, automatically assigns a unique identifier on the database for each user and enforces distinct usernames.

#### Implement an Emergency Access Procedure (R) 164.312(a)(2)(ii)

##### What you need to have and do

You need to implement emergency access for applications you develop using OutSystems.

##### How OutSystems can help you

To allow for emergency failover of data, OutSystems provides the flexibility to use database failover mechanisms as long as:

* They provide a single end-point of access to the OutSystems platform
* Data consistency is maintained regardless of the replica that is active
* Data integrity is maintained

As examples, several database provider solutions can be used such as:

* For Microsoft SQL Server
    * Transactional replication
    * Database mirroring
    * Always-on failover cluster
* For Oracle databases
    * Real Application Cluster (RAC)
    * Oracle Data Guard

#### Implement automatic logoff (A) 164.312(a)(2)(iii)

##### What you need to have and do

You need to ensure that custom applications implement procedures that terminate an electronic session after a predetermined period of inactivity.

##### How OutSystems can help you

The OutSystems Platform uses several mechanisms that allow the server to maintain information about the previous requests the end-user made. Sessions are one example. The session timeout parameter specifies the period of time that a session can remain idle, without any end-user interaction, before the Platform Server ends the session automatically. [More information here](../../building-apps/data/session/session.md).

#### Implement encryption and decryption (A) 164.312(a)(2)(iv)

This section also includes the measures for _Implement Encryption Controls (A) 164.312(e)(2)(ii)_

##### What you need to have and do

You need to ensure that your custom applications implement mechanisms to protect ePHI while at rest, and in transit. Suitable encryption and decryption mechanisms include but aren't limited to secure algorithms, and key management.

##### How OutSystems can help you

In the OutSystems Cloud you can benefit of the compliance of the [OutSystems HIPAA offering](intro.md#hipaa-cloud). Secure methods are provided out of the box to encrypt and decrypt data along with a Key Management System. For more information on how to use it, check [Implement encryption and decryption for HIPAA compliance](../../building-apps/data/hipaa/intro.md).

As alternative options, OutSystems supports using database encryption mechanisms such as [transparent data encryption](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver15) to implement your own encryption schemes at the application level using your own keys.

To add more granular encryption such as, for example, having different encryption keys per application or preventing that those that have access to the database may decrypt data, OutSystems enables developers to use [envelope encryption techniques](https://success.outsystems.com/documentation/11/security/securing_data_at_rest_with_encryption/#how-to-fully-encrypt-your-sensitive-data). An example of this implementation is the Forge component [Crypto API](https://www.outsystems.com/forge/component-overview/437/cryptoapi).

#### Ensure access termination

##### What you need to have and do

You need to ensure that access to ePHI is immediately terminated the moment such access is no longer needed. You need to implement a formal access control policy to remove access to employees leaving your organization, or reduce or remove as appropriate if their roles change and they no longer need such access or at the same level to perform their jobs.

##### How OutSystems can help you

###### For OutSystems IT users

The management consoles have the capability of immediately deactivating a user. Traceability of past actions is preserved for deactivated IT users. Once set as deactivated, IT users will no longer be able to access the management consoles or the application’s code.

More information available [here](../../manage-platform-app-lifecycle/manage-it-teams/intro.md).

###### For OutSystems end users

The default end user module supports deactivating users. Deactivated users will no longer be able to access the applications and their data.

Develop operations that immediately ensure the access termination of a user, while developing your custom applications.

### Audit controls § 164.312(b)

This HIPAA regulation requires the following controls to implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems containing or using ePHI.

#### Develop Audit Policies and Procedures (B)

##### What you need to have and do

You define the scope of the audit controls for systems that store or process ePHI, based on a risk assessment and the context of the organization.

You develop and formally approve an audit policy establishing:

* Which systems, applications, or processes are vulnerable to tampering, inappropriate uses, or unauthorized disclosure?
* Which activities shall be audited?
* What the audit record will include, for example UserID, event type, timestamp, IP address
* Where the audit data will live and be backed up.

##### How OutSystems can help you

OutSystems has defined internal policies and procedures regarding systems monitoring and logging, aligned with ISO 27001 - Annex A. These policies protect any data excerpts (possibly containing ePHI) you may need to send us in the context of receiving customer support from Outsystems.

##### On your or your business associate’s premises

You and your BA are responsible for implementing Audit policies and procedures covering applications developed using OutSystems platform.

#### Implement the audit process

##### What you need to have and do

You need to evaluate existing system capabilities regarding audit logging and monitoring. Deploy the capability of recording and/or logging of user activity in information systems that store or process ePHI shall be deployed (e.g., hardware, software). You also need to audit users' activity and for the protection of audit logs for specific developed applications using the OutSystems platform.

##### How OutSystems can help you

##### For OutSystems IT users

Our management consoles do not contain ePHI. Permissions for OutSystems IT users are according to the principle of least privilege (PoLP), separately and uniquely for each production environment they need to access to perform their roles.
We audit the development of every screen, operation and any other logic.

The databases are equipped with an audit feature that logs the IT user’s access and activity on the database. If an IT user has direct access to the database and queries the data, an audit trail will be generated. Any auditing native mechanism of the database management system can be used with OutSystems.

##### For OutSystems End Users

As a best practice, we recommend developing modules that send information to your chosen security information and event management system (SIEM) or any other log collection mechanism. We also support logging the information to the logs available in the management consoles.

You can use OutSystems development capabilities to build an audit trail of the end user actions on your apps. You can then take the data captured on the audit trail and store it in the SIEM of your choice, leveraging SIEMs capabilities such as more control over the stored data, search capabilities or dashboards. Here more details on building and using your [audit trail](../../app-architecture/data/audit-trails.md).

As an added protection, the OutSystems platform supports the export of audit logs for specific developed applications, to a specific storage with anti-tampering mechanisms.

### Integrity § 164.312(c)(1) and Person or Entity Authentication § 164.312(d)

HIPAA requires you to implement policies and procedures to protect electronic protected health information from improper alteration or destruction.
You’ll need to implement procedures to verify that a person or entity seeking access to electronic protected health information is the one claimed.

#### Develop Information Classification Policies

##### What you need to have and do

You need to develop and formally approve an Information Classification Policy which establishes the protection requirements ensuring the integrity of ePHI can be maintained and validated.

##### How OutSystems can help you

OutSystems has defined internal policies and procedures regarding systems monitoring and logging, aligned with ISO 27001 - Annex A. These policies protect any data excerpts (possibly containing ePHI) you may need to send us in the context of receiving customer support from OutSystems.

#### Validate authenticity (A) 164.312(c)(2)

##### What you need to have and do

You need to evaluate the available authentication methods. Commonly used methods include:

* Password—something you know
* Token or smart card—something you have
* Fingerprint—something you are
* Multi-Factor—combination of two or more of the above methods

##### How OutSystems can help you

Best practice is to integrate the authentication of the management consoles and applications with a owning Identity Provider. In this case, the authentication methods are to be implemented in that provider.

###### For OutSystems IT users

The access management consoles include a built-in authentication mechanism.

OutSystems also supports end user authentication with external identity management providers by [changing the authentication provider](../../manage-platform-app-lifecycle/manage-it-teams/use-an-external-authentication-provider.md). In such cases, the platform delegates authentication to an assigned plugin, which validates user credentials and returns a unique user identifier. That unique identifier maps the authenticated user to an OutSystems IT user. [More details here](https://success.outsystems.com/support/security/outsystems_platform_server_hardening/#external-authentication-provider).

###### For OutSystems End Users

When you start developing a new module it has the built-in logic for end user authentication and respective configuration. Other than the built-in logic, OutSystems offers the four above commonly used methods for end user authentication. [More details here.](https://success.outsystems.com/support/security/outsystems_platform_server_hardening/#improving-end-user-authentication)

### Transmission Security § 164.312(e)(1) and Implement Integrity Controls (A) 164.312(e)(2)(i)

Implement technical security measures to guard against unauthorized access to electronic protected health information that is being transmitted over an electronic communications network.

#### Develop network security policies and procedures

##### What you need to have and do

Develop and formally approve a set of policies and procedures regarding Network Security. Make sure the policies and procedures  address the set of requirements for transmitting ePHI, and safeguarding ePHI, while in transit.

Identify:

* All approved parties who can transmit ePHI, if reasonable and appropriate, following your [access control policy](#access-control).

* Scenarios that may result in modification or disclosure of ePHI by unauthorized parties, while in transit.

Implement security mechanisms to ensure that electronically transmitted ePHI is not improperly modified by unauthorized parties.

##### How OutSystems can help you

* OutSystems fully supports [encryption of data in transit using SSL/TLS](https://www.outsystems.com/tk/redirect?g=3ae4c88e-73a8-4d8a-9a44-88f9b7c18d02) for which you need to install an SSL certificate. HTTPS can then be enforced at the request level on application screens and exposed SOAP Web Services and REST APIs.

* The security level defined at design time can be overridden by IT Managers or Administrators, as they can enforce the [HTTPS security of applications](../enforce-https-security.md). Requests are always secure in Reactive and Mobile apps.

* Since OutSystems runs on top of standard application servers, you can configure your servers for the desired TLS ciphers.

The minimal OutSystems network requirements for correct platform functioning can be found [here](../../setup-infra-platform/setup/network-requirements.md).
