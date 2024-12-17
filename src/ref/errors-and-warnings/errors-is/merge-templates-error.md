---
summary: Troubleshooting steps for a merging templates error in OutSystems 11 (O11) include checking permissions and disk space.
locale: en-us
guid: e57cbb8d-0e91-4934-8226-59778a5f4b13
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, troubleshooting, permission issues, disk space, system administration
audience:
  - platform administrators
  - full stack developers
outsystems-tools:
  - integration studio
coverage-type:
  - unblock
---

# Merge Templates Error

Message
:   `An error occurred while merging template with <error file>: <error detail>.`

Cause
:   During the [merging operation](<../../../integration-with-systems/integration-studio/extension-life-cycle/extension-update-source-code.md>), an internal error was detected.

Recommendation   
:   Check whether the extension source files have the necessary permissions; if your disk has available space; if the folder where the extension is being stored exists; launch the IDE (Integrated Development Environment) and build the solution in order to check the exact error. It could be, for example, an error in the formatting of these files. If the problem persists, contact your System Administrator to ask for help.
