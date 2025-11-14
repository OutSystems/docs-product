---
summary: Learn how to enhance accessibility in OutSystems 11 (O11) using ARIA roles and attributes for dynamic content and complex structures.
tags: accessibility, aria, web accessibility, screen readers, dynamic content
locale: en-us
guid: e4cd9450-4fe2-4145-8f1b-0852ab8c081d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=186:27
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - design-for-accessibility
  - accessibility-screen-reader
---

# Accessible Rich Internet Applications roles and attributes

Accessible Rich Internet Applications (ARIA) is a set of accessibility standards that defines elements to use on top of HTML and OutSystems UI to provide additional information to assistive technology tools. ARIA is a valuable tool for addressing accessibility challenges that go beyond what native HTML handles. There are ARIA roles, states, and properties. ARIA roles define the type of element and its purpose, states indicate the current condition or status of an element, and properties provide additional information about an element. ARIA states and properties are also known as ARIA attributes.

Use ARIA when you need to handle dynamic content or complex page structures. For example, you may have several sections on a page, and setting a **role=main** tells the screen readers where the main content is. If you have a block that takes some time to load, inform the screen readers by setting **aria-busy=true**. A button that opens a popup window can warn users by **aria-haspopup=true**.

Adding ARIA attributes and roles requires familiarity with the concepts of ARIA and how ARIA works with HTML. An important thing to keep in mind is that **you shouldn't use ARIA to override the meaning that the HTML tags and the pages produced by the OutSystems UI provide by default**. Inspect the pages before deciding to add an ARIA role or attribute. OutSystems UI adds some ARIA attributes by default, for example in actions that handle menu visibility.

When developing OutSystems apps, add ARIA roles, states, and properties by editing the **Attribute** property of the widgets. There are also some actions that handle specific ARIA properties, such as **SetAriaHidden** or **SetAccessibilityRole**.

## Set ARIA as a static property

The ARIA property doesn't change when the app runs. To add the ARIA roles or attributes, select the widget, go to the **Properties** tab, and add the role or attribute in the **Attributes** section.

![Screenshot showing how to set ARIA as a static property in OutSystems UI](images/set-aria-as-a-static-property-ss.png "Setting ARIA as a Static Property")

Similarly, you can set an ARIA role.

![Screenshot demonstrating setting an ARIA role in OutSystems UI](images/set-aria-role-ss.png "Setting an ARIA Role")

## Set ARIA dynamically

This ARIA property changes when the app runs, depending on a condition. To set an ARIA role or attribute dynamically, use the **If** keyword in the expression of the **Attribute** field. For example, the value of **aria-invalid** in the expression **aria-invalid=If(Form1.Valid, "false", "true")** changes depending on whether the **Form1.Valid** is true or false.

If the form is invalid, because one of the required fields is missing or a value isn't correct for a field, the form appears as marked with **aria-invalid="true"**. This is a signal to the screen readers to alert the users.

![Screenshot illustrating how to set an ARIA property dynamically based on a condition in OutSystems UI](images/set-aria-dynamically-ss.png "Setting ARIA Dynamically")

## Built-in ARIA actions

These are the built-in actions that support setting ARIA attributes. Use them to set the ARIA properties in your logic flows.

### Hide elements with SetAriaHidden

Use the **SetAriaHidden** action to hide an element and all content inside it from the assistive technology tools. It's equivalent to setting **aria-hidden="true"** explicitly for an element.

To find the **SetAriaHidden** action, go to the **Logic** tab > **OutSystemsUI** > **Accessibility.**

### Change the role of the Alert pattern

To change the ARIA role of the Alert pattern, use the **SetAccessibilityRole** action.
To find the **SetAccessibilityRole** action, go to the **Logic** tab > **OutSystemsUI** > **Accessibility**
For more information, refer to [Alert pattern](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Accessibility#Alert_pattern) section in this document.

<div class="info" markdown="1">

The **SetAccessibilityRole** actions work with the Alert pattern. Alternatively, you can test using SetAccessibilityRole for a child element of widgets.

</div>

## Examples of ARIA

This section shows some examples of how you can use ARIA to extend the functionality of the OutSystems UI.

### Status message

Status messages are pieces of text that assistive tools can read and inform the users about the state of each action. Enabling these messages lets screen readers tell the users about the status of the current action.

To enable the status message, do the following steps:

1. Select the UI Pattern.
1. On the **Properties** tab, go to the **Attributes** section.
1. Create a **role** attribute.
1. In the value field of the new **role** attribute, enter the status message.

The following figure shows an example of a status message:

![Screenshot example of setting a status message using ARIA in OutSystems UI](images/status-message-ss.png "Status Message Example")

### Creating readable labels

This section describes how to create readable labels on UI Patterns, such as a button or a link.

To create a label, do the following steps:

1. Select the UI element on the screen.
1. On the **Properties** tab, go to the **Attributes** section.
1. Create a new **aria-label** attribute.
1. In the value field of the new **aria-label** attribute, enter the descriptive label.
1. Select the button label text, for example, **Cancel**.
1. On the **Properties** tab, create a new **aria-label** attribute.
1. Provide the descriptive text you want screen readers to say.

The following figure shows an example of a readable label on a **Delete** button. In this example, when the user selects this button, the screen reader says "Delete product".

![Screenshot showing an example of creating a readable label with ARIA for a 'Delete' button in OutSystems UI](images/creating-readable-labels-ss.png "Creating Readable Labels")

### Hide text in buttons or links

This section describes how to hide text from the screen readers. If you have a link with a readable text description, for example, "View product in store", you can hide a portion of the text. All text set as hidden is invisible on the screen, but screen readers are able to read the full description.

 To hide text in links, do the following:

1. In your application screen, select the Link you want to edit.
1. Select the portion of the link text you want to hide, for example, "product" in “View product in store”.
1. [Add a CSS class](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Look_and_Feel/Cascading_Style_Sheets_(CSS)) that makes that part of the link invisible.

    ![Screenshot depicting how to hide text in buttons or links for screen readers in OutSystems UI](images/hiding-text-in-buttons-or-links-ss.png "Hiding Text in Buttons or Links")

### Adding detailed descriptions for short labels

You can define what you want screen readers to say when you have short labels on buttons or links. For example, a **Cancel** button. The **aria-label** describes the purpose of the button or link. This enables screen readers to say full descriptions.

To add an **aria-label**, do the following:

1. Select the button label text, for example, **Cancel**.
1. On the **Properties** tab, create a new **aria-label**attribute.
1. Enter the descriptive text you want screen readers to say.

    ![Screenshot showing how to add detailed descriptions to short labels using ARIA in OutSystems UI](images/adding-detailed-descriptions-short-labels-ss.png "Adding Detailed Descriptions to Short Labels")
