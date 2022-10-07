---
summary: You need a Screen Template compatible with your Theme to display the final page properly.
locale: en-us
guid: 40469935-043c-4248-b54d-61e119ee9b2b
app_type: traditional web apps, mobile apps, reactive web apps
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

## Traditional Web Apps

If you're using one of the Traditional Web App Templates inherited from **OutSystems 10** (Lisbon, Dublin, Liverpool, Vanilla, and Website) or the London Theme based Application Template, Web Application:

* [Migrate your web application to OutSystems UI Web framework](<https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/Migrating_UI_of_the_Silk_Web_applications_to_OutSystems_UI_Framework>). The [default Screen Templates](<https://www.outsystems.com/outsystems-ui/screens/>) that come bundled with OutSystems 11 aren't compatible with the Silk UI nor with the London Theme.
* [Create your Screen Templates](<../screen-templates-create/intro.md>) and use your (custom) Theme as the base.
