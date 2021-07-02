---
summary: Check the causes and recomendations on how to solve the different Invalid Expression TrueChange errors
tags:
en_title:
---

# Invalid Expression Error

The Invalid Expression Error is issued when you use an Expression widget. Check [here](../../../ref/logic/expressions/intro.md) for best practices for expressions.

Double-click on the error line in TrueChange to take you directly to the expression that is issuing the error.

## Division by '0' (zero)

**Cause**

Your are trying to divide by 0 in a numeric expression, and this is not possible.

**Recommended action**

Update the [expression](../../../develop/logic/expression-editor.md) to remove the [division](../../logic/expressions/operators.md) by 0.

## Non-terminated 'Text' literal
  
**Cause**

You have not used the correct format for the termination of a Text literal in your expression.

**Recommended action**

Update the [Text literal](../../logic/expressions/operands.md) to the correct termination format in your [expression](../../../develop/logic/expression-editor.md). For example, wrap the literal in quotation marks ("), such as `"Amazing text"`.

## Can't identify &lt;element> element in expression.

**Cause**

Service Studio cannot identify the operand element in the expression.

**Recommended action**

Depending on the type of [operand element](../../logic/expressions/operands.md), do one of the following:

* If you are referencing an element, make sure that the element is in the scope of the current expression and that you entered the element correctly. In the [Expression Editor](../../../develop/logic/expression-editor.md), use the Scope Tree to insert the element.

    ![](images/invalid-expression-01.png?width=400)

* If you are writing a literal value in the expression, ensure you use the correct format:
    
    Text
    :   Wrap the literal in quotation marks ("). For example `"Amazing text"`.

    Date, Time or Date Time
    :   Wrap the literal in number signs (#). For example `#1999-01-20#`.

    Decimal
    :   Use a period (.) to separate the integer and decimal parts. For example `10.1`.

## Syntax error caused by unexpected &lt;element> element in expression.

**Cause**

The expression has a syntax error before the unexpected element.

Service Studio cannot determine the structure of the expression and how the unexpected element relates to the preceding element.

**Recommended action**

Check out the following examples that cause syntax errors in [expressions](../../../ref/logic/expressions/intro.md) and how to solve them:
    
* Missing an operator:  
    Incorrect: `1 2`   
    Correct:  `1 + 2`

* Missing a dot (.) between an element and a property:  
    Incorrect: `User Id`  
    Correct: `User.Id`

* Starting an expression with an operator or connector:  
    Incorrect: `+ 2`  
    Correct: `1 + 2`

* Missing the number sign in a date, time, or date time literal:  
    Incorrect: `1999-01-20#`  
    Correct: `#1999-01-20#`

* Missing the period (.) to separate the integer and decimal parts:  
    Incorrect: `10 1`  
    Correct: `10.1`

## Expecting &lt;element> instead of &lt;element>

**Cause**

The syntax of the expression is not correct. For example, if you end a function call without a right parenthesis, such as `MyFunction(3, 'Sweet'`, the syntax will not be correct.

**Recommended action**

Check your [expression](../../../develop/logic/expression-editor.md) to validate its [operands](../../logic/expressions/operands.md), [operators](../../logic/expressions/operators.md), and [variables](../../../ref/data/handling-data/variables/intro.md).

## Parameter &lt;parameter> in function &lt;function> is mandatory and must be specified

**Cause**

You are invoking a function with no argument for a mandatory parameter.

**Recommended action**

Check the [Built-in function](../../../ref/lang/auto/builtinfunctions.final.md) or the User function definition to validate which [input parameters](../../../ref/lang/auto/Class.Input%20Parameter.final.md) are mandatory.

## Too many arguments specified for function &lt;function>
  
**Cause**

You have mapped more arguments in the function you're using than the number of parameters that it has. Or, you're using at least one named [parameter](../../../ref/lang/auto/Class.Input%20Parameter.final.md) that _advanced_ the position of the corresponding argument, so the continuous arguments exceed the available number of parameters in the function.

**Recommended action**

Check the [Built-in function](../../../ref/lang/auto/builtinfunctions.final.md) or the User function definition to validate its arguments and the function calls syntax.

## Too many levels of nested function calls

**Cause**

You are invoking functions within function arguments successively, which exceeds the maximum number of levels (20) of nesting that is allowed.

**Recommended action**

Replace some of the function calls by [variables](../../../ref/data/handling-data/variables/intro.md) whose value has been previously assigned to invoke the necessary function in the Action flow.

## Unexpected argument named &lt;parameter> in function &lt;function> call

**Cause**

The syntax of the expression is correct, but it has an argument for a parameter that does not exist in your function. You may have deleted this parameter from the function and not updated your expression yet.

**Recommended action**

Check the [Built-in function](../../../ref/lang/auto/builtinfunctions.final.md) or the User function definition to validate its arguments. 

If you deleted a [parameter](../../../ref/lang/auto/Class.Input%20Parameter.final.md), update the [expression](../../../develop/logic/expression-editor.md) to remove the errors. Right-click the error line to see the fixing suggestions OutSystems provides you for this error:
    
* `Create <function> Input Parameter`  
    Creates the argument in the function.
* `Delete Argument`  
    Deletes the argument from the current call to the function.
* `Delete All Similar Arguments`  
    Deletes the argument from all calls to the function.

## Argument named &lt;parameter> was specified more than once in function &lt;function> call
  
**Cause**

You have more than one argument in the function call to the same [parameter](../../../ref/lang/auto/Class.Input%20Parameter.final.md).

**Recommended action**

Check whether you're using the same name more than once or if you already mapped the argument by position and then used its name again in the call.

## &lt;function> function cannot be executed in the database, so it can't receive any attributes from the aggregate as parameter

**Cause**

You are using a User function or [Built-in function](../../../ref/lang/auto/builtinfunctions.final.md) that does not exist in the database.

**Recommended action**

Change the function to use a [parameter](../../../ref/lang/auto/Class.Input%20Parameter.final.md) from outside the [Aggregate](../../../ref/lang/auto/Class.Aggregate.final.md).

## Cannot apply &lt;operator_name> operator to Integer together with Integer
<!-- mm added  -->

**Cause**

You are using an operator in the expression that is not compatible with integers, for example 'and'.

**Recommended action**

Update a valid [operator](../../logic/expressions/operators.md) for the integers in your expression.
