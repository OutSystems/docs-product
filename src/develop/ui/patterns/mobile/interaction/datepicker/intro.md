---
tags: runtime-mobileandreactiveweb;  
summary: Date Picker allows the end user to select a single or a range of dates using a calendar.
---

# Date Picker

You can use the Date Picker UI Pattern to allow users select a single date or a range of dates using a calendar. The Date Picker Pattern is based on the [Pikaday.js library](https://github.com/Pikaday/Pikaday) (version 1.8.2). For more advanced options, you can refer to this library.

<div class ="info" markdown="1">

Only use the Date Picker Pattern if you really need the more advanced use cases it provides. As a general good practice in web development, especially when targeting Mobile, using the HTML [input type=date](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/date) should be prioritized, because by default, it provides the best user experience and accessibility across all browsers with very low impact to performance.

</div>

The following are the main ways you can display the Date Picker widget on a screen:

* Bound to an input using the **InputWidgetId** parameter (shown in the [How to Use the Date Picker UI Pattern](datepicker.md)

* Bound to a trigger element, for example, a button, using the **ButtonTriggerId** parameter

* Rendered flat on the screen by leaving both the **InputWidgetId** and **ButtonTriggerId** properties empty 

## Direction and Internationalization

The Date Picker Pattern sets both directions and translations automatically. If you choose a locale that triggers the Right-To-Left options on the screen, the Date Picker automatically sets the isRTL setting to True.

Translation options are automatically set using the settings in the [Multilingual component](../../../../multilingual-tp/intro.md). This component automatically changes the language based on the current HTML language attribute.
