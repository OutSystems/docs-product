---
kinds: ServiceStudio.Plugin.NRWidgets.ListItemDescriptor
helpids: 30031
summary: Reference information on the List Item widget for allowing you to displays a list item with full swipe behavior capability, containing a List Action widget to define the swiping behavior.
tags: runtime-mobileandreactiveweb; outsystems-designing-screens; reference; designing-screens; list-item-widget; list-item-swipe
locale: en-us
guid: 7378bd28-e563-4ca9-bede-731dca5fa49f
app_type: mobile apps, reactive web apps
---

# List Item

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Displays a list item with full swipe behavior capability, containing a [List Action widget](<ServiceStudio.Plugin.NRWidgets.ListItemAction.final.md>) to define the swiping behavior.

You can use it for example to display an entity record.

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
<td title="TriggerActionOnFullSwipeLeft">Full Swipe Left</td>
<td>Set to Yes to have default action triggered by a full swipe left. Default action is the rightmost right action.</td>
<td>Yes</td>
<td>Yes</td>
<td>The action will only be available on devices that support touch controls (for example, when accessing application on a tablet).</td>
</tr>
<tr>
<td title="TriggerActionOnFullSwipeRight">Full Swipe Right</td>
<td>Set to Yes to have default action triggered by a full swipe right. Default action is the leftmost left action.</td>
<td>Yes</td>
<td>Yes</td>
<td>The action will only be available on devices that support touch controls (for example, when accessing application on a tablet).</td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"list-item"</td>
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
<td title="OnClick">On Click</td>
<td>Screen action to be executed or a screen to navigate to when the widget is clicked.</td>
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

