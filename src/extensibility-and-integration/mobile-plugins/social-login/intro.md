---
summary:
---

# Social login plugin

The Social Login plugin lets you set a login experience that uses an external provider, namely Google, Apple, Facebook, or LinkedIn. The plugin enables you to request access to a subset of your user's data stored by the provider, such as name, email, and profile picture. You can then use this information to create or start a user session on your app.

As a good practice, verify the plugin is available during runtime in your app to prevent the app from crashing. Use the **Logic** > **Client Actions** > **SocialLoginPlugin** > **CheckSocialLoginPlugin** action to check for the plugin availability. If the plugin isn't available to the app, display an error to your users.

<div class="info" markdown="1">

To learn how to install and reference a plugin in your OutSystems apps, and how to install a sample app, see [Adding plugins](../intro.md#adding-plugins).

</div>

## Sample app

OutSystems provides a sample app that contains logic for common use cases. Install the Social Login sample app from Forge and then open it in Service Studio.

This sample app shows you how to do the following:

* Trigger a native social login flow using Apple Sign-In, Google Sign-In, or Facebook Login.

* Trigger a Progressive Web App (PWA) social login using Apple, Google, Facebook, or LinkedIn as providers.

* Use the profile info (including name, email, and profile picture) returned by the provider on a screen.

<div class="info" markdown="1">

The next step in the development of a mobile app is to use the profile info (including name, email, and profile picture) returned by the provider to create a user or manage a session on the OutSystems Users service. This is not shown in the sample app, but it can be done resorting to the User systems database and its entity actions.

</div>

## Enable a frictionless social login experience in your app

The following steps show how to enable your users to log in to your app using an existing social media account:

1. Set up a new provider using the Social Login Configurator.

1. Create logic to trigger a native or PWA social login flow.

1. Create a user interface that uses the user’s profile information.

1. Optionally, create logic to use the profile info (including name, email, and profile picture) returned by the provider to create a user or manage a session on the OutSystems Users service

### Set up a new provider using the Social Login Configurator

Before being able to provide the option for social login, you need to configure a new provider to be used in your app. For that, you can use our Social Login Configurator, a Reactive Web app that lets you set up a new provider to use on your app.


To configure a new provider or edit an existing one you need to add the following information (depending on the provider):

#### Apple

Relevant Information | Description
---|---
Identifier | A public identifier your app on the provider side. It is a string type value available to any registered developer on Apple Developer. You can access the Identifier value on the Certificates, Identifiers, and Profiles pages of your app.
Key ID | ...
Team ID | Identifier of your team on Apple Developer.
Secret (`.p8`) | A confidential code known only to your app and the authorization server. It is a string type value type value available to any registered developer on Apple Developer. You can access the Secret value on …

#### Google

Relevant Information | Description
---|---
Client ID | A public identifier your app on the provider side. It is a string type value available to any registered developer on the Google Cloud Platform. You can access the ClientID value on the OAuth Consent tab on your app's Credentials screen.
Client Secret | A confidential code known only to your app and the authorization server. It is a string type value type value available to any registered developer on the Google Cloud Platform. You can access the ClientSecret value on the OAuth Consent tab on your app's Credentials screen.

#### Facebook

Relevant Information | Description
---|---
App ID | A public identifier your app on the provider side. It is a string type value available to any registered developer on Meta for Developers. You can access the AppID value in your app's settings.
App Secret | A confidential code known only to your app and the authorization server. It is a string type value available to any registered developer on Meta for Developers. You can access the AppSecret value in your app's settings.

#### Linkedin

Relevant Information | Description
---|---
Client ID | A public identifier your app on the provider side. It is a string type value available to any registered developer on LinkedIn Developer. You can access the Identifier value on the "Authentication" side navigation link, underneath the header "Authentication Keys".
Client Secret | A confidential code known only to your app and the authorization server. It is a string type value available to any registered developer on LinkedIn Developer. You can access the Identifier value on the "Authentication" side navigation link, underneath the header "Authentication Keys".

### Create logic to trigger a social login flow

The plugin triggers a social login flow through the StartLogin client action. 

In the **StartLogin** action, set the values for the predefined mandatory variables:

* ClientID - Lets you set the Client ID, or equivalent, of your app; a text type value available to any registered developer on the Provider development platform. You can access the ClientID value on the settings of your OAuth configuration

* RedirectURI - Lets you set the RedirectURI; a URL type value that will send you the authorization result for any backend service you may be using. You can specify the RedirectURI on the settings of your Provider OAuth configuration. 

    The Redirect URI is a combination of your environment URL and the AuthenticationRedirect URL that can be found on **REST integration** > **SocialLoginAuth** of your SocialLoginConfigurator plugin. A final RedirectURI might look like:

    `https://enmobile11-dev.outsystemsenterprise.com/UXTestsSocialLoginCore/rest/SocialLoginAuth/AuthenticateRedirectLinkedIn`

You can also define the optional variable of:

* ReturnURI - An URL type value, necessary for cases where the screen that uses the profile information is different from the screen where the action is being used. You can specify the ReturnURI directly on the StartLogin action.

### Creating a User interface

For you to use the output information of a social login (also known as login scope), you need to (1) use the Authenticate block on the screen where the StartLogin action occurs. After defining a handler action, you need to (2) store the blocks OnAuthenticationCompleted event input parameters to input parameters of your handler action.


After setting up your block handler, you can use the output information of a social login by simply passing the OnAuthenticationCompleted block variables to any destination of your choice.


To show the user’s profile info, you can use an Expression and customize the look and feel of the parent widget (2).
