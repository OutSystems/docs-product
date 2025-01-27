---
tags: css customization, ui design, ui patterns, web development, style customization
summary: Explore advanced customization of Traditional Web Apps in OutSystems 11 (O11) by modifying CSS for UI patterns.
locale: en-us
guid: c7493358-7bab-4ebf-ada6-2f101c53db4e
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:564
audience:
  - frontend developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Section Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Section UI Pattern](images/section-2-diag.png "Section Layout Diagram")

## Advanced use case

### Remove line below title

Write the following CSS in the CSS editor.

 ```css
.section-header {
    border-bottom: none;
    padding-bottom: var(--space-none);
}
```

**Before**

![Screenshot showing the Section UI Pattern before removing the line below the title](images/section-3.png "Section Before CSS Changes")

**After**

![Screenshot showing the Section UI Pattern after applying CSS to remove the line below the title](images/section-4.png "Section After CSS Changes")

## Compatibility with other patterns

Works with Section-Index Pattern on the same screen to create navigable anchors.
