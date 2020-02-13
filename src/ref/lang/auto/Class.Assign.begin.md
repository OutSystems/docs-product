Use the Assign Tool to assign values to variables. The Properties Pane shows assignments in the variable-value pairs, forming the assignment statements. The **Value** in the statement can be other variable, literal or a computed value.

To select a **Variable**, do any of the following in the field of Assign Tool within properties pane:

* Select the name of **Variable** in the drop-down list.
* Enter the variable name (or start typing for a suggestion).
* Double-click the field, click the equal sign icon (![](../../../shared/icons-service-studio/assign.png)), or select **(Select Variable...)** in the drop-down to open the Assign Value window.

Similarly, to assign a value or variable to a **Value** field, you can:

* Select the name of a variable in the drop-down list.
* Enter the value.
* Double-click the field, click the formula icon (![](../../../shared/icons-service-studio/expression.gif)) or select **(Expression Editor...)** in the drop-down to open the Expression Editor.

When assigning values for Record data type, Service Studio can offer to assign the values of attributes automatically if you set an initial assignment of the attributes which identifies the record. If automatic assignment is available, you will see **(Auto Assign &lt;Record&gt;.&lt;Attribute&gt;)** in the drop-down list.

OutSystems assigns by value, with some exceptions for assignment by reference. The value of Record List, Binary Data and Object data types are assigned by reference. Use the `ListDuplicate()` built-in function to create a copy and perform the assignment by value.
