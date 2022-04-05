---
summary: Check the causes and recomendations on how to solve the different Invalid Theme TrueChange warnings.
tags:
---

# Invalid Theme Warning

## The 'Layout' layout of the &lt;theme_name> theme must have placeholders named 'Title' and 'MainContent'.

**Cause**

You tried to set a Web Block as a layout of a theme without having the two placeholders named 'Title' and 'MainContent'.

**Recommended action**

Change the [Web Block](../../../ref/lang/auto/Class.Web%20Block.final.md) to have the 'Title' and 'MainContent' placeholders, or change the [Theme](../../../develop/ui/look-feel/themes.md) Layout property to use a Web Block that already has these placeholders.

## The &lt;Info Balloon/Pop-up Editor/Email> layout of &lt;theme_name> theme must have a placeholder named 'MainContent'.

**Cause**

You tried to set a Web Block as Info Balloon, Pop-up Editor, or Email layout of a theme without that Web Block having a placeholder named 'MainContent'.

**Recommended action**

Change the [Web Block](../../../ref/lang/auto/Class.Web%20Block.final.md) to have the 'MainContent' placeholder, or change the [Theme](../../../develop/ui/look-feel/themes.md) to use a Web Block that already has this placeholder.

## The &lt;web block> is not a valid theme Menu.

**Cause**

You tried to set a Web Block as Menu layout of a theme, however, the Web Block must comply with the requirements outlined for themes.

**Recommended action**

Edit the [Web Block](../../../ref/lang/auto/Class.Web%20Block.final.md) and design it to comply with the requirements of a Menu Layout of a [theme](../../../develop/ui/look-feel/themes.md#blocks) or choose another Web Block. Refer to the existing themes to check the necessary input parameters and entities that should be used in a Menu Web Block.
