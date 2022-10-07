---
locale: en-us
guid: 781daf7e-11c4-4792-b928-e8d9a993f5fe
app_type: traditional web apps, mobile apps, reactive web apps
---

# Deprecated jQuery Version Warning

Message
:   `jQuery version ‘1.4.2 OS’ is currently being deprecated. Consider upgrading to the latest version, since new features might not work as expected.`

Cause
:   The module is using a jQuery version that may no longer provide the correct behavior for new features of OutSystems.

Recommendation
:   To fix this do the following:

    1. Check the list of supported jQuery versions in the 'jQuery Version' property of the module.
    1. Assess the impact (on module elements that use jQuery) of upgrading to the latest version.
    1. Modify module elements that need to be tweaked to work with the new version.
    1. In the 'jQuery Version' property, select the latest jQuery version to finish the upgrade.

---

Message
:   `<widget> widget is not supported with jQuery version '1.4.2 OS'. Consider upgrading to the latest jQuery version.`

Cause
:   The specified widget may not work properly if you are using the referred jQuery version.

Recommendation
:   To fix this do the following:

    1. Check the list of supported jQuery versions in the 'jQuery Version' property of the module.
    1. Assess the impact (on module elements that use jQuery) of upgrading to the latest version.
    1. Modify module elements that need to be tweaked to work with the new version;
    1. In the 'jQuery Version' property, select the latest jQuery version to finish the upgrade.
