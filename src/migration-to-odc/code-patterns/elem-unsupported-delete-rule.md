---
guid: cf6b1c12-4035-435f-a047-396df200f56d
locale: en-us
summary: Learn how to adjust your application logic to manually handle referential integrity between different apps when converting from OutSystems 11 to ODC.
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - full stack developers
  - tech leads
  - architects
tags: outsystems 11,conversion,odc assets,entities and relationships
outsystems-tools:
  - service studio
  - conversion assessment tool
  - odc studio
helpids: "30694"
---

# Unsupported Delete Rule to an entity from another app

In ODC, when you create a relationship between two entities of different apps, the [referential integrity](https://www.outsystems.com/tk/redirect?g=34840e6f-13be-4db8-ae48-dd118a9fe303#referential-integrity) can’t be guaranteed. Thus, the only supported **Delete Rule** for the foreign key attribute is **Ignore**.

## How to solve

To ensure the same [referential integrity you had in O11](../../building-apps/data/modeling/relationship/delete-rules.md) for the relationship between two entities of different ODC apps, you need to adjust your logic. Depending on the original **Delete Rule** set in your O11 app, consider the following to adjust your O11 app to ODC architecture:

* If the original rule was **Delete**: In the ODC converted app, deleting a parent record no longer deletes the related records automatically, which can result in orphaned data. Thus, add logic to manually check for and delete any related records.

* If the original rule was **Protect**: In the ODC converted app, the deletion of a parent record that still has related records is now allowed, but the related records remain in the database. Thus, add logic to prevent the deletion if related records exist, returning a user-friendly error.

OutSystems recommendation is to solve this pattern in O11. However, you can opt to proceed with the code conversion and solve it in ODC.

<div class="info" markdown="1">

The code conversion process automatically changes the **Delete Rule** to **Ignore** for any foreign key that references an entity in another asset.

</div>

### Solve in O11 (recommended)

To solve this pattern in O11, follow these steps:

1. In the O11 app, change the **Delete Rule** of the identified foreign key attribute to **Ignore**.

1. Adjust the application logic accordingly, as described above.

1. Test all scenarios related to data deletion to ensure the adjusted O11 app behaves as expected and data integrity is maintained.

### Fix in ODC

To solve this pattern in ODC, follow these steps:

1. Proceed with the conversion.

    If you have access to the App Conversion Kit, you must set the **Where To Fix** for this finding as **ODC** in the Conversion Assessment Tool.

    <div class="info" markdown="1">

    The **Delete Rule** of the identified foreign key attribute automatically changes to **Ignore** during the conversion.

    </div>

1. Adjust the logic of your converted ODC app, as described above.

1. Test all scenarios related to data deletion to ensure the converted ODC app behaves as expected and data integrity is maintained.
