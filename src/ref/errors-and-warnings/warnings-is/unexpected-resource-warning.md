---
locale: en-us
guid: a718f5ab-fe6d-4f5f-b176-172ed90c9a0c
---

# Unexpected Resource Warning

Message
:   `The Resource <file> should not be included in the Extension.`

Cause
:   Issued when you [add a resource](<../../../extensibility-and-integration/integration-studio/managing-extensions/resource-define.md>) that starts with `OutSystemsHubEdition`, which is a reserved prefix.

Recommendation
:   Rename the resource filename, excluding the reserved prefix.

---

Message
:   `The Resource <file> has a reserved file name and therefore its Deploy Action will be ignored.`

Cause
:   Issued when you verify an extension that has a resource whose filename is a reserved filename, for example, `compressor` and `web.config`.

Recommendation
:   Rename the resource filename.
