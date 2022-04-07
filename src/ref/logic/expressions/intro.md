---
summary: An expression is composed of operands and operators. Edit the expression in the expression editor or inline. Show the value of the expression in the expression widget. 
tags: 
locale: en-us
guid: 7d9ef917-ff30-4562-a5c6-9a21bd4318d8
---

# Expressions

An expression consists of operands and operators, or just one operand. For example, **n + 1** is an expression with two operands, **n** and **1**, joined by the addition operator +. 

If you are creating an expression and encounter errors, check [here](../../../ref/errors-and-warnings/errors/invalid-expression-error.md) for the causes and the actions you can take to resolve them. 

Here is how you can edit expressions and show the expression values.

* Use the [expression editor](../../../develop/logic/expression-editor.md) to **edit expressions**. The expression editor shows you available elements. It automatically completes the text and shows suggestions after you press **Ctrl+Space**.

    ![Expression editor](images/expression-editor-ss.png?width=600)

* **Edit expressions** inline in the properties of elements.

    ![Expression inline](images/expression-inline-ss.png?width=400)

* To **show the result** of an expression, use the [expression widget](../../lang/auto/ServiceStudio.Plugin.NRWidgets.Expression.final.md). This is similar to the **print** command in other programming languages.

    ![Expression widget](images/expression-widget-ss.png?width=400)

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

## Notes

Here are some tips for using expressions.

* You can use  many functions to manipulate the type Text, however, you can only use the  **+** (addition) operand with type Text. 

    Example: `"Hello, " + UserName`, where the value of **UserName** is **Billy**, returns `"Hello, Billy!"`. 

* You can use the [built-in functions](<../../lang/auto/builtinfunction.Date and Time.final.md>) to perform various operations on the types **Date**, **Time**, and **DateTime**.

    Example: `AddDays(#2020-01-01 00:00:00#, 90)`. **AddDays** is a function that adds **n** days to a Date Time value. Date Time is here a literal `#2020-01-01 00:00:00#`. The expression returns `#2020-03-31 00:00:00#`.

* You can only use the operators **=** and **&lt;&gt;** (equality operators) for the type `Record`.

* For the type **Identifier**, use the [built-in functions](<../../lang/auto/builtinfunction.Data Conversion.final.md>). 

* The types **BinaryData** and **Record List** don't support calculations.
