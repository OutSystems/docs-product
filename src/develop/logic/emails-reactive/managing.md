---
summary: Use Emails under UI Flows to design and add available widgets. Add data to emails with the input parameters.
tags: support-application_development,
---

# Managing Emails

In Service Studio, Email is a UI element that lets you design and manage the content of email messages. Like Screens, you can find and create Emails in the UI Flows. However, unlike Screens that usually use the OutSystems UI, Emails require lightweight styles to follow the industry best standards for email sizes.

<div class="info" markdown="1">

This content is about a technical preview. See [Technical Preview - Emails in Mobile and Reactive Web Apps](intro.md) for more information.

</div>

## Creating a new Email

To create a new Email in Service Studio, follow these steps:
 
1. Ensure you have a **UI Flow with a blank Theme** in your module. See [Creating UI Flow without styles](../../ui/navigation/ui-flow.md#creating-ui-flow-without-styles) for instructions.

    ![UI Flow with the Theme property](images/ui-flow-blank-theme-ss.png?width=310)

    <div class="info" markdown="1">

    The name of UI Flow for emails in this document is **Emails**.  

    </div>

    <div class="warning" markdown="1">

    If you try adding an Email to a large Theme, Service Studio warns you about possible rendering issues in email clients.

    Create Emails based on a Theme without styles or a custom minimal Theme. A minimal CSS ensures low size of emails and discourages email readers from clipping the content. For example, Gmail shows **[Message clipped] View entire message** for all emails larger than 102KB.

    </div>

1. Right-click your **Emails** UI Flow and select **Add Email**. Service Studio adds a new Email element under the UI Flow. 

    ![UI Flow and the new Email menu](images/add-email-ui-flow-ss.png?width=410)

1. Select the new Email under the UI Flow, and enter the following details:

    * A name in the **Name** field
    * `"No subject"` as a temporary subject in the **Subject** field

    ![Email properties](images/email-properties.png?width=310)

## Adding content to Email

In the technical preview you can use text, images, and links in Emails. To add content to your Emails, follow these steps in Service Studio:

1. Go to **Interface** > **UI Flows** > **your Emails UI Flow** and double-click the Email you want to edit. The Email opens for editing and the widget list shows the widgets that Emails currently support.
    
    ![Email for editing](images/edit-email-open-ss.png?width=810)

    <div class="info" markdown="1">

    If you don't have Emails in your module, add one by following the instructions in [Creating a new Email](#creating-a-new-email).

    </div>

1. Drag the **Text** widget to the Email and enter some text.

    ![Text in Email](images/edit-email-add-text.png?width=810)

    <div class="info" markdown="1">

    To learn more about what elements you can use in Emails, see [Widgets available in Emails](widgets.md#widgets-available-in-emails). 

    </div>

1. (Optional) Go to the **Text** widget properties and edit the text look and feel in the **Styles** tab.

## Handling inputs in Emails

Customize the content of your Emails by adding custom information to it. Emails support compound data types and can use the data from the client scope of Email.

To add an Input to your Email and show the value in the email body, follow these steps:

1. [Add an Email to your module](#creating-a-new-email) and optionally [add some text](#adding-content-to-email).

1. Right-click the Email in the **Interface** tab and select **Add Input Parameter** from the menu. Service Studio adds an Input Parameter.

    ![Input parameter for Email](images/adding-input-param-emai-ss.png?width=410)

1. Set the following Input Parameter properties:

    * **Name** - enter `Handle`
    * **Data Type** - select **Text**
    * **Is Mandatory** - Select **Yes** to make the **Handle** a required value in the Email

    ![Input parameters for Email](images/inputs-for-emails-ss.png?width=280)

1. Double-click the Email in the **Interface** tab to open it for editing.

1. Drag an **Expression** widget to the Email. The expression editor opens.

1. Enter `"Hello, " + Handle + "!"` and click **Done**.

    ![Email preview](images/expression-preview-ss.png?width=500)


When you open this email in the email client, the expression displays "Hello, John!" when the value of **Handle** is `"John"`.


<div class="warning" markdown="1">

[Follow security best practices](https://success.outsystems.com/Documentation/Best_Practices/Security/Reactive_web_security_best_practices) when designing emails that have user inputs.

</div>

## Clipped content warning { #clipped-content-warning }

If the content of an email is too big, some email readers clip the content. For example, Gmail shows **[Message clipped] View entire message** for all emails larger than 102KB. This can happen if you're generating content in your emails with a Theme that has a lot of CSS not designed for emails.

To reduce the size of the email content, use a UI Flow with a blank Theme. See [Creating UI Flow without styles](../../ui/navigation/ui-flow.md#creating-ui-flow-without-styles) for instructions.
