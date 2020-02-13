---
tags: runtime-traditionalweb; 
summary: LightBoxImage displays an image thumbnail that is clicked to open a fullscreen image.
---

# LightBoxImage

Displays an image thumbnail that is clicked to open a fullscreen image.

Used to open small images in fullscreen for more detail with a larger resolution.

**How to use**

Add an image to the placeholder or set the ImageURL parameter. To navigate thought images in a gallery, set the same Group parameter for them.

1. Drag LightBoxImage pattern into the preview.
1. Drag an image into the Thumbnail placeholder.

    ![](<images/lightboximage-image-1.png>)

1. Publish and test.

    ![](<images/lightboximage-image-2.png?width=600>)

## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| Title  | Title of the image to be displayed | Text | False | none |
| Group  | Images of the same group will be displayed in a gallery. | Text | False | none |
| ImageURL  |  URL for an image that can be a replacement for the Image Placeholder image. |  Text | False | none |
| ImageZoom  |  The zoom value is used to define the size of the image that will open in full screen based on the thumbnail size. Try to use images with the same ratio to avoid rendering problems, for example thumbnail with 100x100 and zoom 2 will open with 200x200 or thumbnail with 500x500 and zoom 0.5 will open with 250x250 |  Decimal | False | 2 |

## Layout and Classes

![](<images/lightboximage-image-3.png>) 

![](<images/lightboximage-image-4.png>)

## Advanced Use Case

### Change the LightBoxImage overlay

It is possible to change the opacity of LightBoxImage overlay when it is open by adding custom CSS. To implement this in your application, copy the CSS code below and add it to the theme.

```css
.pswp__bg {
    background-color: rgba(0, 0, 0, 0.8);
}

.pswp__ui--fit .pswp__top-bar, .pswp__ui--fit .pswp__caption {
    background-color: rgba(0, 0, 0, 0);
}
```
![](<images/lightboximage-image-5.png>)

### Add rounded corners to images inside LightBoxImage

To add rounded corners to images inside LightBoxImage, add the following custom css to the theme.

```css
.lightbox-content-thumbnail img,
.pswp__item img {
  border-radius: var(--border-radius-soft);
}
```
![](<images/lightboximage-image-6.png>)
