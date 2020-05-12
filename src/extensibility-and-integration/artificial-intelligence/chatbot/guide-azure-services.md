---
summary: This document guides you through creating the Azure resources for developing a chatbot.
tags:
---

# Create the chatbot resources in Azure

This document contains instructions for using Azure resources to add and get configurations for your OutSystems chatbot. 

<div class="info" markdown="1">

You need a valid Azure subscription to follow instructions in this document.

</div>

## Create a QnA Maker service in Azure { #create-qna-service }

Follow these instructions to create a QnA Maker service which you need for the FAQ chatbot. QnA Maker is part of Azure Cognitive Services.

1. Log into the Azure portal at [portal.azure.com](https://portal.azure.com).
2. Click the search field (or press **Ctrl + /** ) and enter `QnA Maker`. Locate the **Marketplace** section in the results and click **QnA Maker**.
   
    ![Azure portal search](images/azure-portal-qna-search.png?width=600)

3. Enter the information for your QnA Maker and click **Create**. Here is what you need to provide:

    <div class="info" markdown="1">

    The availability of the settings in Azure depend on how your Azure account is managed. You may create some of the resources or ask your administrators to do it for you. This may apply, for example, to your Azure subscription, resource group, available locations, and service plans.

    </div>

    * **Name**. Name and custom domain for the service. 
    * **Subscription**. The Azure subscription you want to use for the bot.
    * **Pricing tier**. The pricing tier for the service.
    * **Resource group**. The resource group to which you want to add the bot.
    * **Azure search pricing tier**. The pricing tier for the service.
    * **Azure Search location**. The location of the datacenter from which the bot service runs.
    * **App name**. The name of your bot service that is part of the URL to reach the service.
    * **Website location**. The location where you deploy the service.
  
    <br/>
    Optional settings:

    * **App insights**. If you want to track your app performance and collect telemetry information, activate this option.
  
    ![Azure portal search](images/azure-qna-maker-service-new.png?width=500)


4. Click **Create**. After validation and deployment, you are redirected to the Azure home page.

    <div class="info" markdown="1">

    If you reached this step while creating an FAQ chatbot, you should now do one of the following:

    * If you haven't created a knowledge base: [create a new knowledge base](guide-azure-kb.md#create-kb)
    * If you already have a knowledge base: [publish the knowledge base and create a chatbot service](guide-azure-kb.md#publish-kb)

    <br/>
    For an overview see [Getting started: How to create an FAQ chatbot](get-started-faq-chatbot.md).

    </div>

## Add a direct line channel for a bot service { #create-direct-line-channel }

Follow these steps to add a direct line channel and allow the OutSystems chatbot component to communicate with the Azure chatbot back end.

1. Log into the Azure portal at [portal.azure.com](https://portal.azure.com).
   
2. Locate your bot name in **Recent resources** or search the bot in the search bar, then click the bot name. The settings page opens.

    ![Web bot in Azure home](images/azure-web-app-bot-dashboard.png?width=500)

3. Open **Channels** from the side menu, locate **Add a featured channel** and click **Configure direct line channel button**. A page to configure direct line opens. 

    ![New direct line channel for bot](images/azure-web-app-bot-service-direct-channel-new.png?width=500)

4. In **Configure Direct Line** you can copy a direct line key now, or do it later when you are configuring the OutSystem component. Click **Done** to return to the main settings page.

    ![Direct line channel secret key](images/azure-web-app-bot-service-direct-channel-key.png?width=500)

## Getting the settings from bot service { #get-settings }

This section shows you where to locate the Azure settings you need for the OutSystems chat component. You first need to [create a bot service in Azure](#create-bot-service) to get these parameters.

### App id and password { #get-id-pass }

Azure application and password fields are, by default, named **MicrosoftAppId** and **MicrosoftAppPassword**. They are listed under Configuration in the App Service Settings section.

1. Open the chatbot configuration page. You can open it by clicking your bot name in the Azure home page or by searching for the bot name in the search bar.
2. In the chatbot configuration page, click **Configuration** in the side menu.
3. In the **Configuration** page, under the **Application settings** section, locate **MicrosoftAppId** and **MicrosoftAppPassword**. Click the eye icons to reveal the field values. Copy the values.

    ![Configuration values for bot](images/azure-web-app-bot-service-direct-config.png?width=600)

Another way to get the settings is to download the source code. In the bot configuration page, click **Build** in the side menu and then **Download bot source code**. Open the **settings.json** file in the source code folder to get the values.

### Direct line secret { #get-direct-line-key }

You can get the secret after you [create a direct line channel](#add-a-direct-channel-for-a-bot-service) for your bot. 

1. Open the chatbot configuration page. You can open it by clicking your bot name in the Azure home page or by searching for the bot name in the search bar.
2. In the chatbot configuration page, click **Channels** in the side menu.
3. In the Connect to channels page, click **Edit** next to **Direct Line**. **Configure Direct Line** page opens.

    ![Edit direct channel for bot](images/azure-web-app-bot-service-direct-channel-edit.png?width=600)

4. In the **Configure Direct Line** page, click **Show** under one of the secret keys. Copy the value.

    ![Secret key of a direct channel for bot](images/azure-web-app-bot-service-direct-channel-key.png?width=600)

    <div class="info" markdown="1">

    You can select any of the two keys.

    </div>

## Create a bot service in Azure { #create-bot-service }

<div class="info" markdown="1">

Follow these instructions if you need to create a generic bot service in Azure, for example an echo chatbot to test the UI and back end. For creating an FAQ chatbot see [Getting started: How to create an FAQ chatbot](get-started-faq-chatbot.md).

</div>

Follow these steps to create a bot service in Azure. This bot monitors for new messages from your users. 

1. Log into the Azure portal at [portal.azure.com](https://portal.azure.com).
2. Click the plus button titled **Create a resource**.

    ![Azure portal](images/azure-add-resource-button.png?width=400)

3. Select **AI + Machine Learning** and then click **Web App Bot**. A page to create In the new Web App Bot opens.
    
    ![New Web App Bot](images/azure-web-app-bot-service-new.png?width=450)
    
4. Enter the information for your bot and click **Create**. Here is what you need to provide:

    * **Bot handle**. Unique identifier for the bot. 
    * **Subscription**. The Azure subscription you want to use for the bot.
    * **Resource group**. The resource group to which you want to add the bot.
    * **Location**. The location of the datacenter from which the bot service runs.
    * **App name**. The name of your bot service that is part of the URL to reach the service.
    * **Bot template**. Click to expand. In the **SDK language** select **C#**. For creating an echo bot, select **Echo Bot**. For advanced bot service select **Basic Bot**.
    * **App service plan / location**. This is a set of the compute resources which the bot uses.   
    * **Microsoft App ID and password**. Verify the selected option is **Autocreate App Id and password**.

    <br/>![New Web App Bot](images/azure-web-app-bot-service-create.png?width=250)

    <div class="info" markdown="1">

    The availability of the settings in Azure depend on how your Azure account is managed. You may create some of the resources or ask your administrators to do it for you. This may apply, for example, to your Azure subscription, resource group, available locations, and service plans.

    </div>

5. You are back to the Azure home page and there's a notification that a deployment is in process. Once the deployment of your bot finishes, you can get the settings you need for the OutSystems Chatbot component.

## Troubleshooting

Here are troubleshooting tips that can help you resolve issues in Azure.

### Azure resource provider is not registered

While creating a resource in Azure you get the following error: "Azure (resource name) resource provider is not registered, please click to search (resource handle) and register it first".

Check if the combination of settings in **Subscription** and **Resource group** can be used together. You may be trying to create a resource in in a group that doesn't belong to the subscription (or vice versa).
