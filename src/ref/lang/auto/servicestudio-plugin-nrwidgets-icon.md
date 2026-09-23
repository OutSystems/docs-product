---
helpids: 30044
summary: "Icon widget in OutSystems 11 (O11): properties for adding scalable vector icons, and WCAG 2.2 AA accessibility guidance for Mobile Apps and Reactive Web Apps."
tags:
  - Accessibility
  - Front-End
  - JavaScript
  - Mobile app
  - UI
  - Widgets
locale: en-us
guid: 46d19d6d-4088-4950-805d-c07e75825805
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - remember
  - apply
isautopublish: true
---

# Icon

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Shows an icon from a predefined set of icons for common use and content. It allows you to add a visual reference to an action, for example.

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
<td>Identifies an element in the scope where it's defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Icon">Icon</td>
<td>Scalable vector picture to display.</td>
<td>Yes</td>
<td>flag</td>
<td></td>
</tr>
<tr>
<td title="IconSize">Size</td>
<td>Size of the scalable vector picture relatively to the font-size of the first ancestor of this widget.</td>
<td>Yes</td>
<td>2x font size</td>
<td></td>
</tr>
<tr>
<td title="Visible">Visible</td>
<td>Boolean literal or expression that defines the obligatoriness of displaying the widget.</td>
<td>Yes</td>
<td>True</td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"icon"</td>
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
<td>You can pick a property from the drop-down list or type a free text. The name of the property isn't validated by the platform.<br/><br/>Duplicated properties aren't allowed. Spaces, " or ' are also not allowed.</td>
</tr>
<tr>
<td title="Value">Value</td>
<td>Value of the attribute.</td>
<td></td>
<td></td>
<td>You can type the value directly or write expressions using the Expression Editor.<br/><br/>If the Value is empty, the corresponding HTML tag is property="property". For example, the nowrap property doesn't require a value, therefore its property is nowrap="nowrap".</td>
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
<td title="EventName">Event</td>
<td>JavaScript or custom event to handle.</td>
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

## Runtime properties

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

## Accessibility – WCAG 2.2 AA compliance {#accessibility}

The **Icon** widget renders as an inline SVG element. By default, it doesn't expose any accessible name or role, so screen readers either skip it or announce it in a way that doesn't convey its purpose. How you make the **Icon** accessible depends on whether it's decorative or clickable.

### Hide a decorative icon from assistive technologies

Use this approach when the **Icon** is purely visual, for example, when it sits next to a text label that already conveys the same meaning. Exposing the icon to assistive technologies in this case only adds a redundant announcement, which affects WCAG 1.1.1 (Non-text Content).

1. In **Service Studio**, in the **Widget Tree**, select the **Icon** widget.
1. In the **Properties** pane, locate **Attributes** and add a new entry:

    * **Property**: `aria-hidden`
    * **Value**: `true`

1. Publish the module.

Don't add `aria-hidden="true"` to an **Icon** that's the only content conveying an action or a status, since that hides the information from assistive technologies entirely.

### Make a clickable icon accessible

If you add a `click` handler to the **Icon** through the **Events** property, the widget becomes interactive, but it doesn't get a role, a focus stop, or a keyboard interaction on its own. Add the following attributes and behavior to meet WCAG 4.1.2 (Name, Role, Value) and WCAG 2.1.1 (Keyboard).

1. In **Service Studio**, in the **Widget Tree**, select the **Icon** widget.
1. In the **Properties** pane, locate **Attributes** and add the following entries:

    * **Property**: `role`, **Value**: `button`
    * **Property**: `tabindex`, **Value**: `0`
    * **Property**: `aria-label`, **Value**: a text literal or expression that describes the action the icon performs (for example, `"Delete item"`)

1. In the same **Screen**, under **Events**, add a client action to the **OnReady** event that attaches a `keydown` listener to the **Icon**, so the action also runs when the user presses `Enter` or `Space`.

    ```javascript
    // WidgetId input parameter: the Icon widget's Id (for example, Icon.Id)

    var icon = document.getElementById($parameters.WidgetId);

    var onKeydown = function (event) {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            icon.click();
        }
    };

    icon.addEventListener('keydown', onKeydown);
    icon._onKeydown = onKeydown;
    ```

1. Add a client action to the **OnDestroy** event that removes the listener, to prevent memory leaks.

    ```javascript
    // WidgetId input parameter: the Icon widget's Id (for example, Icon.Id)

    var icon = document.getElementById($parameters.WidgetId);

    icon.removeEventListener('keydown', icon._onKeydown);
    delete icon._onKeydown;
    ```

1. Publish the module.

<div class="info" markdown="1">

If the icon triggers a navigation or submits a form, use the **Link** or **Button** widget instead. Both widgets already provide a focusable, keyboard-accessible control, so you don't need to replicate that behavior manually.

</div>

### Result

After completing these steps:

* A decorative **Icon** is skipped by screen readers, so it doesn't add noise to the page's accessible name.
* A clickable **Icon** is announced as a button with a descriptive name, receives focus in the **Tab** order, and responds to `Enter` and `Space`.
