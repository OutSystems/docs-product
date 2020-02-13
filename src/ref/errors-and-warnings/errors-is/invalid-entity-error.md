# Invalid Entity Error

Message
:   `<entity> must have at least one attribute.`

Cause
:   You have an entity with no attributes.

Recommendation
:   You must [add attributes](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-attribute.md>) to this entity. 

---

Message
:   `<entity> identifier attribute data type must be set to 'Integer' or 'Text'.`

Cause
:   You have an entity whose identifier is not of type `Integer` nor `Text`.

Recommendation
:   Select the [Identifier](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) attribute and change its data type to `Integer` or `Text`.

---

Message
:   `<entity> identifier attribute must be set to 'Mandatory'.`

Cause
:   You have an entity whose identifier is not mandatory.

Recommendation
:   Select the [Identifier](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) attribute and change it to be mandatory.

---

Message
:   `<entity> can only have one 'Auto Number' attribute.`

Cause
:   You have an entity with more than one sequential attribute and this situation is not allowed; you can have only one sequential attribute per entity.

Recommendation
:   Check your entity and choose which attribute must be sequential. In the other attribute, you have to [un-check](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-attribute.md>) the Auto Number property. 

---

Message
:   `<entity> must have a table name.`

Cause
:   You have an entity with no physical table name.

Recommendation
:   [Edit this entity](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) and specify the Table Name property. 

---

Message
:   `<entity> already uses table name <table>.`

Cause
:   You have more than one entity using the same physical table name.

Recommendation
:   [Edit one of these entities](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-add.md>) and change the Table Name property. 
