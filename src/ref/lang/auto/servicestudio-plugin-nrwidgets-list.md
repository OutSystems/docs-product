---
kinds: ServiceStudio.Plugin.NRWidgets.ListDescriptor
helpids: 30030
summary: Reference information on the List widget for allowing users to get a list of records on a screen.
tags: runtime-mobileandreactiveweb; outsystems-designing-screens; reference; designing-screens; list-widget
locale: en-us
guid: 836cb2ad-86f5-4d9a-96ac-b7e34b4e82f7
app_type: mobile apps, reactive web apps
platform-version: o11
---

# List

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Use the List widget to display a simple list, for example a list of Expressions, or to display more complex items by adding a [List Item widget](servicestudio-plugin-nrwidgets-listitem.md). The List widget requires a source to populate the items.

## List virtualization

The List widget uses virtualization to render elements that are visible on the screen. Virtualization optimizes performance when rendering lists with a large number of list items, as only the visible items are added to the DOM. Controlling the list items in the DOM reduces the memory footprint of OutSystems applications, which is important for older devices with less resources. Having fewer list items in the DOM improves the initial screen rendering as well as the scrolling experience.

## Viewport threshold

To further enhance the scrolling experience, it’s possible to configure the viewport threshold to render extra elements (at the top or at the bottom of the list in the DOM), so when the user is scrolling, those elements are ready to be displayed on screen. Having elements rendered before they are visible on screen improves the scrolling experience. The extra elements are not visible because they are outside of the list’s viewport window. You can configure the viewport window thresholds by setting the ``virtualization-threshold-before`` or ``virtualization-threshold-after`` value (in pixels) in the **Attributes** of the List.

![Virtualization treshold before and after](<images/virtualization-before-after-ss.png>)

``Virtualization-threshold-before`` renders the elements before the first visible element, even if they are not visible. ``virtualization-threshold-after`` renders the elements after the last visible element, even if they are not visible. 

You can also deactivate the virtualization by setting the List attribute value to ``disable-virtualization=True``.

![Disable virtualization](<images/virtualization-disable-ss.png>)

## Scroll threshold
When the List reaches the scroll threshold value, the list triggers the OnScrollEnding event. You can configure this event to load more data into the list which allows the user to keep scrolling continuously. The scroll threshold default value is 2000 pixels. To change the scroll ending threshold, set the ``infinite-scroll-threshold`` in the **Attributes** of the List.

![Disable virtualization](<images/virtualization-infinite-ss.png>)

## Known Issues
You should avoid using list virtualization when your list items have complex blocks with built-in aggregates or you are using custom or third-party JavaScript that interacts with the list items. Since virtualization adds and removes elements from the DOM, and the aggregates of a block run automatically when they are added to the DOM, scrolling a List whose items contain blocks with aggregates will constantly trigger their execution, which may result in a significant amount of server requests that can hinder server performance. 

To prevent this issue, you can either disable the list virtualization or fetch all the data on the screen and pass it as parameters to the blocks. If you encounter any other UI/UX issues when using the List widget (for example, scrolling or list item visibility), a possible workaround is disabling list virtualization. For more details on how to disable list virtualization, see the [List virtualization](#list-virtualization). 


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

