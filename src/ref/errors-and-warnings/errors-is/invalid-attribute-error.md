---
locale: en-us
guid: 81b14a73-9d6c-443d-8ef8-22819129e350
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Attribute Error

Message
:   `'<attribute>' data type is invalid.`

Cause
:   The data type of the attribute is not valid.

Recommendation
:   Edit the [entity attribute](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-attribute.md>) or structure attribute and set a valid data type for it.

---

Message
:   `'<attribute>' data type is invalid: '<entity>' has no attribute set as Identifier.`

Cause
:   The attribute set in the Identifier property in not an Identifier attribute and there's no Identifier attribute defined in the entity.

Recommendation
:   Edit the [entity](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-define.md>), define the Identifier attribute, and set it on the Identifier property.

---

Message
:   `<attribute> data type must be set to 'Integer' to use 'Auto Number'.`

Cause
:   The attribute is set as `Auto Number` but you can only use Auto Numbers with attributes of `Integer` data type.

Recommendation
:   Edit the [entity attribute](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-attribute.md>) and either set its data type to `Integer` or disable it as `Auto Number`.
