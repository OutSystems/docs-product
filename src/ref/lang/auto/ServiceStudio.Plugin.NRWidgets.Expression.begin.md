---
summary: Reference information on the Expression widget for displaying a text literal or an expression to calculate at runtime on the screen.
tags: outsystems-designing-screens; reference; designing-screens; expression
---

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

The expression widget shows text or result of an expression at runtime. It's similar to the **print** command in other programming languages. To use the expression widget:

1. Search for **expression** in the widget toolbar and drag the widget to a screen, block or placeholder. The expression editor opens.

    ![Expression widget](images/expression-widget-ss.png?width=400)

1. Enter an expression in the expression editor and click **Done**.

    ![An expression in the expression editor](images/expression-editor-ss.png?width=600)
    
    You can use one of these examples as the expression:
   
    * `"Hello, world!"`
    * `"1 + 2 = " + (1 + 2)`
    * `"The square root of 3 is " + Sqrt(3)`
    * `"Today is " + CurrDate() + "!" `
    * `ToUpper("this is text in uppercase")`


1. Publish the app and open the screen.

    Here is what you get if you use one of the examples in the previous step:

    * **Hello, world!**
    * **1 + 2 = 3**
    * **The square root of 3 is 1.73205080756887729352744634151**
    * **Today is (current date)!**, where **(current date)** depends on your server. 
    * **THIS IS TEXT IN UPPERCASE**


