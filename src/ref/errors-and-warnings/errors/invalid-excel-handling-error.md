---
locale: en-us
guid: 554085e9-ccc7-4e7a-8b41-a7dcb7f84429
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Excel Handling Error

The `Invalid Excel Handling` error is issued in the following situations:

* `At least one attribute must be selected`
  
    You are using a Record List to Excel element that does not specify which attributes of the List of records will be downloaded to MS-Excel.

    Edit the action flow and in the Record List to Excel element and specify the attributes in the Attribute Selection property.

* `<element> selected attributes cannot be of 'Binary Data' data type`
  
    The Record List to Excel element has selected attributes of the Binary Data data type.

    Edit the action flow, go to the Attribute Selection property of the Record List to Excel element, and uncheck the attributes of Binary Data data type.

* `<element> selected attributes cannot be of 'Record' or 'Record List' data types`
  
    You are using a Record List to Excel element that has some selected attributes of Record or List data type.

    Edit the action flow, go to the Attribute Selection property of the Record List to Excel element, and uncheck the attributes of Record or List data type.

* `<element> 'Record Definition' cannot contain entities/structures with 'Binary Data' data type attributes`
  
    You are using an Excel to Record List element in which the List definition contains attributes of Binary Data data type.

    Edit the action flow and in the Excel to Record List element, change the definition of the List that you are using to import an MS-Excel file.

* `<element> 'Record Definition' cannot contain structures with nested 'Record' or 'Record List' data type attributes`
  
    You are using a Record List to Excel element in which the List definition contains attributes of Compound data type containing attributes of the Record or List data type.

    Edit the action flow and in the Record List to Excel element, change the definition of the Record List that you are using to export to an MS-Excel file.
