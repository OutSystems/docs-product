# Invalid Entity Index Error

The `Invalid Entity Index` error is issued in the following situations:

* `<entity> entity indexes (<index1>, <index2>) are duplicated, please remove one`
  
    Your entity has duplicated indexes on the same attributes and in the same order.

    Remove one of the indexes from the entity.

* `'Text' data type attribute with length greater than 2000 is not allowed in <index>; index of <entity>`
  
    You have a Text attribute indexed with a size greater then 2000 and this situation is not allowed by some of the databases supported by OutSystems.

    You have to select what best suits your needs: 
    
    * Reducing the size of the Text attribute
    * Do not have this attribute indexed

* `At least one attribute must be defined in <index> index of <entity>`
  
    You have an index with no attributes associated.

    Edit the indexes of the entity and choose the attributes that must be indexed.

* `'Binary' data type attribute is not allowed in <index> index of <entity>`
  
    You have an Attribute of Binary data type that is indexed. This situation is not allowed by some of the databases supported by OutSystems.

    Remove the Binary data attribute from all the indexes that are using it.

Double-click on the error line to take you directly to the entity in the Module Tree.
