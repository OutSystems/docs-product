---
summary: How to call externally defined JavaScript code in OutSystems.
tags: runtime-mobileandreactiveweb
locale: en-us
guid: 8a9bb94e-0720-4c91-ae99-8ed14c8ed6cc
app_type: mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=410:45
---

# Use JavaScript Code from an External Library

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

<div class="info" markdown="1">

OutSystems doesn't recommend using JavaScript libraries that directly manipulate the DOM, such as jQuery. Such libraries can break Reactive and Mobile apps and make them difficult to maintain.

</div>

Before using JavaScript code from an external library or contained in a `.js` file, do the following:

1. Import or create a script under the **Scripts** tree folder. This script may reside in the module (that is, it was created using the context menu options "Create Script" or "Import Script", when right-clicking the "Scripts" folder), or can be a reference to a script defined in another module.

    ![Screenshot showing the context menu options to add a script in OutSystems, with 'Import Script' and 'Create Script' highlighted.](images/module-add-script.png "Adding a Script in OutSystems")

1. In the **Interface** tab, select the screen/block where you want to add the JavaScript code, and its properties select the script in the **Required Scripts** property:

    ![Screenshot of the OutSystems interface tab displaying the screen properties with the 'Select Required Script' dropdown expanded, showing 'Scripts.MyScript' as an option.](images/screen-add-required-script.png "Selecting a Required Script in OutSystems")

The script added as a required script is evaluated in the global scope.
Thus, you can use functions and objects initialized in this script in any JavaScript element of the screen/block.

## Demo

This demo shows how you can easily add a reference to an external javascript and then use it in your app.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xmvxkkkDL5E" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="allowfullscreen"></iframe>
