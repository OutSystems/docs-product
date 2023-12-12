---
summary: This article guides how you can refactor systems roles in O11 for compatiblity with ODC. 
locale: en-us
guid: 32736715-a9d2-4d94-9b20-47cc6039cbe8
app_type: traditional web apps, mobile apps, reactive web appsc
platform-version: o11
figma: 
---

# Refactor anonymous and registered roles 

You can use [roles](../../../develop/security/user-roles/intro.md) to restrict or allow end users to access specific screens and operations of your application. O11 provides the [anonymous and registered](../../../develop/security/user-roles/intro.md#system-roles-and-custom-roles) system roles.  

In ODC, you don't have the **anonymous** and **registered** system roles. Hence, you must remove these roles from screens and logic and replace them with app roles.
