---
tags: runtime-traditionalweb; 
summary: Section separates content into groups, easing visual organization.
---

# Section

Organizes the screen into different sections with accessibility. Can also be used with a Section Index to easily create anchors for each section.

Use the Section to separate content into groups, easing visual organization.

**How to use**

Drag the Section to the screen and then add the title and content to the placeholders.

1. Drag Section pattern into the preview.

    ![](<images/section-image-1.png>)

1. Set the content you need in the placeholders.

1. Publish and test.


## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  |  Add custom style classes to this Block. | Text | False | none |
  
## Layout and Classes

![](<images/section-image-2.png>)

## Advanced Use Case

### Remove line below Title

Write the following CSS in the CSS editor.

 ```css
    .section-header {
        border-bottom: none;
        padding-bottom: var(--space-none);
    }
```

Before:

![](<images/section-image-3.png>)

After:

![](<images/section-image-4.png>)

## Compatibility with other Patterns

Works with Section-Index Pattern on the same screen to create navigable anchors.


