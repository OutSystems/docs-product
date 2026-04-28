---
summary: OutSystems 11 (O11) features a Credentials tab for defining or resetting the Platform Server admin user's password.
locale: en-us
guid: 065a2e85-acf4-4895-87fd-5f176f406932
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3301-130&p=f&t=YWpNVSB3J2vcO8FT-0
tags: security, password management, configuration management, platform administration, system settings
audience:
  - Platform administrator
outsystems-tools:
  - platform server
coverage-type:
  - remember
isautopublish: true
---

# Credentials tab

The **Credentials** tab allows you to define or reset the password of the Platform Server admin user.

![Screenshot of the Credentials tab in the Configuration Tool](images/credentials-tab-ct.png "Credentials tab")

## Platform server administrator section

Define the password for the admin user of Platform Server in the **Password** and **Confirm Password** fields.

The values of the two fields must match and they must fulfill the password rules outlined in Configuration Tool's user interface.

After pressing **Apply and Exit**, the Configuration Tool updates the password in the database.
