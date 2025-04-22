---
summary: Explore key performance best practices in OutSystems 11 (O11), including optimal module referencing and connection pooling strategies.
guid: 30bb25e2-e67a-4d1a-b2ba-a486bb9e0f14
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: module architecture, software architecture, deployment best practices, performance optimization, entity management
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
---

# Performance Best Practices - References

It’s all about software architecture. Usually, opting for the quickest solution produces severe performance problems. Refactoring later on may be a painful and expensive proposition.

## Think twice before creating references between Modules

### Description

Avoid circular reference between Modules or groups of Modules.

### Solution

When dealing with actions that receive or output Record/RecordLists with a large number of attributes consider using structures instead of entities for those records. Structures will narrow down the amount of data that flows through the entire system producing significant net benefits.

### Importance

Having simple tree type reference models, helps the deployment process, and avoids the need to deploy an entire solution just to guarantee that the cyclic references are resolved. Improves deployment processes times.

### Remarks

This is often simpler said than done. When applications reach some level of complexity, the cost of splitting Modules and thus multiplying the number of Modules of a solution is just too high. But that's why this is a best practice that you should have always present. Every time you are creating a new dependency between two Modules think twice if that dependency makes sense in your Modules architecture or if you should create a new Module or use a web service. This best practice should always be used together with best practice **"Evaluate Local Web Services v. Public Actions"**. The balance between the two of them is not easy and only experience and by trial and error will one make the correct option most of the time.

## Evaluate Local Web Services v. Public Actions

### Description

The use of public actions instead of web services increases the performance of the application in run time but it increases the complexity of the application’s reference map which then hinders the performance of the deployment process. Choosing between web services and public actions needs to be well thought out.

### Solution

Whenever possible, avoid using local web services; instead use Module references but evaluate the pros and cons between using the local web service and increasing the complexity of the reference model.

### Importance

Using local web services in screen logic will increase the number of threads processing the screen requests. When the number of calls becomes excessive, this can cause a thread exhaustion on the web server and generate unnecessary application queuing. Although using local references is much faster and doesn't require TCP/IP resources or additional threads, you should evaluate the impact of increasing the complexity of the reference model.

### Remarks

This best practice should always be used together with best practice "Think twice before creating references between Modules". The balance between the two practices is not easy and only experience and try and fail will give you the intuition to take the correct option most of the times.

## Use Connection pooling

### Description

Use connection pooling when connecting to external systems/databases.

### Solution

Always use a connection pool management mechanism in frequent connections to third party database systems, like SQL Server, Oracle, PostgreSQL, DB2 or MySQL, through extension integration.

### Importance

Connection pools enable you to maintain and reuse a “pool” of open database connections from operation to operation, instead of opening and closing a new connection for each operation. For small-scale operations, opening and closing a database connection may not be as expensive. However, as your application scales up, it can become more expensive and impact the application's performance.

### Remarks

Note that this also applies when connecting to the OutSystems database from extensions.

