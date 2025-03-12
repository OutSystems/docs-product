---
summary: Explore best practices for developing and deploying LifeTime plugins in OutSystems 11 (O11) environments.
guid: 001b2cb1-c241-4f40-a4a4-4080b82bbfb7
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: plugin development, best practices, deployment, api usage, environment configuration
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - lifetime
coverage-type:
  - evaluate
---

# Best practices for LifeTime plugins

This article is a guide for the end-to-end lifecycle process of [LifeTime plugins](https://success.outsystems.com/Documentation/How-to_Guides/Development/How_to_create_a_LifeTime_Plugin), from the setup phase to the plugin deployment to production.

Make sure you have LifeTime installed in a dedicated environment. **Installing LifeTime in an existing environment is not supported from version OutSystems 11 onwards.**

## Setting up the plugins development environment

Our recommendation is that you use your application development environment to develop your LifeTime plugins.

Unless you have specific development needs or restrictions that make you have a separate environment to develop your LifeTime plugins, the lifecycle of your plugins will be simpler if you use the same application development environment.

For the environment sizing and configuration, consider also the following:

* The plugins development environment will contain a bundle of sample data imported from your LifeTime environment.

* You can use [LifeTime Services API](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_Services_API) and [LifeTime Deployment API](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_Deployment_API) to complement the set of functionality that [LifeTime SDK](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_SDK) already provides you with. These LifeTime APIs are only available in the LifeTime environment.

Set up the development environment of your LifeTime plugins following the [steps described in this topic](https://success.outsystems.com/documentation/how_to_guides/development/how_to_create_a_lifetime_plugin/).

## Developing your plugins

The development process of your LifeTime plugins should be similar to the process of developing a regular application, depending on the specific requirements of your plugin.

However, a LifeTime plugin usually depends on LifeTime services and data. Therefore, during the development of your plugin, keep the following in mind:

* LifeTime plugins can only be deployed to environments containing the LifeTime SDK. Beware of unintended dependencies from other applications to your LifeTime plugin or the LifeTime SDK, as these dependencies can prevent you from successfully deploy those applications.

* Develop against updated sample data as much as possible to minimize misbehaviors. Export the sample data from LifeTime environment during the [setup process](https://success.outsystems.com/documentation/how_to_guides/development/how_to_create_a_lifetime_plugin/), and refresh it periodically, executing the "Export Sample Data" step of that process when needed.

* If you want to use use [LifeTime Services API](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_Services_API) or [LifeTime Deployment API](https://success.outsystems.com/Documentation/10/Reference/OutSystems_APIs/LifeTime_Deployment_API), consume these APIs from the LifeTime environment, since they are not deployed with the LifeTime SDK. Be mindful of this and advise other developers, as any API action that modifies data will be modifying real LifeTime data.

* Consider safeguarding new features behind feature toggles. With these toggles, you can quickly disable a new feature if it happens to misbehave when the plugin is deployed to production.

## Assuring the quality of your plugins

Although it is an industry practice to have an dedicated environment for Quality Assurance, the lifecycle of your LifeTime plugin will be more complex having an additional environment.

Since a LifeTime plugin project has usually a smaller scope than regular applications, and considering the additional setup and maintenance effort to keep an additional environment in the plugin lifecycle, our recommendation is to go without a QA environment.

Anyway, you should evaluate the benefit of having a QA environment against the characteristics of your LifeTime plugin and the requirement of your own application project.

If you decide to have a QA environment in the lifecycle of your LifeTime plugin, consider the following:

* Similar to your plugin development environment, we recommend that you use your application QA environment to be the QA environment for your LifeTime plugin.

* The Lifetime SDK and sample data must be installed in the plugin QA environment as well. For this, follow the [setup process](https://success.outsystems.com/Documentation/How-to_Guides/How_to_create_a_LifeTime_Plugin) for the QA environment, since you cannot deploy the Lifetime SDK from development to QA environment using LifeTime.

* Be sure to refresh the sample data in your plugin QA environment periodically.

* You can deploy your LifeTime plugin from development to QA using LifeTime, like regular applications.

## Deploying your plugins to production

Deploying a LifeTime plugin to production is different than regular applications deployment, since the environment to where you will deploy is the LifeTime environment, and not the applications production environment.

Since you cannot use LifeTime to deploy your plugin to the LifeTime environment, you must use Service Center application packs (.oap) or solution packs (.osp) to do the final deploy:

1. Go to the Service Center console of your plugin development environment (or QA environment, if you have one).

1. If your LifeTime plugin does not have external dependencies, go to your LifeTime plugin Application page and download the application pack (.oap). Otherwise, create a Solution for your plugin including all external dependencies, and download the new Solution version you created (.osp). You can also opt to use Solutions for easily handle versioning.

1. Go to the Service Center console of your LifeTime environment. Upload and publish the Application or Solution downloaded in the previous step.

The permissions to deploy to the environments managed by LifeTime is configured in LifeTime. However, since LifeTime environment is not managed by itself, you need to configure the deployment permissions using the Service Center console of LifeTime environment.
