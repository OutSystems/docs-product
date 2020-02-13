---
tags: 
---

# Operators

In OutSystems you can use the operators presented below.

## Numeric

\+, -, *, /

### Unary minus

Yields the negation of its numeric operand.

The following are the data types allowed for unary minus (\-) operator:

\- (Unary minus) | Text | Long Integer | Integer | Decimal | Boolean | Date Time | Date | Time  
---|---|---|---|---|---|---|---|---  
 | No | Yes | Yes | Yes | No | No | No | No  
  
### Arithmetic operators /, \-, \*

Perform common arithmetic operations.

The following are the data types allowed for arithmetic operators /, \-, \*:

/, \*, \- | Text | Long Integer | Integer | Decimal | Boolean | Date Time | Date | Time  
---|---|---|---|---|---|---|---|---  
**Text** | No | No | No | No | No | No | No | No  
**Long Integer** | No | Yes(a) | Yes(a) | Yes(a) | No | No | No | No  
**Integer** | No | Yes(a) | Yes(a) | Yes(a) | No | No | No | No  
**Decimal** | No | Yes(a) | Yes(a) | Yes | No | No | No | No  
**Boolean** | No | No | No | No | No | No | No | No  
**DateTime** | No | No | No | No | No | No | No | No  
**Date** | No | No | No | No | No | No | No | No  
**Time** | No | No | No | No | No | No | No | No  

(a) The result of a division operation is always cast as a `Decimal`.

### Arithmetic operator +

Performs sum operation. When one of the operands is `Text`, the other operand is cast to `Text`, and performs the concatenate operation.

The following are the data types allowed for arithmetic operator `+`:

\+ | Text | Long Integer | Integer | Decimal | Boolean | DateTime | Date | Time  
---|---|---|---|---|---|---|---|---  
**Text** | Yes | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a)  
**Long Integer** | Yes(a) | Yes | Yes | Yes | No | No | No | No  
**Integer** | Yes(a) | Yes | Yes | Yes | No | No | No | No  
**Decimal** | Yes(a) | Yes | Yes | Yes | No | No | No | No  
**Boolean** | Yes(a) | No | No | No | No | No | No | No  
**DateTime** | Yes(a) | No | No | No | No | No | No | No  
**Date** | Yes(a) | No | No | No | No | No | No | No  
**Time** | Yes(a) | No | No | No | No | No | No | No

(a) The non-text side is cast to `Text` and then concatenated.

## Logical and Boolean

and, or, not, =, &lt;, &gt;, &lt;&gt;, &lt;=, &gt;=

### AND

Performs the logical 'AND' operation. Allows only `Boolean` type operands.

### OR

Performs the logical 'OR' operation. Allows only `Boolean` type operands.

### Unary NOT

Performs the logical 'NOT' operation. Allows only `Boolean` type operands.

### Comparison operators &lt;, &gt;, &lt;=, &gt;=

Common comparison operations. When one of the operands is Text, the other operand is converted to Text, and it performs the string comparison operation.

The following are the data types allowed for comparison operators:

&lt;, &gt;, &lt;=, &gt;= | Text | Integer | Long Integer | Decimal | Boolean | Date Time | Date | Time | Email | Phone Number | Currency | Binary Data  
---|---|---|---|---|---|---|---|---|---|---|---|---  
**Text** | Yes | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | No | No  
**Integer** | Yes(a) | Yes | Yes | Yes | No | No | No | No | No | No | Yes(c) | No  
**Long Integer** | Yes(a) | Yes | Yes | Yes | No | No | No | No | No | No | Yes(c) | No  
**Decimal** | Yes(a) | Yes | Yes | Yes | No | No | No | No | No | No | Yes(c) | No  
**Boolean** | Yes(a) | No | No | No | No | No | No | No | No | No | No | No  
**Date Time** | Yes(a) | No | No | No | No | Yes | No | No | No | No | No | No 
**Date** | Yes(a) | No | No | No | No | No | Yes | No | No | No | No | No  
**Time** | Yes(a) | No | No | No | No | No | No | Yes | No | No | No | No  
**Email** | Yes(a) | No | No | No | No | No | No | No | Yes | Yes(b) | No | No  
**Phone Number** | Yes(a) | No | No | No | No | No | No | No | Yes(b) | Yes | No | No  
**Currency** | No | Yes | Yes | Yes | No | No | No | No | No | No | Yes | No  
**Binary Data** | No | No | No | No | No | No | No | No | No | No | No | No  

(a) The non-text side is converted to `Text` and the length of both texts are compared.

(b) Both variables are converted to `Text` and the their length is compared.

(c) The `Currency` operand is converted to `Integer` data type and then
compared.

### Equality operators =, &lt;&gt;

Performs equality operations. When one of the operands is `Text`, the other operand is converted to `Text`, and it performs the string comparison operation.

The following are the data types allowed for equality operators:

=, &lt;&gt; | Text | Integer | Long Integer | Decimal | Boolean | Date Time | Date | Time | Email | Phone Number | Currency | Binary Data | Entity / Structure / Record | Integer Identifier | Text Identifier  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
**Text** | Yes | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | Yes(a) | No | No | No | No  
**Integer** | Yes(a) | Yes | Yes | Yes | No | No | No | No | Yes* | Yes* | Yes* | No | No | No | No  
**Long Integer** | Yes(a) | Yes | Yes | Yes | No | No | No | No | Yes* | Yes* | Yes* | No | No | No | No  
**Decimal** | Yes(a) | Yes | Yes | Yes | No | No | No | No | Yes* | Yes* | Yes* | No | No | No | No  
**Boolean** | Yes(a) | No | No | No | Yes | No | No | No | No | No | No | No | No | No | No  
**Date Time** | Yes(a) | No | No | No | No | Yes | Yes* | Yes* | Yes* | Yes* | No | No | No | No | No  
**Date** | Yes(a) | No | No | No | No | Yes* | Yes | No | Yes* | Yes* | No | No | No | No | No  
**Time** | Yes(a) | No | No | No | No | Yes* | No | Yes | Yes* | Yes* | No | No | No | No | No  
**Email** | Yes(a) | Yes* | Yes* | Yes* | No | Yes* | Yes* | Yes* | Yes | Yes* | No | No | No | No | No  
**Phone Number** | Yes(a) | Yes* | Yes* | Yes* | No | Yes* | Yes* | Yes* | Yes* | Yes | Yes* | No | No | No | No  
**Currency** | Yes(a) | Yes* | Yes* | Yes* | No | No | No | No | No | Yes* | Yes | No | No | No | No  
**Binary Data** | No | No | No | No | No | No | No | No | No | No | No | No | No | No | No  
**Entity / Structure / Record** | No | No | No | No | No | No | No | No | No | No | No | No | Yes(b) | No | No  
**Integer Identifier** | No | No | No | No | No | No | No | No | No | No | No | No | No | Yes(c) | No  
**Text Identifier** | No | No | No | No | No | No | No | No | No | No | No | No | No | No | Yes(c)

(a) The non-text side is converted to `Text` and then compared.

(b) Only possible if both operands are of the same type, then, compare the value of the attributes.

(c) Identifiers of different entities can be compared but a warning is issued.

***Equality between Different Types:**

Type of Operand 1 | Type of Operand 2 | Result  
---|---|---  
 Date | Date Time | Converts Date Time operand type to Date type by dropping the time component.  
Date Time | Date | Converts Date operand type to Date Time type by adding the time component (#00:00:00#).  
Time or Date Time | Time or Date Time | Converts Time operand type to Date Time type by adding the date component (#01-01-1900#).  
Currency | Integer, Long Integer, or Decimal | Converts the Currency variable to Integer data type.  
Email or Phone Number | Integer, Long Integer, or Decimal | Converts Decimal, Long Integer or Integer operand type to Text.  
Email | Phone Number | Converts both operands to Text.  
Date Time, Date, or Time | Email or Phone Number | Converts both operands to Text.  
Currency | Phone Number | Converts both operands to Text.  

## Like

This operator is only valid in the Filter Condition Editor of an aggregate and allows you to compare results. It has the same semantic as the `LIKE` keyword in SQL. You can use the `LIKE` operator to compare with an expression. But the advantage of `LIKE` is the fact that it allows you to use the wildcard character `%` that represents one or more characters.

For example, if you want to select the Identifier for every Customer that contains "James" in its name, in any position, the following filter condition allows you to get this information:

`name LIKE '%James%'`

The following are the data types allowed for LIKE operator:

LIKE | Text | Integer | Decimal | Boolean | DateTime | Date | Time  
---|---|---|---|---|---|---|---  
**Text** | Yes | (a) | (a) | (a) | (a) | (a) | (a)  
**Integer** | (a) | No | No | No | No | No | No  
**Decimal** | (a) | No | No | No | No | No | No  
**Boolean** | (a) | No | No | No | No | No | No  
**DateTime** | (a) | No | No | No | No | No | No  
**Date** | (a) | No | No | No | No | No | No  
**Time** | (a) | No | No | No | No | No | No

(a) The non-text side is cast to `Text` and then compared.

## Indexer Declaration

This operator is used to access a specific element of a list. In OutSystems, index (position) starts with zero; to access the first record, you have to type the expression as follows:

`MyRecordList[0]`

When you try to access an index that does not exist, the following runtime error is raised: "Index n is out of range"

Since a record can be a sequence of Entities and/or Structures, you can access to a specific Entity or Structure of a specified record:

`MyRecordList[0].<entity name | structure name>`

You can use an expression inside the indexer operator as long as it returns an integer value. This includes the use of User Functions.

`MyRecordList[i-1].Customer.Name` — where `i` is an integer.

`MyRecordList[EmployeeOfMonth()].Employee.Name` — where `EmployeeOfMonth` is a User Function that returns an integer value.

## Precedence of Operators

The next table presents the precedence of the operators, highest precedence first:

Operator | Description  
---|---  
 \- | Numeric negation  
NOT | Logical negation
/, \* | Multiplicative operators 
\-, \+ | Additive operators.  
&lt;, &gt;, &lt;=, &gt;= | Relational operators 
=, &lt;&gt; | Equality operators  
LIKE | Similarity operator
AND | Logical AND
OR | Logical OR
