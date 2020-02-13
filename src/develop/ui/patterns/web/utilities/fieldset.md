---
tags: runtime-traditionalweb; 
summary: Fieldset labels groups of related interface elements and fields.
---

# Fieldset

Group thematically related elements such as controls and labels.

Use the Fieldset to label groups of related interface elements and fields. This improves the layout and helps users understand the information.  

**How to use**

Set the label of the Fieldset and then drag Input widgets to the content placeholder.

1. Drag the Fieldset pattern into the preview.

1. Set the Title parameter.

1. Set the content you need on the placeholder.

1. Publish and test.

    ![](<images/fieldset-image-1.png>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Title  |  The title that will be the legend of the Fieldset. | Text | True | none |
| ExtendedClass  |  Add custom style classes to this Block. |  Text | False | none |

## Layout and Classes

![](<images/fieldset-image-2.png>)

## Advanced Use Case

### Change the style of Fieldset

Use custom CSS to change the style of Fieldset. The following examples are only two ways of doing it. To use these in your application, copy the CSS code from below and add it to your theme.

Example 1

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
![](<images/fieldset-image-3.png>)

Example 2

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
![](<images/fieldset-image-4.png>)
