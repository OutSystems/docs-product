---
summary: This article outlines how to refactor site properties in your O11 apps for compatibility with ODC.
locale: en-us
guid: 19d82c11-dc9a-43e8-bce1-1767e48e58fd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Refactor site properties to be ODC-compatible

[Site properties](../../../building-apps/data/site.md) are global variables with configurable values. They are used to implement configuration values for an application that can be set at runtime. Site properties can also store configurable variables such as API Key, Client ID, and Client Secret values. 

In ODC, you can use **Settings** to set configuration values for your application. These settings are always read-only at runtime. Therefore, you must change the logic if you are writing on any of the Site properties programmatically. You must create an entity to store configurations that can be changed at runtime.
