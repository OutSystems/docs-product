---
summary: Check the causes and recomendations on how to solve the different Concurrent Publishing TrueChange errors.
tags:
locale: en-us
guid: d16fc208-4a45-4e8e-a4d1-d271d33f00a4
app_type: traditional web apps, mobile apps, reactive web apps
---

# Concurrent Publishing Error

## Your module is currently being locked by another operation. Please try again later. User &lt;user> is publishing module &lt;module> (in Personal Area) since &lt;date/time>

**Cause**

This error is issued in the following situations:

* You are trying to Run the module in your Personal Area while a 1-Click Publish is being processed in the server or another developer with your credentials is also updating your Personal Area.
* You are trying to publish the module while another developer is also publishing the module or running it in the Personal Area.

**Recommended action**

Wait a few moments and try the operation again.
    
If the issue persists, try restarting the deployment controller service. On the OutSystems Cloud, [you can do it in LifeTime](https://success.outsystems.com/Support/Troubleshooting/Infrastructure_management/Restart_services_on_OutSystems_Cloud). In self-managed servers, access the remote server, open the Windows app **Services**, search and restart the **OutSystems Deployment Controller service**.

