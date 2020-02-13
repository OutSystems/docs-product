---
summary: The Network tab allows you to clear the current internal network settings, and allows you to define the IP address the front-end server will register in the deployment controller service.
---

# Network Tab

The **Network tab** allows you to clear the current internal network settings, and allows you to define the IP address the front-end server will register in the deployment controller service.

## Internal Network section

When developing your applications, you can set resources such as web flows (groups of screens), and web services to be available only within your internal network. This configuration is [defined in Service Center](../../../managing-the-applications-lifecycle/secure-the-applications/configure-internal-network.md).

However, you may inadvertently define an Internal Network configuration that blocks you from accessing Service Center altogether. In that case, you can use the **Clear Internal Network Settings** button to clear all internal network settings currently defined.

<div class="warning" markdown="1">

**Warning:** When you clear your internal network settings, your internal applications will be accessible from any origin.

</div>

## Front-end Registration

You can configure the IP address that the front-end server registers in the deployment controller service. This setting is useful for servers with multiple network adapters, allowing you to select on which network the OutSystems services communicate with each other.

Configuration  |  Description  |  Default value  
---|---|---  
Local IP Address | The list displays all IPs available for the front-end server you are configuring. | `(automatic)`
