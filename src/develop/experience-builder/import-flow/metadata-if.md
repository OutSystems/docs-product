---
summary:  Enter the metadata when importing Flow Templates, to correctly integrate them with Experience Builder and allow developers to use them during mobile applications creation.
locale: en-us
guid: b9d9a9ce-0a4b-4ee4-a574-96d022f3324a
---

# Metadata reference

Metadata information about the imported flow templates helps to seamlessly integrate them to Experience Builder.

You can set the metadata property values on the **Import Flows** wizard. All information is stored on the provided templates module. 

## Flow metadata

Property | Is mandatory? |  Description | Value
---|---|---|---
Display name | True | Flow template name displayed in Experience Builder | Allows any text value. Use a name relatable to that in Service Studio.
Tags | False | Keywords used to filter flow templates | List of keywords associated with the flow. The user can search for these tags on the Add Flows modal when creating or modifying an app. Example: `Insurance, Bills, Payment`.
Category | True | Value used to group flow templates | Name of the category used by Experience Builder to organize flow templates. Example: `Dashboard`.
Flow type | True | Value related to the purpose of the flow on the mobile application | Accepts one of following items from the dropdown: `Login, Onboarding, Signup, Dashboard, ChangePasscode, Default`. Refer to [this](faq-if.md#what-is-the-purpose-of-the-flow-type-property-which-one-should-i-choose) section for more details on how to choose the correct type.

## Screen metadata

Property | Is mandatory? | Description | Value
---|---|---|---
Display name | True | Screen name displayed in Experience Builder | Allows any text value. Use a name relatable to that in Service Studio.
Screen position | True | Value indicating the display order of this screen compared to other screens in the flow | Drag the card represeting screen to change the position of the screen.
Has menu? | True | Value that indicates whether the screen should have a menu on the mobile app or not| Boolean value used by Experience Builder when adding the application navigation menu to all screens.

## Exit point metadata

Property | Is mandatory? | Description | Value
---|---|---|---
Display name | True | Name displayed in Experience Builder when hovering over exit points | Allows any text value. This content is displayed to users when hovering over the exit points.
Link type | True | Value related to the purpose of the exit point on the mobile application | Accepts one of following items from the dropdown: `BackButton, Login, Onboarding, Generic`. For more details on how to choose the correct type, refer to [this](faq-if.md#what-is-the-purpose-of-the-exit) section.
