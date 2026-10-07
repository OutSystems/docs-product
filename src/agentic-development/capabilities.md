---
guid: 6e74b8a7-7908-4096-a0ea-feaf4e9a3e60
locale: en-us
summary: Examples of what the agent in your MCP host reads and changes in an O11 module through OutSystems MCP, grouped by task.
figma:
coverage-type:
  - remember
  - understand
content-type:
  - reference
topic:
  - outsystems-mcp-capabilities
app_type: reactive web apps
platform-version: o11
audience:
  - Developer
  - Architect
  - Tech lead
tags:
  - Agentic
  - Blocks
  - Data Model
  - Logic
  - Screens
  - Web
  - Widgets
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# OutSystems MCP capabilities

The agent in your MCP host reads and changes an O11 module through the tools that the Service Studio MCP server exposes. This page groups examples of those capabilities by task: the data model and logic, screens and web blocks, other module elements, changes to the module, and advanced reads.

Use this page to plan a request before you connect an MCP host, or to check whether a task fits what OutSystems MCP in O11 supports. The examples apply to the modules you have open in Service Studio and the elements they use from referenced modules. The examples are representative, not a complete list, and the exact tool set changes between releases.

## Reference scope

The Service Studio MCP server publishes its exact, current tool list, and your MCP host shows that list. This page groups examples by task instead of by tool name, so the examples stay valid when a tool changes.

Reads and changes both apply to the module you have open in Service Studio. For more information about connecting your MCP host, refer to [Get started with OutSystems MCP](get-started.md). For more information about example prompts, refer to [Understand a module](understand-a-module.md).

## Data model and logic

The agent reads a module's data model, for example entities, attributes, foreign keys, and identifiers, including ones reached through referenced modules. The agent reads structures the same way.

For logic, the agent reads server actions, client actions, and service actions, including each action's full flow from start to finish. This lets the agent trace what a specific action does, beyond confirming that the action exists.

## Screens and web blocks

The agent reads a module's screens and web blocks: their layout, widgets, and screen-level actions.

Traditional Web modules use a different shape for screens and web blocks than Reactive modules do. The Service Studio MCP server reports each module's style. The OutSystems skill for O11 instructs the agent to read the shape for that style, so the same request works for both styles. A Traditional Web module gets a smaller set of reads than a Reactive module does, for example screens, web blocks, themes, email templates, and external sites.

## Other module elements

The agent also reads other parts of a module's configuration, for example:

* Client and session variables
* Email templates and external sites
* Events and event handlers
* Exceptions
* Images, resources, and scripts
* Integrations
* Locales
* Roles
* Site settings
* Themes
* Timers

The agent reads each of these elements the same way as the data model and logic. The agent retrieves the current definition from the module, reflecting the state Service Studio holds when you ask.

## Module changes

The write capabilities on this page are Beta Features. Reads are Generally Available. Refer to [Capability status](outsystems-mcp-overview.md#capability-status).

The agent also changes the module you have open, the same as a change you make yourself in Service Studio. For example, when the agent renames an action, every place the module uses that action shows the new name. A change merges into the module according to the **Write permissions** setting in the **MCP Server** window. For the settings and who publishes under each one, refer to [Write review](security-data-handling.md#write-review).

The agent also discards a pending change before it merges, and refreshes the module's references to their latest version, the same as the **Refresh All** action in the **Manage Dependencies** window.

## Advanced reads

For a question that the other reads don't cover, the agent runs a custom query on the module's structure. This covers a cross-cutting request that spans several kinds of objects at once.

The agent also checks a module for validation problems, filtered to errors, warnings, or informational messages. For an edge case that no other read covers, the agent retrieves an object's raw internal representation.
