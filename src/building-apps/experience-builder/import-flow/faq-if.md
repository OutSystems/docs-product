---
summary: Check the answers to the frequently asked questions about importing Flows to Experience Builder.
locale: en-us
guid: c90cf9dd-fbcb-4f66-8bc8-d6bc41a9755e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4454:2893
---

# Import Flows FAQ

## Can I use my own custom layout block on the imported flows?

**No**. Your flows must use the same layout block as the default screens from Experience Builder. This guarantees the correct integration of all features.

## Which layout block should I use on my imported flows?

The **Experience Builder Templates Mobile** app provides two layout options:

* Layout: Block that displays a header, footer, back button, and menu. Should be used on most screens.
* LayoutBlank: Layout block that displays nothing but the screen content. Usually used when a more simple structure is needed, for example, Login and Sign Up pages. Screens that are built with this layout block are not affected by the user's customizations on Experience Builder's menu canvas.

![Screenshot of Experience Builder layout options including the standard layout and LayoutBlank](images/layout-options-eb.png "Experience Builder Layout Options")

## Can I import flows with external dependencies?

**Yes**, but you must ensure that all dependencies are always available on the environment. Otherwise, users may experience runtime errors on generated mobile apps that use imported flows.

## What is the purpose of the Flow type property? Which one should I choose?

The **Flow type** property defines the role of the flow that's being imported. Experience Builder uses this information both for [validation](../ref/error-ref.md) purposes and for generating quality apps.

To find the value that best describes the flow's main objective, see the following table. If none of these categories fit, leave the property blank.

Value | Description |
---|---
ChangePasscode | Identifies flows that allow users to set their authentication passcode
Dashboard | Characterizes flows with dashboards or that are commonly used as app home screen
Login | Labels the flow as capable of handling users login
Onboarding | Distinguishes flows used to onboard users to the app
Signup | Labels the flow as capable of handling users registration

## What is the purpose of the Link type property? Which one should I choose?

The **link type** property identifies the purpose of the exit points in a flow that's being imported. Experience Builder uses this information during the generation of the mobile app (for example, automatically setting the application entry point for logged in users).


To find the value that best describes the exit point's role, see the following table. If none of these categories fit, leave the property blank.

Value | Description |
---|---
BackButton | Identifies exit points used by the user to navigate to the previous screen
Login | Identifies exit points used by the user to enter the application after a successful Login
Onboarding | Identifies exit points that directs the user after being onboarded

![Table describing different exit point types in Experience Builder such as BackButton, Login, and Onboarding](images/exit-point-type-eb.png "Experience Builder Exit Point Types")

## What is the effect of the "Has menu?" property on imported screens

This property defines which screens should have a menu that is automatically added by Experience Builder.

![Illustration of the 'Has menu?' property toggle in Experience Builder indicating whether a screen should have a menu](images/screen-has-menu-eb.png "Experience Builder Screen Menu Property")

Usually, most screens should have a menu to allow users to easily navigate through the app. The exceptions are screens where the user should not leave a process (for example, the intermediary screens on a step-by-step process).
