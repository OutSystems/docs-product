---
locale: en-us
guid: aa586167-cd4f-46aa-bd1b-1ddb48969923
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid Attribute Error

The `Invalid Attribute` error is issued in the following situations:

* `<attribute> data type is invalid`
  
    The data type used in the `<attribute>` is not valid. For example, the data type of an entity attribute/variable is an Entity Identifier of an Entity that no longer exists.

    Check the entity attribute/variable and fix the data type.

* `'Delete Rule' of self-referencing <attribute> cannot be set to 'Delete'`
  
    You have an entity attribute that is a foreign key to the entity itself (self-reference). The Delete Rule property of the attribute cannot be set to Delete to delete itself.

    Change the value of the Delete Rule property to Protect or Ignore, according to your needs.

* `'Decimals' must be set to an 'Integer' literal value in <attribute>`
  
    You have an attribute with the Decimals property set with a value that is not an Integer.

    Change the value of the Decimals property of this attribute to an Integer literal value.

* `'Length' must be set to an 'Integer' literal value in <attribute>`
  
    You have an attribute with the Length property set with a value that is not an Integer.

    Change the value of the Length property of this attribute to an integer literal value.

* `'<attribute>' is an invalid attribute name in <entity>`
  
    You are using an Oracle database and the name of the entity attribute is a reserved word. 
    The reserved words are: 
    
    * timestamp
    * number
    * blob
    * clob
    * varchar2

    You must change the attribute name according to Oracle rules.

* `'Delete Rule' of attribute <entity>.<attribute> must be set to 'Ignore' since <referenced entity> producer is an extension`
  
    You've created a relationship between an Entity and a Foreign Entity (an entity defined in an Extension). In this situation, it is not possible to guarantee the referential integrity
    
    Set the Delete Rule property of the attribute to Ignore.

* `'Delete Rule' of attribute <entity>.<attribute> must be set to 'Ignore' since <referenced entity> is not a reference of this module`
  
    You've created a relationship between an Entity and an Entity that is not a reference of your module. In this situation, it is not possible to guarantee the referential integrity.
    
    Set the Delete Rule property of the attribute to Ignore.

Double-click on the error line to select the attribute that was left with an invalid attribute.
