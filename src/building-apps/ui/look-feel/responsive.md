---
summary: Explore responsive UI features in OutSystems 11 (O11) for adaptive and responsive app development across devices.
tags: ui design, css customization, cross-platform development, adaptive design, screen size detection
locale: en-us
guid: 5d91a5b5-b07e-4858-af62-980f6a558b1d
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?type=design&node-id=1116%3A14411&mode=design&t=VUTD7oZE9xvPWlG0-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - remember
  - apply
---

# Responsive UI

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

On the OutSystems UI, everything is responsive — themes, layouts, and patterns. By default, OutSystems provides a set of adaptive and responsive behaviors that allow developers to easily create applications to work with all browsers, devices, and resolutions.

## Device detection

To have a multiexperience on reactive and native mobile applications, OutSystems has a built-in device detection mechanism that identifies the device type (desktop, tablet, or phone) and screen size and correctly displays layouts and UI patterns accordingly.

When the device type is detected, a set of classes is automatically added to the body HTML element.

![Diagram showing how OutSystems adds CSS classes for device, orientation, browser, operating system, and touch detection](images/responsive-device-detection.png "Responsive Device Detection")

The CSS classes add the following:

* **Device:** .desktop, .tablet, .phone, .iphonex
* **Orientation:** .landscape, .portrait
* **Browser:** .chrome, .firefox, .edge, .safari, etc.
* **Operation system:** .windows, .osx, .ios, .android, etc.
* **Touch devices detection:** .is--touch

**Example:**

```
.desktop .btn { ... }
```

```
.tablet .btn { ... }
```

```
.phone .btn { ... }
```

## OutSystems UI changes based on devices

To improve the experience and the responsive behavior of your application, the OutSystems UI Theme has different rules for each device:

* The OutSystems UI Layouts changes the structure based on each device type and layout configuration
* The text sizes change based on each device type
* **:hover** and **:focus** states are removed from all links
* The size of input widgets, for example, input, textarea, checkbox, and buttons increases so that they have a bigger clickable area
* The login form is full width on phones
* Using the reactive layouts, the buttons and containers are full width on phones
    * In order to keep good readability for all applications on small devices, OutSystems apply this rule so that all containers are full width and the content is broken up on the screen. If you want to override this behavior, add the CSS class **.no-responsive** to each element.

## OutSystems UI layouts

Depending on screen size and resolution, OutSystems UI captures device type (desktop, tablet, or phone) and adapts the content to the screen. To learn more about app templates, see [OutSystems UI Framework App Templates](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/AppTemplates).

![Illustration of OutSystems UI responsive layouts for different devices](images/responsive-layout.png "OutSystems UI Responsive Layouts")

On Reactive applications, the OutSystems UI provides the following fully responsive layouts:

* LayoutSideMenu
* LayoutTopMenu
* LayoutBase

The **LayoutTopMenu** and **LayoutSideMenu** layouts have different settings to control their behaviors. To create applications with a **hero image** and content, the **LayoutBase** is available to which you can add different sections with your custom content.

When an application is open on a mobile device, all the layouts have the same behavior, opening the menu as an overlay on the page content with all the menu items displayed.

![Example of a mobile layout with menu overlay in OutSystems UI](images/responsive-mobile-layout.png "Responsive Mobile Layout")

For Native Mobile applications, OutSystems UI provides a layout to use on a tablet, phone, and progressive web applications (PWA). The layout has the following  behaviors to open the menu:

* **Expandable:** Open the menu, pushing the screen content
* **Overlay:** Opens the menu applying an overlay on top of the screen content
* **Visible:** The menu is always visible

![Depiction of native mobile application layout behaviors in OutSystems UI](images/responsive-native-layout.png "Responsive Native Layout")

**Note:** On the phone, the layout always has the overlay behavior applied because of the available space on smaller screens, even when the **Expandable** or **Visible** behavior is enabled.

## Adaptive patterns

Every app is different. The way your app adapts to a specific device is, therefore, unique. To address this, OutSystems UI offers a set of [adaptive patterns](https://outsystemsui.outsystems.com/OutsystemsUiWebsite/PatternsOverview). These patterns give you full control of how your application will look on different screen sizes, allowing for different settings for phones and tablets.

**Available adaptive patterns:** _Columns2, Columns3, Columns4, Columns5, Columns6, ColumnsMediumLeft, ColumnsMediumRight, ColumnsSmallLeft, ColumnsSmallRight, DisplayOnDevice, Gallery, and MasterDetail._

## Adaptive actions

All patterns on OutSystems UI can adapt the UI to the device, using only CSS. However, if your use case has specific scenarios to show or hide content, navigate to another page, or even run client actions, you need a little extra to run different logic according to the device.

![Screenshot showcasing various adaptive patterns available in OutSystems UI](images/responsive-adaptive-ss.png "Adaptive Patterns Screenshot")

OutSystems UI provides a set of client-side actions that allow developers to decide which screen areas to hide, how images are placed, or even which screen to navigate to, according to the detected device. You can find the client-side actions on the **Logic** tab, inside the **DeviceDetection** folder.

![Screenshot of client-side actions for device detection in OutSystems UI](images/responsive-clientside-ss.png "Client-Side Actions Screenshot")

**Available client-side actions:** _GetBrowser, GetDeviceOrientation, GetDeviceType, GetIsTouch, GetOS, IsDesktop, IsTablet, IsPhone, IsWebApp, IsRunningAsPWA, IsLayoutNative, and SetDeviceBreakpoints._

## Columns responsive behavior

OutSytems UI provides a set of structure patterns that allow dividing content in columns that follow the underlying grid. The structure patterns are blocks with specific responsive parameters, which allow the developer to configure how they react on each mobile device.

![Screenshot displaying responsive structure patterns in OutSystems UI](images/responsive-structpatt-ss.png "Responsive Structure Patterns Screenshot")

Possible values for tablet and phone include the following:

* **Break All:** All columns break. This means each column occupies the total width of the available space:

![Visual representation of the 'Break All' responsive behavior for columns in OutSystems UI](images/responsive-breakall.png "Break All Columns Responsive Behavior")

* **Break First:** Only the first column breaks. This means the first column occupies the total width and the other ones remain side by side:

![Visual representation of the 'Break First' responsive behavior for columns in OutSystems UI](images/responsive-breakfirst.png "Break First Column Responsive Behavior")

* **Break Middle:** All columns break. When there is an even number of columns, they are divided in half, with the same number of columns on top and bottom. When there is an uneven number of columns, there is always one more column on top than on the bottom:

![Visual representation of the 'Break Middle' responsive behavior for columns in OutSystems UI](images/responsive-breakmiddle.png "Break Middle Columns Responsive Behavior")

* **Break Last:** Only the last column breaks. This means the last column occupies the total width and the other ones remain side by side:

![Visual representation of the 'Break Last' responsive behavior for columns in OutSystems UI](images/responsive-breaklast.png "Break Last Column Responsive Behavior")

* **Break None:** No columns break. This means all columns remain side by side:

![Visual representation of the 'Break None' responsive behavior for columns in OutSystems UI](images/responsive-breaknone.png "Break None Columns Responsive Behavior")

With OutSystems UI, you can use the platform grid to organize content, however, it has no responsive behavior. To organize content with responsive behavior, use the columns pattern instead, which allows you to configure the responsiveness yourself.

If you want to use the platform grid and add your content using containers with specific columns width, you can use the **DisplayOnDevice** pattern to set your content and the custom structure that will be shown on each device.

![Screenshot showing the Display On Device pattern for responsive content in OutSystems UI](images/responsive-displayondevice-ss.png "Display On Device Pattern Screenshot")

## Application content changes based on devices

OutSystems UI provides a set of actions — IsDesktop, IsTablet, IsPhone, IsWebApp, IsRunningAsPWA — to manage your content or to use in client actions. These actions also work as functions. You can find these client actions on the **Logic** tab, inside the **DeviceDetection** folder.

![Screenshot of responsive action functions for device-specific content management in OutSystems UI](images/responsive-actionfunctions-ss.png "Responsive Action Functions Screenshot")

You can use actions in the following ways:

* To set values on input parameters:

![Screenshot demonstrating how to set values on input parameters based on device type in OutSystems UI](images/responsive-setvalues-ss.png "Set Values on Input Parameters Screenshot")

![Screenshot showing an example of setting values on input parameters for different devices in OutSystems UI](images/responsive-setvalues2-ss.png "Set Values on Input Parameters Example Screenshot")

* To control the Container’s visibility:

![Screenshot illustrating how to control container visibility based on device type in OutSystems UI](images/responsive-controlcontainer-ss.png "Control Container Visibility Screenshot")

* To set conditions (If widget):

![Screenshot showing how to set conditions in an If widget for responsive design in OutSystems UI](images/responsive-setconditions-ss.png "Set Conditions in If Widget Screenshot")

* To apply logic inside client actions on If conditions:

![Screenshot of applying logic inside client actions based on device type in OutSystems UI](images/responsive-applylogic-ss.png "Apply Logic in Client Actions Screenshot")

## Set responsive breakpoints

On the OutSystems UI, there are default device breakpoints that identify **tablet** and **phone** devices. Screen resolutions between **1024px and 768px of width** are recognized as **tablets** and screen resolutions **lower than 768px of width** are recognized as **phones**.

To override these breakpoints, there is the  **SetDeviceBreakpoints client action** (on the **Logic** tab, inside the **DeviceDetection** folder) that you can on your **application ready**, setting the new breakpoints to be applied:

![Screenshot showing how to set custom responsive breakpoints in OutSystems UI](images/responsive-breakpoints-ss.png "Set Responsive Breakpoints Screenshot")

**Note:** When opening on an iPad Pro (or similar tablet devices) in landscape, it is treated as a desktop.

## Safe area inset support

OutSystems injects CSS variables to handle safe areas on all devices. These variables ensure that your app content doesn't overlap with system UI elements, such as the status bar or home indicator. For detailed information, refer to [Safe area inset support](../../../deploying-apps/mobile-app-packaging-delivery/customize-mobile-app/customize-edge-to-edge.md#safe-area-inset-support-safe-area-inset-support)
