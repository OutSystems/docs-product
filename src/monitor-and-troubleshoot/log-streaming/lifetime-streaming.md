---
summary: The article provides a step-by-step guide on setting up log streaming from LifeTime to Elastic Cloud
tags:
locale: en-us
guid: 172ac547-add4-4cc5-9adf-d72fbe379d35
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=3139%3A323&mode=design&t=IIMVc2WTi7UxHv00-1
---
# Configuring the log streaming service in LifeTime

<div class="info" markdown="1">

To configure log streaming in LifeTime, the user must have the Admin built-in role.

</div>

This example uses **Elastic Cloud** as the destination tool.

1. Go to **LifeTime** > **Environments**.

1. Click **Log Streaming** - **Set up**.

    ![Screenshot of the LifeTime Log Streaming setup page](images/log-streaming-setup-lt.png "LifeTime Log Streaming Setup")

1. Click **Set up log streaming**.

    ![Screenshot showing the 'Set up log streaming' button in LifeTime](images/log-streaming-setupservice-lt.png "Initiating Log Streaming Setup")

1. Select the environment and click **Continue**.

    ![Screenshot of environment selection for log streaming in LifeTime](images/log-streaming-environment-lt.png "Selecting Environment for Log Streaming")

1. Select the destination tool and click **Continue**. 

    ![Screenshot of destination tool selection for log streaming in LifeTime](images/log-streaming-destination-lt.png "Choosing Destination Tool for Log Streaming")

1. Enter the URL and the secret token and click **Continue**.
    
    The connection is tested, and the test data is sent to the destination tool.
    
    ![Screenshot of Elastic Cloud configuration fields for log streaming in LifeTime](images/log-streaming-elastic-lt.png "Configuring Elastic Cloud as Log Streaming Destination")


1. If the connection is successful, click **Complete set up**.

    **Note**: Before you complete the setup, validate that the test data has arrived at the destination tool.  For Elastic Cloud, see [View Logs](elastic.md#view-logs)

    ![Screenshot indicating a successful log streaming connection in LifeTime](images/log-streaming-successfulconnection-lt.png "Successful Log Streaming Connection")
       
    If the connection is not successful, you can retry the test connection or review the destination information to ensure it’s correct.

    ![Screenshot showing a failed log streaming connection with retry option in LifeTime](images/log-streaming-failedconnection-lt.png "Failed Log Streaming Connection")
