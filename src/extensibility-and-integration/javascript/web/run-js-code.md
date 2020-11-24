---
summary: Learn how to define and run JavaScript code in your web application.
tags: runtime-traditionalweb
---

# Define and Run JavaScript Code

## How to Define JavaScript Functions

To add or edit the JavaScript functions of your elements, open the JavaScript editor by clicking **...** (ellipsis) on the **JavaScript** property of the element:

![](images/run-js-code-4.png)

The example below shows a JavaScript function defined locally for a Web Screen:

![](images/run-js-code-2.png)

## How to run JavaScript code

You can run JavaScript code in your web application in the following ways:

* Using the Extended Properties of Web Screens or widgets
* Within unescaped Expressions
* Using the [RunJavaScript](../../../ref/apis/auto/httprequesthandler-api.final.md#RunJavaScript) action of the HTTPRequestHandler API

In all the cases, the JavaScript code runs in the context of the browser.

### Extended Properties example

The example below shows a JavaScript function invoked when the `onclick` event occurs in a button:

![](images/run-js-code-1.png)

Since the value of an Extended Property is an expression, you can also type the JavaScript source code directly in the **Extended Property** value:

![](images/run-js-code-6.png)

### Unescaped Expressions example

You can use unescaped Expressions to add JavaScript at a specific point of your Web Screen, setting the **Escape Content** property to **No**:

![](images/run-js-code-7.png)

![](images/run-js-code-5.png)

### RunJavaScript action example

In your Action Flows, either in a Screen Action or a Server Action, you can use the **RunJavaScript** action of the **HTTPRequestHandler** extension to get your JavaScript code to run in the context of the browser:

![](images/run-js-code-3.png)
