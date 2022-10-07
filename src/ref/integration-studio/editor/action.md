---
locale: en-us
guid: a3688c1a-0d04-4d07-a22e-deb8a36862db
app_type: traditional web apps, mobile apps, reactive web apps
---

# Action Editor

The Action Editor allows you to edit the [properties](<../element-property/action.md>) of an action that belongs to your extension.

This editor is displayed when an action is selected in the [Multi-tree Navigator](<../multi-tree-navigator.md>) or in the [Multi-tab Editor](<../multi-tab-editors.md>).

## Change the Icon of an Action

To change the icon associated with an action, simply use the drop-down list and select the (Browse) option. Integration Studio presents an "Open" window where you can specify the new icon.

The Icon drop-down list contains the icons of all the actions defined for the current extension.

The icon is, afterwards, added as a resource and you can find it under the Icons folder, in the [Resources](<../resources-tree.md>) tree.

## Action Parameters

To manage the action parameters, see [Action Parameters Editor](<action-parameters.md>).

## Change the Action Properties

You can change the properties of the action, at any time. Simply double-click in the action in the [Multi-tree navigator](<../workspace.md>) or select the action in the [Multi-tab editor](<../workspace.md>).

![](images/warning.gif) Since actions set as functions (property Function equal to `Yes`) must have exactly one output parameter, changing this property to Yes could cause a violation of this rule. Integration Studio prevents it but allows you to automatically change the action to meet the requirements to be a function by creating an output parameter, if the action has none and you're trying to set property Function to `Yes`.

## Import Details

This button is enabled when this action was [imported from a .NET assembly](<../../../extensibility-and-integration/integration-studio/managing-extensions/net-assembly-import-action.md>) and displays a report where you can check the original .NET signature and the corresponding action definition. The following information is displayed:

* **Action**: Name of the action with the following syntax:

    `Action <action_name>`

* **Target**: Indicates which C# member of the assembly will be invoked when this action is called inside your module. The Target syntax is as follows:

    `<member_type> <member_name> ( <input_arguments> ): <output_arguments>`

    Member type is one of: Constructor, Method, Property, Field.

* **Declaring Type**: Full name of the class where the member was defined.

* **Parameters**: Input and output parameters of the action created by the wizard. The Parameter syntax is as follows:

    `<parameter_name> (<OutSystems_data_type> <- <.NET_data_type> ): <additional_information>`
