---
locale: en-us
guid: eacad4d3-ae36-4f26-bb60-02ba575bf448
app_type: traditional web apps, mobile apps, reactive web apps
---

# Modified or Missing Reference Warning

Message
:   `'<element>' <type> is incompatible with '<Producer>' <module | extension> definition. Application runtime errors might occur`

Cause
:   Your module has a reference to an element that has been modified in the Producer (module or Extension) making both definitions incompatible.

Recommendation
:   You should refresh the modified reference or missing reference in order to avoid possible runtime errors.

---

Message
:   `'<element>' <type> was not found in the '<Producer>' <module | extension> definition. Application runtime errors might occur`

Cause
:   Your module has a reference to an element that has been removed in the Producer (module or Extension) making both definitions incompatible or this element is no longer public in the Producer.

Recommendation
:   You should remove the reference in order to avoid possible runtime errors.
