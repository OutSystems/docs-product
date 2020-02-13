# Unexpected Attribute Warning

Message
:   `'<attribute>' is an invalid attribute name in <database>.`

Cause
:   You are using an Oracle database and the name of that attribute is a reserved word. The reserved words are as follows: `timestamp`, `number`, `blob`, `clob`, and `varchar2`.

Recommendation
:   Change the attribute name according to Oracle rules.
