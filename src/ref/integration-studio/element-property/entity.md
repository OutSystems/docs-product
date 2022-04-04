# Entity Properties

The next table presents the properties of the [entity](<../../../extensibility-and-integration/integration-studio/managing-extensions/entity-define.md>) element.  

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
Name of the entity.
</td>
<td>
Mandatory
</td>
<td>
</td>
<td>
See [rules for naming elements](<../element-naming.md>).
</td>
</tr>
<tr>
<td>
Physical Table Name
</td>
<td>
Physical table name. The name you specify for this field depends on the database you are connecting to.
</td>
<td>
Mandatory
</td>
<td>
</td>
<td>
In a SQL Server, the full physical table name is:<br/>
`[<server>].[<catalog>].[<owner>].<tab_name>`<br/>
In Oracle, the full physical name is:<br/>
`[<owner>].<tab_name>@[<server>]`
</td>
</tr>
<tr>
<td>
Logical Database
</td>
<td>
The logical name that represents the external database. In Service Center of each environment map the Database Connection to this Logical Database name. This is especially useful when staging between environments, allowing to dynamically change the entity's external database.
</td>
<td>
Optional
</td>
<td>
</td>
<td>
This field is used only for entities imported using Database Connections.
</td>
</tr>
<tr>
<td>
Identifier
</td>
<td>
Attribute that uniquely identifies the entity rows.
</td>
<td>
Optional
</td>
<td>
</td>
<td>
In database terminology, the Identifier is called the Primary Key.
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
</td>
</tr>
<tr>
<td>
Default Value behavior
</td>
<td>
Indicates how the default values of the entity's attributes are stored in the database and retrieved from the database:
`No conversion to/from Database`: all the entity's attributes that have the default value set are stored in and retrieved from the database without any conversion, i.e., it is the default value that is stored in and retrieved from the database.<br/>
`Convert to/from Null value in Database`: all the entity's attributes that have the default value set are stored in the database with the `null` value. When retrieving data from the database, the null value is converted to the attribute's default value. If no default value is defined for the attribute,  the null value is then converted to the Platform default value for the data type.
</td>
<td>
Mandatory
</td>
<td>
`No conversion to/from Database`
</td>
<td>
Only optional attributes are converted. The mandatory attributes cannot be empty so no conversion occurs.
Check also the list of [default values at runtime](<../../data/data-types/available-data-types.md>) and [in the database](<../../data/database/default-values-on-database.md>) for further information.
</td>
</tr>
</table>
