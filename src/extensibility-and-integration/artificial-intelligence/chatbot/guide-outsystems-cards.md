---
summary: Learn how to combine OutSystems logic with Azure for advanced chatbot features. See how to use cards in the chatbot responses.
tags:
---

# Reply with cards

Cards are UI elements that usually have images, buttons, and links to download attachments. They provide a richer experience than the plain text in chatbot conversations. The data structures in OutSystems OutSystems.AI Chatbot component follow the required structure of the Azure Bot Framework cards.

<div class="info" markdown="1">

To add logic that interacts with both Azure Bot Service and OutSystems, you need to [add and configure the chatbot webhook module](guide-outsystems-webhook.md).

</div>

## Available cards

The chatbot UI supports the following types of cards:

* Thumbnail Card
* Card Collections

You can combine elements in a card. Here are some elements:

* Thumbnail image
* Text
* Buttons
* Attachments

## Cards structure

The chatbot cards follow the Azure Bot Framework design. You can browse the data structures, that correspond to the JSON values that the framework requires, in **Data** > **Structures** > **AzureBotFrameworkConnector**.

Create cards by building a response in the **GetMessageResponse** Server Action. In the **GetMessageResponse** action you construct the JSON card structure that the connector sends to the Azure Bot Service. The message then shows in the bot UI. For more information about the cards, see these pages in Microsoft Dev Center:

* [Cards reference](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-reference). Contains more information about cards. Note that not all cards are available in OutSystems.
* [Card actions](https://docs.microsoft.com/en-us/microsoftteams/platform/task-modules-and-cards/cards/cards-actions) lists actions you can use with the cards.

## Reply with a card to download a file

Here is an example of a chatbot logic to send a PDF attachment in the chat window. When the user clicks the text in the chat window, the browser loads the PDF file.

![Creating a chatbot response with a card](images/webhook-card-download-logic-sample-ss.png?width=600)

The bot logic usually has multiple branches, but this short example uses only one flow to focus on the logic of creating the download card.

1. The **GetMessageResponse** Action has the following parameters:

    * **Message** - a default input parameter for GetMessageResponse.
    * **ResponseMessage** - a default output parameter for **GetMessageResponse**. Note that one of the data types in **ResponseMessage** is **Attachments**.
    * **Attachment** - a local variable of the Attachment data type coming from the Azure Bot Framework Connector data structures (in **Data** > **Structures** > **AzureBotFrameworkConnector**).

1. The **Assign** tool sets the properties of the **Attachment** local variable. In this example:

    * **ContentType** - identifies the media type, here a PDF.
    * **Name** - the name of the attachment, which is the file label in the chat window.
    * **ContentUrl** - the link to the file. In this example, the file is a resource within the module and the link is relative.

1. An Action appends **Attachment** to the list **ResponseMessage.Attachments**. You may need to reference **ListAppend** Server Action from **System** producer (press **Ctrl+Q** and search for `(System)`).

1. The **Assign** tool labeled **Response Message** is a generic node that assigns the common values. It's part of the webhook module and comes with the default **GetMessageResponse** Server Action.

Once you run the example logic, the chatbot replies with the following message:

![Creating a chatbot response with a card](images/webhook-browser-preview-pdf-download.png?width=350)

## Reply with a card that has an image and a button

Here is another example, which focuses on the logic overview and tha data structure. The bot logic usually has multiple branches, but this short example uses only one flow for better overview. 

![Creating a chatbot response with a thumbnail card](images/webhook-card-download-thumbnail-sample-ss.png?width=600)

1. **CardAction** local variable with **CardAction** data type corresponds to a clickable button, and in this **Assign** tool you assign the values to it.
1. **ListAppend** action adds the **CardAction** variable to the list of buttons, in **Attachment.Content.Buttons**.
1. **Attachment.Content.Text** and **Attachment.Content.Title** define the text body and the title in the card.
1. **Attachment.ThumbnailUrl** points to the image URL and `Attachment.ContentType="thumbnail"` makes the image show as a thumbnail.
1. **ListAppend** action adds the **Attachment** variable to the list of attachments in **ResponseMessage.Attachments**.
1. **Response Message** is a generic node that assigns the common values of **ResponseMessage**.

Once the chatbot runs, it replies this message to the user:

![Creating a chatbot response with a card](images/webhook-browser-preview-thumbnail.png?width=350)

## Reply with a multiple suggestions card

This is a card that offers several suggestions to the user. For more information, explore the chatbot demo app.

![Creating a chatbot response with a card](images/webhook-browser-preview-multiple-suggestions.png?width=350)