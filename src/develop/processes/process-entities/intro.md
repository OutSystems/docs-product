---
tags: support-application_development; support-webapps
locale: en-us
guid: 8a78e373-ba94-47e7-94e2-0b7dad3296c2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Use Process Entities

A **Process Entity** is a special entity that stores runtime information about processes that can be used in, for example, queries about processes.

## Add a Process Entity

Edit the process properties and set the `Expose Process Entity` property to Yes.

## Process Entity Identifier

Process entities are uniquely identified by the process identifier which means each process instance has one and only one process entity.

## Using a Process Entity

Use the Process Entities to obtain process runtime information to use in your application logic, such as, to check whether the process is suspended or to use the process identifier attribute of the process entity to terminate a process execution.

### Example

Imagine that you have an application with processes to manage documents and you want a document process to end when that document is deleted. Imagine also that a process instance is launched for each newly created document, which means: the document identifier is [an input parameter of the process](../process.md#launching-a-process) and also [an attribute of the process entity](process-entities-attributes.md).

Now, to end the process, design a screen action to be executed when the document is deleted, and execute the ProcessTerminate System action. To obtain the process identifier, add an aggregate using the process entity with the condition that the process entity document identifier attribute must be equal to the identifier of the document you are deleting. Then, use the process identifier attribute of the obtained process entity in the System action.

When you **delete** a process, its process entity is automatically deleted.

In a scenario of having millions of records in the process entity, consider using the best practice for [scaling queries over process entities](../best-practices/scale-queries.md).


## Using Process Entity References

OutSystems provides you with mechanisms to reuse Process Entities among modules. When you expose your Process its Process Entity is automatically exposed or when you use a Process defined in another module its Process Entity can also be used.
