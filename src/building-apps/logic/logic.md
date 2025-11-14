---
summary: Discover key performance optimization strategies for OutSystems 11 (O11), focusing on efficient logic and system monitoring.
guid: faee48f5-9b43-40a6-906d-837feef414df
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: performance optimization, system monitoring, efficient logic, code best practices, application troubleshooting
audience:
  - full stack developers
  - frontend developers
  - backend developers
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - evaluate
---

# Best practices for logic performance optimization

Optimizing application performance requires developers to adhere to high coding standards. The following best practices apply universally to any type of application.

## Use service center reports

### Description

 Use Service Center reports to identify performance bottlenecks in applications and guide optimization efforts.

### Solution

Analyze slow web screens, database queries, or services in Service Center's Analytics section. Focus efforts on resolving identified bottlenecks to reduce troubleshooting time.

### Key point

This is the first step in any performance optimization process.

## Avoid long-running timers and batch jobs

### Description

Avoid doing background processing all in a row. Use control tables and process data in chunks, rescheduling itself at the end of a run.

### Solution

Limit timers to a maximum of 20 minutes. If necessary, reschedule the timer and store process states to resume without issues. Use checkpoints and partial commits to ensure timers can safely restart without data loss.

### Key point

Shorter timers reduce the risk of data inconsistency and system strain.

## Simplify screen preparations

<div class="info" markdown="1">

Applies only to Traditional Web apps.

</div>

### Description

Streamline screen preparation actions to speed up loading times.

### Solution

Avoid overly complex queries, pre-process data during write operations, and minimize redundant permission checks. Executing heavy operations during screen preparation can slow page rendering.

### Key point

Faster page loads improve user experience, so minimize database queries and avoid write operations during screen prep unless necessary.

## Use Site Properties efficiently

### Description

Don't use Site Properties as frequently changing logic variables.

### Solution

Treat Site Properties as constants. For frequently updated values, use a database table and back-office functionality to manage them instead.

### Key point

Constant changes to Site Properties can increase database overhead and result in errors like deadlocks under heavy loads.

## Limit session variables

<div class="info" markdown="1">

Applies only to Traditional Web apps.

</div>

### Description

Minimize the use of large session variables.

### Solution

Reduce session data by storing user-specific information in the database, limiting the need to load large session variables on each request.

### Key point

Large session variables increase load times, especially with AJAX requests, impacting application performance.

## Avoid isolated Aggregates

### Description

Don’t create isolated actions solely to execute Aggregates.

### Solution

Isolating Aggregates prevents the platform from optimizing field retrieval, leading to unnecessary database load.

### Key point

Fetching the entire entity from the database occurs even if not all fields are used.

## Avoid queries inside ‘If’ branches in preparation

<div class="info" markdown="1">

Applies only to Traditional Web apps.

</div>

### Description

 Prevent the unnecessary inclusion of query data in the viewstate.

### Solution

Use local screen variables instead of placing conditional queries inside "if" branches, especially when using data outside the branch.

### Key point

Conditional queries increase the size of the page’s viewstate, slowing down the user experience.
