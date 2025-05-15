---
tags: css customization, ui design, web development, outsystems ui, outsystems traditional web apps
summary: Learn how to customize the Fieldset UI Pattern in Traditional Web Apps using custom CSS in OutSystems 11 (O11).
locale: en-us
guid: 6a58d000-dd26-489f-ae56-94a4ad3dd6a2
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:460
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Fieldset Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of a Fieldset UI Pattern in Traditional Web Apps](images/fieldset-2-diag.png "Fieldset Layout Diagram")

## Advanced use case

### Change the style of Fieldset Pattern

you can use custom CSS to change the style of the Fieldset Pattern. The following examples are only two ways of doing it. To use these in your application, copy the CSS code from below and add it to your theme.

**Example 1**

```css
.fieldset {
    position: relative;
}

.fieldset-legend {
    background: var(--color-background-body);
    padding: 0 var(--space-xs);
    position: absolute;
    right: var(--space-m);
    top: -15px;
}
```

![Screenshot showing an example of custom CSS applied to change the style of the Fieldset Pattern in a Traditional Web App](images/fieldset-3-ss.png "Fieldset Style Example 1")

**Example 2**

```css
.fieldset {
    border: 0;
    padding: var(--space-m) 0;
}

.fieldset-legend {
    border-bottom: 1px solid var(--color-neutral-5);
    padding-bottom: var(--space-s);
    width: 100%;
}
```

![Screenshot demonstrating another example of custom CSS modifications to the Fieldset Pattern in a Traditional Web App](images/fieldset-4-ss.png "Fieldset Style Example 2")
