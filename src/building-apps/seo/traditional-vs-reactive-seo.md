---
summary: Explore SEO configurations for OutSystems 11 (O11) Reactive and Traditional Web apps, detailing differences in module aliases and page rules setups.
tags: seo, service center, custom url, configuration, service studio
locale: en-us
guid: 74EB0BCA-31AD-4EA8-8892-6FA2A2011664
app_type: traditional web apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=3328:27065
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - understand
---

# SEO for OutSystems Reactive Web apps vs Traditional Web apps

The SEO behavior between Reactive and Traditional Web apps is broadly similar, with the exception of module aliases, which are not supported for Reactive web apps but a similar behavior can be achieved through site rules instead.

<div class="info" markdown="1">

Site rules are not functionally equivalent to module aliases, which define alternative names for individual modules in URLs. For more details, see [Site Rules](seo-friendly-url-reactive.md/#site-rules).

</div>

For site and redirect rules, the setup process is the same between app types. You can set this process up in the SEO URLs section of Service Center. Page rules are only configurable through Service Center for Traditional Web apps.

![Screenshot showing the SEO page rules configuration in the Service Center for Traditional Web apps](images/page-rules-sc.png "SEO Page Rules in Service Center")

For Reactive Web apps, you can configure page rules in Service Studio by selecting the screen and setting the **Custom URL** properties **Advanced** properties section.

![Screenshot of the Custom URL properties in Service Studio for configuring page rules in Reactive Web apps](images/custom-url-ss.png "Custom URL Configuration in Service Studio")
