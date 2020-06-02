---
summary: Additional information about settings for Azure and OutSystems.
tags:
---

# Reference

This is a reference document that provides more information about components and settings.

## The chatbot demo app

The chatbot demo app is available in Forge. Go to the [OutSystems.AI Chatbot Reactive](https://www.outsystems.com/forge/component-overview/7315/outsystems-ai-chatbot-reactive), click **Download** and then **Download component + demo**. 

![Forge page to download the chatbot demo](images/chatbot-demo-download-forge.png?width=650)

## Block settings { #chatbot-settings }

These are the settings available in the properties of the Blocks that come with the chatbot component from Forge.

| Property   |      Location      |  Description |
|----------|:-------------:|------|
| DirectLineSecret |  Components\Chatbot, Components\ChatbotAdvanced | An Azure parameter. Lets your chatbot communicate with the Azure chatbot service. No default value. **Mandatory value.**|
| BotName |  Components\Chatbot | The name that shows on the chatbot tab. The default value is `Chatbot`. |
| BotImageURL |  Components\Chatbot | The image that shows next to the bot replies in the chat window. No default value. |
| UserImageURL |  Components\Chatbot | The image that shows next to messages the user enters in the chat window. No default value. |
| WelcomeMessage |  Components\Chatbot | The message that shows when the bot starts running in the screen. No default value. |
| IsInline |  Components\Chatbot | If set to True, the chatbot window shows as an inline element. If set to False, the chatbot window shows as a modal window that the user can close by clicking the close button. The default value is False.|
| StartsClosed |  Components\Chatbot | If set to True, the chatbot window shows as an inline element. If set to False, the chatbot window shows as a modal window that the user can close by clicking the close button.|

## Azure bot parameters

These are some of the settings from Azure that you need for implementing a chatbot in OutSystems. You first need to [create a bot service in Azure](guide-azure-services.md#create-bot-service) to get these parameters.

| Property   |      Location      |  Description |
|----------|:-------------:|------|
| DirectLineSecret |  Web App Bot | **Azure home page** > **your chatbot** > **Channels** > **Direct Line** > click **Edit**. You can use any of the keys in **Default Site** > **Secret keys**. |
| Messaging endpoint |  Web App Bot | **Azure home page** > **your chatbot** > **Settings** > **Messaging endpoint**. |
| MicrosoftClientId |  Web App Bot | **Azure home page** > **your chatbot** > **Configuration** > **Application Settings** > **MicrosoftAppId**. <br/><br/> If you download the source code from Azure, this value is available from the **settings.json** file. |
| MicrosoftClientSecret |  Web App Bot | **Azure home page** > **your chatbot** > **Configuration** > **Application Settings** > **MicrosoftAppPassword**. <br/><br/> If you download the source code from Azure, this value is available from the **settings.json** file.|

## Data structures in OutSystems Bot Framework Connector

The Bot Framework Connector has several data structures that correspond to the data required by the Azure Bot Framework REST Connector API. To check the data structures, open the chatbot webhook module and navigate to **Data** > **Structures** > **AzureBotFrameworkConnector**.

For general information about available features for the structures, see [Azure Bot Framework REST API reference](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-connector-api-reference?view=azure-bot-service-4.0).

For more information about the cards structure, see these pages in Microsoft Dev Center:

* [Cards reference](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference). Contains more information about cards. Note that not all cards are available in OutSystems.
* [Card actions](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-actions) lists actions you can use with the cards.

## Availability in OutSystems apps

The chatbot component, with the UI blocks and the webhook module, is available in two versions. Which version you need to use depends on the type of app you already have. We recommend Reactive Web App and the compatible version of the component for all new and existing Reactive Web projects. 

| App type | Component |
| --- | --- |
| Reactive Web App, Mobile App | [Chatbot component for Reactive Web App](https://www.outsystems.com/forge/component-overview/7315/outsystems-ai-chatbot-reactive) |   
| Traditional Web App | [Chatbot component for Traditional Web App](https://www.outsystems.com/forge/component-overview/5886/) |   

### Component differences for Traditional Web App

Note the following differences in the version of the component for Traditional Web App:

* The name of the app template is Azure Bot Webhook.
* The name of the component is **ChabotWeb**.
* The properties **BotImageURL** and **UserImageURL** are not available in the Web Block.
* When adding action to send a message, add the Server Action **SendMessage** from the Chatbot Web component.
