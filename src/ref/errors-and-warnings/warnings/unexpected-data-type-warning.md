---
summary: Check the causes and recomendations on how to solve the different Unexpected Data Type TrueChange warnings.
tags:
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

Check the [data types](../../data/data-types/available-data-types.md) managed in your [expression](../../logic/expressions/intro.md) or used in the [Built-in function](../../../ref/lang/auto/builtinfunctions.final.md).
