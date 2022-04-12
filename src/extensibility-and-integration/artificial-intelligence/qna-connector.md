---
summary: Use the QnA Maker connector to query your Azure knowledge bases directly in the OutSystems app. QnA Maker is often part of the chatbot logic. 
tags: 
locale: en-us
guid: ab7eb739-c72b-4177-979b-bfe9d58a9334
---

# Use the Azure QnA Maker Connector in OutSystems apps

Azure QnA Maker Connector is a component for working with the Azure knowledge bases. Once you deploy a knowledge base in Azure, use the QnA Maker connector to direct the questions from your users to the knowledge base. The questions are in everyday language. For example, "How do I submit a ticket?" or "What services do you offer?".

You can use Azure knowledge bases as a back end for a chat bot. For more details see [Create AI-powered chatbots](./chatbot/intro.md).

The source of information for a knowledge base can be static content, such as manuals, or structured "questions and answers" content. For more information see [Format guidelines for imported documents and URLs](https://docs.microsoft.com/en-us/azure/cognitive-services/QnAMaker/reference-document-format-guidelines) by Microsoft.

## Before you start

Before you can use the Azure QnA Maker connector, create a knowledge base in Azure and install the connector in your OutSystems environment.

<div class="info" markdown="1">

To create a QnA knowledge base in Azure, you need Microsoft Azure account and permissions to create QnA Maker Service and QnA Maker knowledge base.

</div>

### Create and deploy a knowledge base in Azure

There are two sources of instructions you can follow to create and deploy a knowledge base in Azure. By:

* Following the OutSystems instructions [Create and deploy a knowledge base in Azure](<./chatbot/guide-azure-kb.md>). The document shows how to write an FAQ, and how to use it to create and deploy a knowledge base.
* Jumping right into [knowledge base creation at QnA Maker portal](https://www.qnamaker.ai/Create) and following the instructions there. These are more detailed instructions by Microsoft.

### Install and reference the QnA connector

Here is how you can install the connector and reference it in your app.

1. Install [Azure QnA Maker Connector](https://www.outsystems.com/forge/component-overview/6181/azure-qna-maker-connector) from Forge.
2. In Service Studio, press **Crtl+Q** and find the **AzureQnAMakerConnector** in the **Manage Dependencies** window. Select all public elements and click **Apply**. 

    ![QnA connector structure](images/qna-reference-elements-ss.png?width=600)

3. Now you can add the server actions in **Logic** > **Server Actions** > **AzureQnAMakerConnector** to your logic.

## Get the knowledge base settings 

These instructions show how to get the settings from the Azure QnA Maker service. You need the settings to configure the OutSystems QnA Maker connector.

### Subscription key and the endpoint URL

QnA Maker Service settings are part of the Cognitive Services running in Azure.

1. In Azure, open the QnA Maker service you created for the QnA Knowledge base, as part of the knowledge base creation.

2. Go to **Keys and Endpoints**. Copy the following values:

    * **Service subscription key**. One of the values, **KEY 1** or **KEY 2**.
    * **Service endpoint url**. The URL from the **ENDPOINT** field.

    ![QnA maker service in Azure](<images/qna-keys-tab.png?width=600>)

### Knowledge base deployment details

These settings are available in the QnA Maker portal **after** you deploy a knowledge base.

1. Go to the [QnA Maker portal](https://www.qnamaker.ai/) and select **My knowledge bases** in the top menu.

2. In the **My knowledge bases** page select your knowledge base. Knowledge base editor opens.

3. In the knowledge base editor, go to the **Settings** tab and scroll down to the **Deployment details** section. Copy the following values:

    * **Knowledge base id.** It's the randomized string in the POST URL. For example, if the POST URL is `/knowledgebases/123456-abcd-1234-abcd/generateAnswer`, the knowledge base ID is `123456-abcd-1234-abcd`.
    * **Knowledge base endpoint key**. It's the randomized string in the "Authorization" line.

    Here is a screenshot with the knowledge base ID (1) and the knowledge base endpoint key (2):

    ![Knowledge base deployment details](<images/qna-deployment-details.png?width=600>)

    
## Configure the QnA Maker connector

To use the QnA Maker connector in your app, you need to configure the connector in Service Center.

1. Go to **Service Center** > **Factory** > **Modules**.

1. Enter **AzureQnAMakerConnector** in the **Name** field and press **Filter**.

1. Click **AzureQnAMakerConnector** in the results list to open the module settings. Go to the **Site properties** tab and locate the **SubscriptionKey** setting.
    
    ![Sample logic flow with a QnA maker action](images/qna-properties-subscription-key-sc.png?width=700)

1. Click **SubscriptionKey** and in the **Effective Value** field enter the value of the **Service subscription key** you saved from Azure. Click **Apply**.

## Test the connector

You should test your QnA Maker connector to make sure it's working.

### Request the knowledge base info

Test the connection between the OutSystems connector and Azure by requesting information about the knowledge base from Azure.

1. Create a sample app and reference the QnA Maker connector.

2. Add a client action and drag **GetKnowledgebaseDetails** server action from  **Logic** > **Server Actions** > **AzureQnAMakerConnector** > **QnAMakerAPI_Knowledgebase** to the flow.

3. In the properties of the **GetKnowledgebaseDetails** server action, enter the knowledge base ID in the **KbId** field.

    ![A sample flow to text the connector](images/qna-test-connector-action-properties-ss.png?width=500)

    Notice that the output parameter of the server action is **KnowledgebaseDetails**, of the data type **KnowledgebaseDTO**. In this example, JSONSerialize converts the response to show it as text.

4. Run the sample logic. If the connector is working correctly, you should receive the information about the selected knowledge base. In this example, the user interface shows the information, but you can use the debugger to quickly inspect the returned values.
    
    ![Returned KB info from Azure](images/qna-get-info-browser-preview.png?width=400)

### Request a reply message from the knowledge base

Here is how you can test getting replies with the QnA Maker connector.

1. Create a sample app and reference the QnA Maker connector.
1. Define a question variable of a **QuestionDTO** data type, and then set the question text in **QuestionDTO.Question**. For example, if the parameter name is **MyQuestion** (of the data type **QuestionDTO**), then **MyQuestion.Question** is `"What is your number?"`. **MyQuestion.Question** the question that the connector sends to the knowledge base.

    ![A question parameter](images/qna-question-parameter-ss.png?width=370)

1. Add the **GenerateAnswer** action from **Logic** > **Server Actions** > **AzureQnAMakerConnector** > **QnAMakerAPI_GenerateAnswer** to the flow. Enter the values in the action properties:

    * **QnAResourceName**
    * **KnowledgeBaseId**
    * **Authorization**
    * **Question**

    Check the reference section to learn how to get **QnAResourceName**, **KnowledgeBaseId**, and **Authorization**. You defined **Question** earlier, and it's the parameter of the **QuestionDTO** data type.

1. Store the value the knowledge base sends back in a variable. The reply message is the textual value of **GenerateAnswer.Answer.Answers.Current.Answer**.

    ![A sample logic to get a reply from Azure QnA Maker service](images/qna-logic-sample-ss.png?width=500)
   
1. Run the action. If the connector is working correctly, you should receive the closest match for the question. You can also create a user interface to display the knowledge base reply, or use the debugger to quickly inspect the returned values.
    
    ![A sample reply](images/qna-reply-browser.png?width=400)

## Reference

This section contains additional information.

### Parameters in the connector actions

Here are some QnA Maker connector settings and corresponding values in Azure.

| Property   |      Location      |  Description |
|----------| ------------- |------|
| **KbId**, **KnowledgebaseId** |  QnA Maker connector server actions |  The knowledge base identifier (id). Get the identifier from the QnA Maker portal, from the **Deployment details** in the knowledge base settings. It's the randomized value of the POST URL. |
| **QnAResourceName** |  QnA Maker connector server actions | The name of the service running the QnA Maker in Azure. You can get it from the **Deployment details** in the QnA Maker portal. Check the Host line and grab the first part of the URL. For example, if the Host line is `Host: https://my-example-service.azurewebsites.net/qnamaker`, the resource name is **my-example-service**. You can get the resource name from the service endpoint URL in Azure as well. |
| **Authorization** |  QnA Maker connector server actions | The endpoint key from the **Deployment details** in the knowledge base settings, in the QnA Maker portal. For example, if the Authorization line is `Authorization: EndpointKey abcd123456`, the value you need is **abcd123456**.  |

### Data structures

To see the data structures in the connector, explore **Data** > **Structures** > **AzureQnAMakerConnector** in Service Studio.

### More information about the APIs

OutSystems created the QnA Maker connector on top of the Azure QnA Maker service. To get more details about the Azure APIs, visit the [Azure Cognitive Services REST API reference](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/), in particular:

* QnA Maker API
* QnA Maker Runtime API