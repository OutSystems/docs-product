---
tags: runtime-traditionalweb; 
summary: Search allows the user to find pieces of content without the use of navigation.
---

# Search 

Allow the user to find pieces of content without the use of navigation.

Use the Search so that end-users can easily find pieces of content by entering queries. Unlike navigation, knowledge of the content's location isn't required. 

**How to use**

1. Drag Search pattern into the preview.

    ![](<images/search-image-1.png>)

1. Set a Local Variable for the input of type Text.

    ![](<images/search-image-2.png>)

1. Publish and test.


## Input Parameters

| **Input Name** |  **Description** |  **Type** | **Mandatory** | **Default Value** |
|---|---|---|---|---|
| ExtendedClass  | Add custom style classes to this Block. | Text | No | none |
  
## Layout and Classes

![](<images/search-image-3.png>)

## Advanced Use Case

### Make a reset search button

For this example, refer to the [FourColumns Screen Template](https://outsystemsui.outsystems.com/OutSystemsUILiveStyleGuide/FourColumnGallery.aspx).

1. Go to the Search Pattern presented in Column2 inside the Filters_Wrapper container.
1. Drag a container inside the Actions placeholder.
1. Drag a Icon Widget inside that container and choose `Entities.IconName.times` for the Name parameter. This is the X icon.

    ![](<images/search-image-4.png>)

1. In the container, set the Display parameter to `If(SearchKeyword <> "", True, False)`. This uses the already existing SearchKeyword Local Variable and only displays the container if the search input has text.

    ![](<images/search-image-5.png>)

1. Add an OnClick event and set the handler to the RefreshTable action. 
1. Set the parameters ResetFilters and ResetPagination to True. 
1. In the Category property, set the ProductCategory Local Variable. This way you reset the search input as well as the screen to the default state.

    ![](<images/search-image-6.png>)

1. Publish and test.

    ![](<images/search-gif-1.gif>)
