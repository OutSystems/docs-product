---
tags: ui patterns, outsystems api, css modifiers, ui design, application development
summary: Explore the structure and API of the Gallery UI pattern in OutSystems 11 (O11) for enhancing mobile and reactive web apps.
locale: en-us
guid: b48f442d-6ab3-47c9-96ad-2bae75f24bc8
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=612:353
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

# Gallery Reference

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Structure

![Class diagram image showing the structure of the Gallery UI pattern](images/gallery-class-diag.png "Gallery Class Diagram")

### Modifiers

| **Modifier** | **Attribute** | **Element** | 
|---|---|---|  
|RowItemsDesktop|--gallery-desktop-items <br/>--gallery-list-desktop-items|.osui-gallery|  
|RowItemsTablet|--gallery-tablet-items <br/>--gallery-list-tablet-items|.osui-gallery|  
|RowItemsPhone|--gallery-phone-items<br/>--gallery-list-phone-items|.osui-gallery|  
|ItemsGap|--gallery-gap|.osui-gallery|  


## API

If you are an advanced user, you might want to use our Gallery API (OutSystems.OSUI.Patterns.GalleryAPI) for more advanced use cases.

### Methods

| **Function** | **Description** | **Parameters** | 
|---|---|---|
|ChangeProperty|Changes the Gallery property.|<ul><li>galleryId: string </li><li>propertyName: string</li> <li>propertyValue: any</li></ul>|
|Create|Creates a new Gallery instance and adds it to the GalleryMap.|<ul><li>galleryId: string</li> <li>configs: string</li></ul>|
|Destroy|Destroys the Gallery instance.|<ul><li>galleryId: string</li></ul>|
|GetAllGalleries|Returns the Map with all the Gallery instances on the screen.|<ul><li>Returns array of IDs</li></ul>|
|GetGalleryById|Gets the Gallery instance ID.|<ul><li>galleryId: string</li></ul>|
|Initialize|Initializes the pattern instance.|<ul><li>galleryId: string</li></ul>|



