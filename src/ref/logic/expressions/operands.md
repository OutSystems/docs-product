---
tags: 
---

# Operands

An operand expression can be a literal, any element available in the scope, or a sub-expression.

## Literal

A constant that you want to use in your expression. Literals can be strings, numbers, boolean values, etc.

## Element in Scope

Any element writable or not that is available in the current scope of your expression. These elements can be parameters of any kind, local variables, session variables, site properties, function calls and runtime properties.

### Function call

Service Studio provides some built-in functions. A built-in function always returns a value and can take zero or more parameters, separated by commas. See [Built-in Functions](<../../lang/auto/builtinfunctions.final.md>).

You can also call a User Function. A User Function also returns a value and can take zero or more parameters, separated by commas.

### Runtime properties

In Service Studio there are some elements that provide runtime properties, such as widgets and timers. These are properties that are instantiated at runtime.

In fact, besides literals (which must be typed), an expression operand is basically any element that can be selected in the Expression editor's Scope Tree.