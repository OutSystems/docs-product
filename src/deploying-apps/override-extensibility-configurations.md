---
summary: Override default mobile extensibility configurations in specific environments using OutSystems 11 (O11).
tags: runtime-mobile
locale: en-us
guid: 09207082-720b-48a1-980b-e8937925e461
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=257:766
---

# Override the Default Mobile Extensibility Configurations

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

The [default Extensibility configurations](mobile-app-packaging-delivery/customize-mobile-app/intro.md) of an OutSystems mobile app are defined at design time in the application home module. However, there are some situations when it is necessary to have different extensibility configurations for different environments.

For example, the development team needs to troubleshoot an issue in a plugin used by a mobile app, so they want to increase the plugin logging level in the development environment only, keeping the default logging level in quality and production environments.

With OutSystems you can override, for a specific environment, the default Extensibility Configurations that were defined at design time, with no need to manually change and deploy the application in that environment.

To override the Extensibility Configurations of your mobile app for a specific environment, do the following:

1. In LifeTime management console, go to the details page of the application.

1. Press the **Settings** link.  

    ![Screenshot showing how to access the settings link in the LifeTime management console for a mobile app](images/override-extensibility-configurations-1.png "Accessing Application Settings in LifeTime Console")

1. Choose the environment where you want to override the Extensibility Configurations. The application must be already deployed in that environment.  

    ![Image depicting the selection of a specific environment in the LifeTime console to override extensibility configurations](images/override-extensibility-configurations-2.png "Selecting Environment for Extensibility Configurations")

1. In the **Advanced** section, you will see the default Extensibility Configurations that were defined at design time. Choose the **Custom** option.

    ![Screenshot of the Advanced section in LifeTime console showing the default Extensibility Configurations](images/override-extensibility-configurations-3.png "Default Extensibility Configurations Section")

1. Use the **Copy from Default** button to copy the default configurations to the custom field.

1. In the Custom field, change only the configurations that need to be different for that environment, keeping the remaining configurations as is. Make sure the development team validates or provides you with the custom configurations.

    ![Image illustrating the process of customizing extensibility configurations for a mobile app in a specific environment](images/override-extensibility-configurations-4.png "Customizing Extensibility Configurations")

1. Press the **Save** button.

Now, when a new mobile app package is generated in this environment, the custom configurations will override the default configurations defined in the application module. Also, the custom configurations will be kept for the environment after new application deployments.

## Known issue with the JSON size limit in LifeTime Extensibility Configuration

<div class="info" markdown="1">

Applies only to:

* LifeTime, versions earlier than 11.6.1 **with**
* Platform Server, versions earlier than 11.10.0

</div>

In LifeTime earlier than version 11.6.1 the Extensibility Configuration JSON has a character limit. If you go over the limit, the following error shows: **Failed to deserialize JSON to REST_ErrorRecord: Unexpected character encountered while parsing value: <. Path '', line 0, position 0.**

You can resolve the issue by:

* Upgrading **both** LifeTime to 11.6.1 or later and Platform Server to version 11.10.0 or later.

Or by:

* Editing the Extensibility Configuration JSON in Service Studio.
