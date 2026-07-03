---
summary: How OutSystems FedRAMP and Knox Systems hosting support FedRAMP Certification Class C (Moderate) controls, and where to find the authoritative compliance artifacts.
tags:
  - Authentication
  - Authorization
  - IdP
  - Infrastructure
  - Monitoring
  - Security
locale: en-us
guid: d83fe8d1-da3c-4d24-be18-ca04036345a9
app_type: traditional web apps, reactive web apps
platform-version: o11
figma:
audience:
  - Tech lead
  - Platform administrator
outsystems-tools:
  - none
coverage-type:
  - understand
isautopublish: true
---

# How OutSystems enables FedRAMP controls

OutSystems FedRAMP operates through the Authority to Operate (ATO) held by [Knox Systems](https://knoxsystems.com/platform), at Certification Class C (Moderate). This article explains, at a high level, how the platform and Knox Systems hosting work together to support applicable FedRAMP controls, so you can evaluate the platform for your own compliance process.

<div class="info" markdown="1">

This article is a conceptual overview. The authoritative description of how OutSystems FedRAMP implements each control is in the System Security Plan (SSP), available through the FedRAMP Marketplace.

</div>

## Shared responsibility for controls

FedRAMP controls are shared between the platform provider and the customer, following the [OutSystems Cloud shared responsibility model](https://www.outsystems.com/tk/redirect?g=b04339ce-7b9f-4c93-94b7-e4cf397eab47):

* **Knox Systems and OutSystems** are responsible for the controls that apply to the hosting environment and the platform: infrastructure, monitoring, encryption, personnel, and continuous compliance.
* **You** are responsible for the controls that apply to the applications you build, including secure application design and validating the security of the components you use.

This model doesn't change from the standard OutSystems Cloud offering. You remain responsible for architecting secure applications.

## How the platform supports control areas

The following table maps common FedRAMP Certification Class C control areas to how OutSystems FedRAMP and Knox Systems address them. It's a summary, not a complete control implementation.

| Control area | How OutSystems FedRAMP supports it |
| --- | --- |
| Identification and authentication | IT users and end users authenticate through an external Identity Provider (IdP), with multi-factor authentication (MFA) enforced. The built-in IdP isn't available for IT users. Refer to [Getting started with OutSystems FedRAMP](getting-started.md). |
| Access control | Knox Systems generates and administers the AWS accounts, Virtual Private Clouds (VPCs), and subnets. All traffic enters a Knox-administered environment. |
| System and communications protection | Data is encrypted, with Knox Systems holding the encryption keys. Service Studio is configured for Federal Information Processing Standards (FIPS) compliance, and data is kept within the FedRAMP authorization boundary. |
| Audit and accountability | Knox Systems monitors OutSystems 11 and facilitates monthly reporting and annual third-party compliance audits. |
| Contingency planning | High availability across multiple AWS Availability Zones within the US East region is included for every customer. |
| Personnel security | All support personnel with access to the OutSystems FedRAMP platform are US-based, US citizens, vetted by Knox Systems and OutSystems. |

## Authorization and compliance artifacts

Refer to [OutSystems FedRAMP overview](fedramp-overview.md#ato-types) for a description of the applicable Authorizations to Operate (ATO).

OutSystems and Knox Systems maintain the following compliance artifacts, which a Third-Party Assessment Organization (3PAO) audits each year:

* **System Security Plan (SSP)**: Describes how OutSystems FedRAMP implements FedRAMP controls.
* **Security Assessment Report (SAR)**: The output of the annual 3PAO audit.
* **Plan of Action and Milestones (POA&M)**: Tracks new and ongoing risks, each mapped to a FedRAMP control with a remediation plan. US agencies review POA&Ms monthly.

Your agency references these artifacts when issuing its own Agency-level ATO.

## Verify the certification

Verify the OutSystems 11 Certification on the [FedRAMP Marketplace](https://www.fedramp.gov/marketplace/products/F1206111371/), listed under Knox Systems.
