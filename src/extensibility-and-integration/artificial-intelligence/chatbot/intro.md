---
summary: Let your users interact with your app through a chat interface. This is an introduction to creating a chatbot with the OutSystems chatbot component and Microsoft Azure.
tags:
locale: en-us
guid: c9733003-eb20-49b3-93af-47e313315e30
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Create AI-powered chatbots 

OutSystems is a low-code platform that lets you quickly create chatbots and add them to your apps. Use the [OutSystems.AI Chatbot](https://www.outsystems.com/forge/component-overview/7315/outsystems-ai-chatbot-reactive) component from Forge to create UI and connect your logic to the AI back end.

<div class="info" markdown="1">

To create a chatbot from the Chatbot component, you need:

* A Microsoft Azure account and a permission to create and edit a bot service.
* Permissions to install Forge components in your environment.

</div>

Your chatbot consists of the user interface and logic that generates replies to the user. If you want to quickly add a chatbot to your app, a chatbot that can answer questions based on the information from the knowledge base, check [Getting started: How to create an FAQ chatbot](get-started-faq-chatbot.md) for instructions.

For more options and advanced computational features, such as natural language processing or intent detection, use an AI provided. OutSystems uses Microsoft Azure as the AI provider. Use the [chatbot webhook module](guide-outsystems-webhook.md) to connect to Azure and design advanced responses, for example to send a file or create a card with buttons or suggested actions.

<div class="info" markdown="1">

There's a chatbot demo app in Forge. Install the demo in your environment, check out the logic, and reuse it in your chatbots. Go to [OutSystems.AI Chatbot Reactive](https://www.outsystems.com/forge/component-overview/7315/outsystems-ai-chatbot-reactive), click **Download**, and then **Download component + demo**. 

</div>

Here is an overview of some use cases to get you started. The time to develop and deploy for use cases other than an FAQ chatbot refers to the OutSystems developers with intermediate skills.

| Your chatbot use case | Recommended guides | Time to develop and deploy
| --- | --- | --- |
| Answers frequently asked questions, based on your knowledge base. | See [Getting started: How to create an FAQ chatbot](get-started-faq-chatbot.md) for detailed instructions. | Fast
| Implements interactions with both Azure and OutSystems resources. | See [Create and configure the chatbot webhook module](guide-outsystems-webhook.md) and then see an example how to [reply with an echo message through the webhook module](get-started-advanced-chatbot.md). | Moderate, depends on use case complexity
| Shows cards with thumbnails, buttons, and files for download. | See [Reply with cards](guide-outsystems-cards.md). | Moderate
| Has a fully custom interface. | See [Create custom chatbot UI](get-started-custom-ui.md). | Moderate

Making a working chatbot is only part of the work towards creating a useful chatbot. You also need knowledge about designing interactive user experiences. Check out [Principles of bot design](https://docs.microsoft.com/en-us/azure/bot-service/bot-service-design-principles?view=azure-bot-service-4.0) and [Writing for bots](https://docs.microsoft.com/en-us/style-guide/chatbots-virtual-agents/writing-bots) by Microsoft.