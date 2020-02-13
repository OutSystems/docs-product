---
kinds: ServiceStudio.Model.WebWidgets+Image+Kind, ServiceStudio.Model.WebWidgets+ReferenceImage+Kind
helpids: 4044
---

# Image Widget

Displays an image from a defined source.  

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
<td title="Label">Label</td>
<td>Text literal or expression used as a tooltip when hovering the image or displayed when the image cannot be displayed.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Image">Image</td>
<td>Defines the image to be displayed when the Type property is set to Static.</td>
<td></td>
<td></td>
<td>The semantics of this property depends on the Type property value:<br/>
        <strong>Static</strong>: Defines the image to be displayed both at development time and at runtime;<br/>
        <strong>Database</strong>: Defines the image to be displayed at development time. At runtime, the Image property is ignored;<br/>
        <strong>External</strong>: The Image property is ignored.</td>
</tr>
<tr>
<td title="Type">Type</td>
<td>Specifies the source type of the image: Static, External or Database.</td>
<td>Yes</td>
<td>Static</td>
<td></td>
</tr>
<tr>
<td title="URL">URL</td>
<td>Text literal or expression defining the URL of the image when Type property is set to External.</td>
<td></td>
<td></td>
<td>Mandatory when Type has the value External.</td>
</tr>
<tr>
<td title="Filename">Filename</td>
<td>Text literal or expression with the name of the file, including the extension.</td>
<td></td>
<td></td>
<td>Mandatory when Type has the value Database.</td>
</tr>
<tr>
<td title="Cache">Cache</td>
<td>Maximum time the image is stored in cache when Type property is set to Database.</td>
<td>Yes</td>
<td>1 Week</td>
<td>Mandatory when Type has the value Database.</td>
</tr>
<tr>
<td title="Attribute">Attribute</td>
<td>Entity attribute that contains the image when Type property is set to Database.</td>
<td></td>
<td></td>
<td>Mandatory when Type has the value Database.</td>
</tr>
<tr>
<td title="Entity Identifier">Entity Identifier</td>
<td>Entity Identifier (literal or expression) of the image you want to display when Type property is set to Database.</td>
<td></td>
<td></td>
<td>Mandatory when Type has the value Database.</td>
</tr>
<tr>
<td title="Width">Width</td>
<td>Expression that defines the width of the image in pixels. Other accepted units are points(pt) or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Height">Height</td>
<td>Height of the widget in pixels. Other accepted units are points(pt) or percentage(%). Overrides the style sheet definition.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Style Classes">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="separator">
<th colspan="5">Extended Properties</th>
</tr>
<tr>
<td title="Property">Property</td>
<td>Name of an attribute to add to the HTML translation for this element.</td>
<td></td>
<td></td>
<td>You can pick a property from the drop-down list or type a free text. The name of the property will not be validated by the platform.<br/><br/>Duplicated properties are not allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is created as property="property". For example, the nowrap property does not require a value, therefore nowrap="nowrap" is added.</td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Id</td>
<td>Identifies the widget instance at runtime (HTML 'id' attribute). You can use it in JavaScript and Extended Properties.</td>
<td>Yes</td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

