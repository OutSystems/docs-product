---
summary: OutSystems 11 (O11) encounters an "Invalid Resource Error" when an empty file cannot be stored in the Binaries directory.
locale: en-us
guid: dcd74051-5eb0-49fd-af03-3a2553dc978e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, outsystems platform, platform server, application deployment, extension verification
audience:
  - mobile developers
  - frontend developers
  - backend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - unblock
---

# Invalid Resource Error

Message
:   `Resource '<file>' is empty and cannot be stored in the Binaries directory in the Platform Server.`

Cause
:   The `<file>` is empty and therefore cannot be copied to the `Binaries` folder in the Platform Server. See [Resource Editor](<../../integration-studio/editor/resource.md>)

Recommendation
:   You should [verify](<../../../integration-with-systems/integration-studio/extension-life-cycle/extension-verify.md>) your extension again in order to generate the DLL or JAR correctly.
