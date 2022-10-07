---
locale: en-us
guid: 509dbbc9-652c-44a5-b276-4df9cf8992fd
app_type: traditional web apps, mobile apps, reactive web apps
---

# Unexpected Link Warning

Message
:   `'Validation' should be set to '(none)' in links with 'Method' set to 'Navigate'`

Cause
:   You have a Link widget with the Method property set to 'Navigate' and the Validation property set to either 'Client & Server' or 'Server'. To validate the end user typed values, you have to submit them.

Recommendation
:   Edit your Link and set the Validation property to '(none)' or change the Method property to 'Submit'.

---

Message
:   `'<destination_screen>' should be either a Frequent Destination or the target of a connector from '<originator_screen>'.`

Cause
:   You have a Link/Button widget on screen `<originator_screen>` that are navigating to a `<destination_screen>` (in the Destination property). No connector exists from `<originator_screen>` to `<destination_screen>` and neither the `<destination_screen>` has its Is Freq.Destination  property set to 'Yes'.

Recommendation
:   Edit your web flow and connect the two screens or set the Is Freq.Destination property of the  `<destination_screen>` screen to Yes. If you were explicitly trying to disconnect the two screens, you must edit the Destination property in the `<originator_screen>` widget and select from the drop down list either '(none)' or a different destination.
