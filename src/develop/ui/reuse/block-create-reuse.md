---
summary: Display the same content on several screens by developing reusable Blocks.
tags: support-application_development; support-Front_end_Development; support-Mobile_Apps; support-webapps
locale: en-us
guid: 6cd79d30-4d78-4fd5-8707-b4af2cbd5078
app_type: traditional web apps, mobile apps, reactive web apps
---

# Create and Reuse Screen Blocks

Use Blocks to reuse parts of UI across your apps. With Blocks you can have part of the UI in one place, so changes to the Blocks are automatically visible in all Screens that use it.

Here are notes about reusing Block across **different apps**:

* Blocks must be public.
* You can reuse Reactive Web Blocks in Reactive Web Apps and Mobile Apps. 
* You can reuse Traditional Web Blocks in Traditional Web Apps.

## Using Blocks

1. In a UI Flow, add a Block (in Reactive Web and Mobile Apps) or a Web Block (in Traditional Web Apps). 
1. Implement the user interface and logic in the new Block.
1. Set the Block as public if you want to reuse it across apps.
1. Drag it the Block to the Screen where you want to use it. If you want to use the Block in another App, you first need to reference the Block.

## Example

Here is an example, with two sample apps, of how you can reuse a Block from Reactive Web App in a Mobile App.

**Create MyReactiveApp and a public Block in it:**

1. Create a new Reactive Web App, and add a default Module to it.
1. In the Module, go to **Interface** > **UI Flows** > right-click **MainFlow** > select **Add Block**. Name the Block **MyBlock**.
1. Set the **Public** property of Block to **Yes**.
1. Add some content to the Block. In our example we dragged a Text Widget and entered sample text "Hello from My Reactive App!".

    ![Source app with a public Block](<images/block-reuse-source-app.png?width=600>)

1. Publish the app.

**Reuse the Block in MyPhoneApp:**

1. Create a new Mobile App and add a default Module to it.
1. Add a Screen to the app.
1. Open **Manage Dependencies** (CTRL+Q) and search producers for our app "MyReactiveApp". Select the app.
1. In left pane navigate to **UI Flows** > **Main Flow** > select **MyBlock**. Click **Apply** to confirm and close.

    ![The Block in Manage Dependencies dialog](<images/block-reuse-manage-dependencies.png?width=600>)

1. In the Mobile App, navigate to **Interface** > **MyReactiveApp** (name of our example app) > **MainFlow2** > **MyBlock**.
1. Drag MyBlock to the Screen. You should see "Hello from My Reactive App!" in the preview.

    ![The source Block in the preview](<images/block-reuse-target-app.png?width=600>)

1. Publish the app.

