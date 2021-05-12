---
summary: Change the services consumed from a REST Web Service; get the latest changes or modify the list of consumed methods in Service Studio.
tags: support-Integrations_Extensions
---

# Refresh a REST Web Service

To change the services consumed from a REST Web Service or to modify the list of consumed methods, refresh the service in Service Studio:

1. In the **Logic** tab, expand the **Integrations** folder and then **REST**.

2. Under **REST**, right-click the REST API service and select **Refresh REST API**. In this example, the REST service is called **SoccerTeam**.

    ![](images/ss-rest-refresh-1.png)

3. In the Refresh REST API popup, click **Yes**. 

    ![](images/ss-rest-refresh-confirm-2.png)

4. Enter the REST API URL or upload a new specification, and click **Add Methods**. In this example, the URL points to a JSON file that contains the complete list of REST methods.

    ![](images/ss-rest-refresh-URL-3.png)

5. Select the methods you would like to consume. 

    Note: 
    * The methods you select overwrite previously consumed methods for the service. Be sure to select all methods you want to consume, even if they haven't changed.
    * The following settings are NOT overridden when you refresh: 
        * Basic authentication
        * Advanced settings (Date Format, On Before Request and On After Response)
        * HTTP headers

    The method format displays as **method name [/relative endpoint]** and, if applicable, **(outdated)**. 

    Where:
    * method name = the method you may select to consume or update
    *  [/relative endpoint] = endpoint relative to the base URL
    *  (outdated) = if applicable, identifies methods that were previously imported but no longer exist in the latest specification

    ![](images/ss-rest-refresh-methods-4.png)


6. Click **Finish** to add the selected methods. In this example, all available methods are selected. **AllGoalKeepers**  includes an outdated label, which means it no longer exists in the service and can't be selected.    

