---
tags: runtime-traditionalweb;
summary: Explore advanced search functionalities in Traditional Web Apps using OutSystems 11 (O11).
locale: en-us
guid: cfd34720-b1a4-452c-ab75-0af83bed2963
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=615:554
---

# Search Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![Diagram illustrating the layout and classes of the Search UI Pattern in Traditional Web Apps](images/search-3-diag.png "Search UI Pattern Layout Diagram")

## Advanced use case

### Make a reset search button

For this example, refer to the [FourColumns Screen Template](https://outsystemsui.outsystems.com/OutSystemsUILiveStyleGuide/FourColumnGallery.aspx).

1. Go to the Search Pattern presented in Column2 inside the Filters_Wrapper container.

1. Drag a container inside the Actions placeholder.

1. Drag a Icon Widget inside that container and choose `Entities.IconName.times` for the Name parameter. This is the X icon.

    ![Screenshot showing the implementation of a reset search button in the Search UI Pattern](images/search-4-ss.png "Reset Search Button Example")

1. In the container, set the Display parameter to `If(SearchKeyword <> "", True, False)`. This uses the already existing SearchKeyword Local Variable and only displays the container if the search input has text.

    ![Screenshot demonstrating the conditional display of the reset search button based on the search keyword presence](images/search-5-ss.png "Conditional Display of Reset Button")

1. Add an OnClick event and set the handler to the RefreshTable action.

1. Set the parameters ResetFilters and ResetPagination to True.

1. In the Category property, set the ProductCategory Local Variable. This way you reset the search input as well as the screen to the default state.

    ![Screenshot of the configuration settings for the reset search button including OnClick event and Category property](images/search-6-ss.png "Reset Search Button Configuration")

1. Publish and test.

    ![Animated GIF demonstrating the functionality of the reset search button in the Search UI Pattern](images/search-7-ss.gif "Reset Search Button Test")
