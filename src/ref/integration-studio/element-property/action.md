# Action Properties

The next table presents the properties of the [action](<../../../extensibility-and-integration/integration-studio/managing-extensions/action-define.md>) element.  
  
<table markdown="1">  
<tr>
<th>
Property
</th>
<th>
Description
</th>
<th>
Optionality
</th>
<th>
Default value
</th>
<th>
Obs.
</th>
</tr>
<tr>
<td>
Name
</td>
<td>
Name of the action.
</td>
<td>
Mandatory
</td>
<td>
`Action <n>`
</td>
<td>
See [rules for naming elements](<../element-naming.md>).
</td>
</tr>
<tr>
<td>
Icon
</td>
<td>
Icon associated with the action. This icon will be used in Service Studio to graphically identify this action.
</td>
<td>
</td>
<td>
By default, Integration Studio associates an icon with the extension action. If the action was initially created in this tool, then the icon associated is ![](images/action.gif) `(Default)`. If the action was imported from a .NET assembly, then the default icon associated is ![](images/imported-action.gif).
</td>
<td>
See how to [change the action icon](<../editor/action.md>).
</td>
</tr>
<tr>
<td>
Description
</td>
<td>
Free text that describes the action.
</td>
<td>
Optional
</td>
<td>
</td>
<td>
Useful for documentation and knowledge transfer purposes.
The maximum size of this property is 255 characters.
</td> </tr>
<tr>
<td>
Function
</td>
<td>
Indicates whether this action can be used as a user function in expressions, in Service Studio.
</td>
<td>
Mandatory
</td>
<td>
No
</td>
<td>
</td>
</tr>
<tr>
<td>
Import Details...
</td>
<td>
Presents information about the import operation.
</td>
<td>
Optional
</td>
<td>
</td>
<td>
Only available when the action was added during the Import Actions from .NET Assembly wizard. For more information, see [Action editor](<../editor/action.md#import-details>).
</td>
</tr>
</table>
