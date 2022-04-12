---
summary: Check the causes and recommendations on how to solve an Old Producer error.
tags:
locale: en-us
guid: 0897286f-5a9a-480b-992f-1855920b9ed1
---

# Old Producer Error

Message
:   `Producer module '<producer module name>' hasn't been prepared for the current OutSystems environment version. The Preparation of Modules may not have finished yet, failed, or it is on hold. Check Service Center for more details or try to publish '<producer module name>'.`

Cause
:   The module you are trying to publish has a dependency to a producer module that hasn't been compiled in the current Platform Server version yet. Possible causes are:

    * The environment is being upgraded to a new Platform Server version.

    * The environment was upgraded to a new Platform Server version, but the compilation of the producer module in the new version failed or was skipped.

    * The upgrade of the environment to a new Platform Server version wasn't performed correctly.

Recommendation
:   Wait for the environment upgrade to finish before you publish your applications or modules. You can [check the progress](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Modules_preparation_step_during_Platform_Server_upgrade#progress) of the modules preparation step in the Service Center console. If the step is still ongoing, wait for it to finish.

    If the problem persists, contact your System Administrator.
