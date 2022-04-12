---
tags: runtime-mobileandreactiveweb; 
summary: Advanced use cases for the Rating UI Pattern
locale: en-us
guid: cde868f5-0402-49de-8c91-0754724634cc
---

# Rating

## Events

|**Event** |**Output**|**Description**|
|---|---|---|
|OnSelect: Optional |Value (Decimal)|  Event that returns the current rating value. |
  
## Structure

![Structure diagram](images/rating-diag.png)

<div class="info" markdown="1">

These elements are multiplied by the number of elements in the **RatingScale** input parameter of the **Rating** block.

</div>

### Modifiers

|**Modifier**|**Attribute**|**Element**|
|---|---|---|
|IsEdit|.is-edit|.rating|
|RatingSmall|.rating-small|.rating|
|RatingMedium|.rating-medium|.rating|
|Size|--rating-size|.rating-item|

## API

If you are an advanced user, you might want to use our Rating API (OutSystems.OSUI.Patterns.RatingAPI)for more complex use cases.

### Methods

|**Function**|**Description**|**Parameters**|
|---|---|---|
|ChangeProperty|Changes the Rating property.|<ul><li>ratingId: string</li><li>propertyName: string</li><li>propertyValue: any</li></ul>|
|Create|Creates a new Rating instance and adds it to the ratingMap.|<ul><li>ratingId: string</li><li>configs: string</li></ul>|
|Destroy|Destroys the Rating instance.|<ul><li>ratingId: string</li></ul>|
|GetAllRatings|Returns the Map with all the Rating instances on the screen.|<ul><li>Returns array of Ids</li></ul>|
|GetRatingById|Gets the Rating instance Id.|<ul><li>ratingId: string</li></ul>|
|Initialize|Initializes the pattern instance.|<ul><li> ratingId: string</li></ul>|
