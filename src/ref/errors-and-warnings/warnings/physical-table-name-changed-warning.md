---
locale: en-us
guid: 7e812677-ceb0-4d0d-8e79-b56f14a7a28b
---

# Physical Table Name Changed Warning

Message
:   `Entity <entity> physical table name was set  to <table'> because an external table name <table> already exists.`

Cause
:   The name of the physical table name associated to the entity already exists in the database. Service Studio automatically renamed the physical table name to `<table'>` to avoid name clashing in the database.
