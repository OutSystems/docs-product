---
kinds: ServiceStudio.Model.NewRuntime.Theme+Kind, ServiceStudio.Model.Theme+Kind, ServiceStudio.Model.NewRuntime.ReferenceTheme+Kind, ServiceStudio.Model.ReferenceTheme+Kind
helpids: 0, 17140
locale: en-us
guid: b29c0bb6-f138-4d20-934f-df01ba3c4e2a
---

# Theme

A Theme defines the look and feel of the application, including what layouts are used for the screens, the global stylesheet used, and also the grid definitions used to position and size elements on the screen. 

## Exposed Theme

A Theme cannot be exposed when:

* It has a Web Block with a parameter that is defined using an Entity/Structure that is not exposed.
* It has a Web Block with a parameter that is defined using an Entity/Structure that is reused from another module.
* It contains a Link widget, Button widget, or a consumed Web Screen with arguments of Binary Data, Record, or List data types.

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
<td title="Mobile">Mobile</td>
<td>Set to Yes to optimize screen rendering for small devices.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="OnException Handler">OnException Handler</td>
<td>Specifies the 'OnException' handler to be called by all the flows using this theme. This option can only be used when the 'Global Exception Handler' property of the module is set to '(Theme Exception Handler)'.</td>
<td></td>
<td>Common\OnException</td>
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
<td title="Has Exception Handling">Has Exception Handling</td>
<td>Read-only property informing if the referenced theme includes support for exception handling.</td>
<td>Yes</td>
<td>No</td>
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
<td>20</td>
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
<th colspan="5">Web Blocks</th>
</tr>
<tr>
<td title="Layout">Layout</td>
<td>Specifies the web block used as layout for screens. If undefined, it is inherited from the Base Theme.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Header">Header</td>
<td>Specifies the web block used as layout for the header.</td>
<td></td>
<td>Common\Header</td>
<td></td>
</tr>
<tr>
<td title="Menu">Menu</td>
<td>Specifies the web block used as layout for the menu.</td>
<td></td>
<td>Common\Menu</td>
<td></td>
</tr>
<tr>
<td title="Footer">Footer</td>
<td>Specifies the web block used as layout for the footer.</td>
<td></td>
<td>Common\Footer</td>
<td></td>
</tr>
<tr>
<td title="Info Balloon">Info Balloon</td>
<td>Specifies the web block used as layout used for info balloons.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Pop-up Editor">Pop-up Editor</td>
<td>The Web Block to be used for the layout of popup editor pages. If empty it will inherit from Base Theme.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Email">Email</td>
<td>Specifies the web block used as layout for emails. If undefined, it is inherited from the Base Theme.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Images</th>
</tr>
<tr>
<td title="True Image">True Image</td>
<td>The Image for the True condition of If Widgets in TableRecords or ListRecords.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="False Image">False Image</td>
<td>The Image for the False condition of If Widgets in TableRecords or ListRecords.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Info Balloon Image">Info Balloon Image</td>
<td>The Image for the widget that links to a Info Balloon page.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

