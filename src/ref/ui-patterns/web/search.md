---
tags: runtime-traditionalweb;
summary: Advanced use cases for the Search UI Pattern.
locale: en-us
guid: cfd34720-b1a4-452c-ab75-0af83bed2963
---

# Search Reference

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

## Layout and classes

![](<images/search-3-diag.png>)

## Advanced use case

### Make a reset search button

For this example, refer to the [FourColumns Screen Template](https://outsystemsui.outsystems.com/OutSystemsUILiveStyleGuide/FourColumnGallery.aspx).

1. Go to the Search Pattern presented in Column2 inside the Filters_Wrapper container.

1. Drag a container inside the Actions placeholder.

1. Drag a Icon Widget inside that container and choose `Entities.IconName.times` for the Name parameter. This is the X icon.

    ![](<images/search-4-ss.png>)

1. In the container, set the Display parameter to `If(SearchKeyword <> "", True, False)`. This uses the already existing SearchKeyword Local Variable and only displays the container if the search input has text.

    ![](<images/search-5-ss.png>)

1. Add an OnClick event and set the handler to the RefreshTable action.

1. Set the parameters ResetFilters and ResetPagination to True.

1. In the Category property, set the ProductCategory Local Variable. This way you reset the search input as well as the screen to the default state.

    ![](<images/search-6-ss.png>)

1. Publish and test.

    ![](<images/search-7-ss.gif>)
