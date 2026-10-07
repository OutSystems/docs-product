---
guid: 444b0502-093e-4ee9-a95b-52bae30f5830
locale: en-us
summary: OutSystems MCP in O11 and ODC differ in where the MCP server runs, who changes the app model, and how a change is reviewed.
figma:
coverage-type:
  - understand
  - evaluate
content-type:
  - conceptual
topic:
  - outsystems-mcp-o11-odc
app_type: reactive web apps
platform-version: o11
audience:
  - Architect
  - Developer
  - Tech lead
tags:
  - Agentic
  - AI
  - Architecture
  - C#
  - Deploy
  - Development lifecycle
  - Mentor
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# OutSystems MCP in O11 and ODC

OutSystems MCP connects the agent in your MCP host to OutSystems through the Model Context Protocol (MCP), in both OutSystems 11 (O11) and OutSystems Developer Cloud (ODC). The two implementations differ in where the MCP server runs, what the agent works on, who changes the app model, and how a change is reviewed.

Use this page if you work on both platforms and want to know which guidance applies where. Each section compares one aspect of the two implementations. For the ODC side, refer to [OutSystems MCP](https://www.outsystems.com/tk/redirect?g=acf55a04-48ee-4732-bfca-ce3938a72020) in the ODC documentation.

The following table summarizes the differences:

| Aspect | O11 | ODC |
| --- | --- | --- |
| MCP server | The Service Studio MCP server, on your machine | The OutSystems MCP server, hosted by OutSystems for your tenant |
| Scope | The module you have open in Service Studio | Your tenant and the full app lifecycle |
| App model changes | The agent, through the OutSystems Model API | Mentor, the OutSystems AI, on the agent's behalf |
| Change review | **Compare and Merge**, set by **Write permissions** | The ODC lifecycle, with confirmation before publish, deploy, or rollback |

## MCP server location

In O11, your MCP host connects to the Service Studio MCP server, a local MCP server that runs inside Service Studio on your machine. In ODC, your MCP host connects to the OutSystems MCP server, a remote MCP server that OutSystems hosts for your tenant, and you sign in with your ODC identity.

The O11 connection needs network access only for your MCP host's own connection to its model provider. In ODC, every call reaches the OutSystems cloud. This difference matters when you evaluate OutSystems MCP for an isolated or air-gapped O11 environment.

## Scope

In O11, the agent reads and changes an existing application, one module at a time: the module you have open in Service Studio. In ODC, the agent works across your tenant and the full application lifecycle. It creates an app from a template, changes an existing app, and publishes and deploys the result.

In O11, the agent works on applications you've already built. In ODC, the agent also builds an app in an empty tenant.

## App model changes {#who-changes-the-app-model}

In O11, the agent changes the module itself. It writes C# code that uses the OutSystems Model API and sends that code to the Service Studio MCP server, which runs it on a copy of the module. The OutSystems skill for O11 tells the agent how to write that code.

In ODC, the agent delegates each change to Mentor, the OutSystems AI that edits the app model on the OutSystems side. The agent describes the change, and Mentor makes it.

## Change review

In O11, a change from the agent merges through the same **Compare and Merge** window a manual change goes through, as the **Write permissions** setting determines. For the settings and who publishes under each one, refer to [Write review](security-data-handling.md#write-review).

In ODC, a change runs through the ODC lifecycle and audit trail, tied to ODC Portal roles and permissions. Before a publish, deploy, or rollback, the agent is instructed to restate the operation and wait for your confirmation. Every change produces a record you can trace to the user whose identity authorized it, the same as a change from ODC Portal or ODC Studio.
