# Content creation flow rules

This assistant must follow a step-by-step content creation flow.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Step 0 — Validate MCP Connections

### Objective

Ensure all required MCP servers are **reachable and operational** before starting any content creation tasks.

### Instructions

1. Enumerate all configured MCP servers available to the assistant.
1. Run a status or health check against each MCP server.
   * Use the server's native status, ping, or lightweight test call.
   * Do **not** perform any write operations.
1. Collect and report the results for each MCP server:
   * Server name
   * Connection status (`Available` / `Unavailable`)
   * Any errors or warnings returned
1. Stop immediately if:
   * Any required MCP server is unavailable
   * Authentication fails
   * Partial or inconsistent connectivity is detected

### Output Requirements

* Present a clear, structured summary of MCP server availability.

* Do **not** proceed to the next step automatically.

### Confirmation Gate

After presenting the results, explicitly ask:

> All MCP connections have been validated.  
> Do you want to proceed to Step 1?

The assistant **must wait for explicit user confirmation** before continuing.

## Step 1 — discovery

### Objective

Identify and validate all relevant source materials needed to build documentation or training content.

### Actions

Analyse and decompose the user prompt into searchable portions that could be searched using the available tools.

#### MCP source discovery

From each configured MCP source, retrieve around 5–10 links that best match the user's initial prompt.

For each link:

* Provide a brief summary
* Explain how it relates to the user's request

**Important:** When good data sources contain links to additional content, evaluate those links for possible valuable knowledge about the work piece. Follow and analyze linked content that may provide relevant information.

#### GitHub MCP

Search documentation and training repositories to identify:

* Existing documentation or training relevant to the topic
* Gaps, missing coverage, or improvement opportunities

#### OutSystems tech content MCP

* Perform semantic + keyword search
* Intersect results with GitHub findings
* Highlight overlaps and discrepancies

#### Jira

Search for tickets containing:

* User feedback or knowledge gaps from the "R&D TK Feedback" project (Key: RDTKF) on the "R&D TK Feedback Board"
* Enablement needs, requirements, or documentation related to the topic in any other project or board in Jira

**Important:** When listing Jira tickets as data sources, always include the full link to each ticket (not just the ticket name/key).

#### Confluence

Search for:

* Enablement strategies
* Existing content related to the context being developed

**Important:** When listing Confluence pages as data sources, always include the full link to each page (not just the page name).

If Confluence pages contain Figma links:

* Identify them and use the Figma MCP to retrieve any relevant context

#### Figma Node Discovery

Search for relevant Figma design nodes that can serve as visual sources of data for the content being created. These Figma nodes can be used as sources of data in Step 4 when drafting content.

**Steps to discover Figma nodes:**

1. **Search existing documentation for Figma references:**
   * Use `grep` or codebase search to find all Figma links in the workspace projects
   * Search for patterns like `figma.*node-id` or `figma.com/design` in markdown files
   * Extract Figma file keys and node IDs from existing documentation related to the topic

1. **Identify related node IDs:**
   * Look for Figma node IDs in documentation files that cover similar or related topics
   * Note the file key (e.g., `6G4tyYswfWPn5uJPDlBpvp`) and node IDs (e.g., `8737:1784` or `8737-1784`)
   * Collect node IDs that might contain relevant diagrams, workflows, or visual content

1. **Explore Figma file structure:**
   * Use `mcp_Figma_get_metadata` to explore known node IDs and their parent/child relationships
   * Get metadata for canvas or frame nodes to understand the file structure
   * Look for related nodes in the same canvas or nearby in the file hierarchy

1. **Get design context for relevant nodes:**
   * Use `mcp_Figma_get_design_context` to retrieve design code and context for nodes that match the topic
   * Use `mcp_Figma_get_screenshot` to get visual representations of diagrams or designs
   * Extract component descriptions, design tokens, and visual assets from relevant nodes

1. **Document discovered Figma nodes:**
   * For each relevant Figma node found, document:
     * Full Figma URL (e.g., `https://www.figma.com/design/6G4tyYswfWPn5uJPDlBpvp/Building-apps?node-id=8737-1784`)
     * Node ID and file key
     * Brief description of what the node contains (diagram, workflow, component, etc.)
     * How it relates to the content being created
     * Any design context, code, or assets extracted from the node

1. **Validate and prioritize:**
   * Review all discovered Figma nodes for relevance
   * Prioritize nodes that contain:
     * Diagrams or workflows directly related to the topic
     * Visual content that can enhance documentation
     * Design patterns or components that illustrate concepts
   * Note which nodes should be used as sources in Step 4

**Important:**

* When listing Figma nodes as data sources, always include the full Figma URL (not just the node ID)
* Extract and save any visual assets (screenshots, diagrams) that will be needed in Step 4
* Document the design context and component descriptions that can inform the content structure

#### Current Workspace Projects

Since one of the sources of data is the current workspace, check all projects currently included in the workspace for data regarding the content creation that is going to undergo:

* Search across all workspace projects for existing documentation, training materials, or related content
* Identify relevant files, sections, or resources that relate to the topic
* Note any existing content that could be referenced, updated, or extended
* Document findings from each workspace project

### Output

Present to the user:

* A validated list of source links (including Figma node URLs)
* Identified knowledge gaps
* Figma nodes discovered with their descriptions and relevance
* Clear readiness to proceed to design

### Mandatory user validation

Ask the user to:

* Confirm the selected sources, or
* Provide additional documentation links

**Do not proceed to Step 2 without explicit approval.**

## Step 2 — content design

### Objective

Ingest the content from the relevant source materials identified in Step 1.
Design the content structure and delivery plan, following the Content Design template structure.

Use examples for guidance:

* **Content Design template:** [Content Design template](https://outsystemsrd.atlassian.net/wiki/spaces/TK/pages/5317820691/template+Content+Design)
* **Content Design template (without Enablement Strategy):** [Content Design template without Enablement Strategy](https://outsystemsrd.atlassian.net/wiki/spaces/TK/pages/5412651265/template+Content+Design+without+Enablement+Strategy) — Use this template when creating a content design for a piece that doesn't have a dedicated enablement strategy
* **Training example:** [Async Processing ODC](https://outsystemsrd.atlassian.net/wiki/spaces/TK/pages/4837605449/Async+Processing+ODC+WIP)
* **Documentation example:** [Content Design Data interoperability](https://outsystemsrd.atlassian.net/wiki/spaces/TK/pages/5590777881/Content+Design+Data+interoperability+read+write+SQL+Server)

### Work Item Structure

Arrange work items in a table of contents-like order, not priority ordered, where there can be multiple top levels and nested work items. Each work item should be created as a releasable item.

Once the table is created, assign each work item its priority and target releasable versions, with nested children that can be released at a later date.

**Priority Example:**

```
Main work 1 - priority 1
  Child work 1 - priority 3
  Child work 2 - priority 4
Main work 2 - priority 1
  Child work 1 - priority 2
Main work 3 - priority 2
```

Work items with priority 1 (MVP) should be followed by work items with priority 2 and so on.

### Target Audiences

Before creating the work items table, define a **Target Audiences** section that lists all target audiences for the entire content piece. This section should appear just before the work items table and provide a comprehensive list of all audiences that will be addressed across all work items.

### For Each Content Work Item, Define

**Content type:**

* Demo
* Slide Deck
* Quiz
* Exercise
* Article (for documentation)

**Coverage type:**

* Remember
* Understand
* Apply
* Evaluate
* Unblock

**Reference:**
[Coverage Types Explained](https://outsystemsrd.atlassian.net/wiki/spaces/TK/pages/3621161365/Coverage)

**Target GitHub repositories:**

Specify which GitHub repositories will need to be updated for each work item. For example:

* If creating documentation: specify the documentation repository (e.g., `docs-next`, `docs-product-internal`, `docs-support-internal`, `docs-howtos-internal`, `docs-eap`)
* If creating training content (Exercise, Demo, Slide Deck, Quiz): specify the training repository (e.g., `training-internal`)
* If a work item requires updates to multiple repositories, list all of them

**Examples:**

* Documentation article → `docs-next` repository
* Exercise → `training-internal` repository
* Documentation article + Exercise → `docs-next` and `training-internal` repositories

**Target audiences:**

Specify the target audiences for each work item. This should be a column in the work items table, indicating which audiences from the overall Target Audiences section apply to this specific work piece.

**Content sources:**

Include content sources with matching links for each work item. When referencing Jira tickets or Confluence pages, always provide the full link (not just the name/key).

Assign the correct priorities to all items, if no particular priority specified by the User.

### Mandatory user validation

Ask the user to:

* Confirm the content design
* Confirm priorities and scope

After user validation is approved, create the content design page on Confluence in a space with the name "Test" (personal). Search by space name, not key.
Place the content design page in the following folder structure (create the folder structure if not present):

* For training: Online Training > Content Design
* For documentation: Documentation > Content Design

**Do not proceed to Step 3 without explicit approval.**

## Step 3 — Jira Planning

Create the following items in the Jira project "R&D Demo" (key: "RD") on the board "Demo Problems":

* Dedicated epic for this content piece, where all tickets should be grouped in
* All required Jira tickets (all tickets must include the "AI-TK" label)

### Ticket Naming Convention

All Jira tickets must follow this naming pattern:

**Pattern:** `[Content-type] Ticket name - work type`

**Examples:**

* `[Quiz] AI agent actions quiz - SME Review`
* `[Article] Creating an agent in ODC Studio - Draft`
* `[Slide Deck] Introduction to AI Agents - Peer Review`
* `[Exercise] Build the Intake Agent Exercise - Outline`
* `[Demo] Building a simple agent - SikuliX script`

**Content-type values:** Article, Procedure, Concept, Overview, Troubleshooting, Reference, Slide Deck, Demo, Exercise, Quiz, Visual Assets

**Work type values:** Outline, Draft, Peer Review, SME Review, Visual Assets, SikuliX script

### Define Required Jira Tickets Based on Content Type (per work item)

**Slide Deck / Quiz:**

* Draft ticket
* Peer Review ticket
* SME Review ticket
* Visual Assets ticket

**Demo:**

* Outline ticket
* SikuliX script ticket
* Peer Review ticket
* SME Review ticket

**Exercise / Documentation:**

* Outline ticket
* Draft ticket
* Peer Review ticket
* SME Review ticket
* Visual Assets ticket

**Documentation:**

* Draft ticket
* Peer Review ticket
* SME Review ticket
* Visual Assets ticket

### Blocked By Rules

When creating tickets, configure the Linked work items field by using the "is blocked by" option according to the following rules:

**1. Sequential blocking within a work item:**

Each ticket in a work item should be blocked by the previous ticket in the sequence. This ensures work flows sequentially through the stages.

**Examples:**

* Draft ticket → blocked by Outline ticket
* Peer Review ticket → blocked by Draft ticket
* SME Review ticket → blocked by Peer Review ticket
* Visual Assets ticket → blocked by SME Review ticket (or the appropriate previous ticket in the sequence)

**2. Priority-based blocking across work items:**

The first ticket of each work item (e.g., Outline ticket or Draft ticket, depending on content type) should be blocked by all first tickets of work items with higher priority.

**Examples:**

* All Priority 2 first tickets → blocked by all Priority 1 first tickets
* All Priority 3 first tickets → blocked by all Priority 2 first tickets
* All Priority 4 first tickets → blocked by all Priority 3 first tickets
* And so on...

This ensures that higher priority work items are completed before lower priority ones can begin.

**3. Manual blocked-by link creation:**

Since the Atlassian MCP Server does not currently provide a tool to create links between issues, the assistant must output a comprehensive list of all tickets and their blocked-by relationships after creating the tickets.

The output should include:

* A table or list showing each ticket (with ticket key and title)
* All tickets that each ticket should be blocked by
* Clear indication of both sequential blocking (within work items) and priority-based blocking (across work items)

This list enables manual creation of the blocked-by links in Jira after ticket creation.

Ensure tickets align with:

* Content types
* Review stages
* Assigned priorities
* Blocked by relationships (both sequential and priority-based)

### Mandatory user validation

Ask the user to confirm:

* Sprint structure
* Ticket breakdown

After user validation is approved, create the required items on Jira. Update the Confluence page Content Design Table created in Step 2 with the matching Jira links for each work piece to keep track of progress.

**Important:** When adding Jira links to the Content Design table, format them using `<custom data-type="smartlink">` tags (e.g., `<custom data-type="smartlink">https://outsystemsrd.atlassian.net/browse/TK-12345</custom>`) so that Confluence displays them as inline cards with the ticket data.

**Do not proceed to Step 4 without explicit approval.**

## Step 4 — Draft Generation & PR Creation

### Objective

Create content drafts and open a pull request that strictly follow the approved scope, style, and execution rules.

### Instructions

1. Generate content drafts **only** after all previous steps have been completed and explicitly approved.
1. **Priority-based draft generation:**
   * Generate drafts following the order of priorities assigned in Step 2
   * First, generate all drafts for tickets with priority 1
   * Then, generate all drafts for tickets with priority 2
   * Continue in priority order (3, 4, etc.) until all drafts are completed
   * This ensures MVP content (priority 1) is completed before lower priority items
1. Create drafts in strict compliance with:
   * The **approved design**
   * The **defined style guide**
   * The **Copilot instruction rules**
1. **Writing Style:**
   * **Strictly follow** all writing style guidelines defined in `.github/copilot-instructions.md` when available
   * If something regarding the writing style isn't covered in `.github/copilot-instructions.md`, use Google Dev's writing style
   * **Important:** Review the copilot-instructions.md file before generating drafts to ensure compliance with all style rules
1. **Using Figma nodes as data sources:**
   * Reference Figma nodes discovered in Step 1 when creating content that requires visual elements
   * Use `mcp_Figma_get_design_context` to retrieve design code, component descriptions, and design tokens from relevant Figma nodes
   * Use `mcp_Figma_get_screenshot` to get visual representations of diagrams or designs
   * Extract and incorporate visual assets, diagrams, or design patterns from Figma nodes into the documentation
   * Include Figma URLs in the frontmatter `figma` field when the content references a specific Figma design
   * Convert Figma design code to match the target project's technology stack and styling system when needed
   * Save extracted images or diagrams to the appropriate images directory in the repository
1. **Frontmatter guidelines:**
   * When generating new drafts, leave the `guid` field in the frontmatter empty
   * The `guid` will be automatically generated later through a GitHub action automation
   * Ensure frontmatter includes all required fields as specified in the repository's validation rules and `.github/copilot-instructions.md` if applicable
1. Ensure all generated content aligns with:
   * Jira planning details
   * Assigned priorities
   * Agreed scope and acceptance criteria
1. **Content structure and formatting validation:**
   * Content structure matches the approved design
   * Language, tone, and formatting strictly follow `.github/copilot-instructions.md` guidelines
   * Follow all structure, formatting, and file naming rules specified in `.github/copilot-instructions.md`
   * Ensure all generated content complies with the project's Vale and markdownlint rules
   * No unapproved assumptions or scope expansion are introduced
1. **Repository iteration and PR creation:**
   * Iterate over all repositories in the current workspace that were identified in Step 2 as needing updates
   * For each repository, perform the necessary changes for all tickets that target that repository
   * For each ticket, create a local branch, make changes, and commit them
   * **Push each branch to the remote repository** before creating the Pull Request
   * Create one Pull Request per Jira ticket
   * Each PR should correspond to exactly one ticket created in Step 3
   * The goal is to have multiple PRs from each repository in order to conclude the whole content creation flow
   * **Remember:** Follow priority order when creating PRs (all priority 1 PRs first, then priority 2, etc.)
1. **Table of Contents (toc.yml) maintenance:**
   * When adding new documentation pages, **always** review and update the `toc.yml` file to include the new page reference in the appropriate section
   * When removing documentation pages, **always** review and update the `toc.yml` file to remove the corresponding reference
   * Ensure the new or removed file reference is placed in the correct hierarchical location within the `toc.yml` structure
   * The `toc.yml` update should be included in the same PR as the content changes (file addition or removal)
   * Verify the file path in `toc.yml` matches the actual file location in the repository
1. **Visual assets guidelines:**
   * Strictly follow the "Instructions for OutSystems Visual Assets" section in `.github/copilot-instructions.md`

### Pull Request Rules

* Create one Pull Request per Jira ticket
* PR title must include the ticket number as prefix

**Example:** `TK-123: Draft Async Processing Guide`

* **Before creating a PR, push the local branch to the remote repository:**
    * Ensure all changes are committed to the local branch
    * Push the branch to the remote repository using `git push -u origin <branch-name>`
    * Only after the branch exists on the remote, create the Pull Request
* Iterate through all repositories in the current workspace that require updates
* Group changes by repository and create PRs accordingly
* Ensure all PRs for a given repository are created before moving to the next repository

## Global constraints

* Never skip steps
* Never assume approval
* Always reference the current step explicitly
* Ask clarifying questions if required inputs are missing
* Do not invent sources, tickets, or priorities
* If new information becomes available at any step, update all affected previous steps accordingly. For example:
    * If in Step 4 you gain access to a new source of data, update Steps 2, 3, and 4 based on the changes that the new source provides
    * If anything changes in Step 2 or Step 3, reevaluate all steps that follow it
