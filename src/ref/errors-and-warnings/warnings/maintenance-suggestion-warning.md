---
summary: Learn how to optimize SQL queries in OutSystems 11 (O11) by replacing complete attribute enumeration with wildcard usage for better maintenance.
locale: en-us
guid: d9b03ed2-6a7e-4674-8c03-fec66386a573
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: sql query optimization, database performance, entity management, query wildcards, software maintenance
audience:
  - backend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Maintenance Suggestion Warning

Message
:   `Complete enumeration of <entity> attributes found: consider replacing with <entity>.* in <query>`

Cause
:   You have a SQL query that is fetching all the attributes of an entity. In this situation, and in order to improve the maintenance of your application, you should use the wild card ('*').

Recommendation
:   Edit your SQL query and replace the `SELECT attr1, attr2, ...` by `SELECT {<entity>}.*`.
