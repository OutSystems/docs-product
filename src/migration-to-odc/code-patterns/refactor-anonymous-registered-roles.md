---
summary: This article guides how you can refactor systems roles in O11 for compatiblity with ODC. 
locale: en-us
guid: 32736715-a9d2-4d94-9b20-47cc6039cbe8
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Refactor anonymous and registered roles

You can use [roles](../../user-management/user-roles/intro.md) to restrict or allow end users to access specific screens and operations of your application. O11 provides the [anonymous and registered](../../user-management/user-roles/intro.md#system-roles-and-custom-roles) system role to restrict or allow end users to access specific screens and operations of your application. If you use anonymous role in a screen then the screen can be accessed by everyone including users that aren't logged in (non-authenticated users). However, if you use registered role in a screen, only authenticated logged in users can access the screen. 

In ODC, you don't have the **anonymous** and **registered** system roles. Hence, you must remove these roles from screens and logic and replace them with the corresponding app roles.
