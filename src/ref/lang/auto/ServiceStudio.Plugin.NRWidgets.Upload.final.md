---
kinds: ServiceStudio.Plugin.NRWidgets.UploadDescriptor
helpids: 30045
summary: Reference information on the Upload widget for allowing the users to browse and select a local file to upload into the application.
tags: outsystems-designing-screens; reference; designing-screens; upload-widget
locale: en-us
guid: 2abe40f3-97c8-4405-b758-3baa7e638b72
---

# Upload


The Upload widget lets users browse and select a local file, which you can then upload to the server.

<div class="info" markdown="1">

Notes:

* Users can drag a file to the Upload widget in most **modern browsers**. However, they can't do it in Internet Explorer 11, as that browser doesn't support drag-and-drop.

* The widget can handle files up to 250MB. Larger files might not be loaded properly and end up empty, with a file size of 0 bytes.

</div>

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
<td title="FileContent">File Content</td>
<td>Holds the file selected by the user.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="FileName">File Name</td>
<td>Holds the name of the file.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Accept">Accept</td>
<td>Specifies the type of UI placeholder. The placeholder hints the expected input type.</td>
<td>Yes</td>
<td>Image</td>
<td>The possible values are: Image, Video, Any.</td>
</tr>
<tr>
<td title="Mandatory">Mandatory</td>
<td>Boolean literal or expression that defines if the widget is required.</td>
<td>Yes</td>
<td>False</td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"upload"</td>
<td>When Accept has the value Image, an additional class 'upload-image-withoverlay' is added to this property.</td>
</tr>
<tr >
<th colspan="5">Attributes</th>
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

## Events

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="OnChange">On Change</td>
<td>Screen action to be executed or a screen to navigate to when the value of the element changes.</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Transition">Transition</td>
<td>Transition effect applied when navigating to another screen.</td>
<td></td>
<td>By default defined at module level.</td>
</tr>
<tr>
<td title="EventName">Event</td>
<td>JavaScript or custom event to be handled.</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Handler">Handler</td>
<td>JavaScript event handler.</td>
<td></td>
<td></td>
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
<tr>
<td>Valid</td>
<td>False when required inputs are not present or the input value does not comply with the defined data type. You can override this property value when performing custom validations.</td>
<td></td>
<td>Boolean</td>
<td></td>
</tr>
<tr>
<td>ValidationMessage</td>
<td>Message describing the built-in validation constraints not satisfied when 'Valid' is False. You can override this property value when performing custom validations.</td>
<td></td>
<td>Text</td>
<td></td>
</tr>
</tbody>
</table>

