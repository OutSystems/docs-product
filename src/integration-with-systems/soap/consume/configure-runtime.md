---
summary: Customize the SOAP Web Service endpoint URL and user credentials per environment in Service Center.
locale: en-us
guid: 8f587c50-8581-49eb-a959-fb72411a00de
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Configure a SOAP Web Service at Runtime

When you consume a SOAP Web Service in your module, the Endpoint URL is automatically set. You can the configure both the authentication method and the user credentials to use in Service Studio.

While the values you set in your module for these properties are the default settings, you can customize them per environment in the Service Center management console, overriding the default values.

This allows your application to consume a SOAP Web Service with different configurations in different environments, without having to change or republish the module. For example, you may have a SOAP Web Service endpoint URL for development and test purposes and a different one for production.

To configure the runtime settings of a SOAP Web Service you are consuming, do the following:

1. Go to the Service Center management console of your OutSystems environment.

1. Go to **Factory** and open your application.

1. Open the module where you are consuming the SOAP Web Service.

1. Select the **Integrations** tab and click on the consumed SOAP Web Service name to edit it.

1. Set the **Effective URL** and/or effective authentication credentials (username and password) for the current environment and click **Apply**.
