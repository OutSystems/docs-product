---
locale: en-us
guid: c903f266-1cdc-45fb-9609-188a79440359
app_type: traditional web apps, mobile apps, reactive web apps
---

# Using Process Callback Actions

When designing the process flow of your process, you can add business rules to validate the execution of your process. This allows you to block or quit the process execution if a specified condition is not verified. This behavior is implemented through **Process Callback actions**.


## Add an Process Callback Action

1. In the **module tree**, under **Processes**, right-click on the **Process** element, select **"Add Callback Action"**, and pick one of the available `On Process ...` actions.

1. Design the behavior of the action.

The business rules can be designed for the following available process callback action:

* **On Process Start**: this action is executed before a **Process** starts its execution.

You may also design activity callback actions at the process level. This allows you to move the common business rules in the callbacks of several process activities to a single place at the process level.
