---
helpids: 30046
summary: "Popup widget in OutSystems 11 (O11): properties, events, and WCAG 2.2 AA accessibility steps for Mobile and Reactive Web apps."
locale: en-us
guid: 8815652b-3b2f-47ee-81be-f58165e33a8c
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3289-2&t=CjwzSlGiuLoIuHu8-1
tags:
  - Accessibility
  - Events
  - Front-End
  - JavaScript
  - Mobile app
  - UI
  - Widgets
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

# Popup

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

A floating container/window above other screen content. Popup is a modal container, and therefore must be closed before the user can interact with the main screen again.

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
<td title="ShowPopup">Show Popup</td>
<td>Boolean literal or expression to determine if the popup is displayed.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Style">Style Classes</td>
<td>Specifies one or more style classes to apply to the widget. Separate multiple values with spaces.</td>
<td></td>
<td>"popup-dialog"</td>
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

From **Platform Server 11.43.0**, the **Popup** widget supports WCAG 2.2 AA compliance by default. [See the details below](#automatic).

For previous Platform Server versions, follow [these guidelines](#manual-fix) to ensure predictable and accessible interactions for all users.

### Automatic dialog name and Escape handling {#automatic}

When you enable the **Enable WCAG 2.2** option in the **Platform Configurations** tab of [Factory Configuration](https://www.outsystems.com/forge/component-overview/25/factory-configuration), the **Popup** widget automatically:

* Adds `aria-label="Dialog"` to the popup dialog element, providing an accessible name for screen readers as required by WCAG 4.1.2 (Name, Role, Value).

* Invokes a custom `onEscape` event when the user presses the `Escape` key while focus is inside the Popup, helping you satisfy WCAG 2.1.2 (No Keyboard Trap).

<div class="info" markdown="1">

If you choose to keep the **Enable WCAG 2.2** option disabled, follow [these guidelines](#manual-fix) to manage focus, keyboard navigation, or ARIA attributes as required by WCAG 2.2 AA.

</div>

The widget does not modify the **Popup** visibility variable itself. To close the **Popup** when the user presses `Escape`, wire the `onEscape` event to a client action that sets your **Popup** visibility variable to `False`.

#### Close the popup on Escape {#close}

1. In **Service Studio**, go to the **Interface** tab, and select the **Screen/Block** where you use the **Popup**.

1. In the **Widget Tree**, select the **Popup** widget.

1. In the **Properties** pane, in the **Events** section, add a new entry:

    * **Event**: `onEscape`
    * **Handler**: select or create a client action (for example, `ClosePopup`).

1. In the client action, set the variable bound to **Show Popup** to `False` (for example, `ShowPopupVar = False`).

1. Publish the module.

#### Result

* The popup dialog element exposes `aria-label="Dialog"` so screen readers announce a dialog name.

* Pressing `Escape` while focus is inside the Popup runs the `onEscape` client action, which sets the visibility variable to `False` and closes the Popup. Because the variable changes, the parent can reopen the Popup later by setting it back to `True`.

If **Enable WCAG 2.2** is disabled, the `onEscape` event is not invoked and `aria-label` is not added to the dialog element. Use the [manual workarounds](#manual-fix) in the sections below in that case.

### Manual fix required (for Platform Server versions before 11.43.0) {#manual-fix}

The fixes in this section ensure the focus remains inside the **Popup** while it’s open, supports visible focus on its interactive elements, returns to the trigger when the **Popup** closes, and exposes the correct ARIA relationship between the trigger and the **Popup**.

#### Set visible focus

1. In **Service Studio**, go to the **Interface** tab, and select the **Screen/Block** where you use the Popup.

1. In **Elements**, select the action that opens or closes the Popup.

    ![Screenshot of the Service Studio Elements tree with the Client Action that opens or closes the Popup selected](images/popup-setvisiblefocus-step2-ss.png "Service Studio Client Action Selected")

1. In the action flow, drag an **If** node to validate if the variable that controls the Popup is `True`.  

    ![Screenshot of the Service Studio action flow with an If node added to validate the Popup visibility variable](images/popup-setvisiblefocus-step3-ss.png "Service Studio If Node in Action Flow")

1. In the **True** branch of the **If**, drag a **JavaScript** node to the flow.  

    ![Screenshot of the Service Studio action flow with a JavaScript node added to the True branch of the If](images/popup-setvisiblefocus-step4-ss.png "Service Studio JavaScript Node in True Branch")

1. In the **JavaScript** node, add an input parameter named **WidgetId** (type **Text**), and set it to the **Popup** block or widget ID (for example, `Popup.Id`).  
   Ensure that the **Popup** widget has a **Name** defined in the screen; otherwise, assign one before continuing.

    ![Screenshot of the Service Studio JavaScript node properties with a WidgetId input parameter of type Text](images/popup-setvisiblefocus-step5-ss.png "Service Studio WidgetId Input Parameter")

1. Add the following code to the **Javascript** node:

  ```javascript
  setTimeout(() => {
    const popup = document.getElementById($parameters.WidgetId);
    if (!popup) return;
    
    popup.classList.add("has-accessible-features");
  }, 100);
  ```

1. Publish the module.

#### Add a focus trap

1. In **Service Studio**, go to the **Interface** tab, and select the **Screen/Block** where you use the **Popup**.

1. In **Elements**, select the action that opens the **Popup**.

1. In the **True** branch, drag another **JavaScript** node after the last one.

    ![Screenshot of the Service Studio action flow with a second JavaScript node added to the True branch for the focus trap](images/popup-addfocus-step-3-ss.png "Service Studio Focus Trap JavaScript Node")

1. Add an input parameter named **WidgetId** (type **Text**) and set it to the Popup widget ID (for example, `Popup.Id`).
    Ensure that the **Popup** widget has a **Name** defined in the screen; otherwise, assign one before continuing.

    ![Screenshot of the Service Studio JavaScript node properties with a WidgetId input parameter of type Text for the focus trap](images/popup-addfocus-step-4-ss.png "Service Studio WidgetId Input Parameter")

1. Add the following script:

    ```javascript
    setTimeout(() => {
        const popup = document.getElementById($parameters.WidgetId);
        if (!popup) return;
        
        // Get focusable elements inside the Popup
        function getFocusableElements(popup) {
            return Array.from(popup.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])')).filter(el => {
                // filter disabled and hidden
                return !el.disabled &&
                el.offsetParent !== null && // visibility check
                window.getComputedStyle(el).visibility !== 'hidden';
            });
        }

        function setFocusTrap(event) {
            const items = getFocusableElements(popup);
            if (!items.length) return;
            const idx = items.indexOf(document.activeElement);

            switch (event.key) {
                case 'ArrowDown':
                    event.preventDefault();
                    items[(idx + 1) % items.length].focus({ preventScroll: true });
                    break;
                case 'ArrowUp':
                    event.preventDefault();
                    items[(idx - 1 + items.length) % items.length].focus({ preventScroll: true });
                    break;
                case 'Escape':
                    event.preventDefault();
                    if (typeof $actions !== 'undefined' && typeof $actions.TogglePopup === 'function') {
                        $actions.TogglePopup(); // Make sure this represents the Client Action that closes the Popup
                    }
                    break;
                case 'Tab':
                    event.preventDefault();
                    const next = event.shiftKey
                    ? (idx - 1 + items.length) % items.length
                    : (idx + 1) % items.length;
                    items[next].focus({ preventScroll: true });
                    break;
            }
        }
    
        popup.addEventListener('keydown', setFocusTrap);
        popup._setFocusTrap = setFocusTrap;
    }, 100);
    ```

1. In the **False** branch of the **If** (where the Popup is closed), drag a **JavaScript** node to the flow.

1. In the **JavaScript** node, add an input parameter named **WidgetId** (type **Text**), and set it to the **Popup** widget ID (for example, `Popup.Id`).
   Ensure that the **Popup** widget has a **Name** defined in the screen; otherwise, assign one before continuing.

1. Add the following code to the **JavaScript** node:

    ```javascript
    const popup = document.getElementById($parameters.WidgetId);
    if (!popup || !popup._setFocusTrap) return;

    popup.removeEventListener('keydown', popup._setFocusTrap);
    delete popup._setFocusTrap;
    ```

    ![Screenshot of the Service Studio action flow with a JavaScript node in the False branch to remove the focus trap event listener](images/popup-addfocus-step-8-ss.png "Service Studio DestroyFocusTrap JavaScript Node")

1. Publish the module.

#### Return focus to the trigger

1. In **Service Studio**, go to the **Interface** tab, and select the **Screen/Block** where you use the **Popup**.

1. In **Elements**, select the action that opens the **Popup**.

1. In the **False** branch of the **If**, after the node created to destroy the focus trap, add a **Run Client Action** node.

1. Search for and select **SetFocus()**.

    ![Screenshot of the Service Studio action flow with a Run Client Action node configured to call SetFocus](images/popup-returnfocus-step4-ss.png "Service Studio SetFocus Run Client Action")

1. Set **WidgetId** to the **Popup trigger** ID (for example, `Button.Id`).
    Ensure that the **Button** widget has a **Name** defined in the screen; otherwise, assign one before continuing.

    ![Screenshot of the Service Studio Run Client Action node with WidgetId set to the Popup trigger button ID](images/popup-returnfocus-step5-ss.png "Service Studio SetFocus WidgetId Parameter")

1. Publish the module.

#### Set ARIA on trigger button

1. Go to the **Interface** tab, and select the **Screen/Block** where you use the **Popup**.

1. In the **Widget Tree**, select the button that triggers the **Popup**.

1. In the button Properties, under **Attributes**, :

    ```text
    aria-controls=Popup.id
    aria-expanded=If(ShowPopup, "true", "false")
    ```

    ![Screenshot of the Service Studio button Properties pane with aria-controls and aria-expanded attributes added under Attributes](images/popup-setariaexpanded-ss.png "Service Studio Button ARIA Attributes")

#### Result

* Focus remains inside the **Popup** while it’s open, and keyboard users can move between interactive elements using arrow keys and `Tab`.  
* When the **Popup** closes, focus returns to the original trigger.  
* The trigger exposes the correct ARIA relationship to the Popup via `aria-controls` and `aria-expanded`, helping assistive technologies understand which control opens which content and whether it’s currently visible.

These updates ensure consistent keyboard navigation, predictable focus behavior, and improved support for screen reader users.

Test the pattern in your app to confirm the update.
