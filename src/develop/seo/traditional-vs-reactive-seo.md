---
summary: The SEO behavior between Reactive and Traditional Web apps is broadly similar, with the exception of module aliases which are not supported for Reactive web apps but can be achieved through site rules instead.
tags: runtime-traditionalweb
locale: en-us
guid: 74EB0BCA-31AD-4EA8-8892-6FA2A2011664
app_type: traditional web apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=3328:27065
---

# SEO for OutSystems Reactive Web apps vs Traditional Web apps

The SEO behavior between Reactive and Traditional Web apps is broadly similar, with the exception of module aliases which are not supported for Reactive web apps but can be achieved through site rules instead.

For site and redirect rules, the setup process is the same between app types. You can set this process up in the SEO URLs section of Service Center. Page rules are only configurable through Service Center for Traditional Web apps. 

![Screenshot showing the SEO page rules configuration in the Service Center for Traditional Web apps](images/page-rules-sc.png "SEO Page Rules in Service Center")

For Reactive Web apps, you can configure page rules in Service Studio by selecting the screen and setting the **Custom URL** properties **Advanced** properties section.

![Screenshot of the Custom URL properties in Service Studio for configuring page rules in Reactive Web apps](images/custom-url-ss.png "Custom URL Configuration in Service Studio")
