---
summary: Secure the runtime of web application by encrypting the viewstate to protect sensitive information submitted by end users on the browser.
tags: runtime-traditionalweb
locale: en-us
guid: a07b13f4-d8a9-4d32-8c52-57544422ce46
app_type: traditional web apps
platform-version: o11
---

# Encrypt web apps view state

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

The view state is used by the OutSystems underlying technology for traditional web applications (ASP.NET). This mechanism is used to preserve the client-side state of a web page when a postback occurs. The view state stores the values and controls of the page between requests.
 
The view state is a hidden field in the HTML of the web page. Its value property stores the view state encoded information. It's a good practice to encrypt the view state and avoid using it to store sensitive information.


![viewstate](images/encrypt-viewstate-console.png)

Check the [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/api/system.web.ui.control.viewstate?view=netframework-4.8) for more information about the view state.

## Toggling view state encryption using Factory Configuration

Because a page's view state can contain sensitive information (such as the inputs a user added on a form) the view state is by default encrypted.
You can confirm the view state is encrypted using the supported Forge component [Factory Configuration](https://www.outsystems.com/forge/component-overview/25/factory-configuration). 

If it's encrypted, **Encrypt Viewstate** will be ticked. If it's not, follow these steps:

1. Open Factory Configuration on the browser and login using your LifeTime/Service Center credentials.

1. Navigate to the **Platform Configurations** tab and make sure **Encrypt Viewstate** is ticked. 

1. For an extra level of protection, it's also possible to enable the **Use Session Token to Encrypt View State** option. This will include an extra session generated token in the encrypted view state. This token changes after a login to a different user, and ensures every requested page is only valid in the context of that same user session. 

    <div class="warning" markdown="1">

    There are multiple use cases that are broken by this extra protection. Make sure to read the consequences that are explained in the Factory Configuration contextual help of this option.

    </div>

    ![Factory Configuration](images/encrypt-viewstate-FC.png)

1. [Apply the settings](../deploy-applications/apply-configurations.md#apply-pending-settings-to-a-set-of-modules) to all modules.
