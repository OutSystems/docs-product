# Invalid Public Structure Error

The `Invalid Public Structure` error is issued in the following situations:

* `Public Structure <structure> contains an attribute of record type <type> that is not declared as Public`
  
    In a public structure, you have a compound attribute that is defined by an Entity/Structure that is not public.

    You must set as public the Entity/Structure that defines the attribute.

* `Public Structure <structure> contains an attribute of record type <type> that is a reference`
  
    In a public structure, you have an compound attribute, that is defined by an Entity/Structure that is a module reference. You can only expose elements defined in the current module.

    You must edit the public structure, select the attribute, and use Entities/Structures defined in the current module.

Double-click on the error line to take you directly to the attribute.
