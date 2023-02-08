---
locale: en-us
guid: bad56419-c238-4adc-971c-c4b30c9a2af5
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Screen Error

The `Invalid Screen` error is issued in the following situations:

* `'Cache in minutes' cannot be set on screens and blocks with 'Binary Data', 'Record', or 'List' parameters`
  
    You have a Screen/Block with the Cache in Minutes property set and there are input parameters of the Binary Data, Record, or List data type.

    Unset the Cache in Minutes property of the screen/block that has the input parameter of the Binary Data, Record, or Record List data type.

* `<variable> variable in <screen> cannot be bound to multiple widgets`
  
    You have the same variable associated with more than one input widget.

    Change the logic to have each variable associated with one input widget.

* `Screen <screen> contains a <widget> Widget that is corrupted`
  
    The widget that you see on your screen is not synchronized with its internal definition in the module.

    Delete the widget from the screen and then re-create it again.

Double-click on the error line to take you directly to the element where the situation was detected.
