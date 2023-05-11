---
locale: en-us
guid: d9b03ed2-6a7e-4674-8c03-fec66386a573
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Maintenance Suggestion Warning

Message
:   `Complete enumeration of <entity> attributes found: consider replacing with <entity>.* in <query>`

Cause
:   You have a SQL query that is fetching all the attributes of an entity. In this situation, and in order to improve the maintenance of your application, you should use the wild card ('*').

Recommendation
:   Edit your SQL query and replace the `SELECT attr1, attr2, ...` by `SELECT {<entity>}.*`.
