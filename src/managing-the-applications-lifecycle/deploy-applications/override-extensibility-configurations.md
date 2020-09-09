---
summary: Override the default Extensibility Configurations of a mobile app for a specific environment.
tags: runtime-mobile
---

# Override the Default Mobile Extensibility Configurations

The [default Extensibility configurations](../../deliver-mobile/customize-mobile-app/intro.md) of an OutSystems mobile app are defined at design time in the application home module. However, there are some situations when it is necessary to have different extensibility configurations for different environments.

For example, the development team needs to troubleshoot an issue in a plugin used by a mobile app, so they want to increase the plugin logging level in the development environment only, keeping the default logging level in quality and production environments.

With OutSystems you can override, for a specific environment, the default Extensibility Configurations that were defined at design time, with no need to manually change and deploy the application in that environment.

To override the Extensibility Configurations of your mobile app for a specific environment, do the following:

1. In LifeTime management console, go to the details page of the application.

1. Press the **Settings** link.  

    ![](images/override-extensibility-configurations-1.png?width=700)

1. Choose the environment where you want to override the Extensibility Configurations. The application must be already deployed in that environment.  

    ![](images/override-extensibility-configurations-2.png?width=400)

1. In the **Advanced** section, you will see the default Extensibility Configurations that were defined at design time. Choose the **Custom** option.

    ![](images/override-extensibility-configurations-3.png)

1. Use the **Copy from Default** button to copy the default configurations to the custom field.

1. In the Custom field, change only the configurations that need to be different for that environment, keeping the remaining configurations as is. Make sure the development team validates or provides you with the custom configurations.

    ![](images/override-extensibility-configurations-4.png)

1. Press the **Save** button.

Now, when a new mobile app package is generated in this environment, the custom configurations will override the default configurations defined in the application module. Also, the custom configurations will be kept for the environment after new application deployments.

> NOTE! Lifetime has an open issue which limits your configuration length to be **max 555 characters of valid JSON data**. If your custom configuration is longer than this, you will receive an error:
>
> ![](images/override-extensibility-configurations-error-long-json.png)
