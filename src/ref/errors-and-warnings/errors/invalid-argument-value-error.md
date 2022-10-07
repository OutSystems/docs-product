---
locale: en-us
guid: c28f7649-b364-4139-86ae-5b71089813ac
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid Argument Value Error

The `Invalid Argument Value` error is issued in the following situations:

* `The literal ‘<argument value>’ set in the ‘WebReferenceName’ argument of the action ‘<actionName>’ does not match any Web Service name consumed in the module.`
  
    Some actions have parameters that receive the name of Web Services consumed by the module. The name you supplied does not exist in the module.

    To fix this, check whether the Web Service is being consumed or the name is incorrect, because the Web Service does not exist in the module.

Double-click on the error line to take you directly to the argument of the action where the violation occurs.
