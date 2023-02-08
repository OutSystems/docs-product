---
tags: runtime-traditionalweb; 
summary: Advanced use cases for the Section UI Pattern.
locale: en-us
guid: c7493358-7bab-4ebf-ada6-2f101c53db4e
app_type: traditional web apps
platform-version: o11
---

# Section Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/section-2-diag.png>)

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

![](<images/section-3.png>)

**After**

![](<images/section-4.png>)

## Compatibility with other patterns

Works with Section-Index Pattern on the same screen to create navigable anchors.
