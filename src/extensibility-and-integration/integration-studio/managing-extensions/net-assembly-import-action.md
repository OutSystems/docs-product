# Import Actions from .NET Assembly

The Import Actions from .NET Assembly wizard allows you to import the actions definitions from a .NET assembly. Using introspection into a .NET assembly, this wizard will create the actions you specified according to the signature of the .NET methods.

To import actions from a .NET assembly do the following:

1. Right-click on the **Actions** folder in the [Extension tree](<../../../ref/integration-studio/multi-tree-navigator.md>) or alternatively select **Import** on the [**File** menu](<../../../ref/integration-studio/menu/file/intro.md>).

1. Select ![](images/net-wizard.gif) **Import Actions from .NET Assembly**.

Integration Studio shows you a wizard that guides through a series of steps necessary to complete the import process:

Step 1
:   Welcome to the Import Actions from .NET Assembly wizard.

Step 2
:   In this step you must select the .NET Assembly from which you want to import the actions.

    You can select the assembly from the **Available Assemblies to Import** box, if this assembly was added previously as a [resource](<resource-define.md>) of the extension; or you can type the file name or click **Browse** to specify the .NET assembly.

    ![](images/note.gif) If this .NET assembly has dependencies that are not resources of the extension and could not be resolved automatically, Integration Studio launches the **Missing Assembly Reference** window. In this window you have to specify the location of the assembly that is missing.

Step 3
:   This step presents all the ![](images/class-icon.gif) classes and their members as defined in the .NET assembly you selected in the previous step. Each class is identified by its full namespace. Inside each class folder you might find the following .NET member types:

    * **Constructor**: The associated icon is ![](images/constructor-icon.gif). Each constructor is identified by its name and signature.
    * **Methods**: The associated icon is ![](images/method-icon.gif). Each method is identified by its name and signature.
    * **Properties**: The associated icon is ![](images/property-icon.gif). Each property is identified by its name.
    * **Public Fields**: The associated icon is ![](images/field-icon.gif). Each public field is identified by its name.

    Check the tree node you want to import. If the node has children inside, all the children nodes are automatically checked.

    You also have the option to enable the **Add null checks to imported items** option to have additional null checks included in the platform-generated code.

Step 4
:   In this step you have a complete list with the actions and resources that will be added to your extension, according to your selection, as explained below.

    * **Actions**: The [actions are created](<../../../ref/integration-studio/element-property/net-assembly-import-action.md>) based on the type of members selected in the previous step.

    * **Resources**: The .NET assembly you specified in step 2 and all its recursive references are added as [resources](<../../../ref/integration-studio/resources-tree.md>) of your extension, together with the ![](images/imported-action.gif) **DotNetAction.ico** resource, if it hasn't been added already.

    In this step, you have the possibility of analyzing how the actions will be created in the extension by clicking **View Report**. This button displays the report of the actions created and, if necessary, allows you to save it for future analysis.

## Adding null checks to imported actions

OutSystems uses a strongly typed language and doesn't support or understand some of the values that can be handed over by extensions. **Null references** are one of these values, since the OutSystems language doesn't have a way of representing them (these null references are shown as `-undefined-` in OutSystems).

It's usually up to extension developers to ensure that no null references are handed over to the OutSystems platform. However, if you enable the **Add null checks to imported items** option, the platform-generated code for the actions imported from the .NET assembly will contain additional checks to enforce the correct behavior.

If an extension action is imported from a .NET assembly with this option turned on, any null values handed over by the extension to the platform will be converted to the following default values, according to each data type:

Data Type    | Default value
-------------|--------------
Text         | `""`
Integer      | `0`
Long Integer | `0`
Decimal      | `0`
Boolean      | `False`
Date Time    | `#1900-01-01#`
Date         | `#1900-01-01#`
Time         | `#1900-01-01#`
Phone Number | `""`
Email        | `""`
Binary Data  | `new byte[0]`
Object       | `new <object>`
Currency     | `0`
Record       | `new <record>`
Record List  | `new <recordlist>`
Integer Identifier | `0`
Text Identifier    | `""`
Long Integer Identifier | `0`

## Report contents

For each action created by the wizard, the report displays the following information:

* **Action**: Name of the action with the following syntax:

    `Action <action_name>`

* **Target**: Indicates which C# member of the assembly will be invoked when this action is called inside your module. The Target syntax is as follows:

    `<member_type> <member_name> ( <input_arguments> ): <output_arguments>`

    Member type is: Constructor, Method, Property, or Field.

* **Declaring Type**: Full name of the class where the member was defined.

* **Parameters**: Input and output parameters of the action created by the wizard. The Parameter syntax is as follows:

    `<parameter_name> ( <OutSystems_data_type> <- <.NET_data_type> ): <additional_information>`

For each resource created by the wizard, the report displays the following information:

* **Resource**: Name of the resource with the following syntax:

    `Resource <resource_name>: <additional_information>`
