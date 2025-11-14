---
summary: Explore OutSystems 11's Sanitization API, designed to prevent code injection by sanitizing HTML, JavaScript, and SQL content.
tags: security, code injection prevention, api, sql sanitization, html sanitization
locale: en-us
guid: 6193f89c-cf98-4f38-8308-6eb0eee24f86
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Sanitization API

API that provides server actions to help you avoid code injection in HTML, JavaScript, and SQL snippets that need to include untrusted content, for example, content gathered from end users. To use the server actions from Sanitization API, add the **Sanitization (extension)** as a dependency.

## Summary

| Action | Description |
| ---|--- |
| [BuildSafe_InClauseIntegerList](<#BuildSafe_InClauseIntegerList>) | Returns a comma-delimited text value containing all the integer values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause. |
| [BuildSafe_InClauseTextList](<#BuildSafe_InClauseTextList>) | Returns a comma-delimited text value with the encoded version of all the text values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause. This method should only be used in queries against the Platform's main database. Behavior can be unexpected when used against external databases. |
| [SanitizeHtml](<#SanitizeHtml>) | Sanitizes the provided HTML using [HtmlSanitizer NuGet package](https://github.com/mganss/HtmlSanitizer). |
| [VerifyJavascriptLiteral](<#VerifyJavascriptLiteral>) | **Deprecated**. Ensures the provided JavaScript only contains JavaScript/JSON literals such as string, array, or Object literals. If it contains anything else, an INVALID JAVASCRIPT LITERAL exception is thrown. Learn more about JavaScript literals in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Literals). |
| [VerifySqlLiteral](<#VerifySqlLiteral>) | **Deprecated**. Ensure the provided SQL only contains literals. If it contains anything else, an INVALID SQL LITERAL exception is thrown. |

## Actions

### BuildSafe_InClauseIntegerList { #BuildSafe_InClauseIntegerList }

Returns a comma-delimited text value containing all the integer values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause.

_Inputs_

ValueList
:   Type: RecordList of [IntegerLiteral](<#Structure_IntegerLiteral>). Mandatory.  
    List of integer values to include in the returned value.

_Outputs_

Output
:   Type: Text.  
    A string containing comma-separated integer values to be used in a SQL &quot;IN&quot; clause.

Examples:

```
// ListA and ListB are local variables with data type IntegerLiteral List

ListA[0].Value = 2
ListA[1].Value = 7
BuildSafe_InClauseIntegerList(ListA) = "2,7"

// ListB is empty
BuildSafe_InClauseIntegerList(ListB) = "0"
```

For more information, check [Best practices for building dynamic SQL statements](../../../building-apps/data/operations/build-dynamic-sql-statements.md).

### BuildSafe_InClauseTextList { #BuildSafe_InClauseTextList }

Returns a comma-delimited text value with the encoded version of all the text values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause.

<div class="info" markdown="1">

This method should only be used in queries against the Platform's main database. Behavior can be unexpected when used against external databases.

</div>

_Inputs_

ValueList
:   Type: RecordList of [TextLiteral](<#Structure_TextLiteral>). Mandatory.  
    List of text values to include in the returned value.

_Outputs_

Output
:   Type: Text.  
    A string containing a set of encoded text values separated by commas to be used in a SQL &quot;IN&quot; clause.

Examples:

```
// ListA and ListB are local variables with data type TextLiteral List

ListA[0].Value = "John Doe"
ListA[1].Value = "Mary O'Hara"
BuildSafe_InClauseTextList(ListA) = "'John Doe','Mary O''Hara'"

// ListB is empty
BuildSafe_InClauseTextList(ListB) = "''"
```

For more information, check [Best practices for building dynamic SQL statements](../../../building-apps/data/operations/build-dynamic-sql-statements.md).

### SanitizeHtml { #SanitizeHtml }

Sanitizes the provided HTML using [HtmlSanitizer NuGet package](https://github.com/mganss/HtmlSanitizer).

_Inputs_

Html
:   Type: Text. Mandatory.  
    The HTML to sanitize.

_Outputs_

SanitizedHtml
:   Type: Text.  
    The sanitized HTML.

### VerifyJavascriptLiteral { #VerifyJavascriptLiteral }

**Deprecated**. Ensures the provided JavaScript only contains JavaScript/JSON literals such as string, array, or Object literals. If it contains anything else, an INVALID JAVASCRIPT LITERAL exception is thrown. Learn more about JavaScript literals in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Literals).

_Inputs_

JavascriptLiteral
:   Type: Text. Mandatory.  
    The JavaScript literal to sanitize.

_Outputs_

SanitizedJavascriptLiteral
:   Type: Text.  
    The sanitized JavaScript literal.

### VerifySqlLiteral { #VerifySqlLiteral }

**Deprecated**. Ensures the provided SQL only contains literals. If it contains anything else, an INVALID SQL LITERAL exception is thrown.

The following items are considered valid literals:

* Non-Unicode and Unicode (prefix it with an uppercase N) strings surrounded by single quotes,'. For example `'1900-01-01'`; `'true'`).
* Integers and decimals, for example: `2.5`; `-4`.
* Null, for example: `null`; `NULL`; `Null`.
* Whitespaces.
* Lists containing the previous literals, for example: `'fact'`; `12,0`; `('apple','banana','orange')`.
* Any combination of the previous literals.

_Inputs_

SqlLiteral
:   Type: Text. Mandatory.  
    The SQL to sanitize.

_Outputs_

SanitizedSqlLiteral
:   Type: Text.  
    The sanitized SQL.

## Structures

### IntegerLiteral { #Structure_IntegerLiteral }

Simple structure holding a long integer value. Used as a record definition when providing a list of IntegerLiteral records to include in a SQL &quot;IN&quot; clause.

_Attributes_

Value
:   Type: LongInteger. Mandatory.  
    An integer value to consider when creating a SQL &quot;IN&quot; clause.

### TextLiteral { #Structure_TextLiteral }

Simple structure holding a text value. Used as a record definition when providing a list of TextLiteral records to include in a SQL &quot;IN&quot; clause.

_Attributes_

Value
:   Type: Text (2000). Mandatory.  
    A text value to consider when creating a SQL &quot;IN&quot; clause.
