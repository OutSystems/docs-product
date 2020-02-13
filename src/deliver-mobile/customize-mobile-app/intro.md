---
summary: Customize your mobile app regarding device characteristics and mobile platform, thus fulfilling business requirements or improve the experience of your users.
tags: runtime-mobile
---

# Customize Your Mobile App

Mobile apps can be customized allowing you to define global or mobile platform specific configurations, fulfilling business requirements or improve the experience of your users for all different screen sizes.

The configurations you can define for your app are:

* The preferences and configurations for your app (as the app orientation and minimum acceptable operating system version) 
* Icons of the app to display in the iOS and Android menus 
* Set custom splash screens for all available screen sizes 
* Customize the application status bar (like changing its background color or making it transparent) 
* [Create a plugin to extend the capabilities of your mobile apps](<../../extensibility-and-integration/mobile-plugins/using-cordova-plugins.md>)

To define these advanced configurations, go to the properties of your application's home module and open the **Extensibility Configurations** property. Its value is a JSON string where you can indicate the configurations you want. Check its [schema and constraints](<extensibility-configurations-json-schema.md>) for more info.

![](images/customize-mobile-app-1.png?width=700)

These configurations that you define at design time in your module are the default configurations. If you need to have different extensibility configurations for a specific environment, the default configurations can be [overridden for that environment](../../managing-the-applications-lifecycle/deploy-applications/override-extensibility-configurations.md) in LifeTime.
