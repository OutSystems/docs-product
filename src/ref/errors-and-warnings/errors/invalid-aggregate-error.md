---
locale: en-us
guid: a69b71e6-0e42-4f5c-9452-a60e5432cd93
---

# Invalid Aggregate Error

The `Invalid Aggregate` error is issued in the following situations:

* `The <aggregate> cannot join data from multiple databases. Change it to only use entities from a single database`
  
    You are using entities from multiple databases.  
  
    Change the aggregate to use entities from a single database.

* `The <aggregate> cannot have multiple join conditions with the same entities. Either remove the join conditions, or change them to stop using the same entities`
  
    You have two or more join conditions that join the same entities together.  
  
    Change the join conditions of the aggregate to ensure no two join conditions use the same entities.

* `Cannot calculate the <aggregate> of the <column name> column since it is <data type>`
  
    You are trying to calculate an aggregated function for a calculated column, but that function cannot be applied to the data type of the calculated column.  
  
    Delete the attribute created when you applied the aggregated function, or change the expression of the calculated column.

Double-click on the error line to take you directly to the source of the error.
