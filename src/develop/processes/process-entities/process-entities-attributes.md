# Process Entities Attributes

A **Process Entity** is defined by a set of fixed attributes and another set of dynamic attributes.

## Fixed Attributes

The fixed attributes of a Process entity are as follows:

* **Process_Id**: The identifier of the process instance of the process entity. (Type: Process Identifier)

* **Label**: The label of the process. (Type: Text)

* **Is_Suspended**: Indicates whether the process is suspended. (Type: Boolean)

* **Created**: Date when the process was created. (Type: Date Time)

## Dynamic Attributes

The dynamic attributes of a process entity are the ones used as input parameters for the process. In this way, the process entity stores the runtime values of the process input parameters.

Use these attributes to [query process entities](intro.md#using-a-process-entity) and obtain process information to be used in your application logic.
