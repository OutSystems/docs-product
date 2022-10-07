---
summary: API that provides methods to help you avoid code injection in HTML, JavaScript, and SQL snippets that need to include untrusted content, for example, content gathered from end users.
tags: 
locale: en-us
guid: 6193f89c-cf98-4f38-8308-6eb0eee24f86
app_type: traditional web apps, mobile apps, reactive web apps
---

# Sanitization API


API that provides methods to help you avoid code injection in HTML, JavaScript, and SQL snippets that need to include untrusted content, for example, content gathered from end users.

## Summary

Action | Description
---|---
[BuildSafe_InClauseIntegerList](<#BuildSafe_InClauseIntegerList>) | Returns a comma-delimited text value containing all the integer values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause.
[BuildSafe_InClauseTextList](<#BuildSafe_InClauseTextList>) | Returns a comma-delimited text value with the encoded version of all the text values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause.
[SanitizeHtml](<#SanitizeHtml>) | Sanitizes the provided HTML using the HtmlSanitizer NuGet package.
[VerifyJavascriptLiteral](<#VerifyJavascriptLiteral>) | Ensures the provided JavaScript only contains JavaScript/JSON literals such as string, array, or Object literals. If it contains anything else, an INVALID JAVASCRIPT LITERAL exception is thrown. Learn more about JavaScript literals in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Literals).
[VerifySqlLiteral](<#VerifySqlLiteral>) | **Deprecated**. Ensure the provided SQL only contains literals. If it contains anything else, an INVALID SQL LITERAL exception is thrown.

## Actions

### BuildSafe_InClauseIntegerList { #BuildSafe_InClauseIntegerList }

Returns a comma-delimited text value containing all the integer values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause.

*Inputs*

ValueList
:   Type: RecordList of [IntegerLiteral](<#Structure_IntegerLiteral>). Mandatory.  
    List of integer values to include in the returned value.

*Outputs*

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

For more information, check [Building Dynamic SQL Statements the Right Way](https://success.outsystems.com/Documentation/Best_Practices/Development/Building_Dynamic_SQL_Statements_the_Right_Way).

### BuildSafe_InClauseTextList { #BuildSafe_InClauseTextList }

Returns a comma-delimited text value with the encoded version of all the text values provided as input. The returned value can be safely used in a SQL &quot;IN&quot; clause.

*Inputs*

ValueList
:   Type: RecordList of [TextLiteral](<#Structure_TextLiteral>). Mandatory.  
    List of text values to include in the returned value.

*Outputs*

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

For more information, check [Building Dynamic SQL Statements the Right Way](https://success.outsystems.com/Documentation/Best_Practices/Development/Building_Dynamic_SQL_Statements_the_Right_Way).

### SanitizeHtml { #SanitizeHtml }

Sanitizes the provided HTML using the HtmlSanitizer NuGet package.  
Note: The underlying library was recently changed from OWASP Java HTML Sanitizer Project. Check the [Release Notes](<https://success.outsystems.com/Support/Release_Notes/11/Platform_Server>) for a summary of what changed.

*Inputs*

Html
:   Type: Text. Mandatory.  
    The HTML to sanitize.

*Outputs*

SanitizedHtml
:   Type: Text.  
    The sanitized HTML.

### VerifyJavascriptLiteral { #VerifyJavascriptLiteral }

Ensures the provided JavaScript only contains JavaScript/JSON literals such as string, array, or Object literals. If it contains anything else, an INVALID JAVASCRIPT LITERAL exception is thrown. Learn more about JavaScript literals in the [MDN documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types#Literals).

*Inputs*

JavascriptLiteral
:   Type: Text. Mandatory.  
    The JavaScript literal to sanitize.

*Outputs*

SanitizedJavascriptLiteral
:   Type: Text.  
    The sanitized JavaScript literal.

### VerifySqlLiteral { #VerifySqlLiteral }

**Deprecated**. Ensures the provided SQL only contains literals. If it contains anything else, an INVALID SQL LITERAL exception is thrown.

*Inputs*

SqlLiteral
:   Type: Text. Mandatory.  
    The SQL to sanitize.

*Outputs*

SanitizedSqlLiteral
:   Type: Text.  
    The sanitized SQL.


## Structures

### IntegerLiteral { #Structure_IntegerLiteral }

Simple structure holding a long integer value. Used as a record definition when providing a list of IntegerLiteral records to include in a SQL &quot;IN&quot; clause.

*Attributes*

Value
:   Type: LongInteger. Mandatory.  
    An integer value to consider when creating a SQL &quot;IN&quot; clause.

### TextLiteral { #Structure_TextLiteral }

Simple structure holding a text value. Used as a record definition when providing a list of TextLiteral records to include in a SQL &quot;IN&quot; clause.

*Attributes*

Value
:   Type: Text (2000). Mandatory.  
    A text value to consider when creating a SQL &quot;IN&quot; clause.



