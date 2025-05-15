---
summary: OutSystems 11 (O11) integrates WCAG-compliant accessibility features, enabling developers to create universally usable apps.
tags: accessibility, ui design, wcag, ethical development, legal compliance
locale: en-us
guid: 845ea0d1-6110-4a9f-a4ca-19e53b178825
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=186:9
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - none
coverage-type:
  - understand
  - evaluate
  - apply
topic:
  - design-for-accessibility
  - accessibility-screen-reader
---

# Accessibility

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

To ensure the availability of accessible apps that everyone can use is crucial for ethical, practical, and often legal reasons. OutSystems has developed user interface (UI) features with accessibility in mind, allowing you to create apps that comply with the [Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG21) (WCAG). Additionally, you have the flexibility to tailor both the UI and app logic to meet your specific accessibility goals.

A general recommendation is to start thinking about accessibility **early in the development phase**, test often, identify the issues, and fix the issues or provide workarounds. In this document, you can find some techniques for meeting your accessibility needs.

Here are some guidelines to consider for meeting your accessibility needs:

1. Ensure that your app meets the basic accessibility requirements. For more information, refer to [Enabling the built-in accessibility features](#enable-the-built-in-accessibility-features).
1. Early in development, test your app against the accessibility success criteria for the level you are targeting and fix the issues. For more information, refer to [Testing and fixing accessibility issues](testing-fixing-accessibility-issues.md).
1. Pay close attention to complex interactions and dynamic content. Fix the critical issues immediately. Use ARIA to provide more information to the assistive technology tools and improve the structure of your pages. You can do that with ARIA. Refer to [ARIA roles and attributes](aria-roles-and-attributes.md).
1. Refer to [UI Patterns accessibility reference](ui-patterns-accessibility-reference.md) for special notes about patterns you may be using on a page.

<div class="info" markdown="1">

OutSystems UI is often updated to support more accessibility features. For more information, refer to the OutSystems UI release notes in Forge.

</div>

## Enable the built-in accessibility features

OutSystems has many built-in accessibility features, such as creating applications with the right contrast ratio, focus, and skip-to-content settings. To develop accessible apps, you must activate the accessibility feature in Service Studio. In that case, you may need specific customization and development, covered in [ARIA roles and attributes](aria-roles-and-attributes.md) and [UI Patterns accessibility reference](ui-patterns-accessibility-reference.md).

To enable the built-in accessibility features in Service Studio, do the following steps:

1. Go to **UI Flows** and click on **Layouts**
1. Expand the layout you're using.
1. Select the **EnableAccessibilityFeatures** input parameter.
1. On the parameter properties, set the **Default Value** to **True**.

    ![Screenshot showing how to set the Enable Accessibility Features parameter to true in OutSystems Service Studio](images/enabling-accessibility-features-ss.png "Enabling Accessibility Features in Service Studio")

By setting the **EnableAccessibilityFeatures** set to true, you activate the following features for all screens using the layout:

* **Focus states** - allows you to set and highlight the focus on the current element.
* **Skip to content** - allows the user to skip the navigation elements on the screen, and tab directly to the content.
* **Accessible links** - generates links with high color contrast
* **Enhanced contrast** - allows displaying the content on the screen using a contrast ratio perceivable to people with visual impairments.

### Page title

Screen readers use page titles to inform users of the name of the page they're on. To define the page titles for accessibility, do the following steps:

1. On the **Interface** tab, go to **UI Flows**
1. Select the screen to add the title from the list of screens
1. On the **Properties**, enter the screen title (for example, "Main page") in the **Title** field.

<div class="info" markdown="1">

The default page title of the log-in page is blank. Navigate to **UI Flows** > **Common** > **Login** and enter the title.

</div>

### Page language settings for screen readers

The locale of the app defines the language of the page. For more information refer to[Multilingual Reactive Web and Mobile Apps](https://success.outsystems.com/documentation/11/developing_an_application/design_ui/multilingual_reactive_web_and_mobile_apps/).

### Image text alternatives

Image text alternatives, also known as alt text or alternative text, is a string of text that describes what's in the image. Adding image text alternatives allows screen readers to read the description of the images.

To set an alternative text to an image, do the following steps:

1. Select your image, and go to the  **Properties**.
1. In the **Attributes** section, create an **alt**.
1. Enter the description. When an image is for decorative purposes, set **alt=""**.

    ![Screenshot demonstrating how to add alternative text to images in OutSystems](images/image-text-alternatives-ss.png "Adding Text Alternative to Images")

After adding alt-text to an image, for each of the used images, and published the module, you can test the image text alternatives by using a screen reader.

### Text headings

Text headings are a valuable visual aid for users to understand the page structure. Incorporating varying text sizes, especially larger ones, enhances visual guidance on the page and benefits users with cognitive disabilities. Moreover, text-to-speech readers rely on headings to assist users in navigating through a page.

To ensure proper content organization within your app, establish a clear heading structure. Add [a heading element](https://www.w3.org/WAI/tutorials/page-structure/headings/), for example, **h1**, by enclosing the text in the HTML widget and specifying **h1** as the tag.

To set the text headings, do the following steps:

1. On the toolbox, search for the **HTML Element** widget (1)
1. Drag it to the screen (2).
1. To add an **h1** element to the screen, go to the **HTML Element** widget properties, and in the **Tag** field (3), enter **h1**.
1. Enter some text into the HTML Element.
1. Check the widget structure to verify that the text is within the **h1** element (4).

    ![Screenshot illustrating how to set text headings using the HTML Element widget in OutSystems](images/text-headings-ss.png "Setting Text Headings")

On setting the headings, you can test them using a screen reader.

### Text color contrast

By default, OutSystems UI provides the correct text contrast ratio to comply with the color contrast accessibility requirements. The built-in accessibility features, once turned on, improve the contrast. If you edit the colors in your app, make sure the contrast is still valid, by referring to the [minimum contrast criteria](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum).

### Text spacing

Improve the text readability by letting the users increase the text spacing in your application. To increase the text spacing, create an action that runs the accessibility **ToggleTextSpacing** actions.

1. In your app screen, select the page element that triggers the increased text spacing. For example, a button.
1. To create a new client action, in the **Events** section of the **Properties**, go to the **OnClick** event and select **(new client action)**.
![Screenshot of the process to create a new client action for text spacing in OutSystems](images/new-client-action-ss.png "Creating a New Client Action")
1. Set the action name as **TextSpacing**, for example.

    ![Screenshot showing the configuration of the Text Spacing client action in OutSystems](images/text-spacing-client-action-ss.png "Setting the Text Spacing Client Action")

1. On the **Logic** tab, click on **OutSystemsUI**
1. Click on the **Accessibility** Client Actions folder.
1. Drag the **ToggleTextSpacing** action into the flow.

    ![Screenshot depicting how to set the accessibility ToggleTextSpacing action in OutSystems](images/set-accessibility-role-ss.png "Setting the Accessibility Role")

### Form labels

Labels provide captions to the input fields, describing the information requested from the user. You have to bound the Label widget to inputs in forms to allow screen readers to read each input field caption.

To bind labels with the Forms fields they refer to, do the following steps:

1. Select the **Label** widget in the preview (1)
1. On the **Properties**, go to the **Input Widget** drop-down, and select the widget to associate the label (2).
1. To see a demo of a form, create a screen based on a **Detail** Screen Template.

![Screenshot showing how to bind Label widgets to input fields in OutSystems forms](images/form-labels-ss.png "Binding Form Labels to Input Fields")

On setting these steps for each input field and publishing the module, you can test reading the inputs captions using a screen reader.

<div class="info" markdown="1">

Use the `aria-labelledby` attribute for more control when setting up relationships between objects and their text labels. For more information, refer to [Examples of ARIA](aria-roles-and-attributes.md#examples-of-aria). 

</div>

### Form validation on screen readers

To learn how to validate the input fields of a form, refer to [Validate the fields of a form](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Forms/Validate_the_fields_of_a_form#Examples_of_the_client-side_validation_with_accelerators).

To learn how to signal to screen readers and users that the form isn't valid, check the example in [Set ARIA dynamically](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Accessibility/Accessible_Rich_Internet_Applications_roles_and_attributes#Set_ARIA_dynamically).

### Highlighting selected elements

Turning on the built-in accessibility features allows you to get a visual highlight on the selectable items on the page. When the user navigates between different selectable items with the tab key, the selected element highlights.

#### Selecting an element with the SetFocus action

You can explicitly select an element by using the **SetFocus** action. For example, to highlight an input field when a user enters a page that contains a form.

![Screenshot displaying how to highlight an element using the SetFocus action in OutSystems](images/element-in-focus-ss.png "Highlighting an Element in Focus")

To explicitly select an element on a screen, do the following steps:

1. On the **Interface** tab, select the screen that contains the widget you want to highlight and open it.
1. On the screen **Properties**, go to **Events**, and select the **OnReady** action from the drop-down menu. The **OnReady** action logic opens.
1. On the **Logic** tab, click on **OutSystemsUI** and open the **Accessibility** Client Actions folder.
1. Select the **SetFocus** action and drag it into the logic, as shown in the figure below.
1. On the **Properties**, go to **WidgetId** and select the Id of the widget you want to highlight.

![Screenshot of setting focus on a specific element using the SetFocus action in OutSystems](images/element-in-focus-setfocus-ss.png "Setting Focus on an Element")

After following these steps and published the module, you can test the highlighting of the element.

### Skipping to specific content on a page

By default, text readers skip repetitive elements, such as headers and menus, and jump to the main content of a page for reading it. You might want text readers to skip to a specific section of the page, other than the main content. To do this, do the following steps:

To change the default main container, do the following steps:

1. On the **Interface** tab, go to **UI Flows** and expand the **Layouts**.
1. Select and expand the layout you're using.
1. Double-click the **SkipToContentOnClick** action.
1. Select the **SkipToContent** node in the flow and edit the **TargetId** in the action properties.

![Screenshot illustrating how to set the Skip to Content target ID in OutSystems](images/skip-to-content-target-id-ss.png "Setting Skip to Content Target ID")

<div class="info" markdown="1">

You must enter the name in the widget properties before you can use that widget in the **SkipToContent** action. For example, if you name your element **MainContent**, the identifier is **MainContent.Id**.

</div>

The default content Container is the **MainContentWrapper**. To find it, go to **UI Flows** > **Layouts**, and click on the layout you use in your app.

To find the  **SkipToContent** action, go to **Logic** > **OutSystemsUI** > **Accessibility**.

## Modal dialogs

<div class="info" markdown="1">

Applies to Platform Server 11.11 and later.

</div>

Use the [Popup widget](../../ui/inputs/popup.md) to create accessible modal dialogs. Popup adds the following attributes to the widget:

* `role="dialog"`
* `aria-modal="true"`

Additionally, you must add the class `"has-accessible-features"` manually in the Style Classes of the Popup Widget to enable the accessibility features.
