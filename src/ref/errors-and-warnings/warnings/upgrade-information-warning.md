---
locale: en-us
guid: ac6e349e-376b-4975-aac4-491d09f1a7a7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Upgrade Information Warning

Message
:   `Producer '<producer>' was published with a different Platform Server version. Please republish '<producer>' to prevent runtime errors.`

Cause
:   Your module has references to a Producer module that was not published since the last server upgrade.

Recommendation
:    Notify your Service Center administrator that the producer must be published again. Afterwards, 1-Click Publish your module to prevent further situations of outdated references.

---

Message
:   `Consumer '<consumer>' was published with a different Platform Server version. Please republish '<consumer>' to prevent runtime errors.`

Cause
:   The module selected as Entry Module for the Run has not been published since the last server upgrade.

Recommendation
:   1-Click Publish the module and Run your module again.

---

Message
:   `User Provider '<provider>' was published with a different Platform Server version. Please republish '<module>' to prevent runtime errors`

Cause
:   The Provider module selected as the User Provider module, has not been published since the last server upgrade.

Recommendation
:   Notify your Service Center administrator that the Provider module must be published again. Then, 1-Click Publish your module to prevent further outdated references situations.
