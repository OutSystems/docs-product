# Flexible Updates EAP

<div class="info" markdown="1">

Flexible Updates is a feature currently available under an [Early Access Program](https://www.outsystems.com/eap/).

</div>

Flexible Upgrades is a feature that allows you to skip the "republish all modules" operation in your factory after a platform update. Instead, there's a new step called **module preparation** after upgrading Platform Server, where Platform Server compiles all your modules in the background using the new platform version, but without deploying them. 

<!--
The preparation step takes less time than the republish operation, and you can start using your upgraded Platform Server sooner.
-->

## Prerequisites

The Flexible Updates feature is available:

* in all OutSystems editions except Free
* when updating from OutSystems version 11.x to version 11.9 or later

## What's the module preparation step

An OutSystems update/upgrade now has two steps:

* Platform Server update/upgrade step
* Module preparation step

The module preparation step occurs after updating Platform Server to a new version. In this new step, Platform Server compiles all your modules in the background using the new platform version. For customers in the OutSystems Cloud, this operation takes place outside of your maintenance window, since it doesn't require any downtime.

While the module preparation is in progress, you can't publish any applications/modules in the environment, and you can't apply configurations. Once the module preparation step ends, your environment is ready and you can publish applications or modules again. You can follow the progress of module preparation in Service Center. For more information, see [Check the progress of the module preparation step](#).

Since you're not republishing your applications or modules during module preparation, your currently running applications aren't changed during the platform update/upgrade — you will publish your applications later, following your own schedule.

### Starting the module preparation step

<div class="info" markdown="1">

Applicable only to OutSystems On-premise installations.

</div>

The module preparation step is automatically triggered after the installing the new Service Center version and after publishing System Components.


## Check the progress of the module preparation step

You can check the progress of the module preparation step in **Service Center**.

After a successful Platform Server update and while there's an ongoing module preparation, Service Center displays a message similar to the following:

    SCREENSHOT  
    "Your environment has been successfully upgraded to Platform Server version 11.9.0 (see the Release Notes)."
    "We are now preparing your modules - 38%"

When module preparation finishes and there are no errors, Service Center displays a message similar to the following:

    SCREENSHOT
    "This environment is ready"

If there are errors, first try to republish the affected modules, and if this doesn't solve the issue, contact OutSystems Support.

<div class="info" markdown="1">

For **OutSystems on-premises installations**, you can also check the progress in Configuration Tool, in the window that appears after pressing **Apply/Exit**:

    SCREENSHOT
    Configuration Tool

</div>

## Check for module preparation errors

In some situations, there are errors during the module preparation step. These errors can be due to one of the following:

* A
* B

Lorem ipsum

    SCREENSHOT
    "There are errors in 12 of 256 modules."
