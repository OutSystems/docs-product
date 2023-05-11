---
locale: en-us
guid: 2d30ca21-ea1e-4db2-b580-602938b104aa
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Parameter Error

Message
:   `<parameter> data type is invalid.`

Cause
:   The data type of the parameter is not valid.

Recommendation
:   Edit the [action parameter](<../../../extensibility-and-integration/integration-studio/managing-extensions/action-parameter.md>) and set a valid data type for it.

---

Message
:   `'<parameter>' data type is invalid: '<entity>' has no attribute set as Identifier.`

Cause
:   The attribute set in the output parameter is not an Identifier attribute and there's no Identifier attribute defined in the entity.

Recommendation
:   Edit the [entity](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-define.md>), define the Identifier attribute, and set it on the [action parameter](<../../../extensibility-and-integration/integration-studio/managing-extensions/action-parameter.md>).

---

Message
:   `<parameter> must be set as 'Input' to use 'Mandatory'.`

Cause
:   The output parameter is set as Mandatory but only input parameters can be set as Mandatory.

Recommendation
:   Edit the [action parameter](<../../../extensibility-and-integration/integration-studio/managing-extensions/action-parameter.md>) and un-set it as mandatory.
