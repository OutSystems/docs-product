---
summary: Explore how to customize the application status bar in mobile apps using OutSystems 11 (O11) without plugins.
tags: custom ui development, mobile app design, ui customization, application development, user experience enhancements
locale: en-us
guid: 3a9110d2-7128-413c-a6a4-3b2deed94d87
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=307:224
audience:
  - mobile developers
  - frontend developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Customize the Application Status Bar

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

Since MABS 11, the native status bar in mobile apps has been transparent and appears in front of the app content by default. This behavior can be customized without using any plugin by following the instructions presented in the next section.

For previous MABS versions, the status bar is black and above the app content by default.

## Customizing the Status Bar

1. In Service Studio, open the **home module** of your mobile app. 

2. In the module tree, select the module and, in the properties editor, open the Extensibility Configurations property editor window: 

    ![Screenshot of the Extensibility Configurations property editor in Service Studio](images/ss_extensibility_in_module_properties.png "Extensibility Configurations in Module Properties")

3. Add the JSON properties to customize your application status bar according to the reference information presented below.  
    If you already have some extensibility configurations defined in the module, add the new content making the necessary adjustments.

4. After customizing the status bar you must install an [updated build of the mobile app](<../mobile-app-update-scenarios.md#situations-when-the-user-must-install-a-new-build>) on the devices for the changes to take effect. 

## Status Bar Customization Reference

Property  |  Values  |  Description  
---|---|---  
StatusBarOverlaysWebView  |  `true` <br/> `false` |  Defines whether the content of your app starts after the status bar or can appear behind the status bar.<br/>If set to `true` or **not set** in MABS 11 or newer, the content will appear behind the status bar.<br/>If set to `false` or **not set** in MABS 10, the content will start after the status bar.
StatusBarBackgroundColor  |  `#000000` to `#FFFFFF` |  The background color of the status bar. This is only used when the app content starts after the status bar.<br/>Expected color format: `#RRGGBB`.  
StatusBarStyle  |  `default` <br/> `lightcontent` <br/> `darkcontent` |  Defines the style of the status bar text and icons.<br/>When set to `default` (or **not set**), the status bar text and icons appear with the mobile platform's default color.<br/>When set to `lightcontent` or `darkcontent`, the status bar text and icons appear in a light or dark color defined by the mobile platform.

## Status Bar JSON Template

Use the following template as a reference for defining a custom behavior for the application status bar. Depending on your use case, you can include just one of the properties in your extensibility configurations:

```javascript
{
    "preferences": {
        "global": [{
            "name": "StatusBarOverlaysWebView",
            "value": "<value>"
        },
        {
            "name": "StatusBarBackgroundColor",
            "value": "<#RRGGBB>"
        },
        {
            "name": "StatusBarStyle",
            "value": "<value>"
        }]
    }
}
```

## Examples

### Transparent Status Bar in Full Screen App

![Example of a mobile app with a transparent status bar in full screen mode](images/transparent_statusbar.png "Transparent Status Bar Example")

```javascript   
{
    "preferences": {
        "global": [{
            "name": "StatusBarOverlaysWebView",
            "value": "true"
        }]
    }
}
```

### Status Bar with a Different Color

![Example of a mobile app with a status bar colored in gold](images/differentcolor_statusbar.png "Colored Status Bar Example")

```javascript        
{
    "preferences": {
        "global": [{
            "name": "StatusBarOverlaysWebView",
            "value": "false"
        },
        {
            "name": "StatusBarBackgroundColor",
            "value": "#AF9200"
        }]
    }
}
```

## Known Issues

Here are some known issues in customizing the status bar.

* In iOS 13, when using dark mode, it's not currently possible to use a status bar text color other than white, even when setting the StatusBarStyle to `default`. This is an [issue in Cordova's Status Bar plugin](https://github.com/apache/cordova-plugin-statusbar/issues/148) and should be fixed in a future release.
* If your status bar customization doesn't show, you may be using and outdated version of OutSystems UI. Try updating OutSystems UI from Forge.