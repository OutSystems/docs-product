---
summary: Explore common structure errors and solutions in OutSystems 11 (O11), including attribute requirements and recursive data type issues.
locale: en-us
guid: 998774b6-35c3-4c5b-9284-590d998a302f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, data modeling, web development, outsystems best practices, software troubleshooting
audience:
  - mobile developers
  - frontend developers
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Structure Error

Message
:   `<structure> must have at least one attribute.`

Cause
:   You have a structure with no attributes.

Recommendation
:   Add, at least, one attribute to your structure.

---

Message
:   `<structure>.<attribute> defines a recursive Structure data type definition.`

Cause
:   You have two or more structures with Record attributes that are using a recursive data type definition. For example,you have two structures: `StructureA` and `StructureB`. In `StructureA`, you have a Record attribute whose Record Definition is `StructureB`; and in `StructureB`, you have a Record attribute whose Record Definition is `StructureA`.

Recommendation    
:   [Edit these Record attributes](<../../../integration-with-systems/integration-studio/managing-extensions/entity-attribute.md>) and change their Record Definitions in order to avoid a recursive data type definition. 
