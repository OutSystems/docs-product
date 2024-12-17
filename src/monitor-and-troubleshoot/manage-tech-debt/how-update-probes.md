---
tags: 
summary: OutSystems 11 (O11) is not mentioned in the provided article, which focuses on updating AI Mentor Studio probes.
locale: en-us
guid: d11dd771-148b-49fd-8bfd-dfe0800620c5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=929:738
---

# How to update the AI Mentor Studio probes

<div class="info" markdown="1">

To check the current version of your AI Mentor Studio probes, click the **Help** icon on the top-right corner of AI Mentor Studio and then select **About AI Mentor Studio**.

</div>

If you have [**Full Control** permissions assigned as a default role](how-works.md#update-probes) for the code analysis environment, the following message is displayed when an updated version of the probes is available: 

![Notification message in AI Mentor Studio indicating an update is available for users with Full Control permissions](images/probes-update-full-ams.png "AI Mentor Studio Full Control Update Notification")

After selecting **How to download and update probes**, you go to the **Probes download and update** screen, where you can download the new probes.

![Probes download and update screen in AI Mentor Studio showing options to download new probes](images/probes-procedure-ams.png "AI Mentor Studio Probes Download and Update Screen")

If you have a different permissions level, the following message is displayed when an updated version of the probes is available:

![Notification message in AI Mentor Studio indicating an update is available for users with limited permissions](images/probes-update-listapp-ams.png "AI Mentor Studio Limited Permissions Update Notification")

To install the new probes for AI Mentor Studio, contact your infrastructure administrator.

## Prerequisites

Before configuring the proxy in AI Mentor Studio, make sure you have [**Full Control** permissions assigned as a default role](how-works.md#update-probes) for the code analysis environment.

## Update probes

If you have a previous version of the probes installed there's no need to uninstall it prior to installing the new version of the probes.  
To update the AI Mentor Studio's probes, follow these steps:

1. In the **Probes download and update** screen, select **Download Development probe**.

1. Go to the Service Center console of the **Development environment** (`https://<development_environment>/ServiceCenter`), and install the **Development Environment Probe** in your **Development environment** by following these steps:

    1. Go to **Factory**.
    1. Go to **Solutions**.
    1. Select **Upload & Publish a Solution**.
    1. Select **Choose File** and select the Probe file.
    1. Select **1-Click Publish**.
    1. Validate if the Solution is successfully published by checking for a `Done: The solution was successfully published message`.

    ![Step-by-step instructions for installing the Development Environment Probe in the Service Center console](images/setup-install-probes-sc.png "Service Center Probes Installation Steps")

1. In the **Probes download and update** screen, select **Download LifeTime probe**.

1. Go to the Service Center console of the **LifeTime environment** (`https://<LifeTime_environment>/ServiceCenter`), and install the **LifeTime Environment Probe** in your **LifeTime environment** by following these steps:

    1. Go to **Factory**.
    1. Go to **Solutions**.
    1. Select **Upload & Publish a Solution**.
    1. Select **Choose File** and select the Probe file.
    1. Select **1-Click Publish**.
    1. Validate if the Solution is successfully published by checking for a `Done: The solution was successfully published message`.

