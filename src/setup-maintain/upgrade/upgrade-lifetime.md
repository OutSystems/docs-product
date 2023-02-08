---
summary: This article describes the process to upgrade the LifeTime management console of your OutSystems infrastructure to Release Sep.2018 (11.0.108.0) or later, and what you must take into consideration during that process.
tags: 
locale: en-us
guid: 1dd579f8-20ca-4af9-89fa-40697272f8bc
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---
# Upgrade LifeTime management console

This article describes the process to upgrade the **LifeTime management console** of your OutSystems infrastructure to **Release Sep.2018 (11.0.108.0) or later**, and what you must take into consideration during that process.

Keeping your LifeTime management console upgraded enables you to benefit from the latest features and fixes. OutSystems releases a new LifeTime version on a monthly basis.

## Context

Up to version **OutSystems 10**, upgrading OutSystems to a new major version means upgrading all the infrastructure - LifeTime management console and the application environments.

![](images/upgrade-lifetime-o10-diag.png?width=800)

From version **OutSystems 11 onwards**, LifeTime is distributed independently from the Platform Server, which enables both components to have different upgrading pace.

**LifeTime Release Sep.2018 (11.0.108.0)** marks the beginning of [LifeTime's own release cycle](https://success.outsystems.com/Support/Release_Notes/OutSystems_Product_Releases#release-cycles), allowing better and faster improvements in your LifeTime management console.

Upgrading LifeTime to Release Sep.2018 or later **does not require** the upgrade of your OutSystems application environments. You can benefit from LifeTime latest features and still keep your application environments in a previous supported version while you need.

![](images/upgrade-lifetime-o11-diag.png?width=800)

## Before the upgrade

Check the [breaking changes for LifeTime Management Console](https://success.outsystems.com/Support/Release_Notes/Lifetime_Management_Console).

If you have **LifeTime plugins** deployed in your LifeTime environment or **other integrations with this environment** - applications or systems interacting directly with the environment through OutSystems APIs made available via REST or SOAP - you must do the following:

* Assess how this upgrade can impact your plugins and integrations by checking the following:

    * [LifeTime Breaking Changes](https://success.outsystems.com/Support/Release_Notes/LifeTime_Management_Console#Breaking_Changes)

    * [OutSystems 11 Side Effects and Breaking Changes](https://success.outsystems.com/Support/Release_Notes/11/OutSystems_11_side_effects_and_breaking_changes)

* Make the necessary changes in your plugins and integrations before LifeTime upgrade takes place, to ensure that they will work correctly after the upgrade.

<div class="info" markdown="1">
 
If you are running an OutSystems version that's not supported anymore, you first need to [upgrade to a supported OutSystems version](upgrade-platform.md).
 
</div>

## LifeTime upgrade process

### OutSystems Cloud { #cloud }

In the OutSystems Cloud, the process of upgrading the LifeTime management console is managed by OutSystems, coordinating with you in every step of the way, to guarantee a successful and as effortless as possible procedure:

1. You request the upgrade of your LifeTime management console to a supported upper version, by opening a Support Case using [any of the available mechanisms](https://www.outsystems.com/legal/success/contact-outsystems-technical-support/).

1. OutSystems will promptly contact you to schedule and plan the LifeTime management console upgrade.

1. On the scheduled time frame, OutSystems will upgrade the LifeTime management console in your OutSystems Cloud infrastructure. **During the upgrade, your LifeTime management console and any installed LifeTime plugins will be unavailable.**

1. You will receive a notification email when the upgrade is concluded.

1. If you have **LifeTime plugins** or **integrations**, you should republish all plugins [as described below](#after-upgrade).

### Self-managed (private cloud / on-premises) { #on-prem }

If the environment is self-managed (running in your own private cloud or on-premises) the upgrade process is fully managed by you, without the direct involvement of OutSystems. However, at any time you can [ask OutSystems Support](https://www.outsystems.com/legal/success/contact-outsystems-technical-support/) for assistance if you have any questions or get any errors in the process.​

To upgrade the LifeTime management console to Release Sep.2018 or later, the following **requirements** must be met:

* Your **OutSystems application environments** are running a **supported OutSystems version**. If you are running an OutSystems version that's not supported, you must [upgrade to a supported OutSystems version](upgrade-platform.md).

* Your **LifeTime management console** is installed in a **dedicated environment**. If your LifeTime management console is installed in a shared environment (for example, in your production environment), you must [reinstall LifeTime in a dedicated environment](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Reinstall_the_infrastructure_management_console_in_a_dedicated_environment).

After assuring the above requirements are met, do the following to upgrade the LifeTime management console:

1. Download the latest [LifeTime management console binaries](https://www.outsystems.com/downloads) from the downloads area.

1. Follow the installation checklist that is launched when you run the LifeTime management console installation binary. **During the upgrade, your LifeTime management console and any installed LifeTime plugins will be unavailable.**

1. If you have **LifeTime plugins** or **integrations**, you should republish all plugins [as described below](#after-upgrade).

### Hybrid infrastructure

OutSystems hybrid infrastructures have the LifeTime environment running in OutSystems Cloud, therefore the upgrade process is the same as [OutSystems Cloud upgrade process](#cloud).

<div class="warning" markdown="1">
 
Hybrid configuration is only supported in OutSystems licenses purchased before January 2020.
 
</div>

## After the upgrade { #after-upgrade }

If you don’t have any **LifeTime plugins** or **integrations**, your LifeTime management console is ready to use.

If you have **LifeTime plugins** deployed in your LifeTime environment, you should republish all plugins to avoid runtime errors:

* Open the Service Center console of your LifeTime environment (for example, `https://<lifetime_environment>/ServiceCenter`).

* Go to the **Factory** section, and then to the **Solutions** area.

* Create a solution containing all the modules of your LifeTime plugins.

* Publish the solution.

After the solution has been published, test all your plugins.

Test also your integrations with LifeTime environment to ensure they're working correctly.

## Frequently asked questions

**How do I know which LifeTime version I’m running?**  
Learn how to identify your LifeTime version [here](https://success.outsystems.com/Support/Release_Notes/Check_what_OutSystems_version_you_are_using#lifetime).

**I’m running OutSystems 10. If I want to upgrade my LifeTime to OutSystems 11, must I also upgrade my application environments to OutSystems 11?**  
No. You can upgrade LifeTime and keep your application environments in any supported version. LifeTime 11 is compatible with OutSystems 10 environments.

**I’m running OutSystems 10. If I want to upgrade my LifeTime to OutSystems 11, will anything stop working due to breaking changes?**  
If you don’t have LifeTime plugins or other integrations with the LifeTime environment (eg. using LifeTime APIs to integrate with external tools, such as Jenkins) there will be no impact. If you have LifeTime plugins or other integrations, you should [prepare your applications for the upgrade](upgrade-lifetime.md#before-the-upgrade).

**I’m running OutSystems 10 and I have LifeTime plugins. If I want to upgrade my LifeTime to OutSystems 11, must I also upgrade my application environments to OutSystems 11?**  
You can either develop your plugins in the LifeTime environment directly or upgrade all your application environments to OutSystems 11.

**I’m running OutSystems 11. Must I upgrade all my application environments to the latest version whenever LifeTime is upgraded?**  
No. You can keep your application environments in the same Platform Server version.

**Do I need to continuously upgrade LifeTime in my infrastructure?**  
LifeTime is now [released on monthly basis](https://success.outsystems.com/Support/Release_Notes/OutSystems_Product_Releases). Keeping your LifeTime upgraded enables you to benefit from the latest features and fixes.

### OutSystems Cloud or hybrid infrastructures

**I’m getting an error in LifeTime, that is fixed in the latest LifeTime version. How can I have my LifeTime upgraded to the latest version?**  
You can request the upgrade of your LifeTime management console to the latest version, by opening a Support Case using [any of the available mechanisms](https://www.outsystems.com/legal/success/contact-outsystems-technical-support/).

**I have a hybrid infrastructure. What is the LifeTime maintenance window if most of my environments are self-managed (private cloud / on-premises)?**  
The LifeTime environment runs in OutSystems Cloud and shares its maintenance window with your non-production Cloud environments. To define the maintenance window for LifeTime, follow the steps in [Define the maintenance window for LifeTime environment](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Define_a_maintenance_window_for_OutSystems_Cloud_environments).

**My LifeTime is being upgraded. When can I use LifeTime again after the upgrade?**  
You will receive a notification email when the upgrade is finished. LifeTime will be partially unavailable during the upgrade, which means you won't be able to stage deployments, activate new cloud services, or use your LifeTime plugins and integrations. Having a defined maintenance window, assures your upgrades are scheduled for the time that better fits your needs.
