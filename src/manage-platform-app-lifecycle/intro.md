---
summary: Explore application lifecycle management in OutSystems 11 (O11) using LifeTime for deployment, security, and IT user management across all environments.
tags: support-Application_Lifecycle; support-Application_Lifecycle-overview
locale: en-us
guid: e9f6f711-2df2-42a0-90c1-3b9bc8b3926b
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Managing OutSystems platform and application lifecycle

Application Lifecycle Management (ALM) is the continuous process of managing applications throughout their entire lifecycle: from development to maintenance.

## LifeTime Management Console

**LifeTime** is a unified console with visibility of all environments in your infrastructure. It manages the deployment of applications, IT users, and security across all environments.  

It allows you to increase the control over your factory in the following areas:

Application Deployment and Configuration
:   By having automated deployment processes across all environments, from Development to Production, you simplify processes and increase overall IT efficiency. When using the impact analysis feature, you become aware of the exact impact the deployment of an application will have in Production. Check how to [deploy applications in OutSystems](<../deploying-apps/intro.md>).

Hotfix Development and Deployment
:   Control exactly what is running in Production and easily replicate those versions back into Quality Assurance to fix and test defects with confidence. Check how to [apply a hotfix](<../deploying-apps/apply-a-hotfix.md>).

IT User and Team Management
:   Ensure Developers and Operators have the appropriate privileges in each environment. Simplified cross stage policies give you the control to make sure your application management processes are fast, low risk and efficient. Check how to [manage IT teams](<manage-it-teams/intro.md>).

Security
:   OutSystems supports external authentication providers and VPN usage in order to comply with your security requirements. Additionally, it provides out-of-the-box support for security features like brute-force protection attacks and applying Content Security Policy. Check how you can [secure your applications](<../security/intro.md>).

In LifeTime you have visibility over all environments in your infrastructure. To configure and monitor a specific environment, you can use the management console of the environment (Service Center).

### Daily synchronization

To keep LifeTime and your environments in sync, LifeTime automatically performs a daily synchronization operation. This operation includes the following data:

* IT Users, IT Roles and IT Teams
* Permissions
* Environment status
* Version information of Applications and Modules and their configurations

The synchronization should run while the infrastructure is on low activity. To change the starting time for the daily sync process in LifeTime:

* **Self-managed infrastructures**: Go to **Infrastructure** > **LifeTime Settings**. Then, edit the **Daily Synchronization schedule**.

* **OutSystems Cloud infrastructures**: Go to **Environments**, select **Options** on the right of the screen, and choose **LifeTime Settings**. Then, edit the **Daily Synchronization schedule**.
