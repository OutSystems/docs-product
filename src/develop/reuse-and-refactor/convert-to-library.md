---
summary: How to convert an existing Mobile or Reactive module to a Library.
tags: runtime-mobileandreactiveweb
locale: en-us
guid: 08e6258e-4543-4232-b5dc-1fd3707a0ecf
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
---

# Convert to Library

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

You can convert an existing **Mobile** or **Reactive** module to a Library. Note that there are specific constraints in Libraries that might imply some changes to the modules before the conversion can take place.

1. In the module that you wish to convert, open the **Module** menu and select **Convert** > **Convert to Library Module...**.

    <div class="info" markdown="1">

    If your module has elements that are not allowed in a Library module, the conversion stops and the elements not allowed are listed in an popup message. Remove the listed elements from your module, possibly moving them to a different module, and repeat step 1.  
    If your module has TrueChange errors, the conversion is stopped and an error message is shown. Fix the errors and repeat step 1.

    </div>

1. In the **Convert to Library Module** confirmation window, click **Yes**.

After the conversion is done, you may find that there are some TrueChange errors in the converted module that need to be fixed before being able to publish the module.

If after the conversion you have no TrueChange errors, you can publish the converted module immediately.
