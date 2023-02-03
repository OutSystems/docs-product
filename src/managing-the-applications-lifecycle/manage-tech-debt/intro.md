---
tags: article-page
summary: Learn how to manage the technical debt of your applications at every stage of the development lifecycle.
en_title: Manage technical debt
locale: en-us
guid: 7aa53270-fb01-4543-90e4-57907dcc68fe
app_type: traditional web apps, mobile apps, reactive web apps
---

# Manage technical debt

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>

AI Mentor Studio (https://aimentorstudio.outsystems.com/) is the OutSystems technical debt monitoring tool. It enables IT leaders to visualize complex cross-portfolio architectures and identify problems while also helping developers follow best practices and avoid common pitfalls.

As organizations strive to expedite time-to-market and empower non-professional developers (citizen developers) to create business apps themselves, controlling technical debt naturally becomes a top concern.

With AI Mentor Studio, technical debt can be effectively managed at every stage of the development lifecycle so that when departmental applications evolve to become enterprise-wide solutions, nothing needs to be rewritten.

For architects and development team leaders, it provides an integrated, bird’s eye view of their organization’s technical debt to identify problem areas and prioritize accordingly. Developers can view detailed reports on what best practices are being violated, their impact, and how to fix them.

To integrate AI Mentor Studio's data with third-party tools, use the [AI Mentor Studio API](../../ref/apis/auto/ai-mentor-studio-api.final.md). 

## What AI Mentor Studio analyzes

AI Mentor Studio analyzes the code produced by developers and provides insights regarding code quality that may impact team agility.  

### Code Analysis

AI Mentor Studio runs a set of predefined rules throughout the produced low-code, with the goal of uncovering code patterns in the following categories:

* Performance
* Architecture
* Maintainability
* Security

[Check here for the list of patterns currently being analyzed ](https://success.outsystems.com/Support/Enterprise_Customers/Support_Tools/Architecture_Dashboard/Code_Patterns)

#### Architecture auto-classification

AI Mentor Studio is self-sufficient when it comes to analyzing the architecture of the apps in your infrastructure. With the help of an AI engine, AI Mentor Studio analyzes a module's code and its relationships to identify where it fits in the overall architecture.

AI auto-classification allows you to onboard factories into the AI Mentor Studio and classify each module so that it fits into the right architecture layer. Having the right architecture classification is important as it enables all other code analysis. 

By default, all new infrastructures added to AI Mentor Studio use AI auto-classification. You also have the option of turning AI auto-classification off, however, this means that for architecture classification, you must have Discovery installed.

## Access to AI Mentor Studio features

The availability or scope of some features of AI Mentor Studio depend on the OutSystems Edition associated with your infrastructure:

Teams
:   The ability to filter the app portfolio and technical debt findings per LifeTime team is available for Standard and Enterprise Editions.

Debt Time Machine
:   The ability to check all the history of technical debt analysis is available for Standard and Enterprise Editions. Basic Editions can access one month of technical debt analysis history.

Infrastructures associated with a Free Edition can't use AI Mentor Studio.

## How to access AI Mentor Studio

Before you can start using AI Mentor Studio your infrastructure and your IT user must be associated with AI Mentor Studio. Learn about the [prerequisites and how to set up AI Mentor Studio](how-setup.md).

To access AI Mentor Studio, go to [https://aimentorstudio.outsystems.com/](https://aimentorstudio.outsystems.com "https://aimentorstudio.outsystems.com") and login with your OutSystems account.
