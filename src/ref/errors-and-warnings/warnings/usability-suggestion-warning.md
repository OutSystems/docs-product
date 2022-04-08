---
locale: en-us
guid: 8df1dab2-62e4-4d27-aa62-05c7a2fe8612
---

# Usability Suggestion Warning

Message
:   `If the actual message has more than 160 characters, 'Phone Slot' will be ignored`

Cause
:   You have a Send Message element in your module in which the maximum length is bigger than 160 characters and with a Phone Slot specified. In this situation if the size of the message is bigger than 160 characters at runtime, the message will be sent to the default Phone Slot and the one you specified is ignored.

Recommendation
:   Edit the Send Message element and set the Phone Slot property to the Default value.

---

Message
:   `There are no widgets on ‘<screen>’ submitting inputs to the server. The user inputs will be ignored.`

Cause
:   You have a Screen or a Block that contains input widgets to gather and that information is not being submitted to the server.

Recommendation
:   In order to send data from input widgets to the server, edit the screen or block and do one of the following:

    * Add or edit a Button/Link and set the Method property to 'Submit' or 'Ajax Submit'. Then, use a Screen Action associated with the Button/Link to send inputs to the server;
    * Add or edit a widget with Ajax capabilities and create a new Screen Action associated in the Ajax event of the widget. Design the Screen Action logic to send inputs to the server.

---

Message
:   `<EditableTable> editable table should have at least one action for either On Row Save or On Row Delete events, otherwise user inputs will be ignored.`

Cause
:   You have an Editable Table widget to gather data on a Screen or Block and neither the Save nor the Delete events have a screen action.

Recommendation
:   To send end user inputs back to the server add a new Screen Action to the screen or block that implements the logic of the Save or Delete events. Associate the screen action with the corresponding event on the Editable Table widget.
