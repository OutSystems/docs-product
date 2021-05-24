---
summary: Use Send Email action on the server to send emails. Trigger manual or automatic sending of emails.
tags: support-application_development,
---

# Sending Emails

When designing an app to send emails to your users, you must consider the following types of actions:

* **Sending emails.** This is a generic action. The platform takes an Email you created in Service Studio, renders it as an email, and then sends it to the user inbox.
* **Triggering emails.** This is an event that initiates the sending of an email. This is usually an automated action, but you can trigger sending an email manually in the UI.

<div class="info" markdown="1">

This content is about a technical preview. See [Technical Preview - Emails in Mobile and Reactive Web Apps](intro.md) for more information.

</div>

## Creating logic for sending emails

To create logic that sends an email, follow these steps in Service Studio:

1. Go to the **Logic** tab and create a new server action by right-clicking **Server Actions** and selecting **Add Server Action** from the menu. A new server action opens for editing. The logic for sending emails runs on the server side.

1. Drag the **Send Email** action to the flow. Service Studio adds **Send Email** to the flow and shows an error to let you know some parameters are missing.

    ![Send Email in the logic flow](images/logic-send-email-tool-ss.png?width=700)

1. Go to the **Send Email** properties action and select your Email in the **Email** list. Service Studio now shows the list of input parameters your Email requires.

    ![Send Email in the logic flow](images/logic-send-email-select-ss.png?width=410)

1. To create the parameters in the server action to pass the values to the Email, right-click the Server Action and select **Add Input Parameter**. Repeat as needed to add the following:

    * All parameters that the Email requires
    * The input parameter for the **To** field of the **Send Email** action

1. Go to the **Send Email** action properties in the flow and set **To** property and the required values from the Email you selected in the **Email** list.

    ![Send Email with all parameters set](images/logic-send-email-ready-ss.png?width=410)

    <div class="info" markdown="1">

    Be careful when editing the **From** property in the **Send Email** action. Most spam algorithms reject emails with a misconfigured **from** field.

    </div>

    Your module is now ready for sending the email. The next step is to create logic to trigger sending the email.

## Triggering emails

Depending on the use case, you can use different mechanisms to tell the platform to render and send the email. Your app can have a feature that lets users email each other by clicking a send button. Some other use cases require automated email sending, such as generating onboarding emails.

### Trigger emails manually

You can manually trigger the sending of an email when you test the app and when you have use cases that require it. On the UI, there can be an element, such as a **Button** widget (1) with an **On Click** event to call a client action (2).

![UI for triggering emails](images/trigger-email-manually-ui-ss.png?width=700)

In the client action, you can call the server action that sends the email (3). You must provide the input parameters required by the action. The feedback message from the UI (4) is there to let the user know the app called the logic to send the message. 

![Client action calls server action](images/trigger-email-manually-logic-ss.png?width=410)

### Trigger emails automatically

There are many use cases where you might want to sends an email automatically, for example, when you send an email to users after a registration. Consider an event registration, where users who want to attend the event, need to fill in the registration details in a form.

![Sample registration screen](images/sample-screen-ss.png?width=700)

The logic for new registrations checks if the user entered valid information (1). If the information is valid, the logic handles the registration request (2) and then triggers the sending of the confirmation email (3).

![Sample registration screen](images/sample-logic-new-registration-ss.png?width=500)