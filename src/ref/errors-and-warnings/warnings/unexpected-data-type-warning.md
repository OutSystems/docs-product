---
summary: OutSystems 11 (O11) documentation highlights solutions for data type mismatch issues in expressions and entity identifiers.
tags: data modelling, entity relationship, data conversion, error resolution, best practices
locale: en-us
guid: 7b112440-68dd-47c3-926d-b59e83cf0327
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Unexpected Data Type Warning

## You are comparing an identifier with a different data type. Recheck the expression or use a Data Conversion function.

**Cause**

You are comparing two Entity identifiers of different [data types](../../data/data-types/available-data-types.md).

**Recommended action**

Check the [Entity identifiers](https://success.outsystems.com/Documentation/11/Developing_an_Application/Use_Data/Data_Modeling/Entities#Primary_Key) that you are comparing in your [expression](../../logic/expressions/intro.md).

## &lt;Type> data type expected instead of &lt;Type>. Recheck the expression or use a Data Conversion function.

**Cause**

You are using the incorrect data types in an expression or in a Built-in function.

**Recommended action**

Check the [data types](../../data/data-types/available-data-types.md) managed in your [expression](../../logic/expressions/intro.md) or used in the [Built-in function](../../../ref/lang/auto/builtinfunctions.md).

## &lt;Type&gt; data type expected instead of &lt;Type&gt; for &lt;Record&gt; record. Consider changing the data type to &lt;Type&gt; in attribute &lt;Attribute Name&gt; on Static Entity &lt;Static Entity Name&gt;.

**Cause**

You are using the incorrect [data type](../../data/data-types/available-data-types.md) to reference a Record of another [Static Entity](../../../building-apps/data/modeling/entity-static.md).

**Recommended action**

If you want to reference a Record of another Static Entity, make sure the data type of the Entity Attribute that references the Static Entity is `<Static Entity Name> Identifier`.
