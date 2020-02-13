---
summary: Use Chatbot Web to create your own chatbot and allow your users to interact with your services via a chat interface.
tags:
---

# Set up and use the OutSystems.AI Chatbot component in your OutSystems applications

Chatbots can be the first line of communication and provide support to your users, while increasing efficiency and customer satisfaction. Use the [OutSystems.AI Chatbot Reactive component](https://www.outsystems.com/forge/component-overview/5886/chatbot-web) to create a chatbot in your apps. 

The chatbot consists of:

* UI component, to design user experience. The OutSystems.AI Chatbot Reactive comes with user interface that you can use to bootstrap your chat bot. Optionally, you may want to develop the chatbot with your UI, and for that you can check the section about [ChatbotAdvanced](#use-chatbotadvanced-for-custom-ui). 
* Webhook, to connect the UI and the AI provider. It comes with OutSystems.AI Chatbot Reactive.
* Services by the AI provider. Use your Azure account for this.

<div markdown="1" class="info">

If you're developing a Traditional App, check the section [Chatbot in a Traditional Web App](#chatbot-in-a-traditional-web-app).

</div>

## Prerequisites

To create a chatbot, you need some parameters from Microsoft Azure, and install a Forge component with its dependencies.

### Get the Azure parameters

This component requires Microsoft Azure as the AI provider. [Create a Web App Bot resource](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-quickstart?view=azure-bot-service-4.0#prerequisites) on Azure Portal and get the following values, as you need them in the chatbot setup: 

* **DirectLineSecret**
    
    Locate in Azure Dashboard > Your Web App Bot > Channels, and [add a Direct Line channel](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-channel-connect-directline?view=azure-bot-service-4.0#add-the-direct-line-channel). You will have [two secret keys](https://docs.microsoft.com/en-us/azure/bot-service/rest-api/bot-framework-rest-direct-line-3-0-authentication?view=azure-bot-service-4.0#get-a-direct-line-secret). When configuring your chatbot you can use any of the two values for **DirectLineSecret**.

* **MicrosoftClientId**

    It's located in Azure Dashboard > Your Web App Bot > Configuration. MicrosoftClientId is also known as "Microsoft App ID".

    ![Azure parameters for the chatbot](images/chatbot-azure-params.png?width=400)

* **MicrosoftClientSecret**
   
    It's located in Azure Dashboard > Your Web App Bot > Configuration. MicrosoftClientSecret is also known as "Microsoft App Password"
   
### Install the OutSystems component and dependencies

Download OutSystems.AI Chatbot Reactive and its dependencies from the Forge and publish them to your Environment.

## Add the Chatbot Block to create UI and basic logic

To use the Chatbot Block in your application, do the following:

1. Go to **Manage Dependencies**, select Chatbot and add it as a dependency.
2. Drag the Chatbot Block to the Screen where you want to add it.
3. Enter the values in the fields of the Block:

    * **DirectLineSecret** – the value you got previously from you Azure app
    * **BotName** – the name to be displayed in the chat UI
    * **WelcomeMessage** – the first message to be displayed in the chat 
    * **IsInline** – specifies how to display the chatbot UI within the Screen through a boolean. Setting this value to True renders the chatbot with the width of the parent container. If you set it to False, the chatbot appears in a modal dialog.
    * **StartsClosed** - defines if the chat window starts opened or closed when in a modal
    * **BotImageURL** - the image URL displayed on the left side of a bot message, if left empty no image is displayed
    * **UserImageURL** - the image URL displayed on the right side of a user message, if left empty no image is displayed.

    ![](images/chatbot-web-image9.png?width=400)

4. Customize the icons in the placeholders of the Chatbot Block.

    ![](images/chatbot-web-image2.png?width=400)

5. Publish and try out the UI. You can also interact with the chatbot to confirm that it is correctly linked to your Azure bot.

## Configure the bot service and customize the responses

To create the logic for the bot responses, do the following:

1. Create a new app in Service Studio. Choose the Chatbot Webhook template and create the module.

    ![](images/chatbot-web-image6.png?width=600)

2. Publish the module. We also recommend that you move the module to the application to which you're adding the chatbot.

     ![](images/chatbot-move-module.png?width=600)

3. In **Service Center**, under the **Factory tab**, go to **Modules** and search for the module that you created based on the Chatbot Webhook template.

4. Go to the Site Properties tab and enter the **MicrosoftClientId** and the **MicrosoftClientSecret**. 

    ![](images/chatbot-web-image3.png?width=800)

5. In the module created based on the Webhook template, go to **Logic** > **Integrations** > **REST** > **MessagingWebhook_V1** > open the **PostMessage** Method.

    ![](images/chatbot-web-image10.png?width=600)

6. In the **GetResponseMessage** Server Action, add and customize the logic for the bot responses. The following example illustrates how logic can be customized for a bot that predicts the weather.

    ![](images/chatbot-web-image11.png?width=600)

7. In the Logic tab, go to Integrations, right-click **MessagingWebhook_V1** and click on **Open Documentation**. A new tab opens in your browser with details about the REST service.

8. Copy the Request URL (in our example it's the PostMessage endpoint) of the service from the tab in the browser.

    ![](images/chatbot-web-image5.png?width=600)

9.  Update the messaging endpoint in the Azure bot service with the endpoint URL. Go to **Azure Dashboard** > **Your Web App Bot** > **Settings** > enter the Request URL in the **Messaging endpoint** field. Save the settings.

## Use ChatbotAdvanced for custom UI

<div class="info" markdown="1">

This section is optional and needed if you're developing your user interface for the chatbot.

</div>

Use the ChatbotAdvanced Block to create customized chatbots for your business needs. You can either create your own UI or use any existing, customized UI with the logic we provide in the ChatbotAdvanced Block.

1. In your application, go to Manage Dependencies, select Chatbot, and add the **ChatbotAdvanced** Block and **SendMessage** Action as dependencies.

    ![](images/chatbot-web-image12.png?width=400)

2. Drag the ChatbotAdvanced Block to the Screen.

3. Fill the **DirectLineSecret** input field with the secret key.

4. To handle events, create two new Screen Actions: one to handle the Initialize and another to handle the MessageReceive. Add the following two local variables to the Screen:

    * DLConversation of DLConversation data type.
    * ChannelAccount of ChannelAccount data type.

    ![](images/chatbot-web-image13.png?width=400)

5. In the Screen Action handling Initialize, add an **Assign**. Assign the local variables to the respective input parameters.

    ![](images/chatbot-web-image14.png?width=400)

6. In the Screen Action handling MessageReceive, use a **ListAppend** to append the message received as input to the message list.

    ![](images/chatbot-web-image15.png?width=400)

7. Add a new Screen Action to your Screen and in the logic flow of the Screen Action, and add the Action SendMessage from the Chatbot component.

8. In **SendMessage**, fill the input parameters:

    * **ConversationId** with the previously created local variable DLConversation
    * **DirectLineSecret** with the same value used in the Block
    * **From** with the previously created local variable ChannelAccount 
    * **TextMessage** with the message the end-user sends to the bot

    ![](images/chatbot-web-image16.png?width=400)

## Chatbot in a Traditional Web App

<div markdown="1" class="info">

For adding a chatbot in a Traditional App, install the [OutSystems.AI Chatbot Web component](https://www.outsystems.com/forge/component-overview/5886/chatbot-web).

</div>

Follow the steps for adding the chatbot components and configuring them, but notice the following differences:

* The name of the application template is Azure Bot Webhook.
* The name of the component is **ChabotWeb**.
* The properties **BotImageURL** and **UserImageURL** are not available in the Web Block.
* When adding action to send a message, add the Server Action **SendMessage** from the Chatbot Web component.
