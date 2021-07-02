---
summary: Check the causes and recomendations on how to solve the different Concurrent Publishing TrueChange errors.
tags:
en_title:
---

# Concurrent Publishing Error

## Your module is currently being locked by another operation. Please try again later. User &lt;user> is publishing module &lt;module> (in Personal Area) since &lt;date/time>

**Cause**

This error is issued in the following situations:

* You are trying to Run the module in your Personal Area while a 1-Click Publish is being processed in the server or another developer with your credentials is also updating your Personal Area.
* You are trying to publish the module while a Run is being processed in the server or another developer is also publishing the module.

**Recommended action**

Wait a few moments and try the operation again.
    
If the issue continues to persist, try [restarting the OutSystems Services](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Restart_Services_on_OutSystems_PaaS) in LifeTime. This resets the service that stopped during a publishing step.

