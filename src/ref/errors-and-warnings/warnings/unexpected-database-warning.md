---
locale: en-us
guid: dc568697-e3e5-4dae-9f80-7c4663228e68
---

# Unexpected Database Warning

Message
:   `module 'Database' property (<database>) does not match Platform Server database type (<database>)`

Cause
:   The Database module property is different from the type of the OutSystems database.

Recommendation
:   You should set this property with the exact database type or choose '(Both)'. Besides, you should also validate whether your SQL queries are compliant with the database type you are using.
