---
locale: en-us
guid: 8d848bc2-1057-4692-8e94-9ba8c4212806
app_type: traditional web apps, mobile apps, reactive web apps
---

# ExBuilder_MPat

To learn more about the custom UI patterns, check out the [live style guide](https://experiencebuilder.outsystems.com/ExBuilder_CustomPatterns_Samples/CustomPatternsList)
.
Module with the custom patterns and widgets that will be used on app types.

## Summary

Client Action | Description
---|---
[ChatWrapper_LoadedNewItems](<#ChatWrapper_LoadedNewItems>) | Client action to remove the class that is used as a block to trigger new and multiple scroll events.
[ChatWrapper_ScrollToBottom](<#ChatWrapper_ScrollToBottom>) | 
Client variable to update the scroll position to the last added item.

Structure | Description
---|---
[CustomInputValidations](<#Structure_CustomInputValidations>) | Structure to handle the basic information about native select and custom input masks validations.
[NativeSelect](<#Structure_NativeSelect>) | Structure to handle the basic information about a native select option.
[NativeSelectOptions](<#Structure_NativeSelectOptions>) | Structure to handle the basic information about native select options.

Static Entity | Description
---|---
[DisplayToggleStructure](<#StaticEntity_DisplayToggleStructure>) | Static entity with a set of options to define the apearance structure on the Display_ToggleShow pattern.
[FilterTypes](<#StaticEntity_FilterTypes>) | Static entity with the available filter types. It's used in order to enable the filter or sort option.


## Client Actions

### ChatWrapper_LoadedNewItems { #ChatWrapper_LoadedNewItems }

Client action to remove the class that is used as a block to trigger new and multiple scroll events.
*Inputs*

MessagesWrapperElem
:   Type: mandatory, Text.  
    Input variable with messages list wrapper html element.

### ChatWrapper_ScrollToBottom { #ChatWrapper_ScrollToBottom }

Client variable to update the scroll position to the last added item.

*Inputs*

MessagesWrapperElem
:   Type: mandatory, Text.  
    Input variable with messages list wrapper html element.

## Structures

### CustomInputValidations { #Structure_CustomInputValidations }

Structure to handle the basic information about native select and custom input masks validations.

*Attributes*

Valid
:   Type: Boolean.  
    Indicates if the field is filled properly.

ValidMessage
:   Type: Text.  
    Indicates the message to show as a valid message.

### NativeSelect { #Structure_NativeSelect }

Structure to handle the basic information about a native select option.

*Attributes*

Code
:   Type: Boolean.  
    Indicates the option code.

Value
:   Type: Text.  
    Indicates the option value.

### NativeSelectOptions { #Structure_NativeSelectOptions }

Structure to handle the basic information about native select options.

*Attributes*

X_COMBO
:   Type: [NativeSelect](#Structure_NativeSelect).  
    Indicates the selected option.

## Static Entities

### DisplayToggleStructure { #StaticEntity_DisplayToggleStructure }

Static entity with a set of options to define the apearance structure on the Display_ToggleShow pattern.

*Attributes*

Label
:   Type: Text (50).  
    Label of the display toggle.

*Records*

* Inline
* ReverseRows

### FilterTypes { #StaticEntity_FilterTypes }

Static entity with the available filter types. It's used in order to enable the filter or sort option.

*Attributes*

Label
:   Type: Text (50).  
    Label of the filter type.

*Records*

* PriceAndRating
* Sort
