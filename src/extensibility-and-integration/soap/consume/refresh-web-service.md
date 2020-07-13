---
summary: Refresh the Web Service when you want to get the latest changes on a consumed SOAP Web Service or modify the list of consumed methods in Service Studio.
tags: support-Integrations_Extensions
---

# Refresh a SOAP Web Service

If there are changes in the services consumed from a SOAP Web Service or if you want to modify the list of consumed methods, refresh the service in Service Studio.

Do the following:

1. In the **Logic** tab, open the **Integrations** folder.

1. Under the **SOAP** element, right-click the SOAP Web Service you want to refresh and select **Refresh SOAP Web Service**.

    ![](images/soap-refresh-menu.png)

    The Refresh operation asks you to confirm the location (URL or local file path) of the WSDL for the service before proceeding, since it might have changed. Service Studio then re-reads the WSDL, showing you the list of available methods and allows you to remove/add any consumed methods.

1. Change the list of consumed methods by checking or unchecking them, and press **Finish** to apply your changes.

    ![](images/soap-refresh-methods.png)

    Service Studio shows consumed methods no longer present in the service definition as "(outdated)" and new methods as "(new)".
