---
summary: Secure the runtime of web application by encrypting the viewstate to protect sensitive information submitted by end users on the browser.
tags: runtime-traditionalweb
locale: en-us
guid: a07b13f4-d8a9-4d32-8c52-57544422ce46
---


# Encrypt web apps view state

The view state is used by the OutSystems underlying technology for traditional web applications (ASP.NET). This mechanism is used to preserve the client-side state of a web page when a postback occurs. The view state stores the values and controls of the page between requests.
 
The view state is a hidden field in the HTML of the web page. Its value property stores the view state encoded information. It's a good practice to encrypt the view state and avoid using it to store sensitive information.


![viewstate](images/encrypt-viewstate-console.png)

Check the [Microsoft documentation](https://docs.microsoft.com/en-us/dotnet/api/system.web.ui.control.viewstate?view=netframework-4.8) for more information about the view state.

## Encrypting the view state using Factory Configuration

Because a page's view state can contain sensitive information (such as the inputs a user added on a form) it's a good practice to encrypt the view state.
It’s possible to encrypt the view state using the supported Forge component [Factory Configuration](https://www.outsystems.com/forge/component-overview/25/factory-configuration):

1. Install Factory Configuration in the environment you wish to encrypt the view state.

1. Open it on the browser and login using your LifeTime/Service Center credentials.

1. Navigate to the **Platform Configurations** tab and make sure **Encrypt Viewstate** is ticked. For an extra level of protection, the option **Use Session Token to Encrypt View State** will include the value of the session cookie **osVisitor** in the encrypted view state. This ensures that, in each user session, every requested page is only valid in the context of that same user session.

    ![Factory Configuration](images/encrypt-viewstate-FC.png)

1. [Apply the settings](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Applying_Configurations_in_Service_Center#Apply_Pending_Settings_to_a_Set_of_Modules) to all modules.
