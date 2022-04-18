---
locale: en-us
guid: dcd74051-5eb0-49fd-af03-3a2553dc978e
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid Resource Error

Message
:   `Resource '<file>' is empty and cannot be stored in the Binaries directory in the Platform Server.`

Cause
:   The `<file>` is empty and therefore cannot be copied to the `Binaries` folder in the Platform Server. See [Resource Editor](<../../integration-studio/editor/resource.md>)
    
Recommendation    
:   You should [verify](<../../../extensibility-and-integration/integration-studio/extension-life-cycle/extension-verify.md>) your extension again in order to generate the DLL or JAR correctly.
