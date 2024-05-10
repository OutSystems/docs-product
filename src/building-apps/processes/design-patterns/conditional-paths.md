---
summary: Explore conditional path design in OutSystems 11 (O11) using the Decision tool for process flow management.
locale: en-us
guid: 5a27b7c6-3710-4a8b-807b-6b71e26670d1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=269:3
---
# Designing Conditional Paths

Use this pattern to design multiple paths where only one of them is followed in the process flow. Use the [Decision](<../../../ref/lang/auto/class-decision.md>) tool to design this pattern.

When the process is executed, it follows the path of the connector corresponding to the **Outcome** of the **Decision**.


## Example

As an example, think of a recruitment process that ends taking one of two actions: send an email if the candidate is approved or does nothing if not approved.

![Diagram showing conditional branches in a recruitment process flow with two paths: one for approved candidates leading to an email notification, and another for non-approved candidates leading to no action.](images/conditional-braches.png "Conditional Branches in a Process Flow")

In this example there are two named connectors, therefore, two outcomes have to be defined in the flow of the **Decision**:

![Screenshot of the Decision tool interface with two defined outcomes for a recruitment process flow.](images/decision-flow.png "Decision Flow Outcomes") 
