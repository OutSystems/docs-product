---
summary: OutSystems 11 (O11) displays warnings when an extension lacks actions, resulting in no .NET source code to update or compile.
locale: en-us
guid: 0131cdff-f588-45e9-8b7a-720cb79a2399
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: extension development, error handling, development best practices, .net integration, outsystems ide
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - integration studio
coverage-type:
  - unblock
---

# Source Code Expected Warning

Message
:   `The Extension has no .NET source code to update.`
  
Cause
:   Your extension has no [actions](<../../../integration-with-systems/integration-studio/managing-extensions/action-define.md>) associated with it and therefore there is no source code to update.

---

Message
:   `The Extension has no source code to compile.`

Cause
:   Your extension has no [actions](<../../../integration-with-systems/integration-studio/managing-extensions/action-define.md>) associated with it and therefore there is no source code to compile.

---

Message
:   `The Extension has no .NET source code to compile.`

Cause
:   Your extension has no [actions](<../../../integration-with-systems/integration-studio/managing-extensions/action-define.md>) associated with it and therefore there is no source code to compile.