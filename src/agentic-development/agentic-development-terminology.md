---
guid: de84c486-6008-47c8-8970-e507f9bd81d5
locale: en-us
summary: Definitions of the terms used across OutSystems MCP in O11, including MCP host, agent, Service Studio MCP server, the OutSystems skill for O11, and Compare and Merge.
figma:
coverage-type:
  - remember
  - understand
content-type:
  - reference
topic:
  - mcp-terminology
app_type: reactive web apps
platform-version: o11
audience:
  - Developer
tags:
  - Agentic
  - AI
  - MCP
  - Terminology
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# Agentic development terminology

This page defines the terms that the OutSystems MCP pages for OutSystems 11 (O11) use. Each definition explains what the term means and links to the related page. Use this page to look up a term. It also explains terms whose meaning depends on the context, such as OutSystems MCP, which names related but different setups in O11 and ODC.

## OutSystems MCP and its parts

The following terms name OutSystems MCP in O11 and the parts it consists of.

| Term | Definition |
| ---- | ---------- |
| MCP Server window | The Service Studio window where you start and stop the Service Studio MCP server, turn on **Start when Service Studio opens**, and set **Write permissions**. You open it from **Edit** > **MCP Server**. Refer to [Start the Service Studio MCP server](get-started.md#start-the-service-studio-mcp-server). |
| OutSystems MCP | In O11, the OutSystems capability that lets the agent in an MCP host read and change the module you have open in Service Studio. OutSystems MCP in O11 has two parts: the Service Studio MCP server and the OutSystems skill for O11. Refer to [OutSystems MCP](outsystems-mcp-overview.md). |
| OutSystems skill for O11 | The instructions that tell the agent how to use the Service Studio MCP server tools and how to write changes with the OutSystems Model API. The skill uses the `SKILL.md` format. Refer to [Install the OutSystems skill for O11](get-started.md#install-the-outsystems-skill-for-o11). |
| Service Studio MCP server | The local MCP server that runs inside Service Studio on your machine. It accepts connections only on the loopback address, exposes the OutSystems tools, and runs each tool call on the module you have open. Refer to [Local endpoint and port](outsystems-mcp-overview.md#local-endpoint-and-port). |

## MCP terms

The following terms describe the parts that connect your AI application to Service Studio. MCP host, MCP client, and tool come from the Model Context Protocol (MCP) specification, which defines how AI applications connect to external tools. Agent follows common usage in AI tools.

| Term | Definition |
| ---- | ---------- |
| Agent | The AI model that your MCP host uses through its model provider. The agent interprets your requests, calls OutSystems tools, and reports the results to you. In O11, the agent writes each change as Model API code. In ODC, the agent delegates each change to Mentor, the OutSystems AI. Refer to [MCP host and agent roles](outsystems-mcp-overview.md#mcp-host-and-agent-roles). |
| MCP client | The component inside the MCP host that maintains a dedicated connection to one MCP server. The MCP host creates one MCP client for each MCP server it connects to. Refer to the [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture). |
| MCP host | The AI application you work in. The MCP host sends your requests to the agent and passes the agent's tool calls to MCP servers. It also manages your session and holds the MCP configuration that points to the Service Studio MCP server. Refer to [Supported MCP hosts](outsystems-mcp-overview.md#supported-mcp-hosts). |
| Model Context Protocol (MCP) | An open protocol that connects AI applications to external tools and data. MCP defines three roles: the MCP host, the MCP client, and the MCP server. Refer to the [MCP architecture overview](https://modelcontextprotocol.io/docs/learn/architecture). |
| Tool | A function that an MCP server exposes for the agent to call, such as a read of the data model or a change to the module. Refer to [OutSystems MCP capabilities](capabilities.md). |

## Changes to a module

The following terms name how a change from the agent reaches your module.

| Term | Definition |
| ---- | ---------- |
| Beta Feature | A non-final OutSystems capability that OutSystems provides to collect customer feedback. A Beta Feature can change significantly, including through breaking changes, or OutSystems can discontinue it. In OutSystems MCP in O11, write capabilities are Beta Features and reads are Generally Available. Refer to [Capability status](outsystems-mcp-overview.md#capability-status). |
| Compare and Merge | The Service Studio window where you review a change before it reaches the module. With the default **Write permissions** setting, every change from the agent opens **Compare and Merge**. Refer to [Write review](security-data-handling.md#write-review). |
| Connection approval | The Service Studio dialog, **Allow AI agent to connect?**, that asks you to approve a new agent session before the agent reads or changes the module. Refer to [Authorize the connection](get-started.md#authorize-the-connection). |
| Model API | The OutSystems C# API for reading and changing an application model. The agent writes a change as Model API code, and the Service Studio MCP server runs that code on a copy of the module. Refer to [App model changes](compare-o11-odc.md#who-changes-the-app-model). |
| Modified copy | The copy of the module that holds the agent's pending changes. Reads from the agent return the modified copy until the change merges or is discarded. Refer to [Write review](security-data-handling.md#write-review). |
| Write permissions | The **MCP Server** window setting that controls how a change from the agent merges. **Manual review changes in compare and merge** is the default, and **Allow automatically merge and publish** merges without review. Refer to [Write review](security-data-handling.md#write-review). |

## Context-dependent terms

Some terms mean different things depending on the context they appear in, such as O11, ODC, or the wider AI industry. Each of the following entries names the contexts and the term these pages use in each one.

| Term | Definition |
| ---- | ---------- |
| Harness | In AI engineering, an agent harness is the software around an AI model that runs its tool loop and manages its memory and context. Each MCP host includes its own agent harness. In some OutSystems setup guides and skill files, harness means the MCP host. These pages use MCP host for the application you work in. Refer to the entry for MCP host on this page. |
| OutSystems MCP | In O11, OutSystems MCP connects the agent to the Service Studio MCP server on your machine and works on the module you have open. In ODC, OutSystems MCP connects the agent to an MCP server that OutSystems hosts for your tenant and works across the tenant. Refer to [OutSystems MCP in O11 and ODC](compare-o11-odc.md). |
| OutSystems MCP server | In ODC, the remote MCP server that OutSystems hosts for your tenant. In O11, the MCP server runs inside Service Studio, and these pages call it the Service Studio MCP server. Refer to the entry for Service Studio MCP server on this page. |
