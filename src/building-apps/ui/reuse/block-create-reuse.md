---
summary: Display the same content on several screens by developing reusable Blocks.
tags: support-application_development; support-Front_end_Development; support-Mobile_Apps; support-webapps
locale: en-us
guid: 6cd79d30-4d78-4fd5-8707-b4af2cbd5078
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=201:2
---

# Create and Reuse Screen Blocks

Use Blocks to reuse parts of UI across your apps. With Blocks you can have part of the UI in one place, so changes to the Blocks are automatically visible in all Screens that use it.

Here are notes about reusing Block across **different apps**:

* Blocks must be public.
* You can reuse Reactive Web Blocks in Reactive Web Apps and Mobile Apps.
* You can reuse Traditional Web Blocks in Traditional Web Apps.
* To reuse it, go to **Manage Dependencies** and search producers for our app or library.

## Using Blocks

1. In a UI Flow, add a Block (in Reactive Web and Mobile Apps) or a Web Block (in Traditional Web Apps).
1. Implement the user interface and logic in the new Block.
1. Set the Block as public if you want to reuse it across apps.
1. Drag it the Block to the Screen where you want to use it. If you want to use the Block in another App, you first need to reference the Block.

### Advanced use cases to pass data between blocks

For more advanced use cases to pass data between blocks and using block events, please get more info on [Pass Data Between Blocks](block-communicate.md). This article explains how to create a block that communicate between them and pass data. For example, a block containing a date picker that, when changed, requires updating a chart plotted by another block.

## Example

Here is an example, with two sample apps, of how you can reuse a Block from Reactive Web App in a Mobile App.

**Create MyReactiveApp and a public Block in it:**

1. Create a new Reactive Web App, and add a default Module to it.
1. In the Module, go to **Interface** > **UI Flows** > right-click **MainFlow** > select **Add Block**. Name the Block **MyBlock**.
1. Set the **Public** property of Block to **Yes**.
1. Add some content to the Block. In our example we dragged a Text Widget and entered sample text "Hello from My Reactive App!".

    ![Screenshot of the source Reactive Web App with a public Block named MyBlock containing the text 'Hello from My Reactive App!'](images/block-reuse-source-app.png "Source App with Public Block")

1. Publish the app.

**Reuse the Block in MyPhoneApp:**

1. Create a new Mobile App and add a default Module to it.
1. Add a Screen to the app.
1. Open **Manage Dependencies** (CTRL+Q) and search producers for our app "MyReactiveApp". Select the app.
1. In left pane navigate to **UI Flows** > **Main Flow** > select **MyBlock**. Click **Apply** to confirm and close.

    ![Screenshot of the Manage Dependencies dialog in OutSystems showing the selection of MyBlock from the MyReactiveApp](images/block-reuse-manage-dependencies.png "Manage Dependencies Dialog")

1. In the Mobile App, navigate to **Interface** > **MyReactiveApp** (name of our example app) > **MainFlow2** > **MyBlock**.
1. Drag MyBlock to the Screen. You should see "Hello from My Reactive App!" in the preview.

    ![Screenshot showing the preview of MyBlock from MyReactiveApp in the Mobile App's screen with the text 'Hello from My Reactive App!'](images/block-reuse-target-app.png "Block Preview in Target App")

1. Publish the app.
