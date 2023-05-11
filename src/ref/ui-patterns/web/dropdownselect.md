---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Dropdown Select UI Pattern.
locale: en-us
guid: 4d9ccb38-173c-42fa-9f2f-6ea73e338b52
app_type: traditional web apps
platform-version: o11
---

# Dropdown Select Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/dropdownselect-3-diag.png>)

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

![](<images/dropdownselect-4-ss.gif?width=600>)

With List Box:

![](<images/dropdownselect-2-ss.gif?width=600>)

## Notes

The SearchEnabled parameter doesn't work with ListBox.
