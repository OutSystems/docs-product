---
tags:
summary: Learn about the architecture of apps published with Experience Builder and insights on how to extend these apps.
---

# Extend your Experience Builder app in Service Studio

Experience Builder lets you create a prototype of your final app. When your team and stakeholders are happy with the user journeys of your prototype app, you can use Service Studio to complete your app by adapting it to your business and extending it.

After an app is published with Experience Builder, you can access it by connecting to the environment with Service Studio. The app's name, description, and icon are already set and reflect the branding defined in Experience Builder.

## App dependencies

Experience Builder apps have dependencies to the following apps and components.

### Experience Builder Components package

Apps created with Experience Builder use [custom UI patterns](#experience-builder-ui-patterns) and [actions](ref/intro.md) included the **Experience Builder Components** package. This package is installed during setup and may need to be updated later.  
Make sure to use these UI patterns and actions when extending an app created using Experience Builder.

### Mobile plugins

Depending on the flows, an Experience Builder app can have dependencies to one or several of the following plugins:

* Calendar Plugin v3.1.1
* Camera Plugin v7.0.0
* Common Plugin v3.0.1
* CryptoAPI v2.2.0
* DialogsPlugin v1.2.0
* Facebook Login Plugin v2.0.8
* File Plugin v3.0.1
* File Transfer Plugin v2.0.0
* File Viewer Plugin v2.0.0
* Google Core v1.0.0
* Google Login Plugin v2.0.2
* InAppBrowser Plugin v2.4.1
* JavaScript Utils v2.0.1
* Key Store Plugin v2.1.4
* Location Plugin v5.1.3
* OutSystems Maps v1.0.0
* Social Sharing Plugin v1.0.2
* Speech Recognition Plugin v2.0.1
* Touch ID Plugin v3.3.0

## Architecture of Experience Builder apps

Apps published with Experience Builder include the following modules:

* A frontend module, named **&lt;app-name&gt;**, where &lt;app-name&gt; is the name of the app.

* A mobile theme module, named **&lt;app-name&gt;_MTh**.

* A resources module, named **&lt;app-name&gt;_Resources**.

* A mobile core widgets module, named **&lt;app-name&gt;_MCW**.

### Frontend module

The name of the UI flows and screens in this module reflect the names defined in Experience Builder.

Screens include logic and are functional, for example the screens of the sign up flows include all the logic needed to create a new user, including validation logic to ensure the forms are filled in correctly.  
All the screens and screen actions check for network status, and in case of network unavailability, redirect the users to a “No internet connection" screen, named **OfflineScreen**.

#### Replacing sample data

Some screens use OutSystems UI sample data.  
Usually, the screens fetches the sample data using Data Actions that call a Server Action named **Get&lt;entity&gt;**, where &lt;entity&gt; is the name of the sample data entity. These server actions are called Sample Data Helpers, and create and structure sample information in order for it to match the screen structure.

You can replace a Sample Data Helper action with your own server side action. If you ensure that the output structure of your action matches the output structure of the Sample Data Helper action, you don’t need to change the screen logic.

#### Experience Builder UI patterns

Experience Builder includes several custom UI patterns and widgets that build upon OutSystems UI experience,by adding visual changes and extra native behaviors.

Use these UI patterns when you extend a app created using Experience Builder.  
Check all the available patterns in the [live style guide](https://experiencebuilder.outsystems.com/ExBuilder_CustomPatterns_Samples/CustomPatternsList)
These patterns are available in the **ExBuilder_MPat** module of the **Experience Builder UI** app, which is part of the **Experience Builder Components** pack.

### Mobile theme module

The application theme structure depends on the flows used while creating the app in Experience Builder. Each flow is based on an AppType.

The module includes the following themes:

* **AppTypes_Theme**, a copy of AppType_Theme and based on ExBuilder_Theme. If the app uses flows from more than one app type, the theme is based on the themes of each app type, and the CSS is optimized to ensure only the needed code is included.

* **Flows_Theme**, based on AppTypes_Theme. Each existing flow theme is concatenated into this theme.

* **&lt;app-name&gt;_MTh**, based on the Flows_Theme. This theme sets the primary color and the uploaded splash screen.

Experience Builder creates apps based on the latest version of OutSystems UI, which uses CSS variables. You can override these CSS variables in **&lt;app-name&gt;_MTh**.

### Resources module

This module ensures the following:

* Your app includes all the versions of the app icon and the **Extensibility Configurations** that enable [the use of custom icons](../../deliver-mobile/customize-mobile-app/modify-the-app-icon.md). The **res.zip** resource contains all the icon versions. Your app needs this to be published in app stores.

* Your app includes all the splash screen image sizes and the **Extensibility Configurations** that enable [the use of a custom splash screen](../../deliver-mobile/customize-mobile-app/use-custom-splash-screens.md). The **res.zip** resource contains all the needed versions of the splash screen image and of the icon.

* Your app includes the **Extensibility Configurations** needed to ensure the correct orientation and color when you distribute it as a Progressive Web App (PWA) or as a native mobile app. Your app needs this to be published in app stores.

* If your app uses Google login, your app includes all the **Extensibility Configurations** needed to integrate with Google login services.

### Mobile core widgets module

This module includes a set of business-related blocks to ensure an app architecture that follows the best practice that says that business-related blocks should be included in a separate module.

This module is only created if you use flows from an app type that includes this type of blocks.
