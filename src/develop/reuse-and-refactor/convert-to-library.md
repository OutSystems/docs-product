---
summary: How to convert an existing Mobile or Reactive module to a Library.
tags: runtime-mobileandreactiveweb
---

# Convert to Library

You can convert an existing **Mobile** or **Reactive** module to a Library. Note that there are specific constraints in Libraries that might imply some changes to the modules before the conversion can take place.

1. In the module that you wish to convert, open the **Module** menu and select **Convert** > **Convert to Library Module...**.

    <div class="info" markdown="1">

    If your module has elements that are not allowed in a Library module, the conversion stops and the elements not allowed are listed in an popup message. Remove the listed elements from your module, possibly moving them to a different module, and repeat step 1.  
    If your module has TrueChange errors, the conversion is stopped and an error message is shown. Fix the errors and repeat step 1.

    </div>

1. In the **Convert to Library Module** confirmation window, click **Yes**.

After the conversion is done, you may find that there are some TrueChange errors in the converted module that need to be fixed before being able to publish the module.

If after the conversion you have no TrueChange errors, you can publish the converted module immediately.
