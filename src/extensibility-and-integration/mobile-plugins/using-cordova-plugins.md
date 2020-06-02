---
summary: Create your own mobile plugin by wrapping an Apache Cordova plugin into an OutSystems module. Reference the plugin from the npm registry or git repository, or write it from zero.
tags: runtime-mobile; support-Integrations_Extensions; support-Mobile_Apps
---

# Using Cordova Plugins

Use Apache Cordova plugins by wrapping them into modules which you can then reference in your mobile apps. To get started, you can clone the [Template Plugin from Forge](<https://www.outsystems.com/forge/component-overview/1676/template-plugin/>) which has the groundwork for all custom Cordova plugins. You must wrap each plugin in its own dedicated module and application, meaning that if you want to use several plugins you must create an application for each plugin, each containing a single wrapper module. The relevant actions and entities of the wrapper module must be public. The wrapper module should have a meaningful name (for example, "SamplePlugin"). A module that wraps a Cordova plugin should not reference another module that also wraps a Cordova plugin.

The functionality of Cordova plugins can be tested in native mobile applications only.

This document demonstrates wrapping an existing Cordova plugin into a module. 
For step by step instructions on how to create and wrap your own Cordova plugin, read the following blog post: [How to Create a Cordova Plugin from Scratch](<https://www.outsystems.com/blog/posts/how-to-create-a-cordova-plugin-from-scratch/>).


## Referencing Cordova Plugins

Wrap a Cordova plugin through the **Extensibility Configuration** module property. Specify the plugin using one of the following keys within the JSON settings:

* the public repository URL (the value of the `url` key)
* the Cordova identifier (the value of the `identifier` key)
* the ZIP file from **Resources** folder from the **Data** tab (the value of the `resource` key)

Unless it’s a [plugin supported by OutSystems](intro.md) and you are using a public repository to reference the plugin, it is recommended to fork the plugin repository or to use a tagged version (for example, `https://example.com/sampleplugin/sampleplugin.git#1.1.0`). This prevents breaking changes in the plugin and the applications using it. Additionally, if tags are not used, two different builds may produce different results. This is especially important on deployments across one or more environments, where testing in one environment may be invalidated by a different build that is generated for another environment.

The JSON can be used for additional settings needed by the plugin. For the full description of the JSON check the article [Extensibility Configurations JSON Schema](<../../deliver-mobile/customize-mobile-app/extensibility-configurations-json-schema.md>).

![](<images/plugin-exensibility-window.png>)

### JSON Examples

This is a sample JSON file for the **Extensibility Configuration** module property. Note that you can use only one of the plugin references in the `plugin` key: `url` or `identifier` or `resource`.

A plugin from the npm registry:

```javascript
{
    "plugin": {
        "identifier": "sampleplugin"
    }
}
```

A plugin from a git repository:

```javascript
{
    "plugin": {
        "url": "https://example.com/sampleplugin/sampleplugin.git#1.1.0"
    }
}
```

A plugin from a ZIP file:

```javascript
{
    "resource": "my-plugin.zip",
    "plugin": {
        "resource": "my-plugin"
    }
}
```

The file is placed in **Resources** folder of the **Data** tab, in the file `my-plugin.zip`. Select **Do Nothing** in the **Deploy Action** attribute of the **Resource** property. The location of `plugin.xml` within the zip file is `my-plugin\plugin.xml`. In the `plugin.xml` file, there is `id="my-plugin"` attribute within the root `plugin` element.

If the plugin requires additional arguments, you can supply them in the `name` and `value` key-value pairs. 
Here is an example:

```javascript
{
    "plugin": {
        "url": "https://example.com/sampleplugin/sampleplugin.git",
        "variables": [
            {
                "name": "<plugin_var1>",
                "value": "<value_var1>"
            },
            {
                "name": "<plugin_var2>",
                "value": "<value_var2>"
            }
        ]
    }
}
```

## Wrapper Module Structure

Each plugin should have a `Check<Capability>Plugin` action (e.g. "CheckCameraPlugin") with an IsAvailable output parameter of type Boolean. This enables you to check if the plugin is available in the target module.

Create actions within the wrapper module and add a JavaScript flow element with the variables. Make the actions public so that they are available in the application. Write the descriptions for all the public actions, inputs and outputs. This helps when using the module in the target application.

![](<images/plugin-exensibility-actions.png>)

Insert the code that connects the wrapper to the Cordova plugin into a JavaScript element:

![](<images/plugin-exensibility-js.png>)
