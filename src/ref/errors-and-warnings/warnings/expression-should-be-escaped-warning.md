---
locale: en-us
guid: 69801bb7-6818-4061-acb2-4ee403966040
---

# Expression Should Be Escaped Warning

Message
:   `The expression contains '<script>'. Consider setting the 'Escape Content' property to 'No' or the expression will be displayed as text`

Cause
:   Your expression contains an HTML tag, so it is probable that you want to render the expression as HTML instead of text.

Recommendation
:   Change the 'Escape Content' of the expression property to 'No' to render the expression as HTML, or leave it as 'Yes' if you want to display the expression as text.
