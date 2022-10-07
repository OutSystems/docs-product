---
helpids: 30168
locale: en-us
guid: 2e53abeb-cf9d-4231-808e-33e9b5c1d17e
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid SOAP Static Entity Usage Error

This error is issued in the following situations:

  * Invalid Property Value: `'<static_entity> Identifier' is defined by a consumed SOAP Web Service and cannot be used as Data Type of an Entity Attribute.`

    Static entities defined by consumed SOAP web services cannot be used as data types in some OutSystems elements.

    Choose a different data type for the entity attribute.

  * Invalid Property Value: `'<static_entity>' is defined by a consumed SOAP Web Service and cannot be used as an Aggregate Source.`

    Static entities defined by consumed SOAP web services cannot be used as data sources in aggregates.

    Exclude the source causing the error from the aggregate.

  * Unknown SourceAttributeRecord: `'<static_entity>' is defined by a consumed SOAP Web Service and cannot be used as a Combo Box Source Entity.`

    Static entities defined by consumed SOAP web services cannot be used as sources of combo boxes.

    Choose a different source entity for the combo box.

  * Invalid SQL: `<static_entity> is defined by a consumed SOAP Web Service and cannot be used in an SQL clause.`

    Static entities defined by consumed SOAP web services cannot be used in SQL clauses.

    Exclude the static entity from your SQL clause.

