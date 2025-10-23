---
helpids: 30082
locale: en-us
guid: f6eaf671-e183-45ce-8034-d3e16656b3b2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?type=design&node-id=2836%3A3583&mode=design&t=Ix2yojgoXorQvo4C-1
summary: Explore how OutSystems 11 (O11) enhances code commenting with features like reminders and link embedding in the TrueChange™ tab.
tags: ide usage, reactive web apps, tutorials for beginners, code commenting, development best practices
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Comment

Comment is a tool that lets you add a text box with code comments for developers. Comments are handy when you need to add remarks or reminders for yourself or team members.

If you write **TODO**, **TBD**, or **REMINDER** in uppercase, the comment shows in the TrueChange&#8482; tab. You can also set **Is Reminder** of any comment to **Yes** to make it visible in the tab.

You can add links in comments by using the `a` HTML tag. For example: `This a <a href="https://www.example.com">link to a website</a>.`

![Comment tool interface in Service Studio](images/comment-tool-ss.png "Comment Tool Screenshot")

## Properties

|Name|Description|Mandatory|Default value|Observations|
|---|---|---|---|---|
|Text| Text to display. The HTML **a** tag is allowed.|Yes |"Write your comment here"| |
|Is Reminder|Set to Yes to have the comment displayed as a reminder in the TrueChange tab.|Yes|No|The upper-cased keywords TODO, TBD, and REMINDER automatically set the comment as a reminder. Removing such keywords won't set `Is Reminder` to `No`|
