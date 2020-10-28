# Flexible Updates EAP

<div class="info" markdown="1">

Flexible Updates is a feature currently available under an [Early Access Program](https://www.outsystems.com/eap/).

</div>

Flexible Upgrades is a feature that allows you to skip the "republish all modules" operation in your factory after a platform update. Instead, there's a new step called **module preparation** after upgrading Platform Server, where the platform compiles all your modules in the background using the new platform version, but without deploying them.

<!--
The preparation step takes less time than the republish operation, and you can start using your upgraded Platform Server sooner.
-->

## Prerequisites

The Flexible Updates feature is available:

* in all OutSystems editions except Free
* when updating from OutSystems version 11.x to version 11.9 or later

## Module preparation

An OutSystems update/upgrade now has two steps:

* the Platform Server update/upgrade step
* the module preparation step

The **module preparation** step occurs after updating Platform Server to a new version. In this new step, Platform Server compiles all your modules in the background using the new platform version. For customers in the OutSystems Cloud, this operation takes place outside your maintenance window, since it doesn't require any downtime.

While the module preparation is in progress, you can't publish any applications/modules in the environment, and you can't apply configurations. Once the module preparation step ends, your environment is ready and you can publish applications or modules again. You can follow the progress of module preparation in Service Center. For more information, see [Checking the progress of the module preparation step](#progress).

Since you're not republishing your applications or modules during module preparation, your running applications aren't changed during the platform update/upgrade — you'll publish your applications later, according to your own schedule. When you publish a module after the module preparation step, the platform reuses the compilation artifacts generated during this step.

## Starting the module preparation step

<div class="info" markdown="1">

In the **OutSystems Cloud**, the module preparation step starts automatically during the upgrade process. See how to [check the progress of the module preparation step](#progress).

</div>

When updating an on-premises Platform Server installation, the module preparation step starts after you install the new Service Center version and publish System Components.

When you click **Apply and Exit** in Configuration Tool, as mentioned in the installation checklist, the Configuration Tool asks you if you wish to go ahead with the following tasks:

* Publishing the latest version of Service Center
* Publishing the latest version of System Components
* Prepare modules

Press **OK** to start the publishing and module preparation tasks.

Note: Closing the Configuration Tool during the module preparation step doesn't interrupt the operation.

## Checking the progress of the module preparation step { #progress }

You can check the progress of the module preparation step in **Service Center**.

After a successful Platform Server update and while there's an ongoing module preparation, Service Center displays a message like the following:

    SCREENSHOT  
    "Your environment has been successfully upgraded to Platform Server version 11.9.0 (see the Release Notes)."
    "We are now preparing your modules - 38%"

When module preparation finishes and there are no errors, Service Center displays a message like the following:

    SCREENSHOT
    "This environment is ready"

Sometimes there are errors during the module preparation step — learn how to [check for module preparation errors](#check-for-errors) and what you should do to fix them.

<div class="info" markdown="1">

In **on-premises installations**, you can also check the progress in Configuration Tool, in the window that appears after pressing **Apply/Exit**:

    SCREENSHOT
    Configuration Tool

</div>

## Checking for module preparation errors { #check-for-errors }

When there are errors in module preparation step, Service Center displays the error count in a banner message like the following:

    SCREENSHOT
    "There are errors in 12 of 256 modules."

These errors can be due to one of the following:

* A
* B

When there are errors, try to republish the affected modules. If this doesn't solve the issue, [contact OutSystems Support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support).
