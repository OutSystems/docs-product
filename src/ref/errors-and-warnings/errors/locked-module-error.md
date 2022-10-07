---
summary: Check the causes and recommendations on how to solve the different Locked Module errors.
tags:
locale: en-us
guid: abc85ab7-84f6-4409-8e23-527447edf15b
app_type: traditional web apps, mobile apps, reactive web apps
---

# Locked Module Error

Message
:   `The 1-Click Publish started by <user> at <time> can't proceed because there is an ongoing Modules upgrade, started by Compiler Service at <time>, that is locking '<module>' module.`

Cause
:   The environment is being upgraded to a new Platform Server version, and the [modules preparation step](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade) hasn't finished yet. You cannot publish any application or module in the environment while the modules preparation step is still in progress.

Recommendation
:   Wait for the modules preparation step to finish before you publish your applications or modules. You can [check the progress](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade#progress) of the modules preparation step in the Service Center console. For further details about the ongoing upgrade, contact your System Administrator.

---
  
Message
:   `The Delete module started by <user> at <time> can't proceed because there is an ongoing Modules upgrade, started by Compiler Service at <time>, that is locking '<module>' module.`

Cause
:   The environment is being upgraded to a new Platform Server version, and the [modules preparation step](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade) hasn't finished yet. You cannot delete a module while the modules preparation step is still in progress.

Recommendation
:   Wait for the modules preparation step to finish before you delete the module. You can [check the progress](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade#progress) of the modules preparation step in the Service Center console. For further details about the ongoing upgrade, contact your System Administrator.

---
  
Message
:   `The <1-Click Publish/Delete module> started by <user> at <time> can't proceed because there is an ongoing <operation>, started by <user> at <time>, that is locking '<module>' module.`

Cause
:   The 1-Click Publish or Delete module operation you are trying to execute failed because another user or process was already executing an operation over the same module. Possible ongoing operations are:

    * 1-Click Publish
    * Delete the module
    * Apply Settings
    * Publish a solution containing the module

    If the ongoing operation is "Modules upgrade", see the above recommendations.

Recommendation
:   Wait a few minutes for the ongoing operation to finish and try again. If the problem persists:

    * Align with the user who started the ongoing operation.
    * If the ongoing operation was started by a system user (for example, the Compiler Service), contact your System Administrator to check the environment.
