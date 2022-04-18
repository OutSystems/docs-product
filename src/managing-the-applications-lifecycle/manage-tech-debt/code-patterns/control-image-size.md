---
tags: 
summary: 
locale: en-us
guid: ea0f4bea-2a44-4d6d-bd9b-1ec11f8beffa
app_type: traditional web apps, mobile apps, reactive web apps
---


# Control image size

The images in web or mobile applications are often produced by design agencies whose primary goal is to achieve high definition and many details. This produces big image files. Other typical situation is the use of existing images from a database, originally collected for a purpose different than mobile/web application.

These result in images that are too large for the target display size. Developers tend to resolve this by simply controlling the width and height of the HTML attributes of an image. However, they should prepare the images for optimized load times.

## Impact

The first load of a screen is directly impacted by large images that are yet to be cached in browser. Moreover, caching is irrelevant for Banner images that keep changing on each screen load. This problem is augmented on mobile devices, because of the limited device capabilities and network latency.

## Best practices

* Reduce the image size to the displaying size.

* Compress images to the maximum rate not perceivable by the human eye.

* Don’t use the same image for different form factors.

* Don’t use the same image for displaying both full size and thumbnail.
