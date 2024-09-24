---
summary: The article explains how to extend OutSystems UI Patterns using provider client actions and JavaScript, listing patterns with their external providers and versions
tags: runtime-mobileandreactiveweb;
locale: en-us
guid: E9183915-DC47-4192-ACE3-AE04472EFCB2
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=4647%3A10004&mode=design&t=ANpsYvOCthr9AWot-1
---
# OutSystems UI Pattern extensibility

<div class="info" markdown="1">

This article refers to the latest version of each UI Pattern only. Some deprecated patterns use different providers and a different extensibility solution through the **AdvancedFormat** parameter.

</div>

Some of  OutSystems UI Patterns are based on external providers. Although these providers have many different extensibility options available, OutSystems only offers a curated list of them using input parameters and client actions.

However, you can access all of the extensibility options offered by the providers by using the following OutSystems extensibility features: 

* [Provider client actions](ext-provider-client-actions.md)
* [Provider instance and JavaScript](ext-provider-instance-java.md)

The following table shows the list of OutSystems UI Patterns that use external providers:

UI Pattern | Provider | Library version  
---|---|---
Carousel | [Splide](https://splidejs.com/) | 4.1.3  
Date Picker | [Flatpickr](https://flatpickr.js.org/)| 4.6.13
Date Picker Range | [Flatpickr](https://flatpickr.js.org/)| 4.6.13 
Dropdown Search | [VirtualSelect](https://sa-si-dev.github.io/virtual-select/#/) | 1.0.37
Dropdown Tags | [VirtualSelect](https://sa-si-dev.github.io/virtual-select/#/) | 1.0.37 
Range Slider | [noUiSlider](https://refreshless.com/nouislider/) | 15.6.1  
Range Slider Interval | [noUiSlider](https://refreshless.com/nouislider/)| 15.6.1  
