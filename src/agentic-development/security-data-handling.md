---
guid: 80185e8e-0ce7-4e36-a700-5b45a991b93f
locale: en-us
summary: OutSystems MCP in O11 runs locally in Service Studio. Learn what data leaves your machine, how changes are reviewed, and which records an agent session leaves.
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
  - Architect
  - Tech lead
  - Platform administrator
tags:
  - Agentic
  - AI
outsystems-tools:
  - service studio
helpids:
isautopublish: true
---

# Security and data handling

This page describes how OutSystems MCP in OutSystems 11 (O11) handles your data, which controls apply to an agent session, and which records the session leaves. Use it to assess OutSystems MCP in a security or risk review.

OutSystems MCP in O11 is a deterministic tool layer that runs on your machine. The agent in your MCP host calls a defined set of tools. The Service Studio MCP server translates each call into an operation on the application model and returns a structured result. Your MCP host sends your prompts to its model provider, and the model selects which tool to call. OutSystems runs no model and no inference in this flow.

## Data flow

The Service Studio MCP server runs inside Service Studio on your machine and binds only to the loopback address `127.0.0.1`, so other machines on your network don't reach it. Reads operate on a snapshot of the module in a folder in your local temp directory. Only your operating system account has access to that folder. When you discard a change from the agent, or Service Studio drops one, the modified copy stays in that folder as a full copy of the module.

The following traffic leaves your machine during an agent session:

* Your MCP host's calls to its model provider.
* Service Studio's calls to your O11 environment when you publish a change. These are the same calls a manual publish makes.
* Service Studio's telemetry to OutSystems. Refer to [Telemetry](#telemetry).

No OutSystems-hosted service receives your application model. For this reason, OutSystems MCP in O11 works in on-premises and air-gapped installations.

## Model provider

The only model in the flow is the model your MCP host uses. Your agreement with that model provider and your MCP host's data settings govern how the provider processes your prompts, including any module content the agent adds to them.

Treat the call from your MCP host to its model provider as the point where module content leaves your machine. OutSystems doesn't receive your prompts, transcripts, or module files, and doesn't use them for training, fine-tuning, evaluation, or product improvement. Service Studio also sends a limited set of telemetry to OutSystems. Refer to [Telemetry](#telemetry).

## Telemetry

Service Studio sends usage and diagnostic data about OutSystems MCP to OutSystems. The following list describes what the data contains:

* **Usage events:** The Service Studio MCP server starts. You approve or reject a connection. You change **Start when Service Studio opens** or **Write permissions**. A change merges automatically, the module's references refresh, or a publish succeeds or is refused.
* **Tool calls:** For each call, the tool name, the name of the MCP host, the name of the module, the duration, and whether the call succeeded. Session tokens are shortened to their first characters.
* **Diagnostics:** The first 200 characters of the code or query that the agent sends, a fingerprint of the full text, and the outcome. When an error occurs, the error message and its stack trace.

The data doesn't include your prompts or your conversation with the agent. The previews and error messages come from the code, queries, and errors themselves, so they include any module element names that appear in them. OutSystems processes these events under its standard product telemetry practices.

## Data exposure

OutSystems MCP exposes the same model elements you see and change in Service Studio, for both reads and changes. Elements outside that boundary aren't available to the agent.

Your existing O11 access model controls what an agent session reaches. An agent session reaches only the environments and modules that the developer can access, and works on the module open in Service Studio.

The agent reads the default value of a site property, including a site property with **Is Secret** set to **Yes**. That default value becomes part of any prompt the agent sends to its model provider. To keep a secret out of the agent session, leave the default value empty in the module and set the value per environment in Service Center.

## Privileges and authentication

OutSystems MCP runs inside Service Studio under your operating system account and privileges, and requests no elevation. The processes Service Studio starts run under the same account.

Authentication uses Service Studio's existing mechanisms. You sign in to the environment before any tool call runs, and every change goes through the standard O11 lifecycle and validation. The agent makes only the changes you can make yourself in Service Studio.

## Write review

A change from the agent never applies directly to your module. Each change produces a modified copy first, and a separate merge step brings that copy into your module. The **Write permissions** setting in the Service Studio **MCP Server** window determines how that merge runs.

Until a change merges or is discarded, reads from the agent return the modified copy. The agent reads its own pending changes before they reach the module.

When you edit the module in Service Studio while a change from the agent is pending, Service Studio keeps your edit and drops the pending change without merging it. To make the dropped change, the agent applies it again to a fresh snapshot that includes your edit.

The following table describes each setting:

| Setting | Behavior |
| --- | --- |
| **Manual review changes in compare and merge** | The default setting. Opens the **Compare and Merge** window for every change, including a change with no conflicts. The change reaches the module after a developer accepts it. |
| **Allow automatically merge and publish** | Merges a change without the confirmation step, and lets the agent publish the module. A developer turns this setting on explicitly. |

Each developer sets **Write permissions** in their own Service Studio installation. If your policy restricts unattended merges, include this setting in your internal development standards.

With the default setting, you publish the merged change from Service Studio. With either setting, the publish runs under your identity through the standard O11 lifecycle. For the configuration steps, refer to [Get started with OutSystems MCP](get-started.md). For the review process, refer to [Merging and versioning](../building-apps/merge/intro.md).

## Input validation

Prompt-injection protection starts in your MCP host. The agent selects the operation before the tool call reaches the Service Studio MCP server. The prompt-injection controls, model policies, and content filtering you apply to your MCP host are the primary safeguard.

The Service Studio MCP server applies the following controls to every tool call:

* Validates the arguments of every tool call and rejects invalid or unsafe operations.
* Rejects a tool call that doesn't carry the session token from an approved connection.
* Restricts write code to the OutSystems Model API and accepts imports only from the `OutSystems.Model` namespace.
* Rejects write code that accesses files, processes, environment variables, the registry, the network, reflection, or interop, before the code runs.
* Keeps internal properties out of reach and blocks changes to runtime behavior.
* Accepts connections only on the loopback address.
* Requires a developer to approve each new agent session in Service Studio. Refer to [Connection approval](outsystems-mcp-overview.md#connection-approval).
* Stops a tool call that exceeds the configured execution timeout.

With the default **Write permissions** setting, a change also passes a developer's review in **Compare and Merge** before it reaches the module. **Allow automatically merge and publish** removes that review step. Weigh that trade-off when you set the team standard for this setting.

## Audit records

An agent session produces two complementary records. The following list describes each one:

* **Your MCP host's session log:** Records each tool call, its arguments, and its result, when your MCP host provides enterprise logging.
* **Service Center and LifeTime:** Record each published change with the developer's identity and a timestamp, the same as a manual change.

Service Center and LifeTime attribute a change from the agent to the developer whose session made it, and record agent changes and manual changes the same way. To identify which changes the agent made, use your MCP host's session log.

## Compliance scope

OutSystems MCP in O11 runs inside Service Studio on the developer's machine and adds no OutSystems-hosted service to the data flow. For the data that leaves your machine, refer to [Data flow](#data-flow) and [Telemetry](#telemetry).

OutSystems Cloud certifications cover OutSystems-hosted infrastructure. The machine that runs Service Studio sits in your infrastructure, so your organization manages its infrastructure and operational security controls, the same as for any other on-premises component.
