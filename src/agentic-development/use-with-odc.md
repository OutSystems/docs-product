---
guid: 0b834f38-0760-4736-803d-3ed56d5089e7
locale: en-us
summary: Keep OutSystems MCP requests on O11 when your MCP host also connects to ODC. Recognize the Service Studio MCP server, name the platform, and restore missing tools.
figma:
coverage-type:
  - understand
  - apply
content-type:
  - conceptual
topic:
  - name-platform-in-requests
  - outsystems-mcp-o11-odc
  - restore-missing-o11-tools
app_type: reactive web apps
platform-version: o11
audience:
  - Developer
  - Architect
  - Tech lead
tags:
  - AI
  - Agentic
  - Troubleshooting
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# Use OutSystems MCP in O11 alongside ODC

When your MCP host connects to the Service Studio MCP server and to the OutSystems MCP server for OutSystems Developer Cloud (ODC), the agent has tools for both platforms. This page covers the O11 side. It explains how to recognize the Service Studio MCP server, how to word requests so that they reach it, and what to check when the O11 tools are missing.

For the ODC side, refer to [OutSystems MCP](https://www.outsystems.com/tk/redirect?g=acf55a04-48ee-4732-bfca-ce3938a72020) in the ODC documentation. For a comparison of the two products, refer to [OutSystems MCP in O11 and ODC](compare-o11-odc.md).

## Prerequisites

Before you work with both platforms from one MCP host, make sure the following are in place:

* The Service Studio MCP server is connected in your MCP host, and the OutSystems skill for O11 is installed. Refer to [Get started with OutSystems MCP](get-started.md).
* The OutSystems MCP server for ODC is connected in the same MCP host. Refer to [Get started with OutSystems MCP](https://www.outsystems.com/tk/redirect?g=3d7c70ce-dbd2-47ee-a927-76b6009b0b84) in the ODC documentation.

## The Service Studio MCP server

The following facts identify the O11 side, so that you recognize which tools and prompts belong to it:

* **Name in your MCP host:** The server appears as `servicestudio`.
* **Where it runs:** Inside Service Studio on your machine, on the local loopback address. Refer to [Local endpoint and port](outsystems-mcp-overview.md#local-endpoint-and-port).
* **When it's available:** After you start it in the **MCP Server** window, or when Service Studio opens if you turn on **Start when Service Studio opens**.
* **What it works on:** The module you have open in Service Studio.
* **How a change reaches the module:** The agent writes the change as Model API code, and the **Write permissions** setting controls how it merges. Refer to [Write review](security-data-handling.md#write-review).
* **Approval:** Service Studio asks you to approve each new agent session. Refer to [Connection approval](outsystems-mcp-overview.md#connection-approval).

## Name the platform in your requests

A request such as "Add a DueDate attribute to the Task entity" doesn't state which platform it targets. State the platform, and for O11 the module you have open in Service Studio. For example:

* "In the O11 module open in Service Studio, add a DueDate attribute to the Task entity."
* "Summarize the O11 module open in Service Studio."

For a first request that confirms the connection, refer to [Verify the connection](get-started.md#verify-the-connection).

## Restore missing O11 tools

The Service Studio MCP server is available only while it runs. While it's stopped, your MCP host has no O11 tools, and the agent has only the tools of other OutSystems servers, such as the one for ODC. A request meant for an O11 module can then reach ODC. Before you ask for a change, confirm that the O11 tools are available, and name the platform in your request.

To restore the O11 tools, follow these steps:

1. In Service Studio, open the module you want to work on.
1. Go to the **Edit** menu > **MCP Server**.
1. Select **Start MCP server**. The port status changes to **Running**.
1. Confirm that the endpoint in your MCP host matches the **URL** field of the **MCP Server** window.

To start the server every time you open Service Studio, turn on **Start when Service Studio opens**.

Some MCP hosts load an MCP server only in the folder where you registered it. If the O11 tools are missing in a different folder, check how your MCP host scopes MCP servers.

## Instruction files

Some MCP hosts read the OutSystems skill from a shared instruction file, such as `AGENTS.md` or `.github/copilot-instructions.md`. The OutSystems skill for ODC uses these files in some MCP hosts too.

Before you install the OutSystems skill for O11, check whether the file already exists and whether it holds another OutSystems skill. Keep the existing content. For the installation steps, refer to [Install the OutSystems skill for O11](get-started.md#install-the-outsystems-skill-for-o11).

## Approval and sign-in prompts

With both servers connected, you see two kinds of prompts. The approval prompt in Service Studio belongs to OutSystems MCP in O11. Refer to [Connection approval](outsystems-mcp-overview.md#connection-approval). A sign-in in your browser belongs to OutSystems MCP in ODC.

## Next steps

Continue with the page that fits your task:

* To understand how OutSystems MCP in O11 differs from OutSystems MCP in ODC, refer to [OutSystems MCP in O11 and ODC](compare-o11-odc.md).
* To ask the agent about an O11 module, refer to [Understand a module](understand-a-module.md).
* To look up the terms that differ between the platforms, refer to [Agentic development terminology](agentic-development-terminology.md#context-dependent-terms).
