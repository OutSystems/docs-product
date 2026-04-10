---
name: content-creation-flow
description: Step-by-step content creation workflow for documentation and training materials. Includes MCP validation, discovery, content design, Jira planning, and draft generation with priority-based execution. Use when starting the content creation flow, creating documentation or training materials, or when the user asks to follow the content creation workflow.
isautopublish: true
---

# Content creation flow rules

This assistant must follow a step-by-step content creation flow.
After each step, the user must explicitly confirm before proceeding to the next step.
Do not move forward without confirmation.

## Step 0 — Validate MCP connections

### Objective

Ensure all required MCP servers are **reachable and operational** before starting any content creation tasks.

### Instructions

1. Run a status or health check only against the MCP servers listed below, using the following specific tool for each:
    * **Atlassian MCP Server:** Use the `atlassianUserInfo` tool
    * **Figma MCP Server:** Use the `whoami` tool
    * **outsystems-tech-content MCP Server:** Use the `check_health` tool
    * **GitHub MCP Server:** Use the `get_me` tool
    * Do **not** perform any write operations.
1. Collect and report the results for each MCP server:
    * Server name
    * Connection status (`Available` / `Unavailable`)
    * Any errors or warnings returned
1. Stop immediately if:
    * Any required MCP server is unavailable
    * Authentication fails
    * Partial or inconsistent connectivity is detected

### Output requirements

* Present a clear, structured summary of MCP server availability.

* Do **not** proceed to the next step automatically.

### Confirmation gate

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

Search for issues containing:

* User feedback or knowledge gaps from the "R&D TK Feedback" project (Key: RDTKF) on the "R&D TK Feedback Board"
* Product Board details from the project with key RPOR, where some Product Board content is mirrored. Search for tickets, epics, or initiatives that match the topic or initiative the user is querying about. Use initiative names, feature names, or topic keywords to find relevant entries. Extract any context, goals, requirements, or strategic rationale that can inform the content being created.
* Enablement needs, requirements, or documentation related to the topic in any other project or board in Jira

**Important:** When listing Jira tickets as data sources, always include the full link to each ticket (not just the ticket name/key).

#### Confluence

Search for:

* Enablement strategies
* Existing content related to the context being developed

**Important:** When listing Confluence pages as data sources, always include the full link to each page (not just the page name).

If Confluence pages contain Figma links:

* Identify them and use the Figma MCP to retrieve any relevant context

#### Figma node discovery

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

#### Current workspace projects

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

### Work item structure

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

### Target audiences

Before creating the work items table, define a **Target Audiences** section that lists all target audiences for the entire content piece. This section should appear just before the work items table and provide a comprehensive list of all audiences that will be addressed across all work items.

### For each content work item, define

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

After user validation is approved, create the content design page, following the Content Design templates listed above, on Confluence in a space with the name "Technical Knowledge team" (key: "TK").
Place the content design page in the following folder structure (create the folder structure if not present):

* For training: AI Generated > AI Online Training > Content Design
* For documentation:  AI Generated > AI Documentation > Content Design

**Do not proceed to Step 3 without explicit approval.**

## Step 3 — Jira planning

### Project and board selection

**Before creating any Jira tickets, ask the user which Jira project and board should be used:**

* **For testing purposes:** Jira project "R&D Demo" (key: "RD") on the board "Demo Problems"
* **For production tickets:** Jira project "Technical Knowledge Team" (key: "TK") on the board "Technical Knowledge Board"

**Do not proceed with ticket creation until the user has explicitly selected a project and board.**

Once the user has selected the project and board, create the following items:

* Dedicated epic for this content piece, where all tickets should be grouped in
* All required Jira tickets for each of the work items

### Ticket naming convention

All Jira tickets must follow this naming pattern:
**Pattern:** `[Work type] Ticket name/description - Content-type`

**Examples:**

* `[Apply Peer Feedback + SME Review + Apply SME Feedback] AI agent actions quiz - Quiz`
* `[Draft] Creating an agent in ODC Studio - Article`
* `[Peer Review] Introduction to AI Agents - Slide Deck`
* `[Outline] Build the Intake Agent Exercise - Exercise`
* `[SikuliX script] Building a simple agent - Demo`

**Work type values:** Outline, Draft, Visual Assets Creation from Draft, Peer Review, Apply Peer Feedback + SME Review + Apply SME Feedback, Visual Assets Review, SikuliX script, Publish

**Content-type values:** Article, Procedure, Concept, Overview, Troubleshooting, Reference, Slide Deck, Demo, Exercise, Quiz, Visual Assets

### Ticket ladder by content type

For **each** work item, use the list below that matches that work item’s **content type** (from Step 2).

**Documentation / Slide Deck / Quiz:**

* Draft ticket
* Peer Review ticket
* Apply Peer Feedback + SME Review + Apply SME Feedback ticket
* Visual Assets Review ticket
* Publish ticket

**Demo:**

* Outline ticket
* SikuliX script ticket
* Peer Review ticket
* Apply Peer Feedback + SME Review + Apply SME Feedback ticket
* Publish ticket

**Exercise:**

* Outline ticket
* Draft ticket
* Peer Review ticket
* Apply Peer Feedback + SME Review + Apply SME Feedback ticket
* Visual Assets Review ticket
* Publish ticket

#### Ticket to Jira issue type mapping

Use this mapping when choosing the Jira issue type for each ticket activity:

| Activity | Jira issue type |
| --- | --- |
| Outline | Task |
| Draft | User Story |
| SikuliX script | User Story |
| Peer Review | Peer Review |
| Apply Peer Feedback + SME Review + Apply SME Feedback | Task |
| Visual Assets Review | Peer Review |
| Publish | Task |

If an activity from this flow is not listed in the table above, choose the closest mapped activity and ask the user to confirm before creating tickets.

#### Story points by Jira work type

Use the following baseline SP values as the default estimate for each ticket type:

* Outline ticket: `3`
* Draft ticket: `5`
* SikuliX script ticket: `5`
* Peer Review ticket: `1`
* Apply Peer Feedback + SME Review + Apply SME Feedback: `3`
* Visual Assets Review: `3`
* Publish ticket: `0`

These values are recommendations. Adjust one level up or down when justified by scope, complexity, or risk.
Use this decision flow for each ticket estimate:

1. Identify the ticket work type.
1. Apply the baseline SP value.
1. Adjust one level up or down if justified.
1. If estimate exceeds `8`, split the work and re-estimate each split ticket.
1. Confirm estimates in the Step 3 validation gate before creation.

**Note**: On **TK** and **RD** , Story Points use REST field is `customfield_10004`.

### Sprint planning

#### Objective

Assign every ticket to a Jira sprint so delivery matches team cadence, capacity, and the sequential **blocked by** chain.

#### TK sprint naming (technical knowledge board)

On boards that follow the TK convention, sprint names use a fixed pattern so you can infer **order** and **calendar placement** from the title.

The pattern is:

`TK` + two-digit year + `.` + quarter + `.` + sprint number within that quarter

* **Year:** Last two digits of the calendar year (for example, `26` is 2026).
* **Quarter:** `Q1`, `Q2`, `Q3`, or `Q4`.
* **Sprint number:** The **n**th two-week sprint in that quarter, counting from `1`.

**Example:** `TK 26.Q2.1` is the **first** two-week sprint of **Q2** of **2026**. Sprints are **two weeks** long.

Sprints are created on the board to match this scheme; use the **exact** sprint name from Jira when assigning issues.
**Note**: On **TK** and **RD**, Sprint uses REST field `customfield_10006` (set to the sprint’s numeric id).

#### Mapping tickets to sprints

For each work item, use the **ticket order** already defined in **Ticket ladder by content type** (earlier in this step). Assign sprints by walking that list from **first ticket to last**, in the same order as the sequential **blocked by** chain.

Use these **allocation rules** on top of that order:

* **One stage per sprint** by default: the first ticket in the ladder goes in the **current** sprint (or the earliest agreed sprint with the user), the next ticket in the following sprint, and so on—unless the user agrees to a different cadence.
* If the ladder has **more** stages than **available** sprints, walk the ladder in order: assign **one** ticket per sprint across consecutive available sprints until you reach the **last** available sprint, then assign **all** remaining tickets to that **last** sprint. **Blocked by** order still applies: a ticket’s sprint must be the same as or later than the sprints of all tickets that block it.

#### Instructions

1. Resolve sprint names and dates with the user from the **selected board** (current sprint and upcoming sprints). When the board uses the TK convention, interpret and order sprints using **TK sprint naming** above. If the board uses different naming, map stages to those sprints while preserving ladder order.
1. Assign **each** ticket to **one** sprint using **Ticket ladder by content type** and the allocation rules above.
1. Verify sprint dates do not violate **blocked by** order: a ticket’s sprint must be the **same as or later than** the sprints of all tickets that block it.
1. Summarize sprint assignments in the Step 3 validation gate (ticket key, summary, sprint name or identifier).

### User assigning

#### Default assignee

Except where **Peer Review and Visual Assets Review exceptions** apply, assign **every** issue you create in Step 3—the **Epic** and **all** work-item tickets to the **current user**: the person running this content creation flow. Use the Jira identity that matches that person when the Atlassian tools expose or require an assignee field.

#### `Peer Review` and `Visual Assets Review` exceptions

For tickets whose **work type** in the naming convention is **Peer Review** or **Visual Assets Review** (refer to **Ticket naming convention** and **Ticket ladder by content type**), do **not** use the default assignee.

Before creating **each** of those issues, ask the user **which** Jira user must be the assignee. Accept whatever identifier the user provides that your Jira integration can resolve (for example, email, account ID, or display name—match what the Atlassian MCP or Jira metadata supports).

#### Instructions

1. Before or during Step 3.3, collect assignees for every **Peer Review** and **Visual Assets Review** ticket from the user.
1. Add the full assignee plan (default user plus each named reviewer ticket) to the Step 3 validation summary alongside sprint planning.
1. When calling `createJiraIssue`, set assignee using the correct Jira field for the project and issue type (confirm field keys from issue metadata when needed).

### Required labelling

All tickets created in this step must include labels based on the target repository scope:

* Always add the `AI-TK` label.
* If the work item targets `training-internal`, add the `Training` label to each ticket in that work item.
* If the work item targets documentation repositories, add the `Documentation` label to each ticket in that work item.

### Blocked by rules

When creating tickets, configure the Linked work items field by using the "is blocked by" option according to the following rules:

**1. Sequential blocking within a work item:**

Each ticket in a work item should be blocked by the previous ticket in the sequence. This ensures work flows sequentially through the stages.

**Examples:**

* Draft ticket → blocked by Outline ticket
* Peer Review ticket → blocked by Draft ticket
* Apply Peer Feedback + SME Review + Apply SME Feedback ticket → blocked by Peer Review ticket
* Visual Assets Review ticket → blocked by Apply Peer Feedback + SME Review + Apply SME Feedback ticket
* Publish ticket → blocked by Visual Assets Review ticket

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

* Selected Jira project and board
* Sprint structure
* Ticket breakdown
* Story point mapping and estimates per work type
* Sprint planning
* Jira ticket to user assignment

### Creating Jira issues

After user validation is approved, verify the connection to the Atlassian MCP Server before creating tickets:

1. **Check Atlassian MCP Server connection:**
    * Run a test call to verify the Atlassian MCP Server is accessible and authenticated
    * If the connection fails or returns authentication errors, **stop immediately** and ask the user to re-authenticate
    * Do **not** proceed with ticket creation until the connection is verified and working

Once the connection is verified, create the Jira issues using the Atlassian MCP Server. Do NOT loop, ask for additional confirmation, or delay. Execute the creation steps below in sequence.

#### Step 3.1: Get cloud ID

1. Call `mcp_Atlassian-MCP-Server_getAccessibleAtlassianResources` to retrieve the cloudId
1. Use the cloudId from the response (typically: `"3755dbe1-fa22-4c37-956e-59bea84af9cf"`)

#### Step 3.2: Create epic

**Create the Epic FIRST** using `mcp_Atlassian-MCP-Server_createJiraIssue` with these exact parameters:

```json
{
  "cloudId": "3755dbe1-fa22-4c37-956e-59bea84af9cf",
  "projectKey": "[Selected project key from user, e.g., 'RD' or 'TK']",
  "issueTypeName": "Epic",
  "summary": "[Content Piece Title from Step 2]",
  "description": "[Full content design description from Step 2 Confluence page, in Markdown format]",
  "additional_fields": {
    "labels": ["AI-TK"]
  }
}
```

**Data mapping for Epic:**

* `projectKey`: Use the project key selected by the user in the Project and Board Selection step (e.g., "RD" for testing or "TK" for production)
* `summary`: Use the main title/topic from the content design created in Step 2
* `description`: Use the full content design description from the Confluence page created in Step 2 (convert to Markdown if needed)
* Store the returned Epic key (e.g., `RD-123` or `TK-456`) for reference

#### Step 3.3: Create all work-item issues

**For EACH work item** defined in Step 2, create the required tickets from **Ticket ladder by content type**. Use `mcp_Atlassian-MCP-Server_createJiraIssue` for each issue.

**For each issue, set:**

* **Issue type:** Use **Ticket to Jira issue type mapping** (`User Story`, `Peer Review`, or `Task`—not every issue is a Task).
* **Labels:** Follow **Required labelling** (`AI-TK`, plus `Training` or `Documentation` per work item target).
* **Sprint:** Follow **Sprint planning** (correct sprint for that ticket’s stage).
* **Assignee:** Follow **User assigning** (default user vs reviewer-picked assignees).
* **Story points:** Follow **Story points by Jira work type**; use the project’s Story Points custom field and allowed values (`0`, `1`, `3`, `5`, `8`). Resolve field keys from Jira issue metadata before creating issues.

Example payload shape (replace placeholders; add sprint, assignee, and story points in `additional_fields` using the keys your project uses):

```json
{
  "cloudId": "3755dbe1-fa22-4c37-956e-59bea84af9cf",
  "projectKey": "[Selected project key from user, e.g., 'RD' or 'TK']",
  "issueTypeName": "[User Story | Peer Review | Task from Ticket to Jira issue type mapping]",
  "summary": "[Work type] [Work item name/description] - [Content-type]",
  "description": "[Work item description from Step 2, including target audiences, content sources, and any relevant details, in Markdown format]",
  "parent": {
    "key": "[Epic key from Step 3.2, e.g., RD-123 or TK-456]"
  },
  "additional_fields": {
    "labels": ["AI-TK", "Training"]
  }
```

Add sprint, assignee, and story-point keys your project uses to `additional_fields` (names vary by Jira project).

**Note:** All work-item issues MUST link to the Epic from Step 3.2. Use the `parent` parameter with the Epic key (e.g., `"parent": { "key": "RD-123" }` or `"parent": { "key": "TK-456" }`).

**Data mapping for work-item issues:**

* `summary`: Follow **Ticket naming convention**: `[Work type] Ticket name/description - Content-type`
    * Work type: Outline, Draft, Peer Review, Apply Peer Feedback + SME Review + Apply SME Feedback, Visual Assets Review, SikuliX script, Publish (and any other value from **Work type values** in that section)
    * Content-type: Article, Procedure, Concept, Overview, Troubleshooting, Reference, Slide Deck, Demo, Exercise, Quiz, Visual Assets
    * Work item name: The name/title of the work item from Step 2
* `additional_fields`: Must include:
    * `labels`: `AI-TK` plus `Training` or `Documentation` per **Required labelling**
    * Story Points field (key from metadata) with the estimate from **Story points by Jira work type** and allowed values (`0`, `1`, `3`, `5`, `8`)
    * Sprint field (key from metadata) per **Sprint planning**
    * Assignee field (key from metadata) per **User assigning**
* `description`: Include:
    * Work item description from Step 2
    * Target audiences (from the work item)
    * Content sources (with full links)
    * Priority level
    * Target GitHub repositories
    * Any other relevant details from the work item
    * Format as Markdown

**Execution order:**

1. Create all tickets for Priority 1 work items first
1. Then create all tickets for Priority 2 work items
1. Continue in priority order (3, 4, etc.)
1. For each work item, create tickets in the order given in **Ticket ladder by content type** for that work item’s content type

**Store all created ticket keys** (e.g., `RD-124`, `RD-125` or `TK-456`, `TK-457`, depending on the selected project) for the blocked-by relationship mapping.

#### Step 3.4: Document blocked-by relationships

After all tickets are created, output a comprehensive table showing:

* Each ticket key and summary
* All tickets it should be blocked by (sequential and priority-based)
* This enables manual creation of blocked-by links in Jira

#### Step 3.5: Update Confluence content design

Update the Confluence Content Design page created in Step 2:

1. Add the Epic link to the page
1. Add each work-item issue link to its corresponding work item in the Content Design table
1. Format Jira links using `<custom data-type="smartlink">` tags:
    * Example: `<custom data-type="smartlink">https://outsystemsrd.atlassian.net/browse/RD-123</custom>` or `<custom data-type="smartlink">https://outsystemsrd.atlassian.net/browse/TK-456</custom>` (use the actual ticket keys created)

**Do not proceed to Step 4 without explicit approval.**

## Step 4 — Draft generation & PR creation

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
    * **Strictly follow** the documentation style guide:
        * `.github/doc-styles/formatting.md`
        * `.github/doc-styles/tone.md`
        * `.github/doc-styles/structure.md`
    * If something regarding the writing style isn't covered in the documentation style guide, use Google Dev's writing style.
    * **Important:** `.github/copilot-instructions.md` is an index that points to the current style guide files.
1. **Using Figma nodes as data sources:**
    * Reference Figma nodes discovered in Step 1 when creating content that requires visual elements
    * Use `mcp_Figma_get_design_context` to retrieve design code, component descriptions, and design tokens from relevant Figma nodes
    * Use `mcp_Figma_get_screenshot` to get visual representations of diagrams or designs
    * Extract and incorporate visual assets, diagrams, or design patterns from Figma nodes into the documentation
    * Include Figma URLs in the frontmatter `figma` field when the content references a specific Figma design
    * Convert Figma design code to match the target project's technology stack and styling system when needed
    * Save extracted images or diagrams to the appropriate images directory in the repository
1. **Frontmatter guidelines:**
    * When generating drafts on **NEW** files, leave the `guid` field in the frontmatter empty. For changes to existing files, leave the `guid` as it is.
    * The `guid` will be automatically generated later through a GitHub action automation
    * Ensure frontmatter includes all required fields as specified in the repository's validation rules (and any applicable guidance referenced by `.github/copilot-instructions.md`).
1. Ensure all generated content aligns with:
    * Jira planning details
    * Assigned priorities
    * Agreed scope and acceptance criteria
1. **Content structure and formatting validation:**
    * Content structure matches the approved design
    * Language, tone, and formatting strictly follow the documentation style guide referenced by `.github/copilot-instructions.md`
    * Follow all structure, formatting, and file naming rules in the documentation style guide
    * Ensure all generated content complies with the project's Vale and markdownlint rules
    * **Vale rule updates:** When Vale validation reports issues of type **ERROR** that cannot be resolved by changing the content (because the rule itself needs updating - exceptions), update the corresponding Vale rule file in the `docs-validation` repository. The `docs-validation` repository is included in the workspace, so rule files can be edited directly. For instance, if `OutSystems.Headings` incorrectly flags "JSON" in "Building JSON strings" title as a capitalization error, but "JSON" is a valid acronym that should remain uppercase, add "JSON" to the exception list in `docs-validation/styles/OutSystems/Headings.yml`. After modifying the corresponding rule, commit the changes and create a pull request in the `docs-validation` repository. Note that the rule changes will not take effect in the documentation repositories until the PR is merged in `docs-validation` and the changes are synced to those repositories.
    * No unapproved assumptions or scope expansion are introduced
1. **Repository iteration and PR creation:**
    * Iterate over all repositories in the current workspace that were identified in Step 2 as needing updates
    * For each repository, perform the necessary changes for all tickets that target that repository
    * For each ticket:
        * Create a local branch and make the necessary changes
        * **Before committing, ask the user to validate the draft changes:**
            * Present a summary of the changes made (files created/modified, key content updates)
            * Show the diff or key changes for review
            * Explicitly ask: "Please review the draft changes for [ticket name]. Do you approve these changes to proceed with committing and creating the pull request?"
        * **Do not commit or proceed with the pull request until the user explicitly approves the draft changes**
        * After user approval, commit the changes
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
    * Strictly follow `.github/doc-styles/visual-assets.md`

### Pull request rules

* Create one Pull Request per Jira ticket
* PR title must include the ticket number as prefix

**Example:** `TK-123: Draft Async Processing Guide`

* **Before creating a PR, push the local branch to the remote repository:**
    * Ensure all changes are committed to the local branch
    * Push the branch to the remote repository using `git push -u origin <branch-name>`
    * Only after the branch exists on the remote, create the Pull Request
* **When creating PRs in GitHub, include a label called "AI-TK" on each PR**
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
