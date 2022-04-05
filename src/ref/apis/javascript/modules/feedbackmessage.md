---
tags: runtime-mobileandreactiveweb
summary: Displays personalized feedback messages to the user.
---

# FeedbackMessage

Displays personalized feedback messages to the user.

## Summary

|Function|Description|
|---|---|
|[closeFeedbackMessage](feedbackmessage.md#closefeedbackmessage)|Closes the FeedbackMessage that is currently open.|
|[showFeedbackMessage](feedbackmessage.md#showfeedbackmessage)|Shows a FeedbackMessage with a specified message. You can enable HTML encoding, add CSS classes, and set the behavior on click.|

## Functions

### closeFeedbackMessage

**closeFeedbackMessage(): void**

Closes the FeedbackMessage that is currently open.

Returns: void

### showFeedbackMessage

**showFeedbackMessage(message: string, messageType: FeedbackMessageType, [encodeHTML: boolean = true], [extraCssClasses: string], [closeOnClick: boolean = true], [onClick: function]): void**

Shows a FeedbackMessage with a specified message. You can enable HTML encoding, add CSS classes, and set the behavior on click.

Example:

```javascript
// prevent feedback message's default close-on-click behavior
$public.FeedbackMessage.showFeedbackMessage("Your data has been submitted.", 1, true, "", false);
```

Parameters:

* **message**: string<br/> Message to be displayed.
* **messageType**: FeedbackMessageType<br/> Type of feedback message to show (0 = Info, 1 = Success, 2 = Warning or 3 = Error).
* (Default value) **encodeHTML**: boolean (default: true) <br/> Whether to escape HTML characters (default is `true` so the message is treated as text).
* (Optional) **extraCssClasses**: string<br/> Whitespace-separated class names to be added to the feedback message container to customize the appearance of the message.
* (Default value) **closeOnClick**: boolean (default: true) <br/> When `true`, indicates that the message box will be closed when the user clicks on it.
* (Optional) **onClick**: function<br/> Function to be executed whenever the feedback message is clicked.

Returns: void

