# Unexpected Attribute Warning

Message
:   `<attribute> is an invalid attribute name in Oracle`

Cause
:   Your module is prepared to use an Oracle database or both databases, and you have an attribute with a name that is a reserved word in Oracle.

Recommendation
:   You should edit the entity attribute and change the name. The Oracle reserved words are as the following: `timestamp`, `number`, `blob`, `clob`, and `varchar2`.
