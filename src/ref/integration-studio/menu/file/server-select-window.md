---
locale: en-us
guid: 99378b9c-3cd1-4b75-a0d0-189ad54153a1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3090-2&t=KPNGTaQL5AdMrozR-1
summary: Explore server connection options in OutSystems 11 (O11) using the Select Server window for efficient platform integration.
tags: server connection, platform integration, user authentication, outsystems ide, configuration management
audience:
  - full stack developers
  - frontend developers
  - backend developers
  - platform administrators
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - remember
---

# Select Server Window

The Select Server... window ![Animated GIF showing the process of connecting to a Platform Server using the Select Server window](images/connect-server-icon.png "Select Server Window") allows you to [connect to a specific Platform Server](<../../../../integration-with-systems/integration-studio/extension-life-cycle/server-connect.md>). This window is launched automatically whenever necessary, or you can explicitly invoke it in the File menu or in the Toolbar.

The parameters of the Select Server... window are presented below.

Host name
:   Name or IP address of the machine where the Platform Server is running. You can type the host name or select the host name from a drop-down list that displays all the host names that you have used so far.

User name
:   Name of an existing user in the Platform Server, as specified above.

Password
:   Password of the user. The value you insert is always displayed as `****`.

If you are not a user of the Platform Server you have specified, request user rights from the Service Center administrator.
