---
summary: Add JavaScript code to a Traditional Web App to make it more dynamic, adding custom behavior to pages executed on the user's browser while minimizing the number of calls to the server.
tags: runtime-traditionalweb
locale: en-us
guid: ade87f50-8404-4392-88d0-e33397418fe9
app_type: traditional web apps
---

# Extend Your Traditional Web App Using JavaScript

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

You can add JavaScript code to Traditional Web Apps to make them more dynamic, adding custom behavior to pages executed on the user's browser while minimizing the number of calls to the server. You can use JavaScript code defined in your OutSystems app or in an external location.

Tools like [Ajax Refresh](<../../../ref/lang/auto/Class.Ajax Refresh.final.md>) already allow you to refresh parts of your screen in an action flow without forcing a page reload. However, you may want to define some custom behavior using JavaScript in your app, or use an existing JavaScript library to improve the user experience.

To run JavaScript code in your Traditional Web App do the following:

1. [**Add a JavaScript code block to one of the supported elements**](#add-js-code-block).  
    The following elements support JavaScript code blocks:

    * Module
    * Web Screen
    * Web Block

    Define large JavaScript code blocks in one of these elements. You can later invoke the code that you defined in this step. This way you can avoid having JavaScript code blocks in several places across your Web Screens and Web Blocks, and have a central place for JavaScript code in a given scope.

    When you deploy your app, OutSystems creates separate `.js` files for the JavaScript code defined at three levels: Module, Web Screen, and Web Block level.

    Each rendered HTML page (corresponding to a Screen in your Traditional Web App) includes these JavaScript files by adding `<script>` tags inside the `<head>` element of the page. This means that the browser interprets the JavaScript code **before** loading all the elements in the page.

    <div class="info" markdown="1">

    You can also [include JavaScript files hosted outside your OutSystems infrastructure](#external-js).

    </div>

1. [**Run JavaScript code**](#run-js-code).  
    You can run any JavaScript statement in a Web Screen or Web Block using one of the following methods:

    * Using the **Extended Properties** of Web Screens or widgets.
    * Using an unescaped **Expression**.
    * Using the [RunJavaScript](../../../ref/apis/auto/httprequesthandler-api.final.md#RunJavaScript) action of the HTTPRequestHandler API.

    Even though you can define the JavaScript code right before (or instead of) calling it, this is **not recommended** for code blocks with more than a few lines of JavaScript.  
    You should define JavaScript code blocks in one of the supported elements (see above) and then call it using one of these methods.

## 1. Add a JavaScript code block { #add-js-code-block }

Do the following:

1. In Service Studio, select the element in the element tree where you want to add or edit JavaScript code (must be a Module, a Web Screen, or a Web Block).

1. In the properties pane, click **...** (ellipsis) on the **JavaScript** property to open the JavaScript editor.

![Opening the JavaScript editor for a Web Screen](images/run-js-code-4-ss.png)

**Note:** You can also [include JavaScript files hosted outside your OutSystems infrastructure](#external-js).

**Example**

The example below shows a JavaScript function defined in the "ContactDetail" Web Screen:

![Example of a JS function defined for a Web Screen](images/run-js-code-2-ss.png)

## 2. Run JavaScript code { #run-js-code }

There are several possibilities for running JavaScript code in your Traditional Web App. Check the following sections for more information.

### Run JavaScript code using Extended Properties

You can invoke a JavaScript function when a given event occurs (for example, `onkeypress` or `onclick`) in a Web Screen or in a widget, like a Button or a Link.

1. In Service Studio, select the element where you want to invoke the JavaScript function when an event occurs.

1. In the "Extended Properties" property group, select the event on which you want to run JavaScript code in the **Property** property (without any quotes). For example, `onclick`.

1. In the **Value** property, enter the JavaScript statement you want to run (between double quotes).

**Example**

This example shows the properties of a Button configured to invoke the `AlertFieldMustBeFilled()` JavaScript function when the user clicks the button.

![Calling a JS function in Extended Properties](images/run-js-code-ext-properties-1-ss.png)

<div class="info" markdown="1">

**Note:** Since the value of an Extended Property is an expression, you can enter any JavaScript statement directly as the **Extended Property** value:

![Entering JS statements directly in Extended Properties](images/run-js-code-ext-properties-2-ss.png)

</div>

### Run JavaScript code using an unescaped Expression

You can use unescaped Expressions to include JavaScript statements at a specific location in your Web Screen or Web Block. The browser runs these JavaScript statements as soon as it evaluates the Expression element on the page.

1. In Service Studio, add an **Expression** element to your Web Screen or Web Block.

1. In the screen/block properties, enter the JavaScript code in **Value** property, between `<script></script>` tags.

    ![Expression Editor showing unescaped content](images/run-js-code-expression-editor-ss.png)

1. Set the **Escape Content** property to **No**.

![Expression set as having unescaped content](images/run-js-code-expression-ss.png)

### Run JavaScript code using the RunJavaScript action

In your action flows, either in a Screen Action or a Server Action, you can use the [RunJavaScript](../../../ref/apis/auto/httprequesthandler-api.final.md#RunJavaScript) action of the HTTPRequestHandler extension to get your JavaScript code to run in the context of the browser.

1. In Service Studio, add the **RunJavaScript** Server Action of the HTTPRequestHandler API as a dependency of your module. For more information, check [Reuse functionality from other modules](../../../develop/reuse-and-refactor/expose-and-reuse.md#reuse).

    ![Manage Dependencies window showing the RunJavaScript Server Action](images/run-js-code-runjavascript-ss.png)

1. In the flow of a Screen Action or Server Action, add a **Run Server Action** element and select the **RunJavaScript** Server Action.

1. Enter the JavaScript code you wish to run in the **Script** property of the **RunJavaScript** Server Action.

    ![Properties of the RunJavaScript Server Action element](images/run-js-code-runjavascript-props-ss.png)

<div class="info" markdown="1">

**Note:** If you're using the RunJavaScript action in a Screen Action that handles a click in a Button or in a Link, you must set the **Method** property of the Button/Link to **Ajax Submit**.

You must do this so that the current page doesn't get refreshed when clicking the Button/Link. This way, the JavaScript code defined in the RunJavaScript action runs in the context of the currently loaded page.

</div>

## Add and run a JavaScript file hosted elsewhere { #external-js }

Besides defining JavaScript code in one of the supported elements (Module, Web Screen, or Web Block) you can also reference an existing JavaScript file hosted elsewhere in a Screen of your Traditional Web App.

Do the following:

1. Get the full URL of the JavaScript file you wish to include in a Screen of your app. For example, `https://cdn.mycompany.com/js/util.js`.

1. In Service Studio, add the [AddJavaScriptTag](../../../ref/apis/auto/httprequesthandler-api.final.md#AddJavaScriptTag) Server Action of the HTTPRequestHandler API as a dependency of your module. For more information, check [Reuse functionality from other modules](../../../develop/reuse-and-refactor/expose-and-reuse.md#reuse).

1. In the **Preparation** of the Screen where you want to include the JavaScript code, add a call to the **AddJavaScriptTag** Server Action. Set the **JavaScriptURL** argument to the URL you previously identified.

    ![Call AddJavaScriptTag in Screen Preparation](images/javascript-addjavascripttag-flow-ss.png)
