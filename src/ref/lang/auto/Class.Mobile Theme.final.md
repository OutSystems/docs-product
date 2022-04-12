---
kinds: ServiceStudio.Model.NewRuntime.Theme+Kind, ServiceStudio.Model.Theme+Kind, ServiceStudio.Model.NewRuntime.ReferenceTheme+Kind, ServiceStudio.Model.ReferenceTheme+Kind
helpids: 0, 17140
locale: en-us
guid: f2ef48f5-3cab-43e9-b6af-cd355e10abab
---

# Mobile Theme

A Theme defines the look and feel of the application, including what layouts are used for the screens, the global stylesheet used, and also the grid definitions used to position and size elements on the screen.  

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Base Theme">Base Theme</td>
<td>Specifies a theme from which this theme inherits its definitions by default.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Public">Public</td>
<td>Set to Yes to allow the element to be added as dependency by other modules.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td>Yes</td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr>
<td title="Style Sheet">Style Sheet</td>
<td>The theme's style sheet.</td>
<td></td>
<td></td>
<td>Click on "..." to edit the property value.</td>
</tr>
<tr >
<th colspan="5">Grid</th>
</tr>
<tr>
<td title="Grid Type">Grid Type</td>
<td>Specifies the grid behavior when sizing and aligning widgets. If undefined, it is inherited from the Base Theme.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Columns">Columns</td>
<td>Size of each column in the grid (in 'px').</td>
<td>Yes</td>
<td>12</td>
<td></td>
</tr>
<tr>
<td title="Column Width">Column Width</td>
<td>Size of the grid columns (in 'px')</td>
<td>Yes</td>
<td>60</td>
<td></td>
</tr>
<tr>
<td title="Gutter Width">Gutter Width</td>
<td>Space between columns in the grid (in 'px').</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Total Width">Total Width</td>
<td>Total grid width calculated from the previous properties (in 'px').</td>
<td>Yes</td>
<td></td>
<td>This property is read-only.</td>
</tr>
<tr>
<td title="Min. Width">Min. Width</td>
<td>Minimum size of the fluid grid (in 'px')</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Max. Width">Max. Width</td>
<td>Maximum size of the fluid grid (in 'px')</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Blocks</th>
</tr>
<tr>
<td title="Layout">Layout</td>
<td>Specifies the web block used as layout for screens. If undefined, it is inherited from the Base Theme.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

