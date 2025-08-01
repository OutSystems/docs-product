---
guid: a77ed222-6660-413d-b16d-b399acb6bc82
locale: en-us
summary: Learn how to ensure all O11 end users have valid and unique email addresses before migrating to ODC.
figma:
coverage-type:
  - unblock
topic:
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - full stack developers
  - data engineers
tags: email validation, data migration, outsystems 11, end user management, duplicate emails
outsystems-tools:
  - users app
helpids: 30661
---
# User email validation

This pattern identifies end users in the assessed environment with duplicate email addresses or no email defined.

## How to solve

You must solve this pattern in the O11 source environment before proceeding with the data migration to ODC.

### Solve in O11

Ensure that all active and inactive end users of the OutSystems 11 apps you want to migrate have a valid and unique email address defined in the data source environment. Otherwise, you can’t proceed with the data migration to ODC.

Follow these steps to fix the end users' email addresses:

1. In the [Users app](../../user-management/end-user-manage/accessing-users.md), export your end users to an Excel file.  

2. Identify the users with empty or duplicate email addresses.  

3. Go back to the Users app and add or modify the identified users to ensure their email addresses are valid and unique.

<div class="info" markdown="1">

If you have access to the Migration Kit, the Migration Assessment Tool identifies this pattern for you and provides you with a JSON-format file containing the users with duplicate or empty email addresses.

</div>
