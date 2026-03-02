---
tags: ide usage, reactive web apps, tutorials for beginners, ui design, customization
summary: Explore how to use the Tag UI Pattern in OutSystems 11 (O11) to enhance user interfaces by styling texts with customizable colors, shapes, and sizes.
locale: en-us
guid: ad4f4ddf-d346-4347-b78d-8741dea7cb94
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=205:66
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - apply
---

# Tag

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can use the Tag UI Pattern to style small texts in a colored tag format. Use the Tags UI Pattern to display statuses, labels, or categories thus providing great user experience.

## How to use the Tag UI Pattern

1. In Service Studio, in the Toolbox, search for `Tag`.
  
    The Tag widget is displayed.

    ![Screenshot of Service Studio showing the Tag widget in the Toolbox](images/tag-1-ss.png "Service Studio Tag Widget")

    If the UI widget doesn't display, it's because the dependency isn't added. This happens because the Remove unused references setting is enabled. To make the widget available in your app:

    1. In the Toolbox, click **Search in other modules**.

    1. In **Search in other Modules**, remove any spaces between words in your search text.

    1. Select the widget you want to add from the **OutSystemsUI** module, and click **Add Dependency**.

    1. In the Toolbox, search for the widget again.

1. To From the Toolbox, drag the Tag widget into the Main Content area of your application's screen.

    ![Dragging the Tag widget from the Toolbox into the Main Content area in Service Studio](images/tag-2-ss.png "Drag Tag Widget to Main Content")

1. Add your content to the placeholders. In this example, we add some text.

    ![Adding text content to the Tag widget's placeholders in Service Studio](images/tag-3-ss.png "Add Content to Tag Placeholder")

1. On the properties tab, you can change the Tag's look and feel by setting the (optional) properties, for example, size and color.

    ![Service Studio properties tab showing options to change the Tag's size and color](images/tag-4-ss.png "Tag Properties Configuration")

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

| Property | Description |
| ---- | ---- |
| Color (Color Identifier): Optional | Set the Tag's background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available. Examples: _Blank_ - Displays the badge in the color you chose when creating the app (default value). _Entities.Color.Red_ - The Tag's background is red. |
| Shape (Shape Identifier): Optional | Set the Tag's shape. Rounded, soft rounded, and sharp are the predefined shapes available. Examples: _Blank_ - Displays a rounded shaped Tag (default value). _Entities.Shape.Sharp_ - Displays a square shaped Tag. |
| Size (Size Identifier): Optional | Set the Tag's size. Small and medium are the predefined sizes available. Examples: _Entities.Size.Medium_ - Displays a medium-sized Tag. _Entities.Size.Small_ - Displays a small sized Tag. |
| IsLight (Boolean): Optional | Specify the Tag's background color. Examples: _Blank_ - A darker hue of the color is applied to the Tag and a lighter color to the text (default value). _True_ - A brighter hue of the color is applied to the Tag and a darker color to the text. _False_ - A darker hue of the color is applied to the Tag and a lighter color to the text. |
| ExtendedClass (Text): Optional | Adds custom style classes to the Pattern. You define your [custom style classes](../../../look-feel/css.md) in your application using CSS. Examples: Blank - No custom styles are added (default value). "myclass" - Adds the ``myclass`` style to the UI styles being applied. "myclass1 myclass2" - Adds the ``myclass1`` and ``myclass2`` styles to the UI styles being applied. You can also use the classes available on the OutSystems UI. For more information, see the [OutSystems UI Cheat Sheet](https://outsystemsui.outsystems.com/OutSystemsUIWebsite/CheatSheet). |

## Accessibility – WCAG 2.2 AA compliance

By default, the **Tag** UI Pattern uses color combinations that might not meet the minimum contrast ratio required for WCAG 2.2 AA compliance. This happens because the **OutSystems UI** color palette was designed to provide broad coverage across many projects, similar to other design systems.

With so many available colors, it’s easy to create combinations that don’t provide enough contrast. Some of these combinations are also part of the default Tag configuration, which wasn’t specifically optimized for accessibility. However, these combinations only pose an issue when they’re used or become available through dynamic settings.

In most cases, customizing the palette to match your brand styles or adjusting individual color tokens might resolve the contrast problems—or, if done without testing, make them worse.

### OutSystems UI colors with low contrast combinations

<div class="info" markdown="1">

Some colors in the **OutSystems UI** palette don’t meet the minimum recommended contrast ratio **(4.5:1 for normal text or 3:1 for large text)** when used together as text and background colors. The following colors, for example, may create low-contrast combinations when applied to text, icons, or interactive elements such as buttons and links:

* orange

* yellow

* lime

* green

* neutral-5

* neutral-6

* light-yellow

* light-lime

* light-transparent

* light-neutral-6

</div>

You can still use these colors for decorative or non-textual purposes, as long as they don’t affect readability or information perception.

If your application relies on these color tokens, update the related CSS variables to improve contrast across all components. When applying custom or brand colors, always validate the contrast between text and background to ensure WCAG 2.2 AA compliance.

Use a contrast checking tool such as:

* [Color Contrast Checker by Pivotal Accessibility](https://chromewebstore.google.com/detail/color-contrast-checker/gbfgefkhkofclanlcgnhlbmfgjjomock)

* [Accessible Color Picker](https://chromewebstore.google.com/detail/accessible-color-picker/bgfhbflmeekopanooidljpnmnljdihld)

* [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)

* [Contrast Ratio by Lea Verou](https://contrast-ratio.com/)

  ![Example of how to use Color Contrast Checker to validate compliant colors](images/tag-greencontrast-ss.png "Validating contrast color with Color Contrast Checker")

### Update CSS variables to improve contrast

Update the theme color tokens so text and background combinations meet WCAG 2.2 AA. Replace each placeholder value with your brand colors (hex or rgba) and publish.

1. In **Service Studio**, go to the **Elements** tab.

1. Select your **Theme** in **Themes**.

1. In the theme’s CSS, add or update the needed variables.

1. Replace the placeholder values with new accessible colors and **Publish** the module.

<div class="info" markdown="1">

**Disclaimer:**  
The following code block lists all root color variables for quick reference. You don’t need to include all of them in your theme — only the ones you intend to update.  

For readability, the examples use a black hex value (`#000000`), but you can replace it with any valid CSS color format, such as `rgb()`, `rgba()`, `hsl()`, or `oklch()`.

</div>

```css
:root {
    /* ── Color > Brand ───────────────────────────────────── */
    --color-primary:          [#000000 /* replace */];
    --color-secondary:        [#000000 /* replace */];
    --color-primary-hover:    [#000000 /* replace */];
    --color-primary-selected: [#000000 /* replace */];
    --color-primary-lightest: [#000000 /* replace */];

    /* ── Color > Focus ───────────────────────────────────── */
    --color-focus-outer:      [#000000 /* replace */];
    --color-focus-inner:      [#000000 /* replace */];

    /* ── Color > Extended (Reds) ─────────────────────────── */
    --color-red-lightest:     [#000000 /* replace */];
    --color-red-lighter:      [#000000 /* replace */];
    --color-red-light:        [#000000 /* replace */];
    --color-red:              [#000000 /* replace */];
    --color-red-dark:         [#000000 /* replace */];
    --color-red-darker:       [#000000 /* replace */];
    --color-red-darkest:      [#000000 /* replace */];

    /* ── Color > Extended (Oranges) ──────────────────────── */
    --color-orange-lightest:  [#000000 /* replace */];
    --color-orange-lighter:   [#000000 /* replace */];
    --color-orange-light:     [#000000 /* replace */];
    --color-orange:           [#000000 /* replace */];
    --color-orange-dark:      [#000000 /* replace */];
    --color-orange-darker:    [#000000 /* replace */];
    --color-orange-darkest:   [#000000 /* replace */];

    /* ── Color > Extended (Yellows) ──────────────────────── */
    --color-yellow-lightest:  [#000000 /* replace */];
    --color-yellow-lighter:   [#000000 /* replace */];
    --color-yellow-light:     [#000000 /* replace */];
    --color-yellow:           [#000000 /* replace */];
    --color-yellow-dark:      [#000000 /* replace */];
    --color-yellow-darker:    [#000000 /* replace */];
    --color-yellow-darkest:   [#000000 /* replace */];

    /* ── Color > Extended (Limes) ────────────────────────── */
    --color-lime-lightest:    [#000000 /* replace */];
    --color-lime-lighter:     [#000000 /* replace */];
    --color-lime-light:       [#000000 /* replace */];
    --color-lime:             [#000000 /* replace */];
    --color-lime-dark:        [#000000 /* replace */];
    --color-lime-darker:      [#000000 /* replace */];
    --color-lime-darkest:     [#000000 /* replace */];

    /* ── Color > Extended (Greens) ───────────────────────── */
    --color-green-lightest:   [#000000 /* replace */];
    --color-green-lighter:    [#000000 /* replace */];
    --color-green-light:      [#000000 /* replace */];
    --color-green:            [#000000 /* replace */];
    --color-green-dark:       [#000000 /* replace */];
    --color-green-darker:     [#000000 /* replace */];
    --color-green-darkest:    [#000000 /* replace */];

    /* ── Color > Extended (Teals) ────────────────────────── */
    --color-teal-lightest:    [#000000 /* replace */];
    --color-teal-lighter:     [#000000 /* replace */];
    --color-teal-light:       [#000000 /* replace */];
    --color-teal:             [#000000 /* replace */];
    --color-teal-dark:        [#000000 /* replace */];
    --color-teal-darker:      [#000000 /* replace */];
    --color-teal-darkest:     [#000000 /* replace */];

    /* ── Color > Extended (Cyans) ────────────────────────── */
    --color-cyan-lightest:    [#000000 /* replace */];
    --color-cyan-lighter:     [#000000 /* replace */];
    --color-cyan-light:       [#000000 /* replace */];
    --color-cyan:             [#000000 /* replace */];
    --color-cyan-dark:        [#000000 /* replace */];
    --color-cyan-darker:      [#000000 /* replace */];
    --color-cyan-darkest:     [#000000 /* replace */];

    /* ── Color > Extended (Blues) ────────────────────────── */
    --color-blue-lightest:    [#000000 /* replace */];
    --color-blue-lighter:     [#000000 /* replace */];
    --color-blue-light:       [#000000 /* replace */];
    --color-blue:             [#000000 /* replace */];
    --color-blue-dark:        [#000000 /* replace */];
    --color-blue-darker:      [#000000 /* replace */];
    --color-blue-darkest:     [#000000 /* replace */];

    /* ── Color > Extended (Indigos) ──────────────────────── */
    --color-indigo-lightest:  [#000000 /* replace */];
    --color-indigo-lighter:   [#000000 /* replace */];
    --color-indigo-light:     [#000000 /* replace */];
    --color-indigo:           [#000000 /* replace */];
    --color-indigo-dark:      [#000000 /* replace */];
    --color-indigo-darker:    [#000000 /* replace */];
    --color-indigo-darkest:   [#000000 /* replace */];

    /* ── Color > Extended (Violets) ──────────────────────── */
    --color-violet-lightest:  [#000000 /* replace */];
    --color-violet-lighter:   [#000000 /* replace */];
    --color-violet-light:     [#000000 /* replace */];
    --color-violet:           [#000000 /* replace */];
    --color-violet-dark:      [#000000 /* replace */];
    --color-violet-darker:    [#000000 /* replace */];
    --color-violet-darkest:   [#000000 /* replace */];

    /* ── Color > Extended (Grapes) ───────────────────────── */
    --color-grape-lightest:   [#000000 /* replace */];
    --color-grape-lighter:    [#000000 /* replace */];
    --color-grape-light:      [#000000 /* replace */];
    --color-grape:            [#000000 /* replace */];
    --color-grape-dark:       [#000000 /* replace */];
    --color-grape-darker:     [#000000 /* replace */];
    --color-grape-darkest:    [#000000 /* replace */];

    /* ── Color > Extended (Pinks) ────────────────────────── */
    --color-pink-lightest:    [#000000 /* replace */];
    --color-pink-lighter:     [#000000 /* replace */];
    --color-pink-light:       [#000000 /* replace */];
    --color-pink:             [#000000 /* replace */];
    --color-pink-dark:        [#000000 /* replace */];
    --color-pink-darker:      [#000000 /* replace */];
    --color-pink-darkest:     [#000000 /* replace */];

    /* ── Color > Neutral ─────────────────────────────────── */
    --color-neutral-0:        [#000000 /* replace */];
    --color-neutral-1:        [#000000 /* replace */];
    --color-neutral-2:        [#000000 /* replace */];
    --color-neutral-3:        [#000000 /* replace */];
    --color-neutral-4:        [#000000 /* replace */];
    --color-neutral-5:        [#000000 /* replace */];
    --color-neutral-6:        [#000000 /* replace */];
    --color-neutral-7:        [#000000 /* replace */];
    --color-neutral-8:        [#000000 /* replace */];
    --color-neutral-9:        [#000000 /* replace */];
    --color-neutral-10:       [#000000 /* replace */];

    /* ── Color > Semantic ────────────────────────────────── */
    --color-error-light:      [#000000 /* replace */];
    --color-error:            [#000000 /* replace */];
    --color-warning-light:    [#000000 /* replace */];
    --color-warning:          [#000000 /* replace */];
    --color-success-light:    [#000000 /* replace */];
    --color-success:          [#000000 /* replace */];
    --color-info-light:       [#000000 /* replace */];
    --color-info:             [#000000 /* replace */];
}
```

### Result

After you update the theme color variables with accessible values, validate that each combination of background and text colors used in the **Tag** meets the WCAG 2.2 AA contrast requirements.

When validating in a Style Guide or Design System context, make sure to check both the default state and the **IsLight** variant, which inverts background and text colors.
