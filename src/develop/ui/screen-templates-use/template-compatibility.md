---
summary: You need a Screen Template compatible with your Theme to display the final page properly.
---

# Theme compatibility in Screen Templates

<a id="helpid-30171"></a>

When working with Screen Templates you may see the following warning message: **The Themes are not compatible. The final Screen may look different than the preview. To use this Screen Template, you need a module with a Theme based on (module name)\(theme name).** This means that your module and Screen Template are not compatible, which may cause the final page not to display correctly.

If you are using one of the [built-in Application Templates](<../../application-templates/intro.md>):

* Select a compatible Screen Template. The Screen Templates that come with Service Studio are compatible with the built-in Application Templates.
* [Create your Screen Templates](<../screen-templates-create/intro.md>) and use your (custom) Theme as the base.

If the Screen Template was compatible with your module, but now it's not:
 
* Revert the changes you did to the module Theme. 
* Check if you set the correct Theme in the **Default Theme** property field of your module or UI Flow.

![Theme Compatibility warning](images/template-layout-theme-mismatch.png)
