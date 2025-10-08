---
guid: 4ec81e8d-f2c7-47e6-a25c-28b2b75e6faa
locale: en-us
summary: Learn how to solve the findings for the conversion code pattern "Library with cyclic dependency to another ODC library".
figma:
coverage-type:
  - unblock
topic:
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - architects
  - tech leads
outsystems-tools:
  - service studio
helpids: 30671
tags: cyclic dependency, o11 modules, odc libraries, code conversion, business domain
---
# Library with cyclic dependency to another ODC library

In ODC, libraries can't have circular references. This means that Library A can't depend on Library B if Library B already depends on Library A.

This pattern occurs when two O11 modules that have a cyclic dependency between them are mapped to two different ODC libraries.

## How to solve

You must solve this pattern in O11, before proceeding with the code conversion to ODC.

### Solve in O11

Depending on your scenario, solve this pattern in one of the following ways:

* **If the modules belong to the same business domain**, indicates that they're too tightly coupled to be independent libraries. Follow these steps to solve the pattern:

  1. Move the O11 modules into the same O11 app.

  1. Map that single O11 app to a single ODC library.

* **If the modules belong to distinct domains**, break the invalid dependency:

  1. Identify the shared logic causing the cycle and extract it into a new O11 module and app.

  1. Map that new O11 app to a new ODC library.  
     The original modules can then both depend on this new shared library, breaking the circular reference.

