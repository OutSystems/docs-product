---
tags: runtime-traditionalweb;
summary: Explore CSS customization options for Dropdown Select UI Pattern in OutSystems 11 (O11) for Traditional Web Apps.
locale: en-us
guid: 4d9ccb38-173c-42fa-9f2f-6ea73e338b52
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:456
---

# Dropdown Select Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Dropdown Select UI Pattern for Traditional Web Apps](images/dropdownselect-3-diag.png "Dropdown Select Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| Dropdown |  .choices__list--dropdown.is-active |  Defines if the drop-down is closed or opened  |

## Advanced use case

### Change the border color

Write the following CSS in the CSS editor and change the `yourcolor` variable:

```css
.choices__inner {
    border: var(--border-size-s) solid yourcolor;
}
```

Or using the CSS variable `var(--color-yourcolor)` example:

```css
.choices__inner {
    border: var(--border-size-s) solid var(--color-yourcolor);
}
```

### Change removable tags color

Write the following CSS in the CSS editor and change the `yourcolor` variable:

```css
.choices__list--multiple .choices__item.choices__item--selectable {
    background: yourcolor;
}
```

Or using the CSS variable `var(--color-yourcolor)` example:

```css
.choices__list--multiple .choices__item.choices__item--selectable {
    background: var(--color-yourcolor);
}
```

## Browser previews

With Combo Box:

![Animated preview showing the Dropdown Select UI Pattern with Combo Box in a browser](images/dropdownselect-4-ss.gif "Dropdown Select Combo Box Preview")

With List Box:

![Animated preview showing the Dropdown Select UI Pattern with List Box in a browser](images/dropdownselect-2-ss.gif "Dropdown Select List Box Preview")

## Notes

The SearchEnabled parameter doesn't work with ListBox.
