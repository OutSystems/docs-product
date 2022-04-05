---
summary: Email widgets are lightweight and let you design emails most emails readers can open. Container, Expressions, If, Image, Link, Table, Text.
tags: support-application_development,
---

# Widgets in emails

OutSystems designed widgets to help you create lightweight emails that most email readers can open. When you edit an email, Service Studio shows the [available Email widgets](#widgets-available-in-emails) in the widgets toolbar.

![widgets for emails](images/email-available-widgets-ss.png?width=700)

<div class="info" markdown="1">

To use this feature, make sure you meet the [prerequisites](intro.md#prerequisites).

</div>

Use the Email widgets like you use the Screen widgets, with the following common differences designed to make the emails light and secure:

* Email widgets don't have features that require handling plenty of data. For example, Table in Emails doesn't show the pagination section.
* You can't use JavaScript and custom actions in Email widgets. Most email clients don't support JavaScript due to security concerns.

## Widgets available in Emails

You can use the following widgets in Emails.

| Widget      | Description                                         | Notes                                                          |
| ----------- | --------------------------------------------------- | -------------------------------------------------------------- |
| Container   | Lets you arrange other widgets.                     |                                                                |
| Expressions | Evaluates expressions and displays variable values. |                                                                |
| If          | Shows content based on a condition.                 |                                                                |
| Images      | Embeds an image.                                    | Using binary content from a data base available in Platform Server 11.13.0 and later. |
| Link        | Adds a navigational element.                        |                                                                |
| List        | Shows records as items in a list.                   | To quickly create a list in a Mobile App, drag an Entity to Email.                                                                |
| Table       | Shows records in columns and rows.                  | To quickly create a table in a Reactive Web App, drag an Entity to Email. See also: [Creating and editing tables](../../ui/table/intro.md).                                                               |
| Text        | Adds plain text.                                    |                                                                |
