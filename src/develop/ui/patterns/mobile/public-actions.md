---
tags: runtime-mobileandreactiveweb;  
summary: 
locale: en-us
guid: e4899a53-ca9e-4c13-b021-06518a34fba2
app_type: mobile apps, reactive web apps
---

# Public Actions

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

## Accordion

You can use the [Accordion](<content/accordion.md>) actions described below anywhere in OutSystems.

### AccordionCollapseAll 

Function to collapse all the expanded items of an Accordion.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text | Accordion block identifier. |

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### AccordionExpandAll 

Function to expand all the collapsed items of an Accordion.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text | Accordion block identifier. |

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### AccordionItemAllowTitleEvents

Enable the events of an AccordionItem title’s elements. Use this action to trigger element events (for example, link on click) without opening/closing the Accordion Item.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text | Accordion block identifier. |

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### AccordionItemCollapse

Closes an Accordion Item.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text |AccordionItem block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### AccordionItemExpand

Opens an Accordion Item.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text |AccordionItem block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

## Bottom Sheet

You can use the [Bottom Sheet](<interaction/bottomsheet.md>) actions described below anywhere in OutSystems.

### BottomSheetClose

Closes a Bottom Sheet.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text |Bottom Sheet block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### BottomSheetOpen

Opens a Bottom Sheet.

|Input parameter | Type | Description | 
|---|---|---|
|WidgetId| Text |Bottom Sheet block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

## Carousel

You can use the [Carousel](<interaction/carousel.md>) actions described below anywhere in OutSystems.

### CarouselGoTo

Set the item that the Carousel goes to.

<!-- Use this action to go to a specific element in the Carousel. It works on static elements or elements created with a list. When the button that is assigned this action is pressed, the Carousel moves to the specific position of the element. If that position doesn't exist, the Carousel jumps to the last element. -->

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Carousel block identifier.|
|ItemIndex| Integer|Index of the item that the Carousel goes to.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### CarouselNext

Use to move the Carousel to the next item.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Carousel block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### CarouselPrevious

Use to move the carousel to the previous item.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text | Carousel block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### CarouselToggleDrag

Enable the drag to navigate between items.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Carousel block identifier.|
|HasDrag|Boolean|Set to True to enable the drag functionality of the Carousel block.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### SetCarouselDirection

Set the direction in which the Carousel is sliding when it is automatically looping (Loop). By default, the carousel direction is from left to right.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Carousel block identifier.|
|Direction| CarouselDirection |The direction of the carousel. By default, the Carousel moves from left to right.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

<!-- ### ListRemove

To remove elements from the Carousel, create an action with the ListRemove and UpdateCarousel actions.

## Stacked Cards

You can use the [Stacked Cards](<interaction/stackedcards.md>) actions described below anywhere in OutSystems.

![](images/StackedCards_Actions.png)

### SwipeLeft Action

Calling this public action in relation to a button triggers the SwipeRight action and moves the card. You need to set the Stacked Cards ID (Widget ID).

### SwipeRight Action

Calling this public action in relation to a button triggers the SwipeRight action and moves the card. You need to set the Stacked Cards ID (Widget ID).

### SwipeTop Action

Calling this public action in relation to a button triggers the SwipeTop action and moves the card. You need to set the Stacked Cards ID (Widget ID).

### UpdateStackedCards Action

You must use this action on the ListRemove action. The action updates all cards and rearranges the order, scale, and opacity of each one of them.

### ListRemove

To remove elements from the Stacked Cards, create an action with the ListRemove and UpdateCarousel actions (see the example below).

![](images/ListRemove.png) --> 

## Date Pickers

You can use the [Date Picker](<interaction/datepicker.md>) actions described below anywhere in OutSystems.

### DatePickerClear

Resets the selected dates (if any) and clears the input of a Date Picker.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Date Picker block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerClose

Closes a Date Picker.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text |Date Picker block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerOpen

Opens a Date Picker.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Date Picker block identifier.|

|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerRangeUpdateDates

Update the selected start and end dates shown in a given Date Picker Range.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text |Date Picker block identifier.|
|NewStartDate| Date Time |The new selected start date for the DatePickerRange.|
|NewEndDate| Date Time |The new selected end date for the DatePickerRange.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerSetEditableInput

Use this action to enable the end-user to write on the Date Picker input. By default, the input is read-only.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Datepicker block identifier.|
|IsEditableInput| Boolean |If True, the input is editable. If False, the input is read only. |

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerSetLanguage

Set a new language on a Date Picker. All the elements shown in the Date Picker are translated into the selected language.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text |Datepicker block identifier.|
|Language| DatePickerLanguage Identifier|The ISO 639-1 language code. For example, en, fr, jpn.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerToggleNativeBehavior

Use this action to control the Date Picker behavior when opened in mobile. By default, the Date Picker is opened as native, in mobile.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text |Datepicker block identifier.|
|IsNative| Boolean|Set to True to open as native in mobile.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### DatePickerUpdateDate

Update the selected date displayed in a Date Picker.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text |Datepicker block identifier.|
|NewDate| Date Time|The new selected start date for the Date Picker.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

## Dropdowns

You can use the [Dropdown](<interaction/dropdownsearch.md>) actions described below anywhere in OutSystems.

### DropdownClear

Method used to clear any selected values for a Dropdown.

|Input parameter |Type | Description | 
|---|---|---|
| WidgetId| Text |Dropdown identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|


### DropdownClearValidation

Method used to clear the validation style of a Dropdown.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Dropdown identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|


### DropdownDisable

Method that sets a Dropdown to disabled.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Dropdown identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success|Boolean| Boolean that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Shows details about errors that occur after performing the action. It contains a code and a message explaining the error.|

### DropdownEnable

Method that sets a Dropdown to enabled.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Dropdown identifier|

|Output parameter | Type | Description | 
|---|---|---|
|Success|Boolean| Boolean that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Shows details about errors that occur after performing the action. It contains a code and a message explaining the error.|

### DropdownGetSelectedValues

Method that returns a list with the selected value from a Dropdown.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Dropdown identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|


### DropdownNotValid

Method used to set a not valid style to a Dropdown.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Dropdown identifier.|
|ValidationMessage |Text |Text to be added when Dropdown not IsValid.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|


### DropdownTogglePopup

Use this action to enable/disable the default behavior of Dropdowns opening as a popup in Native Apps. By default, Dropdowns open as popups in Native Apps.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |ID of the pattern to be affected.|
|EnablePopup |Boolean|Set to True to open the Dropdown as a popup in Native Apps. This is the deafult value.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

## Flip Content

You can use the [Flip Content](<content/flipcontent.md>) actions described below anywhere in OutSystems.

### FlipContentBack

Shows the back of the Flip Content.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Flip Content identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### FlipContentFront

Shows the front of the Flip Content.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Flip Content identifier.|

||Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### FlipContentToggle

Flips the content of the Flip Content.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Flip Content identifier|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

## Notification

You can use the [Notification](<interaction/notification.md>) actions described below anywhere in OutSystems.

### NotificationClose

Closes a Notification.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Notification block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### NotificationOpen 

Opens a Notification.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Notification block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

## Progress

You can use the [Progess Bar](<numbers/progressbar.md>) and [Progress Circle](<numbers/progresscircle.md>) actions described below anywhere in OutSystems.

### ResetProgressBar

Resets the Progress Bar value to the Progress value.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Progress Bar block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### ResetProgressCircle

Resets the Progress Circle value to the Progress value.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Progress Circle block identifier.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|


### SetProgressBarValue

Set a value on the Progress Bar.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Progress Bar block identifier.|
|Progress|Integer|The value to set the progress.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|

### SetProgressCircleValue

Set a value on the Progress Circle.

|Input parameter |Type | Description | 
|---|---|---|
|WidgetId| Text |Progress Circle block identifier.|
|Progress|Integer|The value to set the progress.|

|Output parameter | Type | Description | 
|---|---|---|
|Success| Boolean| Boolean value that indicates if the action was successfully performed. |
|ErrorMessage|ErrorMessage|Message detailing the errors that occur after performing the action. The message contains an error code and explains the error.|
