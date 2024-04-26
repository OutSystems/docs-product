---
summary: The basics of CSS in OutSystems.
tags: support-application_development; support-Front_end_Development
locale: en-us
guid: d9c9539a-bb5f-4775-9abc-86c9ba2c36ad
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=199%3A108&mode=design&t=VUTD7oZE9xvPWlG0-1
---

# Cascading Style Sheets - CSS

Cascading Style Sheets (CSS) is a language for describing how HTML content should look in a browser. OutSystems apps use the OutSystems UI framework that comes with the base Theme and CSS. You can add new styles and modify the existing ones by copying them from the base Theme.

These app UI elements have CSS which you can edit:

* [Themes](themes.md)
* Screens and Emails
* Blocks
* Widgets (complex widgets have more than one style)

## Applying CSS with the class attribute

You can specify static CSS classes of an element in the properties pane by using the **Style Classes**:

* In Mobile and Reactive Web apps, insert the class names with quotes and separated by a space (`"bold red"`)
* In Traditional Web apps, insert the class names without quotes and separated by a space (`bold red`)

![Screenshot of the CSS Style Properties pane in OutSystems Service Studio](images/css-style-properties.png "CSS Style Properties Pane")

To specify the CSS classes dynamically use an **Expression**:

* In the **Style Classes** field (Mobile and Reactive Web apps)
* In the `class` attribute of the **Extended Properties** (Traditional Web app)

## Editing CSS

You can edit the CSS code in the Style Sheet Editor. Open the editor by double-clicking the **Style Classes** property on the **Properties** tab.

You can also open the Style Sheet Editor by clicking the **CSS** button in the Main Editor toolbar. Select the tab with the app name and define or edit the style to make it available to all elements. Alternatively, select the tab with the name of the currently selected screen or block to narrow the scope of the style to that screen or block.

![Image showing the CSS Style Sheet Editor interface in OutSystems](images/css-style-sheet-editor.png "CSS Style Sheet Editor")

## CSS specificity

The styles have different priorities and the order Service Studio imports the style sheets affects how the browsers apply them. The last style to be applied has the highest priority.

1. System style sheet for Container widgets in the Grid.
1. Block style sheet.
1. Theme style sheet, which also includes a base theme (if specified).
1. Screen or Email style sheet.
1. Theme extra style sheet, with the Grid settings defined in the Theme properties.
1. Styles that Service Studio generates when you use Styles Editor.
1. Inline style you define in **Attributes** or **Extended Properties**.

## Inline CSS

Define your inline CSS in the **Attributes** section of the **Properties** tab. Add the `style` attribute and then enter the CSS rules with quotes (for example, `"background-color: yellow;"`).

![Example of defining inline CSS in the Attributes section of the Properties tab in OutSystems](images/css-extended-properties.png "CSS Extended Properties")

In Traditional Web you can create inline CSS by adding `style` in the **Extended Properties**.

![Illustration of CSS properties usage in Traditional Web app within OutSystems](images/css-properties.png "CSS Properties")

## OutSystems grid

OutSystems uses a high-level grid system. If you specify the number of columns in the Theme grid settings, the width of elements can be expressed in columns. In **Margin Left** you can use the `(Auto)` property to have the values calculated automatically.

## Importing CSS

Use the `@import` CSS at-rule in Style Sheet Editor to import style rules from other locations. Put it as the first line in your sheet.

## Preprocessors

OutSystems development tools don't support the use of CSS preprocessors (such as Sass or LESS) in apps.

## CSS Best Practices:

1. **Avoid Inline Styles**: Inline styles can quickly become hard to manage and maintain, especially in large and complex projects. When styling is scattered throughout the HTML elements, it becomes challenging to track and modify styles, leading to code duplication and potential errors.
1. **Avoid using ID selector**: The Id of each element is managed by the platform depending on its scope and could be changed anytime. To avoid unexpected behaviors, use CSS classes instead.
1. **Centralize CSS in theme**: Adding styles in blocks and screen stylesheets can lead to maintainability and scalability issues. It leads to style duplication and also may have some impact on performance because it increases the file requests to the server.
1. **Use CSS variables**: CSS variables allow you to define reusable values that can be used across your entire stylesheet. This makes it easy to maintain consistent styles throughout your application.
