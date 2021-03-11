---
summary: Check the causes and recomendations on how to solve the different Old Producer errors.
tags:
---

# Old Producer Error

Message
:   `Producer '<module>' hasn’t been upgraded to the current OutSystems environment version, even though it had been previously upgraded to an old environment version. (...)`

Cause
:   The module you are trying to publish has a dependency to a producer module that hasn't been compiled in the current Platform Server version yet. Possible causes are:

    * The environment is being upgraded to a new Platform Server version.

    * The environment was upgraded to a new Platform Server version, but the compilation of the producer module in the new version failed or was skipped.

    * The upgrade of the environment to a new Platform Server version wasn't performed correctly.

Recommendation
:   Wait for the environment upgrade to finish before you publish your applications or modules. You can [check the progress](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/01_Upgrade_OutSystems_Platform) of the modules preparation step in the Service Center console. If the step is still ongoing, wait for it to finish.

    If the problem persists, contact your System Administrator.

---
  
Message
:   `Producer '<module>' hasn’t been upgraded to the current OutSystems environment version. (...)`

Cause
:   The module you are trying to publish has a dependency to a producer module that hasn't been compiled in the current Platform Server version yet. Possible causes are:

    * The environment is being upgraded to a new Platform Server version.

    * The environment was upgraded to a new Platform Server version, but the compilation of the producer module in the new version failed or was skipped.

    * An upgrade of the environment to a new Platform Server version wasn't performed correctly.

Recommendation
:   Wait for the environment upgrade to finish before you publish your applications or modules. You can [check the progress](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/01_Upgrade_OutSystems_Platform) of the modules preparation step in the Service Center console. If the step is still ongoing, wait for it to finish.

    If the problem persists, contact your System Administrator.
