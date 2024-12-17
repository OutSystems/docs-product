---
summary: Explore how OutSystems 11 (O11) handles Invalid Data Dependency errors, including fetch property conflicts and circular dependencies.
locale: en-us
guid: bdac6bb2-8fa2-4c3b-b006-d30a08fa4566
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: data dependencies, fetch properties, error handling, circular dependencies, application performance
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
---

# Invalid Data Dependency

The Invalid Data Dependency error is issued in the following situations:

* `You can't set Fetch property At Start on a data source that depends on a source with Fetch set to On Demand. Change the Fetch property value of '{0}' or '{1}'.`

    Change the Fetch properties on your data sources. You probably designed two dependent data sources with **At Start** and **Only on demand** properties, but they won't fetch any data because of the wrong order. If you are implementing, for example, a master-detail pattern, the "master" data sources should fetch all data with On Start while "detail" data is fetched On Demand.  

* `'{0}' can depend on single data source only. Remove the references to other data sources.`
  
    A data source can only depend on another data source (for example, Screen Aggregates, or Data Actions). One data source can't depend on two or more data sources. Merge multiple data sources into one or reference a client variable instead.

* `Loop detected in '{0}'. Edit the data source references to remove circular dependency.`
  
     The fetching of your data is designed in such a way that it references itself. This causes loop that can freeze the app. Change the data dependency to remove this circular dependency.
