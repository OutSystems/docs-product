---
guid: 7f720bcf-3fae-49c7-bce8-9349abb192d4
locale: en-us
summary: Use the MCP agent to explain an O11 module, map dependencies, and surface security, performance, and quality issues in Service Studio.
figma:
coverage-type:
  - understand
content-type:
  - conceptual
topic:
app_type: reactive web apps
platform-version: o11
audience:
  - Developer
  - Business analyst
  - Product owner
tags:
  - AI
  - Agentic
  - Data Model
  - Logic
  - Performance
  - Screens
  - Security
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# Understand a module

With OutSystems MCP, the agent in your MCP host explains an O11 module, maps its dependencies, and surfaces security, performance, compliance, and quality issues. The agent reads the module you have open in Service Studio, together with the elements it uses from referenced modules, and leaves the module unchanged.

These requests apply when you take over a module, plan a change to a shared element, or review code quality. They also apply when you frame or review work on a module as a product owner or business analyst. You describe what you want to know in business terms, and the agent reads the module to answer. Each section gives an example request and describes what the agent reads to answer it. For reusable versions of these requests, refer to [Prompt blueprints](prompt-blueprints.md).

Before you ask, connect your MCP host to the Service Studio MCP server, and open the module in Service Studio 11.55.91 or later. For the setup, refer to [Get started with OutSystems MCP](get-started.md).

The agent's answers are AI-generated interpretations of what it reads from the module. Verify a finding in Service Studio before you act on it.

## Read scope

Reads are scoped to the module you have open in Service Studio. The agent works from that module alone, so open the module you want it to analyze before you start a session.

For an element that the module uses from a referenced module, such as an entity or an action, the agent reads the element's signature. To analyze the logic and data model of a referenced module, open that module in Service Studio.

## Module explanation

Ask the agent to explain what the open module does and how it's structured. For example:

* "Walk me through what this module does and how it's structured."

The agent reads the module's data model, logic, and screens from Service Studio to answer.

The explanation reflects the module's current structure, including for a module you didn't build. The agent works from the contents of the module, which stay current when separate documentation goes out of date.

## Dependency map

Ask what the open module depends on, and which parts of the module use an element you plan to change. For example:

* "What does this module depend on, and which screens and actions in this module use this action?"

The agent traces references across the entities, actions, and screens of the open module, and reads the signatures of the elements the module uses from referenced modules.

This dependency map reflects the module at the moment you ask. Modules that consume the open module are outside the map. To analyze a consumer module, open it in Service Studio.

## Security, performance, and compliance review

The agent reviews the open module for security, performance, and compliance concerns, including in code that someone else wrote. For example:

* "Are there any security, performance, or compliance concerns in this module?"

The agent reviews the module's logic with the same reads it uses to explain the module.

## Dead code detection

The agent finds dead code in the open module. For example:

* "Find dead code in this module."

This gives you a baseline before you invest time cleaning up a module, so you can prioritize the parts that carry the most risk first.

The agent checks usage inside the open module. A public element that only other modules use appears unused from inside the module. Check the consumer modules before you remove a public element.

## Specification drafts

Use the agent's explanation of a module to draft specifications for new work. The agent writes this documentation from the same reads it uses to explain a module to a developer, so it reflects the module's structure at the moment you ask. For example:

* "Describe the architecture of this module, including its screens, entities, and main actions, in terms a business analyst can review."

Name the entities or screens your request concerns, so the agent focuses on them. For a ready-made request, refer to the architecture overview blueprint in [Prompt blueprints](prompt-blueprints.md#generate-a-module-architecture-overview).

OutSystems MCP doesn't store this documentation. Ask the agent to write it again whenever the module changes, so your specifications reflect the module's current state.
