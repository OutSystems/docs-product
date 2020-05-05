---
tags: runtime-mobileandreactiveweb;  
summary: Advanced Use Cases for the Gallery UI Pattern.
---

# Gallery UI Pattern Reference

## Layout and Classes

![](images/Gallery_Layout.png)

## Advanced Use Case

### Using Animations Inside the Gallery

1. Use the **Animate** block as the first element inside the list.

![](images/Gallery_animate.png)

1.  Place your content inside the b block.

![](images/Gallery_ellipsis.png)
1. Define the **Animate** block with your desired type of animation, and set
the delay with current row number from the list.

![](images/Gallery_interaction.png)

**Note**: If you are using a List inside a Gallery, you need to disable
virtualization.

![](images/Gallery_list.png)


