---
summary: Send emails from Reactive Web Apps and Mobile Apps. Learn more about how emails work in OutSystems.
tags: support-application_development, article-page
---

# Technical Preview - Emails in Mobile and Reactive Web Apps

Create and send emails from Mobile and Reactive Web Apps, as part of a technical preview. The technical preview consists of **Emails for Mobile and Reactive** and **Attachments in Mobile and Reactive emails**. See the prerequisites section to learn about product versions that support features you want to try out. 

## Prerequisites

To use this feature, you must meet the following requirements for the [technical previews](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_features).

**General requirements**

* Your Service Studio is up to date.
* You have configured the SMTP server. See [Configure OutSystems to Send Emails](../../../extensibility-and-integration/configure-send-emails.md) for instructions.

**Emails and basic widgets**

* You're using Platform Server 11.12.0 or later.
* You have activated the technical preview **Emails for Mobile and Reactive** in LifeTime in all environments.

**Email templates, Image with binary content, List, Table, If**,

* You're using Service Studio 11.12.0.
* You're using Platform Server 11.13.0 or later.
* You have activated the technical preview **Emails for Mobile and Reactive** in LifeTime in all environments.

**Attachments** 

* You're using Service Studio 11.12.0.
* You're using Platform Server 11.13.0 or later.
* You have activated the technical previews **Emails for Mobile and Reactive** and **Attachments in Mobile and Reactive emails** in LifeTime, in all environments.

## Getting started

The following are the steps to get you started with creating and sending emails:

1. Create an email and add some content to it. See: [Managing emails](managing.md)
2. Create logic that sends emails to users. See: [Sending emails](sending.md)
3. Optionally, add attachments in your emails. See: [Adding email attachments](attachments.md)

For more information about emails, see the following resources:

If you want to... | Check out... |
| - | - |
| Create a new email | [Creating a new Email](managing.md#creating-a-new-email) | 
| Add content for an email | [Adding content to Email](managing.md#adding-content-to-email)| 
| Add content based on user inputs  | [Handling inputs in Emails](managing.md#handling-inputs-in-emails)| 
| Add attachment to emails  | [Adding email attachments](attachments.md)| 
| Create logic to send emails | [Sending Emails](sending.md)| 
| See what widgets you can use  | [Widgets available in Emails](widgets.md#widgets-available-in-emails)| 
| See what data types you can use in inputs  | [Available data types](../../../ref/data/data-types/available-data-types.md), in particular [compound data types](../../../ref/data/data-types/available-data-types.md#compound-data-types)  | 
| Validate or format email addresses | [Email built-in functions](../../../ref/lang/auto/builtinfunction.Email.final.md)  | 
| Learn more about security | [Security best practices](https://success.outsystems.com/Documentation/Best_Practices/Security/Reactive_web_security_best_practices) and [server-to-client data transfer optimization](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Technical_Preview_-_Server-to-client_data_transfer_optimization) | 
| Send us feedback or ask for tips! | Create [a new post with the **technical preview** tag](https://www.outsystems.com/forums/tag/6875/technical-preview/) in Forums. |

## About emails in Reactive Web Apps and Mobile Apps

The following sections cover the more technical details related to the emails as a technical preview in Reactive Web Apps and Mobile Apps. If you need more specific information, let the team know in [a new post with the **technical preview** tag](https://www.outsystems.com/forums/tag/6875/technical-preview/) in Forums.

### How emails work

In Service Studio, you first define the structure of the email and the expressions the platform evaluates to generate the email content. Then, the platform turns the structure into a HTML template, evaluates the expressions, replaces the content, and creates the final HTML. Finally, the platform sends the email message using the configurations you provide in Service Center.

### Data considerations

You can create content for emails by using input parameters, local variables and the scope of the Email widgets expressions. Elements like Aggregates, Data Actions, or Client Variables aren't available in the scope of an Email element.

Emails support compound data types.

### Security consideration

Most modern apps run some logic in the client devices which makes it straightforward to inspect and manipulate the code. When you design emails that require input fields from the client-side of the app, make sure that you [follow security best practices](https://success.outsystems.com/Documentation/Best_Practices/Security/Reactive_web_security_best_practices).

### Email clients and CSS

There are many email clients and there's no consistent support for CSS. OutSystems recommends that you test your email content regularly in different clients. To check how different platforms support the CSS you want to use, you can use tools such as, [Can I email](https://www.caniemail.com/).

### CSS from producers

In this technical preview, when your Email modules (consumers) use CSS from other modules (producers), the emails show the latest styles that you published in the environment. When you publish the producer, continue using the consumer to get the latest styles from the producer. There's no need to republish the producer.

### Clipped content in Gmail

Google Gmail clips messages if the HTML code is larger than 102 KB. OutSystems recommends you start with Emails that have only basic styles, without the CSS from OutSystems UI.
