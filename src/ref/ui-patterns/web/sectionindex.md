---
tags: css customization, ui patterns, section index, sticky elements, web design
summary: Explore the CSS customization and layout features of the Section Index UI Pattern in Traditional Web Apps with OutSystems 11 (O11).
locale: en-us
guid: fd1fc012-8659-4cd2-861e-220cfa3090ec
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:568
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Section Index Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Section Index UI Pattern in Traditional Web Apps](images/sectionindex-4-diag.png "Section Index Layout Diagram")

## CSS selectors

| **Element** |  **CSS Class** |  **Description**  |
| ---|---|---  
| .section-index |  .section-index.is--sticky|  Defines if the SectionIndex position is fixed or not  |
| .section-index-item |  .section-index-item.is--active|  Defines the current active link  |

## Advanced use case

### Change active color

1. Write the following CSS in the CSS editor and change the `yourcolor`.

        a.section-index-item.is--active {
            border-left-color: yourcolor;
            color: yourcolor;
        }

1. Or using CSS variables: `var(--color-yourcolor)`.

        a.section-index-item.is--active {
            border-left-color: var(--color-yourcolor);
            color: var(--color-yourcolor);
        }

For RTL compatibility, make sure to also add the following code:

    .is-rtl a.section-index-item.is--active {
        border-right-color: yourcolor;
        color: yourcolor;
    }
