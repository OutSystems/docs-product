---
summary: 
tags: 
locale: en-us
guid: 172ac547-add4-4cc5-9adf-d72fbe379d35
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=3139%3A323&mode=design&t=IIMVc2WTi7UxHv00-1
---

# Configuring the log streaming service in LifeTime 

This example uses **Elastic Cloud** as the destination tool.

1. Go to **LifeTime** > **Environments**.

1. Click **Log Streaming** - **Set up**.

    ![Click Log streaming set up](images/log-streaming-setup-lt.png)

1. Click **Set up log streaming**.

    ![Click Set up log streaming](images/log-streaming-setupservice-lt.png)

1. Select the environment and click **Continue**.

    ![Select environment](images/log-streaming-environment-lt.png)

1. Select the destination tool and click **Continue**. 

    ![Select destination](images/log-streaming-destination-lt.png)

1. Enter the URL and the secret token and click **Continue**.
    
    The connection is tested, and the test data is sent to the destination tool.
    
    ![Successful connection](images/log-streaming-elastic-lt.png)


1. If the connection is successful, click **Complete set up**.

    **Note**: Before you complete the setup, validate that the test data has arrived at the destination tool.  For Elastic Cloud, see [View Logs](elastic.md#view-logs)

    ![Successful connection](images/log-streaming-successfulconnection-lt.png)
       
    If the connection is not successful, you can retry the test connection or review the destination information to ensure it’s correct.

    ![Failed connection](images/log-streaming-failedconnection-lt.png)
