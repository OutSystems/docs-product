---
summary: OutSystems 11 (O11) tutorial on creating many-to-many relationships using a junction entity.
tags: data modeling, database design, entity relationship, mobile app development, web application development
locale: en-us
guid: 9a7e1290-8439-4b9b-8471-ee1114d03024
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=159:12
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
---

# Create a Many-to-Many Relationship

A many-to-many relationship happens when one entity has a one-to-many relationship with another entity, and vice-versa. For example, an `Author` can write several `Books`, and a `Book` can be written by several` Authors`. This kind of relationship is also known as **N to M** relationship.

Resolve this kind of relationships by adding a third entity, called **junction entity**. It must have at least two foreign keys, one to each entity in the relationship. Other attributes can also be added if needed (see the example).

To create a many-to-many relationship, follow these steps:

1. [Create a relationship entity](<../entity-create.md>).
1. Add an attribute and set the data type to the identifier of the first entity.
1. Add another attribute and set the data type to the identifier of the second entity.

If you want to ensure that an entity has unique records (like a `Book` can only have one `Publisher`), then add a [unique index](../index-create.md) to the two foreign keys.

Check here our [online training videos ](https://learn.outsystems.com/training/journeys/modeling-data-relationships-642/many-to-many-relationship/o11/448)on this topic:

<div style="padding:56.25% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/874768910?badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write" style="position:absolute;top:0;left:0;width:100%;height:100%;" title="Many-to-Many Relationship [en-US / 11]"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>


## Example

You have a mobile application called GoOut, where end users can find and review places like restaurants, hotels, etc. An end user can review many places and a place can have reviews from many end users, i.e. a many-to-many relationship. We will call these two entities `Review` and `Place`. Besides the two foreign keys, a review has also other attributes: classification, comments, and submission date.

Let's create the `Review` entity:

1. In the Data tab, open the GoOutWebDataModel entity diagram.
1. Drag the User system entity and the `Place` entity to the diagram.
1. Right-click the diagram canvas and select 'Add Entity'.
1. Name the entity as `Review`.
1. Drag the `User.Id` attribute to the `Review`.
1. Drag the `Place.Id` attribute to the `Review`.
1. Add the remaining attributes:
    * `Classification`, Integer type
    * `Comments`, Text type
    * `SubmittedOn`, Date type

![Diagram illustrating a many-to-many relationship with a Review entity connected to User and Place entities in the GoOut mobile application data model](images/many-to-many-relationship-1.png "Many-to-Many Relationship Diagram")
