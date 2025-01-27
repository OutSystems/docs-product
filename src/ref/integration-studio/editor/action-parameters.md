---
locale: en-us
guid: ef146002-08c3-4bb8-8602-0a48cfa16b7d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3043-316&t=EDoWHHiECWnNFXux-1
summary: Explore the functionalities of the Action Parameters Editor in OutSystems 11 (O11), which facilitates the management of action parameters in extensions.
tags: extension development, parameter management, service studio interface, ide features, outsystems extensions
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Action Parameters Editor

The Action Parameter Editor allows you to edit the [properties](<../element-property/action-parameter.md>) of the action parameter that belongs to your extension.

This editor is displayed together with the [Action Editor](<action.md>).

## Add and Remove Parameters

To **add** a parameter, simply type a new row in this editor or press the ![Animated button for adding a new parameter in the Action Parameter Editor](images/add-icon.png "Add Parameter Button") button in the editor or in the right menu.

To **remove** a parameter, select the parameter row and press the ![Animated button for deleting a parameter in the Action Parameter Editor](images/delete-icon.png "Delete Parameter Button") button in the editor or in the right menu.

![Warning icon indicating a potential issue when removing or toggling parameters in the Action Parameter Editor](images/warning-icon.png "Warning Icon") Since actions set as functions (property Function equal to `Yes`) must have exactly one output parameter, the remove operation could cause a violation of this rule. Integration Studio prevents it but allows you to automatically change the action to meet the requirements to be a function by setting property Function to No, if you're deleting a single output parameter of a function action.

## Input and Output Parameters

By default, the parameter is an input parameter. To define an Output parameter, simply click on the Input icon ![Toggle icon to switch a parameter to input in the Action Parameter Editor](images/input-icon.png "Input Parameter Icon") and Integration Studio switches to an Output parameter. In fact, both the Input ![Toggle icon to switch a parameter to input in the Action Parameter Editor](images/input-icon.png "Input Parameter Icon") and Output ![Toggle icon to switch a parameter to output in the Action Parameter Editor](images/output-icon.png "Output Parameter Icon") icons have a toggle behavior, allowing you to easily change the type of the parameter.

![Warning icon indicating a potential issue when removing or toggling parameters in the Action Parameter Editor](images/warning-icon.png "Warning Icon") Since actions set as functions (property Function equal to `Yes`) must have exactly one output parameter, this "toggle" operation could cause a violation of this rule. Integration Studio prevents it but allows you to automatically change the action to meet the requirements to be a function:

* By setting the property Function to `No`, if you're adding another output parameter to a function action. 

* By setting the property Function to `No`, if you're deleting a single output parameter of a function action.

## Change the Parameters Order

The order of the parameters must be the same in both the extension action and in the corresponding C# method. The Action Parameter Editor contains the necessary buttons to define the order of the parameters:

Button | Description
:-----:|:-----------
![Button to move the selected parameter down one position in the Action Parameter Editor](images/bottom-one-icon.png "Move Parameter Down Button") | Move the selected parameter down.
![Button to move the selected parameter to the bottom of the list in the Action Parameter Editor](images/bottom-all-icon.png "Move Parameter to Bottom Button") | Move the selected parameter to the bottom of the list.
![Button to move the selected parameter up one position in the Action Parameter Editor](images/top-one-icon.png "Move Parameter Up Button") | Move the selected parameter up.
![Button to move the selected parameter to the top of the list in the Action Parameter Editor](images/top-all-icon.png "Move Parameter to Top Button") | Move the selected parameter to the top of the list.

## Change the Parameter Properties

You can change the properties of the parameter, at any time. Simply double-click in the action in the [Multi-tree navigator](<../workspace.md>) or select the action in the [Multi-tab editor](<../workspace.md>) and change the parameter properties.
