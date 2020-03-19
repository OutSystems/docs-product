---
summary: The basics of CSS in OutSystems.
tags: support-application_development; support-Front_end_Development; css;
---

# Cascading Style Sheets (CSS)

Cascading Style Sheets (CSS) is a language for describing how HTML content should look in a browser. OutSystems apps use the OutSystems UI framework that comes with the base Theme and CSS. You can add new styles and modify the existing ones by copying them from the base Theme.

These app UI elements have CSS which you can edit:

* [Themes](<themes.md>)
* Screens and Emails
* Blocks
* Widgets (complex widgets have more than one style)

## Applying CSS with the class attribute

You can specify static CSS classes of an element in the properties pane by using the **Style Classes**:

* In Mobile and Reactive Web apps, insert the class names with quotes and separated by a space (`"bold red"`)
* In Traditional Web apps, insert the class names without quotes and separated by a space (`bold red`)

![CSS specifies in the Style Classes property](images/css-style-properties.png?width=630)

To specify the CSS classes dynamically use an **Expression**:

* In the **Style Classes** field (Mobile and Reactive Web apps)
* In the `class` attribute of the **Extended Properties** (Traditional Web app)

## Editing CSS

Edit the CSS code in Style Sheet Editor. You can open it by double-clicking **Style Classes** property in the properties pane when you edit an element with attached CSS styles.

You can also open Style Sheet Editor by clicking the **CSS** button in the Main Editor toolbar. Select the tab with the app name and define or edit the style to make it available to all elements. Alternatively, select the tab with the name of the currently selected screen or block to narrow the scope of the style to that screen or block.

![CSS of the Theme](images/css-style-sheet-editor.png?width=600)

## CSS specificity

The styles have different priority and the order Service Studio imports the style sheets affects how the browsers apply them. The last style to be applied has the highest priority.

1. System style sheet for Container widgets in the Grid.
2. Block style sheet.
3. Theme style sheet, which also includes a base theme (if specified).
4. Screen or Email style sheet.
5. Theme extra style sheet, with the Grid settings defined in the Theme properties.
6. Styles that Service Studio generates when you use Styles Editor.
7. Inline style you define in **Attributes** or **Extended Properties**.

## Inline CSS

Define your inline CSS in the **Attributes** part of the properties pane. Add the `style` attribute and then enter the CSS rules with quotes (for example, `"background-color: yellow;"`).

![The style property with quotes around CSS](images/css-extended-properties.png?width=600)

In Traditional Web you can create inline CSS by adding `style` in the **Extended Properties**.

![Inline CSS in Traditional Web app](images/css-properties.png?width=550)

## OutSystems Grid

OutSystems uses a high-level grid system. If you specify the number of columns in the Theme grid settings, the width of elements can be expressed in columns. In **Margin Left** you can use the `(Auto)` property to have the values calculated automatically.

## Importing CSS

Use the `@import` CSS at-rule in Style Sheet Editor to import style rules from other locations. Put it as the first line in your sheet.

## Preprocessors

OutSystems development tools do not support the use of CSS preprocessors (such as Sass or LESS) in apps.
