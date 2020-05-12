---
summary: How to add the UI chatbot component to an app. This is a quick solution that covers many use cases.
tags:
---

# Add a chatbot UI block to your app

This is a step-by-step guide to add the chatbot UI block to an OutSystems app. To have a functional chatbot, you also need a logic to handle the responses. [Create an FAQ chatbot for your app](get-started-faq-chatbot.md) provides detailed instructions for an FAQ bot. If you're implementing advanced use cases, check 
[Create advanced logic and reply with cards](get-started-advanced-chatbot.md).


<div class="info" markdown="1">

You need to install the [OutSystems.AI Chatbot](https://www.outsystems.com/forge/component-overview/7315/outsystems-ai-chatbot-reactive) component to follow the guide. 

</div>

Follow these steps to add the chatbot UI block to your app.

1. Create a new Reactive Web App and add a module of the same type to it. You can also use an existing Reactive Web App.
2. Open the **Manage Dependencies** dialog (press **Ctrl+Q**). Search for `Chatbot`. Select **Chatbot** in the producers pane, and then select all elements in the elements pane. Click **Apply**.
       
    ![Chatbot references](images/chatbot-add-references-ss.png?width=500)

    With this you add elements from the Chatbot component to create UI and configure the chatbot.

4. Add a Screen to the module. Alternatively, if you're using an existing app, open a Screen.
5. Add the chatbot block to the Screen. Navigate to **Interface** > **(you app)** > **UI Flows** > **Chatbot** > **Components**. Drag the **Chatbot** Block to the Screen. The Chatbot preview now shows in the Screen.
   
    ![Chatbot references](images/chatbot-drag-chatbot-block-ss.png?width=500)

6. Select the Chatbot component Block. In the properties, locate **DirectLineSecret**. Paste the direct line key from Azure, surrounded by the quotation marks.

    ![Direct line property](images/chatbot-direct-line-ss.png?width=500)

    <div class="info" markdown="1">

    Direct line secret is a value from the Azure bot service. Depending on how you got to this step, you need to do one of the following:

    * If you already created a chatbot service and related resources check [how to get a direct line secret from Azure](guide-azure-services.md#get-direct-line-key).
    * If you haven't created a chatbot service and related resources, see [Get started: create an FAQ chatbot for your app](get-started-faq-chatbot.md) for instructions.

    </div>

7. Publish your app and test the chatbot. Enter a message in the chat window. If you get replies from the chatbot, then your chatbot is working correctly.

    ![Chatbot in a browser](images/chatbot-faq-example-browser.png?width=400)

    You can now start developing a more complex chatbot.

    <div class="info" markdown="1">

    For information on how to configure other parameters, including the welcome message, check the [chatbot reference](reference.md#chatbot-settings).

    </div>

## Troubleshooting

This section contains some of the issues you may run into while developing your chat but, as well as information how to fix those issues.

### Bad argument: invalid token or secret

If you get an error with the message "Bad argument: invalid token or secret message" after you run the app with the chatbot, [check if the direct line value is valid](guide-azure-services.md#get-direct-line-key).