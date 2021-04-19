---
summary: Learn how to add a record or row, remove a record or row, and change an attribute or cell in Service Studio.
tags: 
---

# How to edit the data of an entity in Service Studio

Before checking the rest of this article, check out

## Add a record or row { #add }

To add a record or row, follow these steps:

1. In the module where the entity exists, go to the **Data** tab, and double-click the entity to **View or Edit Data**.

1. Select **Add row**.

1. If one or more cells' has a red outline, it probably means they're mandatory attributes. [Define each one of those cells](#modify).

1. [Optional] [Define each one of the remaining cells](#modify).

1. Check and fix any issues with your pending changes.

1. Select **Apply**.

## Remove a record or row { #remove }

To remove a record or row, follow these steps:

1. In the module where the entity exists, go to the **Data** tab, and double-click the entity to **View or Edit Data**.

1. Right-click the row you want to remove, and select **Delete row**.

1. Select **Apply**.

## Modify a record's attribute { #modify }

To modify a record's attribute or cell, follow these steps:

1. In the module where the entity exists, go to the **Data** tab, and double-click the entity to **View or Edit Data**.

1. Double-click an empty space inside the cell you want to change.

1. Depending on the data type of the cell, set the data in one of the following ways:

    * For a **Text** or **Phone** cell, enter a text string, for example `text` or `+1 555 565 3730`.
    * For an **Email** cell, enter a text string with at least two characters separated by a **@**, for example `fran.wilson@example.com`.
    * For a **Integer** or a **Long Integer** cell, enter an integer for example, `10`.
    * For a **Decimal** or a **Currency** cell, enter a decimal, for example, `10.8`.
    * For a **Date** cell, enter a date using the `YYYY-MM-DD` format, for example, `1988-08-28`.
    * For a **Time** cell, enter a time using the `HH:MM:SS` format, for example, `23:59:59`.
    * For a **Date Time** cell, enter a time using the `YYYY-MM-DD HH:MM:SS` format , for example, `1988-08-28 23:59:59`.
    * For a **Boolean** cell, enter **true** or **false**, capitalization is irrelevant.
    * For a **Binary** cell, select and upload a file.
    * For an entity identifier cell, select a value from the dropdown.
    * For a static entity identifier cell, select a value from the dropdown.

1. If the cell has a red outline, hover over the highlighted cell to learn about the issue, and then fix the issue.

1. Select **Apply**.
