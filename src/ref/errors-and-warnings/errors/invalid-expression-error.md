# Invalid Expression Error

The `Invalid Expression` error is issued in the following situations:

* `Division by '0' (zero)`
  
    You are trying to divide by 0.

    Fix the expression that has this division by 0.

* `Non-terminated 'Text' literal`
  
    You are not handling a Text literal properly.

    Fix this Text literal in your expression.

* `Can't identify '<element>' element in expression.`
  
    Service Studio cannot identify the [operand element](../../logic/expressions/operands.md) in the expression.

    Depending on the type of operand element, do one of the following:

    * If you are referencing an element, make sure that the element is in the scope of the current expression and that you entered the element correctly. In the Expression Editor, use the Scope Tree to insert the element.

        ![](images/invalid-expression-01.png?width=400)

    * If you are writing a literal value in your expression make sure to use the correct format:
    
        Text
        :   Wrap the literal in quotation marks ("). For example `"Amazing text"`.

        Date, Time or Date Time
        :   Wrap the literal in number signs (#). For example `#1999-01-20#`.

        Decimal
        :   Use a period (.) to separate the integer and decimal parts. For example `10.1`.

* `Syntax error caused by unexpected '<element>' element in expression.`
  
    The expression has a syntax error right before the unexpected element.
    This means that Service Studio cannot understand the structure of the expression and how the unexpected element relates with the preceding element.
    
    Check out the following examples of patterns that cause syntax errors and how to solve them:
    
    * Missing an operator  
    Incorrect: `1 2`   
    Correct:  `1 + 2`

    * Missing a dot (.) between an element and a property  
    Incorrect: `User Id`  
    Correct: `User.Id`

    * Starting an expression with an operator or connector  
    Incorrect: `+ 2`  
    Correct: `1 + 2`

* `Expecting <element> instead of <element>`
  
    The syntax of the expression is not correct. For example, if you do not end a function call properly, with a right-parenthesis: `MyFunction(3, 'Sweet'`.

    Check your expression to validate its operands, operators, and variables.

* `Parameter '<parameter>' in function '<function>' is mandatory and must be specified`
  
    You are invoking a function with no argument for a mandatory parameter.

    Check the Built-in function or the User function definition, to validate which input parameters are mandatory.

* `Too many arguments specified for function '<function>'`
  
    You have mapped more arguments in the function you're using than the number of parameters that it actually has. Or, you're using at least one named parameter that _advanced_ the position of the corresponding argument, so the continuous arguments exceed the available number of parameters in the function.

    Check the Built-in function or the User function definition to validate its arguments and the function calls syntax.

* `Too many levels of nested function calls`
  
    You are invoking functions within function arguments successively, exceeding the maximum number of levels (20) of nesting that is allowed.

    Replace some of the function calls by Variables where their value has been previously assigned invoking the necessary function, in the action flow.

* `Unexpected argument named '<parameter>' in function '<function>' call`
  
    The syntax of the expression is correct, but it has an argument for a parameter that does not exist in your function. Probably you've deleted this parameter from the function and have not "clean up" your expression yet.

    Check the Built-in function or the User function definition, to validate its arguments. In case you've actually deleted a parameter, fix the expression errors. Right-click the error line to see the fixing suggestions OutSystems provides you for this error:
    
    * `Create <function> Input Parameter`: Creates the argument in the `<function>`.
    * `Delete Argument`: Deletes the argument from the current call to `<function>`.
    * `Delete All Similar Arguments`: Deletes the argument from all calls to `<function>`

* `Argument named '<parameter>' was specified more than once in function '<function>' call`
  
    You have more than one argument in the function call to the same parameter.

    Check whether you're using the same name more than once or if you already mapped the argument by position and then used its name again in the call.

* `'<function>' function cannot be executed in the database, so it can't receive any attributes from the aggregate as parameter`
  
    You are using a user-function or built-in function that does not exist in the database.

    Change the function to use a parameter from outside the aggregate.

Double-click on the error line to take you directly to the invalid expression.
