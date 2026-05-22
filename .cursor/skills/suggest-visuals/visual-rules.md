# Visual asset rules

Coverage-type is the primary driver. Audience shapes diagram type and complexity.

## Coverage type: Asset decision

| Coverage type | Goal | Recommended asset | Mermaid-eligible? | Rationale |
| --- | --- | --- | --- | --- |
| remember | Aid recall of key terms, concepts, or component relationships | Compact diagram (`mindmap` or `flowchart TD`) — or a summary table for purely textual recall | ✅ Yes | A small visual structures the mental model and works as a quick reference |
| understand | Explain a concept, architecture, or the theory behind a feature | Diagram (`flowchart`, `sequenceDiagram`, or `architecture`) | ✅ Yes | Concepts and relationships are easier to grasp visually than in prose |
| evaluate | Compare options, trade-offs, or suitability | Comparison table — or `flowchart LR` with decision branches when the comparison is procedural | ✅ Yes | Side-by-side structure makes trade-offs scannable |
| apply | Demonstrate how to perform a task | Annotated screenshots in sequence | ⚠️ Default no | UI-driven steps need exact product context; a diagram rarely adds value once the user is clicking through screens. An orientation diagram is OK if the procedure spans multiple products or surfaces |
| unblock | Show what went wrong and what a fix looks like | Annotated screenshots (error state + corrected state) | ⚠️ Default no | Troubleshooting needs the literal error in the product, not an abstraction |

**Key insight:** Use screenshots for tactical, hands-on instructions (apply, unblock).
Use diagrams for strategic, conceptual explanations (understand, evaluate, remember).

## Audience → complexity and focus

| Audience | Complexity / Focus |
| --- | --- |
| Architect | High-level, abstract; system-wide scope |
| Business analyst | User-experience flow, business process |
| Developer | Code-level; API calls, data processing |
| Front-end developer | UI flow, state management, client-side calls |
| Platform administrator | Infrastructure, deployment topology, environment containment |
| Product owner | Feature overviews, business workflows |
| Tech lead | Detailed; code flow, API integrations, system patterns |

Diagram type is driven by what the section is about (process, interaction, hierarchy, topology), not by audience. Use the Diagram type reference for that decision; the audience row above shapes the _altitude_ of the diagram (which nodes to show, how much to abstract).

## Diagram type reference

| Mermaid Type | Best For |
| --- | --- |
| `flowchart TD` | Hierarchies, top-down processes, concept trees |
| `flowchart LR` | Left-to-right pipelines, linear workflows |
| `sequenceDiagram` | Multi-actor interactions, API calls, auth flows |
| `architecture` | Infrastructure, component topology |
| `erDiagram` | Data models, entity relationships |
| `mindmap` | Concept overviews, mental models |
