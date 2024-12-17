---
tags: ui patterns, accordion component, api usage, ui design, outsystems patterns
summary: Explore accordion management features and APIs in OutSystems 11 (O11) for enhancing mobile and reactive web apps.
locale: en-us
guid: e1c30cdd-a7f1-4ce5-aae5-2dddb7a845b9
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=1413%3A1728&mode=design&t=xOFe93sVU3cU3chE-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Accordion Reference

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Events - Accordion

|**Event** |**Description**| 
|---|---|
| AccordionCollapseAll: Optional |<ul><li>Function that collapses all the expanded items of a given accordion.</li><li>WidgetId (text): The accordion's ID to perform the action.</li></ul>|
| AccordionExpandAll |<ul><li>Function to expand all the collapsed items of a given accordion.</li><li>WidgetId (text): The accordion's ID to perform the action.</li></ul>|

## Events - Accordion Item

|**Event** |**Description**| 
|---|---|
| AccordionCollapseAll: Optional |<ul><li>Closes an AccordionItem with a given identifier.</li><li>WidgetId (text): Identifier of the AccordionItem block.</li></ul>|
| AccordionExpandAll |<ul><li>Opens an AccordionItem with a given identifier.</li><li>WidgetId (text): Identifier of the AccordionItem block.</li></ul>|

## Structure

### Accordion base structure

![Diagram illustrating the base structure of an accordion component in a UI pattern](images/accordion-base-structure-diag.png "Accordion Base Structure Diagram")

### Accordion and List widget

![Diagram showing the relationship between accordion and list widget in a UI pattern](images/accordion-list-widget-diag.png "Accordion and List Widget Diagram")

## API - Accordion

If you are an advanced user, you might want to use the Accordion API (OutSystems.OSUI.Patterns.AccordionAPI) for more complex use cases.

### Methods

|**Function** |**Description**|**Parameters**|
|---|---|---|
|ChangeProperty|Changes the property of the Accordion|<ul><li>accordionId: string</li><li>propertyName: string</li><li>propertyValue: any</li></ul>|
|CollapseAllItems|Collapses all the expanded items of a given accordion|<li>accordionId: string</li>|
|Create|Creates the new Accordion instance and adds it to the AccordionMap.|<ul><li>accordionId: string</li><li>configs: string</li><li>provider: string</li></ul>|
|Dispose|Destroys the instance of the given Accordion.|<li>accordionId: string</li>|
|ExpandAllItems|Expands all the collapsed items in a given accordion.|<li>accordionId: string</li>|
|GetAllAccordions|Returns the Map with all the Accordion instances at the page.|<li>Returns array of Ids</li>|
|GetAccordionById|Gets the Carousel instance ID.|<li>accordionId: string</li>|
|Initialize|Initializes the pattern instance.|<li>accordionId: string</li>|

## API - Accordion Item

If you are an advanced user, you might want to use the Accordion Item API (OutSystems.OSUI.Patterns.AccordionItemAPI) for more advanced use cases.

### Methods

|**Function** |**Description**|**Parameters**|
|---|---|---|
|ChangeProperty|Changes the property of the Accordion Item.|<ul><li>accordionItemId: string</li><li>propertyName: string</li><li>propertyValue: any</li></ul>|
|Collapse|Closes the Accordion Item|<li>accordionItemId: string</li>|
|Create|Creates the new Accordion Item  instance and adds it to the AccordionItemMap.|<ul><li>accordionItemId: string</li><li>configs: string</li><li>provider: string</li></ul>|
|Dispose|Destroys the instance of the given AccordionItem.|<li>accordionItemId: string</li>|
|Expand|Opens the AccordionItem|<li>accordionItemId: string</li>|
|GetAllAccordionItems|Returns the Map with all the Accordion Item instances at the page.|<li>Returns array of Ids</li>|
|GetAccordionItemById|Gets the AccordionItem instance ID.|<li>accordionItemId: string</li>|
|RegisterCallback|Registers a callback on this pattern.|<ul><li>accordionItemId: string</li><li>callback: OSUIFramework.Callbacks.Generic</li></ul>|
