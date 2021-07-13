---
summary:
tags: support-application_development,
---

# Widgets in emails


OutSystems designed widgets to help you create lightweight emails that most email readers can open. When you open Email for editing, Service Studio shows the available widgets in the widgets toolbar.

Use the [widgets in Email](#widgets-available-in-emails) like you use the widgets for Screens, with the following common differences designed to make the emails light and secure:

* Screen widgets have features that work in a UI that can handle plenty of data. For example, Table in Screens supports pagination.
* You can use JavaScript and custom actions in Screen widgets only. Most email clients don't support JavaScript due to security concerns.
 
## Table

<div class="info" markdown="1">

To quickly create a table in a Reactive Web App, drag an Entity to Email. 

</div>

When you place the Table widget to an Email, add columns and drag attributes to create columns and cells. For more information on how to work with the Table widget, see [Creating and editing tables](../../ui/table/intro.md).

## List

<div class="info" markdown="1">

To quickly create a list in a Mobile App, drag an Entity to Email. 

</div>

Drag the List widget to an Email, then drag attributes or other widgets like Image or Expression to create the list items. 

## Widgets available in Emails

You can use the following widgets in Emails.

| Widget      | Description                                         | Notes                                                          |
| ----------- | --------------------------------------------------- | -------------------------------------------------------------- |
| Container   | Lets you arrange other widgets.                     |                                                                |
| Expressions | Evaluates expressions and displays variable values. |                                                                |
| If          | Shows content based on a condition.                 |                                                                |
| Images      | Embeds an image.                                    | Binary content available in Platform Server 11.13.0 and later. |
| Link        | Adds a navigational element.                        |                                                                |
| List        | Shows records as items in a list.                   |                                                                |
| Table       | Shows records in columns and rows.                  |                                                                |
| Text        | Adds plain text.                                    |                                                                |
