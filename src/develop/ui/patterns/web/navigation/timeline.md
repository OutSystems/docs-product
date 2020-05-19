---
tags: runtime-traditionalweb; 
summary: Timeline indicates related events in chronological order.
---

# Timeline

You can use the Timeline UI Pattern to show related events in a chronological order, such as a user’s upcoming, current, and past activities.

![](<images/timeline-image-6.png>)


**How to use the Timeline UI Pattern**

1. In Service Studio, in the Toolbox, search for `Timeline`. 

    The Timeline widget is displayed.

    ![](<images/timeline-image-7.png>)

1. From the Toolbox, drag the Timeline widget onto your application’s screen.

    ![](<images/timeline-image-2.png>)

    By default, the Timeline widget contains a Timeline Item widget which contains an Icon, Date, and Content placeholder. You can add as many Timeline Items as required.

1. Set the required content in the Icon, Date, and Content placeholders. 

    ![](<images/timeline-image-8.png>)

After following these steps and publishing the module, you can test the pattern in your app.

## Properties

**Timeline**

| **Property** |  **Description** | 
|---|---|
| ExtendedClass (Text): Optional  | <p>Add custom style classes to the Timeline UI Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Timeline UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Timeline UI styles being applied.</li></ul></p> |


**Timeline Item**

| **Property** |  **Description** | 
|---|---|
| Color (Color Identifier): Optional  | Icon background color. Red, orange, yellow, lime, green, blue, violet, and pink are just some of predefined colors available for the badge. <p>Examples <ul><li>_Blank_ - The icon background color is the color you chose when creating the app (default value).</li><li>_Entities.Color.Red_ - The icon background color is red.</li></ul></p> |
| ExtendedClass (Text): Optional  | <p>Add custom style classes to the Timeline Item UI Pattern. You define your custom style classes in your application using CSS.</p> <p>Examples <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_''myclass''_ - Adds the _myclass_ style to the Timeline Item UI styles being applied.</li><li>_''myclass1'' ''myclass2''_ - Adds the _myclass1_ and _myclass2_ styles to the Timeline Item UI styles being applied.</li></ul></p> |
