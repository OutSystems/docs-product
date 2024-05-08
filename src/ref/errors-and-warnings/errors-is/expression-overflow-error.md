---
summary: OutSystems 11 (O11) addresses Expression Overflow errors by recommending adjustments to default values for Decimal and Integer data types.
locale: en-us
guid: b28e1b36-ce34-4cae-b7e9-75fa23cb70ec
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Expression Overflow error

Message
:   `'Decimal' value exceeded.`

Cause
:   The Decimal literal you are using exceeds the maximum supported value.

Recommendation
:   Edit the Default value property of the [Action parameter](<../../integration-studio/element-property/action-parameter.md>), [Entity attribute](<../../../integration-with-systems/integration-studio/managing-extensions/entity-attribute.md>), or Structure attribute and fix the value in use. See the range of values for the Decimal data type.

---

Message
:   `'Integer' value exceeded.`

Cause
:   The Integer literal you are using exceeds the maximum supported value.

Recommendation
:   Edit the Default value property of the [Action parameter](<../../integration-studio/element-property/action-parameter.md>), [Entity attribute](<../../../integration-with-systems/integration-studio/managing-extensions/entity-attribute.md>), or Structure attribute and fix the value in use.  See the range of values for the Integer data type.
