---
summary: Explore performance optimization best practices for OutSystems 11 (O11) to enhance application speed and efficiency.
guid: 5ec53f32-ba14-4732-bbdf-44b8588c5fd2
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: performance optimization, database indexing, database maintenance, query optimization, server configuration
audience:
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - evaluate
---

# Performance Top 10 Rules

Good applications have at least one thing in common – they are really fast. Beyond built-in OutSystems Platform optimizations, keep these best practices in mind. 

## Index your entities

Creating indexes for the most used entity attributes will significantly improve the performance of select queries at the cost of slight overhead in insert and update operations.

## Setup database maintenance plans

Maintenance plans with reorganization of indexes and statistics update allow the database engine to optimize queries and take advantage of the existing entity indexes. Don't forget to involve the resident DBA.

## Use Service Center reports

Use Service Center reports as the starting point for all application tuning efforts. These reports provide a full view of the slowest operations; are divided by application screens, web services, timers, queries and extensions.

## Don't join over linked server

Cross server joins are very inefficient because the table in the linked server is completely loaded to the local DB server and then the join is performed. Cross server joins may be acceptable if the tables are small and unavoidable but as a rule cross server joins should be avoided as much as possible.

## Configure web server memory settings

Apply the webserver tuning settings to optimize memory usage and application server performance according to the checklist best practices. Using .NET stack, process recycling affects performance and should be minimized, while in the Java stack, the virtual machine memory settings should be fine-tuned to improve availability.

## Isolate large text and binary data

Avoid the use of 2000+ characters in a text field; data fields greater than 2000 bytes are converted into a Text data type which in turn are much slower to process and decrease performance overall. As a rule, isolate binary and/or large text fields in separate entities and only retrieve them when they are strictly necessary.

## Avoid long running timers and batch jobs

Timers and batch jobs should be built having partial processing capability and auto-timeout mechanisms. These features will prevent run-away jobs, endless data reprocessing and data inconsistencies.

## Simplify screen preparations

Screen preparation processing affects the user experience and therefore should be simple and fast to execute. This is especially important for web screens having a high access volume like home pages

## Avoid using preparation data in screen actions

Don't use preparation data in screen actions because it increases the network traffic between the server and the browser. This in turn increases network usage and degrades server request processing performance. This applies only to Traditional Web Apps. 

## Minimize the number of fields fetched from the database

Use specific structures with the necessary attributes, instead of returning the whole database entity as I/O parameters of actions. This allows the platform to optimize the queries, improving database performance. 

