---
locale: en-us
guid: 6a94d155-a80f-423c-95c5-5267e603a46d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Potential Loop at Runtime Warning

<a id="helpid-30144"></a>

Message
:   `'<OnRender action>' changes the <Screen | Block>'s data, which triggers the on render event again. To avoid infinite rendering loops, don't change screen or block data in '<OnRender action>'.`

Cause
:   The OnRender event occurs every time the screen or block data changes. If you change the screen or block data inside the OnRender action, you will trigger the OnRender action again, causing an infinite loop.

Recommendation
:   Don't change screen or block data in the [OnRender](<../../../develop/logic/screen-block-lifecycle-events.md#on-render>) action.

---

<a id="helpid-30145"></a>

Message
:   `Refreshing '<Aggregate | Data Action>' in '<OnAfterFetch action>' triggers the on after fetch event again. To avoid an infinite loop, remove the refresh of '<Aggregate | Data Action>' from '<OnAfterFetch action>'.`

Cause
:   The OnAfterFetch action of an Aggregate or Data Action runs right after it finishes fetching data. If you refresh the Aggregate or Data Action inside its own OnAfterFetch action, it will start fetching data again and run the OnAfterFetch action afterwards, causing an infinite loop.

Recommendation
:   Remove the Aggregate or Data Action refresh from its own [OnAfterFetch](<../../../develop/logic/screen-block-lifecycle-events.md#on-after-fetch>) action.
