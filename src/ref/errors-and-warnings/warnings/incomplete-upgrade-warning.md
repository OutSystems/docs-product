---
summary: Explore how to resolve incomplete upgrade warnings in OutSystems 11 (O11) by ensuring all modules are updated post-server upgrade.
tags: upgrade issues, deployment best practices, error resolution, server management, application lifecycle management
helpids: 30220
locale: en-us
guid: E5F5D75D-ABCE-4BAF-956E-30F5E6111B05
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - unblock
---

# Incomplete upgrade warning

Message
: Incomplete Upgrade Module `<module>` was deployed with an old OutSystems Platform Server version. Please publish `<module>` to fix it.

Cause
: After a Platform Server upgrade, you're publishing a module in Service Studio that consume other modules that weren't upgraded yet to the new version.

Recommendation
: Make sure that after upgrading the Platform Server, you [upgrade your apps](https://success.outsystems.com/Support/Enterprise_Customers/Upgrading/01_Upgrade_OutSystems_Platform#Step_3._Upgrade_applications_to_the_new_version) before proceeding with further development.
