---
guid: d0d5deb2-77b3-4c57-9a09-f97a2ba8c2ad
locale: en-us
summary: A prompt blueprint is a reusable prompt for a named read workflow, a module architecture overview, a tech debt report, or an onboarding summary.
figma:
coverage-type:
  - understand
  - apply
content-type:
  - reference
topic:
app_type: reactive web apps
platform-version: o11
audience:
  - Architect
  - Business analyst
  - Developer
  - Product owner
tags:
  - AI
  - Agentic
  - Architecture
  - Templates
  - Technical Debt
  - Workflows
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# Prompt blueprints

A prompt blueprint is a reusable prompt for a named read workflow, a module architecture overview, a tech debt report, or an onboarding summary. Each blueprint names the capability it targets, which keeps it valid as the tool set changes between releases.

Each blueprint runs on the module you have open in Service Studio. You copy the example prompt into your MCP host, adjust it to your module, and use the output to plan work, assess quality, or bring a colleague up to speed. Blueprints only read the module, so the module stays unchanged.

## Generate a module architecture overview

This blueprint asks the agent to map an open module's structure, dependencies, and entities into an architecture overview. Use one of the following example prompts:

* "Walk me through what this module does and how it's structured."
* "What does this module depend on, and which screens and actions in this module use this action?"

Use this blueprint when you start work on a module you didn't build. It also produces a plain-language explanation you can share with a colleague who doesn't use Service Studio.

Both a developer new to a module and a non-developer role trying to understand a module can use this same blueprint. It draws on the same reads either way.

## Generate a tech debt report

This blueprint asks the agent to report an open module's dead code and its security, performance, and compliance issues. Use one of the following example prompts:

* "Find dead code in this module."
* "Are there any security, performance, or compliance concerns in this module?"

Use this blueprint to baseline a module's quality before you plan a refactor, or to decide what to fix first.

This blueprint surfaces issues in a module regardless of who wrote it, including a module built by someone else on your team.

## Generate an onboarding summary

This blueprint asks the agent to summarize an open module for a role new to it. For example:

* "Generate onboarding documentation for this module."

Use this blueprint to bring a new team member up to speed, or to give a non-developer role enough context to draft their own requirements.

The agent generates this summary from the module's current structure, whether or not separate documentation for the module exists. The summary is an AI-generated interpretation, so review it before you share it.
