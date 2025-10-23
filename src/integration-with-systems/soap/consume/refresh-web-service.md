---
summary: OutSystems 11 (O11) provides a method to refresh SOAP Web Services in Service Studio by updating the consumed methods and services.
tags: web services, soap, wsdl, service integration, api management
locale: en-us
guid: 68e18433-b490-4ba2-9269-0261f6b656fd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=418:14
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Refresh a SOAP Web Service

To change the services consumed  from a SOAP Web Service or to modify the list of consumed methods, refresh the service in Service Studio:

1. In the **Logic** tab, open the **Integrations** folder.

1. Under **Integrations** > **SOAP**, right-click the SOAP Web Service you want to refresh and select **Refresh SOAP Web Service...**.

    ![Context menu in Service Studio showing the option to refresh a SOAP Web Service](images/soap-refresh-menu-ss.png "Refresh SOAP Web Service Menu Option")

1. Confirm the URL or local file path for the WSDL, and then click **Select methods**. Service Studio re-reads the WSDL and displays a selectable list of available methods to consume.

1. Select all methods you want to consume. Note that:

    * The list of methods you select replaces the list you consumed previously; be sure to select all methods you want to consume, even if they haven't changed.
    * Refreshing does NOT wipe out authentication and On Before Request settings. These settings are not impacted when.
    * Methods no longer in the WSDL have an **(Deleted)** label; these will no longer exist in the service.  
    * New methods include a **(New)** label.

1. Click **Confirm** to consume the selected methods.
