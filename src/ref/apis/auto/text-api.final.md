---
summary: Provides actions to manipulate character strings such as joining, splitting, search and replace using regular expressions, and custom formatting of DateTime expressions.
tags: 
locale: en-us
guid: 6892cbf0-85c1-4403-8d32-0e4a89ee1331
app_type: traditional web apps, mobile apps, reactive web apps
---

# Text API


OutSystems Text API provides functionality to manipulate texts as, for example: search and replace using a regular expression, split, join, or format DateTimes.

Elements in this API are available in the **Text** module.

To make these elements available in your module do the following:

1. In Service Studio, open the **Manage Dependencies** window.
1. Select the **Text** module in the producer modules list (left side).
1. Select the elements you want to use in your module (right side).
1. Press **OK**.

For more information on adding elements from other modules as dependencies, check [Expose and Reuse Functionality Between Modules](../../../develop/reuse-and-refactor/expose-and-reuse.md#reuse).

## Summary

Action | Description
---|---
[Format_DateTime](<#Format_DateTime>) | Formats a DateTime by replacing the allowed keywords with their values.<br/>Available Keywords:<br/>[yyyy] - Represents the year as a four-digit number;<br/>[MM] - Represents the month as a number from 01 through 12;<br/>[MMM] - Represents the abbreviated name of the month;<br/>[MMMM] - Represents the full name of the month;<br/>[dd] - Represents the day of the month as a number from 01 through 31;<br/>[ddd] - Represents the abbreviated name of the day of the week;<br/>[dddd] - Represents the full name of the day of the week;<br/>[hh] - Represents the hour as a number from 01 through 12;<br/>[HH] - Represents the hour as a number from 00 through 23;<br/>[mm] - Represents the minute as a number from 0 through 59;<br/>[ss] - Represents the seconds as a number from 00 through 59;
[Regex_Replace](<#Regex_Replace>) | Replaces all occurrences of a specified regular expression pattern with a replacement string.
[Regex_Search](<#Regex_Search>) | Searches the input string for an occurrence of a regular expression.
[String_Join](<#String_Join>) | Concatenates all the strings in a List, yielding a single string. The individual elements are separated, in the resulting string, by the string Separator.
[String_LastIndexOf](<#String_LastIndexOf>) | Reports the index position of the last occurrence of a specified Pattern within a Text.
[String_Split](<#String_Split>) | Splits a string into individual elements delimited by any of the characters in Delimiters.
[StringBuilder_Append](<#StringBuilder_Append>) | Appends a string to a StringBuilder.
[StringBuilder_Create](<#StringBuilder_Create>) | Creates a StringBuilder. Use it if you need to create a string by repeatedly appending substrings. A StringBuilder optimizes memory management when dealing with highly dynamic strings.
[StringBuilder_ToString](<#StringBuilder_ToString>) | Returns the content of the StringBuilder's buffer.

Structure | Description
---|---
[Text](<#Structure_Text>) | Structure with single Text attribute

## Actions

### Format_DateTime { #Format_DateTime }

Formats a DateTime by replacing the allowed keywords with their values.  
Available Keywords:  
[yyyy] - Represents the year as a four-digit number;  
[MM] - Represents the month as a number from 01 through 12;  
[MMM] - Represents the abbreviated name of the month;  
[MMMM] - Represents the full name of the month;  
[dd] - Represents the day of the month as a number from 01 through 31;  
[ddd] - Represents the abbreviated name of the day of the week;  
[dddd] - Represents the full name of the day of the week;  
[hh] - Represents the hour as a number from 01 through 12;  
[HH] - Represents the hour as a number from 00 through 23;  
[mm] - Represents the minute as a number from 0 through 59;  
[ss] - Represents the seconds as a number from 00 through 59;

*Inputs*

DateTime
:   Type: DateTime. Mandatory.  
    The Datetime to be formated.

Format
:   Type: Text. Mandatory.  
    The Text with the available keywords used to format the Date Time.

*Outputs*

FormattedDateTime
:   Type: Text.  
    The Text with the formatted Date Time according to the specified Format.

### Regex_Replace { #Regex_Replace }

Replaces all occurrences of a specified regular expression pattern with a replacement string.

*Inputs*

Text
:   Type: Text. Mandatory.  
    Text in which to search for a Pattern.

Pattern
:   Type: Text. Mandatory.  
    The string to modify.

Replace
:   Type: Text. Mandatory.  
    The replacement string.

IgnoreCase
:   Type: Boolean. Default: True.  
    Specifies case-insensitive matching.

MultiLine
:   Type: Boolean. Default: False.  
    Changes the meaning of ^and $ so the match at the beginning and end, respectively, of each line, and not just the beginning and end of the entire string.

SingleLine
:   Type: Boolean. Default: False.  
    Changes the meaning of the dot (.) so it matches every character (instead of every character except \n).

*Outputs*

Result
:   Type: Text.  
    The modified character string.

### Regex_Search { #Regex_Search }

Searches the input string for an occurrence of a regular expression.

*Inputs*

Text
:   Type: Text. Mandatory.  
    Text in which to search for a Pattern.

Pattern
:   Type: Text. Mandatory.  
    Pattern to search in Text.

IgnoreCase
:   Type: Boolean. Default: True.  
    Specifies case-insensitive matching.

MultiLine
:   Type: Boolean. Default: False.  
    Changes the meaning of ^and $ so the match at the beginning and end, respectively, of each line, and not just the beginning and end of the entire string.

SingleLine
:   Type: Boolean. Default: False.  
    Changes the meaning of the dot (.) so it matches every character (instead of every character except \n).

*Outputs*

Found
:   Type: Boolean.  
    True if Pattern is found in the Text.

PatternResult
:   Type: Text.  
    Represents the matched string.

FirstIndex
:   Type: Integer.  
    Index of the first occurrence of Pattern in Text.

### String_Join { #String_Join }

Concatenates all the strings in a List, yielding a single string. The individual elements are separated, in the resulting string, by the string Separator.

*Inputs*

List
:   Type: RecordList of [Text](<#Structure_Text>). Mandatory.  
    List of strings to be concatenated.

Separator
:   Type: Text. Mandatory.  
    Separating element.

*Outputs*

Text
:   Type: Text.  
    Result of concatenation.

### String_LastIndexOf { #String_LastIndexOf }

Reports the index position of the last occurrence of a specified Pattern within a Text.

*Inputs*

Text
:   Type: Text.  
    The Text to analyse.

Pattern
:   Type: Text. Mandatory.  
    The pattern to seek.

*Outputs*

Position
:   Type: Integer.  
    The index position of the pattern if it was found, or -1 if it was not. If the Text is empty, the returned Position is 0.

### String_Split { #String_Split }

Splits a string into individual elements delimited by any of the characters in Delimiters.

*Inputs*

Text
:   Type: Text. Mandatory.  
    Text to be splitted into individual strings.

Delimiters
:   Type: Text. Mandatory.  
    Contains all the characters that should be considered as separators.

*Outputs*

List
:   Type: RecordList of [Text](<#Structure_Text>).  
    List of strings that results from splitting the original Text.

### StringBuilder_Append { #StringBuilder_Append }

Appends a string to a StringBuilder.

*Inputs*

StringBuilder
:   Type: Object. Mandatory.  
    The StringBuilder instance. Returned by the Action StringBuilder_Create.

String
:   Type: Text. Mandatory.  
    The string to append to the StringBuilder's buffer.

### StringBuilder_Create { #StringBuilder_Create }

Creates a StringBuilder. Use it if you need to create a string by repeatedly appending substrings. A StringBuilder optimizes memory management when dealing with highly dynamic strings.

*Inputs*

InitialCapacity
:   Type: Integer. Mandatory.  
    Initial capacity of the StringBuilder buffer. The buffer will be automatically resized if its capacity is exceeded. Set it to the maximum expected capacity to avoid buffer resizing.

*Outputs*

StringBuilder
:   Type: Object.  
    The StringBuilder instance. Use it as input to the other StringBuilder Actions.

### StringBuilder_ToString { #StringBuilder_ToString }

Returns the content of the StringBuilder's buffer.

*Inputs*

StringBuilder
:   Type: Object. Mandatory.  
    The StringBuilder instance. Returned by the Action StringBuilder_Create.

*Outputs*

String
:   Type: Text.  
    The content of the StringBuilder's buffer.


## Structures

### Text { #Structure_Text }

Structure with single Text attribute

*Attributes*

Value
:   Type: Text (50). Mandatory.  
    


