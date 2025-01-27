---
summary: Explore how OutSystems 11 (O11) handles missing file warnings during extension creation, merging, or saving processes.
locale: en-us
guid: 7b6384db-c1de-4732-a61f-e6afe49c9e3d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: error handling, extension management, resource management, file system integration, outsystems best practices
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - integration studio
coverage-type:
  - unblock
---

# Missing File Warning

Message
:   `The file '<file>' was not found on the file system.`
  
Cause
:   During the [creation of the extension](<../../../integration-with-systems/integration-studio/extension-life-cycle/extension-create.md>), [merge](<../../../integration-with-systems/integration-studio/extension-life-cycle/extension-update-source-code.md>) or save that file, which was previously added as a [resource](<../../integration-studio/resources-tree.md>), was not found.

Recommendation
:   Re-open the extension in order to recover the files in the file system.
