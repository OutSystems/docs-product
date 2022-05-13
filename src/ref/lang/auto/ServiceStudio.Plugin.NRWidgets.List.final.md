---
kinds: ServiceStudio.Plugin.NRWidgets.ListDescriptor
helpids: 30030
summary: Reference information on the List widget for allowing users to get a list of records on a screen.
tags: runtime-mobileandreactiveweb; outsystems-designing-screens; reference; designing-screens; list-widget
locale: en-us
guid: 836cb2ad-86f5-4d9a-96ac-b7e34b4e82f7
app_type: mobile apps, reactive web apps
---

# List

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Use the List widget to display a simple list, for example a list of Expressions, or to display more complex items by adding a [List Item widget](ServiceStudio.Plugin.NRWidgets.ListItem.final.md). The List widget requires a source to populate the items.

## Virtualization

The List widget uses virtualization to render only those elements that are visible in the screen. You can set the value for virtualized pixels with `virtualization-threshold-before` and `virtualization-threshold-after` in the **Attributes** of List. Adjust the threshold values to tweak the scroll behavior.

You can also deactivate the virtualization with `disable-virtualization=True`. 

## Scroll threshold

When List reaches the scroll threshold value, the app requests new records and then adds them to the list of items. The default value is 2000 pixels. Set the scroll threshold with `infinite-scroll-threshold` in the **Attributes** of List.

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
<td title="Source">Source</td>
<td>Specifies a list with records to populate the widget.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="AnimateItems">Animate Items</td>
<td>Set to Yes to Animate Items on append, insert or remove.</td>
<td></td>
<td>Yes</td>
<td></td>
</tr>
<tr>
<td title="Mode">Mode</td>
<td>Set to Custom to define a custom HTML tag to be used by the widget in runtime. Default mode sets tag as div.</td>
<td>Yes</td>
<td>Default</td>
<td></td>
</tr>
<tr>
<td title="Tag">Tag</td>
<td>Wrapper HTML tag to be used by this widget in runtime.</td>
<td>Yes</td>
<td>div</td>
<td>Only available when Mode is set to Custom.</td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"list list-group"</td>
<td></td>
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
<td title="OnScrollEnding">On Scroll Ending</td>
<td>Screen action to be executed or a screen to navigate to when the user scrolling is nearing the end of the loaded list.</td>
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
</tbody>
</table>

