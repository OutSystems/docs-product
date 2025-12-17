# Instructions for documentation

## General guidelines for grammar and content

Follow these guidelines to ensure consistent and high-quality documentation.

### Tone and voice

Use the appropriate tone and voice in your content. Your content must be:

* Friendly and straightforward
* Clear and concise
* Inclusive and respectful
* Free of jargon and sales talk

### Be brief and concise

Write short sentences and well-structured paragraphs. Don't repeat yourself.

**Example**

**Yes:** The style guide is a document with your brand colors and patterns. The style guide is important for user interface usability and consistency, as well as for adherence to your brand rules.

**No:** The Style Guide is a document with your brand theme colors and patterns ready to use to create a consistent user experience on your applications. It is an essential piece to ensure adherence to your brand rules, user interface consistency, and foster usability. It is designed to guide you through all delivery assets to optimize the development process and user experience.

### Use American English

Use American English. This applies to spelling, word use, and writing dates.

### Use the present tense

Use the present tense whenever possible. Using the present tense helps make sentences clear and straightforward to understand.

**Example**

**Yes:** Click the Save button. The data updates immediately.

**No:** Click the Save button. The data will be updated.

### Capitalization

Use the following rules for capitalization.

#### Common nouns versus proper nouns

Understanding the difference between common nouns and proper nouns is essential for correct capitalization:

**Common noun**: A general person, place, or thing (for example, app, icon, stage). Only capitalize common nouns when they begin a sentence. If a common noun consists of two words, then capitalize only the first word when it starts a sentence.

**Examples**

* **Yes**: Mobile apps help users access information on the go.

* **No**: Mobile Apps help users access information on the go.

**Proper noun**: A specific place, person, or thing. Always capitalize proper nouns.

At OutSystems, a proper noun is typically:

* Something the user named (for example, My Business app)

* A product name (for example, Service Studio)

#### Don't capitalize common nouns

Don't capitalize generic technical terms unless they're part of a proper noun:

* environment, app, module, screen, action

* database, server, cloud, platform

* developer, user, administrator

**Examples**

* **Yes**: 
  1. Configure app settings after deployment.

  1. Click **Save**.

      For more information, refer to the troubleshooting guide

* **No**: 

  1. Configure App Settings After Deployment

  1. Click the **save** button

      For more information, refer To the Troubleshooting Guide

#### Capitalize proper nouns and brand names

Always capitalize:

* Product names: OutSystems, Service Studio, LifeTime, ODC Portal
* Technology names: JavaScript, CSS, HTML, SQL
* Company names: Microsoft, Google, Amazon Web Services
* Service names: Azure Active Directory, Amazon S3

**Examples**

* **Yes**: You can integrate your app with Azure Active Directory using the OutSystems authentication system.

* **No**: You can integrate your app with azure active directory using the outsystems authentication system.

* **Yes**: Deploy your app to the production environment.

* **No**: Deploy your Application to the Production Environment.

#### Special cases

Adhere to these rules for special cases:

* APIs and endpoints: Use the exact capitalization as defined in the API documentation
* Code elements: Maintain original capitalization (variables, functions, classes)
* Abbreviations: Follow standard conventions (HTML, CSS, API, UI, URL)

### Use contractions

Use common contractions instead of full forms. Some of the common contractions you need are: it's, doesn't, there's, can't/cannot.

Contractions help create friendlier and informal sentences, as full forms are generally reserved for formal writing. Avoid making contractions from a noun and a verb, especially with nouns denoting OutSystems products.

**Examples**

**Yes:** Don't use this function to encode text that might get executed as part of the SQL statement.

**No:** Do not use this function to encode text that might get executed as part of the SQL statement.

**Yes:** Iterating more than once over a query result isn't a good practice.

**No:** Iterating more than once over a query result is not a good practice.

**Yes:** LifeTime is an OutSystems management console.

**No:** LifeTime's an OutSystems management console. (No contractions with a noun, here a product name.)

### Use the active voice

The active voice makes the sentence dynamic and clear. It also makes it clear who (the user, the system, and so forth) is doing what.

**Example**

**Yes:** After you validate the new SQL element, delete or deactivate the original Aggregate.

**No:** The original Aggregate is kept in the flow editor for your manual deletion after validating the new SQL element.

### Be careful with modal verbs

Avoid using modal verbs like can, could, may, might, will, shall, would, should, and must when possible. Technical content should confidently describe what the product does. Using a modal often creates a weak and wordy sentence.

**Examples**

**Yes:** OutSystems lets you create several app types.
**No:** There are several app types you can create.

**Yes:** OutSystems handles unforeseen or unhandled errors in applications.
**No:** OutSystems handles unforeseen or unhandled errors that might occur in applications.

### Use second person

Use the second person "you" to address the reader or readers. However, don't overuse it.

Exceptions: Use "I" in FAQs.

When referring to OutSystems, don't use we.

**Examples**

**Yes:** You can deploy and manage apps from the ODC Portal.

**No:** Deployment and app management are handled through the ODC Portal.

**Yes:** You can review the configuration in Service Center.

**No:** Let us review the configuration in Service Center.

**Yes:** How can I prevent accidental activations?

**No:** How can a developer prevent accidental activations? (This is from an FAQ section, where "I" fits well as it's a developer who's asking the question.)

**Yes:** OutSystems recommends backing up your data every 3 months.

**No:** We recommend backing up your data every 3 months.

### Be clear and precise

The language in technical content must be clear and precise. Avoid being vague.

**Examples**

**Yes:** Do the following in all of your apps.
**No:** Some tasks must be used as a rule of thumb.

**Yes:** Error. The library uses an API that's not available.
**No:** Error. The library might be using an API that's not available.

### Keep accessibility in mind

Your content should be accessible to all people, to those without and with disabilities. Be mindful of:

* How you refer to people with disabilities. Use inclusive language.
* How you describe interactions with the user interface. Consider providing alternative methods or steps.
* How you use words to indicate a location (left, right, top, below, up, down) on screen. Provide more context for people using screen-readers.
* How you use the words "easy" and "simple". What may be simple to do for some people may not be simple to do for all.

**Yes:** For more information about accessibility, refer to [Writing for all abilities](https://docs.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).

**No:** For more information about accessibility, see [Writing for all abilities](https://docs.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).

### Don't use the words "sorry" and "please"

Avoid using apologetic or polite filler words in technical documentation.

**Examples**

**Yes:** To view the document, click _View_.
**No:** To view the document, please click _View_.

### Use sentence case for headings and titles

Capitalize the first letter in headings and titles.

**Examples**

**Yes:** Configure app settings after deployment.

**No:** Configure Application Settings After Deployment.

**Yes:** Use Actions to encapsulate logic

**No:** Use Actions to Encapsulate Logic

**Yes:** Bootstrap an Entity using an Excel file

**No:** Bootstrap an Entity Using an Excel File

### Avoid overusing parentheses

Don't put important information in parentheses. Readers may ignore them. If the info is important, use commas, dashes, or separate sentences.

### Serial comma

In a series of three or more items, use a comma before the final "and" or "or".

**Example**

**Yes:** Consider an infrastructure with the following environments: development, preproduction, and production.
**No:** Consider an infrastructure with the following environments: development, preproduction and production.

### Keep it international

Ensure content is accessible to people of different cultures.

* Use plain English.
* Don't use idioms (e.g., "cost an arm and a leg").
* Don't try to be funny.

### Use gender-inclusive language

You should make the gender visible only if it's important to understand the content. This means you shouldn't use words like he/she, himself/herself, man/woman, unless you're referring to a particular individual. Instead, use a non-gender alternative, like plural forms and "they". Furthermore, you shouldn't use language that reinforces stereotypes.

For more details, refer to [Bias-free communication](https://docs.microsoft.com/en-us/style-guide/bias-free-communication) by Microsoft.

**Examples**

**Yes:**

* When developers download a Forge component, they can install it in Service Studio. (Use plural to avoid referring to gender.)
* When a developer downloads a Forge component, they can install it in Service Studio. (Use "they" to refer to a single person without mentioning their gender.)
* When you download a Forge component, install it in Service Studio. (Are your target readers developers? If yes, then "you" is a better choice.)

**No:**

* When a developer downloads a Forge component, he can install it in Service Studio. (Service Studio is not used exclusively by male developers or developers who identify as men.)

### Use standardized example domains

Use `example.com` for domain examples. Do not use real customer domains or other domains.

### Avoid Latin abbreviations

Use "that is" instead of "i.e." and "for example" or "such as" instead of "e.g.".

**Examples**

**Yes:** Design the process behavior, that is, the process flow.

**No:** Design the process behavior, i.e., the process flow.

**Yes:** Make sure the Textarea Input has the Name property set (for example, myTextArea).

**No:** Make sure the Textarea Input has the Name property set (e.g., myTextArea).

### Timeless documentation

Ensure documentation remains relevant by following these practices:

* Avoiding time-based words and phrases: Do not use words like new, now, currently, latest, or future when describing a product's features. These words quickly become outdated and require maintenance.
* Focusing on the current state: The documentation should describe how a product works as if it is the current, stable state, not a recent change.
* Providing a specific reference point (if necessary): If you absolutely must refer to a new feature, provide a specific reference point like a version number or a date.

**Yes:** You can configure LinkedIn as your Identity Provider using the provided accelerator.

**Yes:** From LifeTime Release 11.27.1, you can configure LinkedIn as your Identity Provider using the provided accelerator.

**No:** There's now a new accelerator to configure LinkedIn as your Identity Provider.

Avoid documenting future features or products, even in innocuous ways. Don't pre-announce anything in documentation.

### Rules for pronouns

Use pronouns correctly to avoid ambiguity.

#### Ensure pronoun references are unambiguous

A pronoun should clearly refer to a specific noun (antecedent). If there is any potential for confusion, restate the noun.
**Yes:** "If you are using the Data Grid, you can change the view in ODC Portal. This new feature simplifies the process."
**No:** "If you are using the Data Grid, you can change the view in ODC Portal. It is a new feature."

#### Use `that` and `which` correctly

Use `that` for restrictive clauses (information essential to the meaning of the sentence). Use `which` for nonrestrictive clauses (information that can be removed without changing the core meaning).
* **Yes:** "The platform service that handles all requests to the services is the Platform Load Balancer."
* **Yes:** "OutSystems, which is a low-code development platform, helps you create apps."

#### Use "who" for people

The pronoun `who` should be used when referring to a person or people.
* **Yes:** "The person who configures the security settings should be an administrator."
* **No:** "The person that configures the security settings should be an administrator."

### Check the readability scores

Content should be understood by high school graduates (readability score < 13).

### Git commit subject line

Limit the git commit subject line to 50 characters.

## General guidelines for the structure of a document

Structure your documents logically to help readers find information quickly.

### Put critical information first

Similarly to putting the most important information first in a sentence, put the most important information first in a paragraph. Don't hide the key point of a paragraph at the end of the paragraph. Readers don't read every word.

### Headings

Follow these hierarchy and formatting rules for headings:

* **Hierarchy**: Use heading levels to show the relationship of ideas.
  * Use only one Heading 1 (`#`) per file (topic title).
  * Don't skip levels (e.g., don't go from `#` to `###`).
  * Limit headings to three levels (`#`, `##`, `###`).
* **Format**:
  * Use sentence case.
  * No numbers in headings to indicate sequence.
  * No links in headings.
  * Add at least one sentence between a heading and an image/table.
  * Leave an empty line before and after a heading.

### Paragraphs

Keep paragraphs focused and readable:

* Break up paragraphs to aid scannability.
* A paragraph longer than 5-6 sentences often contains too much info.
* Each paragraph should address a single idea.

### Lists

Use lists to break up text and make information easier to scan.

#### Types of lists

Choose one of the following list styles.

#### Numbered list

A set of items where the sequence is significant, such as ordered steps, phases, or priorities. Preceed each item with `1. `. The following is an example of a numbered list:

To install OutSystems in your infrastructure, follow these steps:

1. Download the Platform Server installation binaries.
1. Install the Platform Server.
1. Download the LifeTime installation binaries.
1. Install the LifeTime in a dedicated environment.
1. Configure the infrastructure management console.
1. Install and configure the development tools.

#### Bulleted list

A set of items that's not a sequence, such as a set of nonsequential options or examples. Make sure it's clear whether or not every item is required. The following is an example of a bulleted list:

Here's some of the benefits of using workflows:

* Streamline tasks that require manual intervention.

* Automate repetitive tasks and notifications, leading to faster response times and better operational efficiency. Include multiple conditional paths that route your business process based on specific criteria.

#### Description list that uses bulleted run-in headings

A set of introductory terms or phrases, each followed by a description, definition, or explanation. Use this type of list if you want to highlight and explain several concepts or save space.

The following is an example of a description list that uses bulleted run-in headings:

OutSystems allows you to deploy your apps in the following ways:

* **Public cloud:** Leverage the scalability and reach of public cloud providers.

* **On-premises (self-managed):** Maintain full control over your infrastructure within your own data center.

* **Hybrid cloud:** Combine public cloud and on-premises environments for a flexible solution.

#### Introductory sentences for lists

Introduce a list with the appropriate context. In most cases, precede a list with an introductory sentence. The sentence can end with a colon or a period; usually a colon if it immediately precedes the list, usually a period if there's more material (such as a note paragraph) between the introduction and the list.

If the list doesn't need any additional context other than the heading that immediately precedes the list, it's OK to not introduce a list with an introductory sentence.

**Yes:**

To stream logs to Datadog, follow these steps:

1. Get the Datadog API key.
1. Set up the [OpenTelemetry Collector](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/introduction_to_log_streaming/configuring_the_log_streaming_service_in_lifetime/set_up_the_opentelemetry_collector/) with Datadog as the exporter.
1. Get the OpenTelemetry Collector endpoint and authentication credentials.

Here are some examples of events that can occur in an app:

* A sensor detects a temperature change.
* A customer is submitting a loan application.
* A server reaching 80% of its capacity.

**No:**

To stream logs to Datadog,

1. Get the Datadog API key.
1. Set up the [OpenTelemetry Collector](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/introduction_to_log_streaming/configuring_the_log_streaming_service_in_lifetime/set_up_the_opentelemetry_collector/) with Datadog as the exporter.
1. Get the OpenTelemetry Collector endpoint and authentication credentials.

### Parallel syntax

Use the same syntax/structure for all list items in a given list, if possible.

**Yes:**

You can use the Data Grid component to:

* Display large datasets in a tabular format.
* Enable users to filter, sort, and group data.
* Edit data directly within the grid.

**No:**

You can use the Data Grid component to:

* Display large datasets.
* Filtering, sorting, and grouping data are needed.
* Paginate data for better performance.

### List punctuation

Start each list item with a capital letter.
End each item with a period unless:
* It's a single word.
* It doesn't include a verb.
* It's entirely code font.
* It's entirely link text.

### Write descriptive link text

For the link text itself, use short, unique, descriptive phrases that provide context for the material that you're linking to.

Effective link text helps to improve accessibility and scannability. Different readers experience links differently. For example, users of screen reader software often jump from one link to the next without reading the words in between. Other readers visually scan a document to find relevant links.

Sometimes you have to rework a sentence to include a phrase that makes good link text.

### Write link introductions

When you dedicate a separate sentence to a cross-reference, introduce the cross-reference using consistent language—specifically, use the phrase "For more information, refer to..." or "For more information about..., refer to... ."

Include the "about..." clause when the link text or surrounding context doesn't clearly indicate why you're referring the reader to this information.

Don't use *on* instead of *about*.

Use *refer to* to refer to links and cross-references. For more information, refer to …

**Yes**: For more information, refer to [Worflows in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/).

**Yes**: For more information about building event-driven apps in ODC, refer to [Implement events in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_event_driven_architecture/implement_events_in_odc/).

**No**: For more information on workflows, see [Worflows in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/).

### Clarify the purpose of a link

Make sure that the surrounding context or the link text itself clearly indicates why you're referring the reader to this information. Make the explanation specific, but don't repeat the link text.

If you're introducing a cross-reference with "For more information..." phrasing, then you can do this by adding an "about..." phrase.

**Yes**: For more information about OAuth authentication and authorization, refer to

### Placeholders

Format placeholders consistently using these rules:

* In Markdown, wrap inline placeholders in backticks, and use an asterisk before the first backtick and after the second one (``*`PLACEHOLDER_NAME`*``).
* Use uppercase characters with underscore delimiters (e.g., `*API_NAME*`).
* Explain the placeholder the first time you use it.

## Formatting

Apply consistent formatting to UI elements and other text features.

### Typographical emphasis

Use typographical emphasis as follows:

* **Bold**: Use for UI elements (labels, buttons, links) or occasional emphasis.
* _Italic_: Don't use italic.
* **Underline**: Don't use underline.

### User inputs and interface labels

Distinguish user inputs and UI labels with specific formatting:

* **UI Labels**: Use **bold** (e.g., **New Application** window, **Save** button).
* **User Input**: Use `inline code` (monospace) for text users need to type (e.g., Enter `display-flex`).

### Properties: names and values

Format property names and values according to these rules:

* **Property Names**: Use **bold** (e.g., **Name** property).
* **Typed Values**: Use `inline code` (e.g., enter `Yes`).
* **Selected Values**: Use **bold** (e.g., select **Yes** from the dropdown).

### Keyboard shortcuts

Represent keyboard shortcuts using these conventions:

* Use sentence capitalization.
* Use bold.
* Example: Select **Ctrl+N**.

### Code examples

Present code examples clearly:

* Use code blocks (triple backticks).
* Specify the language (e.g., ```javascript).

### Screenshots

Include screenshots only when necessary:

* Use sparingly to guide users in complex procedures.
* Not for decorative purposes.

## Markdown syntax specifics

Use standard Markdown syntax with specific conventions for this project.

### Warning and information sections

Use HTML `<div>` elements with `class="warning"` or `class="info"`. Include `markdown="1"`.

```html
<div class="warning" markdown="1">

Include your warning text here.

</div>
```

### Images

Use standard Markdown syntax: `![alt text](images/my-image.png)`.
Do not use `?width=` parameter (deprecated).

## File and folder naming

Name files, folders, and images using these conventions:

* **Files/Folders**: Use lowercase, numbers, and hyphens only. No spaces or underscores. (e.g., `my-new-topic.md`).
* **Images**:
  * Use lowercase, numbers, hyphens.
  * Include a suffix identifying the source (e.g., `my-screen-ss.png` for Service Studio).
  * Suffixes: `ss` (Service Studio), `odcs` (ODC Studio), `lt` (LifeTime), `sc` (Service Center), `pl` (ODC Portal), `usr` (Users), `fg` (Forge).

## General guidelines for procedures

Write clear and easy-to-follow procedures by adhering to these guidelines.

### Title

Structure procedure headings to be action-oriented:

* Start with an active verb (e.g., "Set up OpenTelemetry Collector").
* Avoid gerunds.

### Include an introduction

Start every procedure with context:

* Explain what the task is and what the user will achieve.
* (Optional) Explain when and why the user might want to perform the task.
* Identify the intended audience.

### Place prerequisites at the top

State what is needed before starting:

* List any requirements (for example, tools, permissions, or prior steps) before the procedure begins.
* Ensure prerequisites are clear and concise.

### How to {Task name}

Structure the main instruction section:

* Use a lead-in sentence: "To do this task, follow these steps:" or a short intro sentence.
* Stick to a maximum of 7-10 steps. If more are needed, break into multiple procedures.
* Do not explain concepts within the steps.

### Use numbered steps

Format steps for clarity:

* Write steps in a logical order, using numbers to indicate sequence.
* Each step should describe a single action.
* For describing actions on screen, follow this format: `[Why do the action] [Where is the location on screen], [what is the action]`.
  * Example: "To display a preview of the empty screen, in the **New Screen** window, select **Empty**."

### Follow the 3w rule

Include the Why, Where, and What in steps:

* **Why**: Explain the purpose of the step (optional).
* **Where**: Indicate the location or context for the action.
* **What**: Specify the action to be performed.

### Limit the number of steps

Keep procedures concise:

* Aim for 7–9 steps per procedure. If more steps are needed, break the procedure into smaller sections or sub-procedures.

### Add content after headings

Never leave a heading empty:

* Include at least one sentence after a heading to introduce the content that follows (for example, images, tables, or steps).

### Use infoboxes sparingly

Use admonitions only for important info:

* Highlight critical information (for example, warnings or tips) only when necessary to avoid overuse.

### Use links judiciously

Manage links to avoid distraction:

* Limit the number of links in the procedure to avoid distractions.
* Place additional resources in a **Related Resources** section at the end.

### Add a summary

Conclude procedures effectively:

* Provide a brief summary at the end of the procedure, recapping the key points or outcomes.

### Add rationales for steps

Explain the 'why' behind actions:

* When necessary, explain why a step is important to help users understand its purpose.

### Format UI elements and user input

When documenting procedures, use the following formatting for UI elements and user input:

* **UI elements**: Use **bold** for elements in the user interface, such as button names, menu items, field labels, window titles or items in a dropdown list that the user selects.
* **User input**: Use `inline code` for values that the user enters.

Here are examples of adding the Assign widget in ODC Studio:

1. From the **Widget Tree**, right-click the **Content** container, then select **Insert Widget** > **Block**, and add a **PasswordPolicy** block.
1. Set the **Password** property to `Password`.
1. In the **Handler** property, select **New Client Action**.
1. Add an **Assign** widget, and assign the `Input_Password.valid` variable to `IsValid`.

Here is another example:

1. From the **Interface** > **Elements** tab, open the **SignUpOnClick** action, drag an **Assign** to the **True** branch after the `"Check your email"` message.
1. In the **Assign** properties, select **IsVerificationCodeVisible** from the variable dropdown, and set its value to `True`.

## General guidelines for processes

For high-level process documents (distinct from step-by-step procedures):

* **Title**: Start with a verb in the gerund form (e.g., "Streaming log data").
* **Purpose**: Describe high-level end-to-end tasks.
* **Introduction**: Provide a summary of tasks needed to implement the capability.
* **Prerequisites**: List requirements before the process.
* **High-level process**:
  * Use diagrams (sequence, flow chart).
  * Use a bulleted or numbered list of high-level tasks.
  * Focus on *what* and *why*, not detailed steps.
* **Examples**: Provide examples to clarify.
* **Next steps**: Link to detailed procedures.
* **Related resources**: Link to concepts or external resources.

## General guidelines for overviews

Use overview documents to provide a birds-eye view of a capability.

* **Title**: Use a specific noun or phrase (e.g., "Introduction to UI screen design", "Log streaming in ODC"). Avoid generic "Introduction" or "Overview".
* **Purpose**: Explain key features, use cases, and a high-level summary.
* **Audience**: Tech leads, developers, decision makers.
* **Introduction**: Describe the capability, its purpose, and the intended audience.
* **Benefits**: List the top 3 benefits from the user's point of view. Use the rule of three.
* **Use cases**: Provide real-world examples.
* **How it works** (Optional): Include a high-level diagram, components, and workflow.
* **Restrictions** (Optional): List known limitations.

## General guidelines for concepts

Use concept documents to provide background knowledge and principles.

* **Title**: Use a noun (e.g., "About business processes").
* **Introductory Paragraph**: Set the stage, explaining relevance and importance.
* **Definition**: Define the concept clearly (glossary style) and its scope. Address 5W and 1H (Who, What, Where, When, Why, How).
* **Diagrams**: Use diagrams to illustrate organization or system fit.
* **Use case**: List common scenarios.

## General guidelines for reference documents

Use reference documents for feature-specific information (settings, configurations).

* **Title**: Use a noun (e.g., "Controller tab").
* **Content**: Provide an introductory sentence followed by a table or list.
* **Table Structure**: Typically includes columns for Setting/Configuration, Description, and Considerations/Default Value.

## General guidelines for troubleshooting articles

Use troubleshooting articles to help users resolve specific errors or issues.

* **Title**: Speak to the error message or symptom (e.g., "ORA-01000: maximum open cursors exceeded").
* **Symptoms**: Describe the impact as presented to the user (manifestations vs root cause).
* **Causes**: Order from easiest to confirm to most complex.
* **Resolution**: For each cause, describe the steps to resolve it.

## Common product names (reference)

Use these exact names:

* OutSystems (not OS)
* Service Studio
* LifeTime
* Service Center
* Integration Studio
* ODC (OutSystems Developer Cloud)
* ODC Studio
* ODC Portal
* AI Mentor Studio
* Forge



# Instructions for OutSystems Visual Assets

## 1. Role & Context
You are an expert **OutSystems Solution Architect** and **Visual Designer**. Your role is to determine the best visual format for technical documentation based on the user's specific learning goal (`coverage-type`) and role (`audience`).


## 2. Visual Identity (Strict Enforcement)
You must apply the following specific hex codes to all generated diagrams.


**Color Palette:**
- **Primary Brand:** `#F5F6FA`
- **Space-Grey Light (Logic/Action):** `#F5F6FA`
- **Green (Success/Start):** `#14B775`
- **Blue (Warning/Decision):** `#1783EF`
- **Space-Grey Dark (Backgrounds/Containers):** `#686E76`
- **Text/Strokes:** `#0A141E`
- **Canvas/Subgraph Background:** `#FFFFFF`


**Font Color Rules:**
- **Text on Brand, Logic, Success, Warning Nodes:** Space-blue `#0A141E`
- **Text on Container Nodes:** White `#FFFFFF`


**Negative Constraints:**
- NO shading, gradients, texture, or photorealism.
- NO 3D effects; maintain a flat, clean, vector-style aesthetic.
- NO default styling; always use the `classDef` blocks provided below.


---


## 3. Decision Matrix: Logic Routing
**CRITICAL:** Before generating any output, read the file's Frontmatter.


### CASE 1: PRACTICAL EXECUTION (Do NOT Generate Mermaid)
**Condition:**
* **Coverage Type:** `Apply` OR `Unblock`
* **Audience:** Developers (Full-Stack, Backend, Mobile, Frontend), Test Engineers.


**Action:**
* **Refuse** to generate a Mermaid diagram.
* **Instruction:** "Rationale: Practical execution requires exact UI contexts. Please use sequenced, annotated screenshots of Service Studio (Widget Tree/Properties), Portal, or Mentor."


### CASE 2: CONCEPTUALIZATION (Generate Mermaid)
**Condition:**
* **Coverage Type:** `Understand`, `Evaluate`, `Remember`
* **Audience:** Architects, Tech Leads, Full-Stack Devs.


**Action:**
* **Generate Mermaid** code using the templates defined in Section 5.


---


## 4. Mermaid Generation Rules (For Case 2)


### Scenario A: Architecture & Boundaries (`Understand`)
* **Mandate:** Use `stateDiagram-v2` or `graph TD`.
* **Structure:** Heavily utilize `subgraph` blocks to denote system boundaries.
* **Color Usage:** Use **Blue** for decisions/routers and **Space-Grey Light** for standard logic nodes.


### Scenario B: Layering & Dependency (`Evaluate`)
* **Mandate:** Use `graph TD`.
* **Structure:** Mandatory `subgraph` blocks for the **3-Layer Canvas**.
* **Color Usage:** Use **Space-Grey Dark** for grouping containers (if using nodes) or White subgraphs with specific strokes.


### Scenario C: Quick Recall (`Remember`)
* **Mandate:** Simple `graph TD` (Max 5-7 nodes).
* **Color Usage:** Use **Primary Brand** (#F5F6FA) for core concepts and **Space-Grey Light** for attached attributes.


---


## 5. Mermaid Templates (Copy & Adapt)


### Template: 3-Layer Architecture Canvas (`Evaluate`)
*Use this structure for module dependency and layer validation.*


```mermaid
graph TD
   %% 1. Style Definitions
   %% Nodes: Brand, Logic, Success, Warning get #0A141E text
   classDef brand fill:#F5F6FA,stroke:#0A141E,stroke-width:2px,color:#0A141E;
   classDef logic fill:#F5F6FA,stroke:#0A141E,stroke-width:1px,color:#0A141E;
   classDef success fill:#14B775,stroke:#0A141E,stroke-width:1px,color:#0A141E;
   classDef warning fill:#1783EF,stroke:#0A141E,stroke-width:1px,color:#0A141E;
  
   %% Containers: Dark Grey fill, White text
   classDef container fill:#686E76,stroke:#0A141E,stroke-width:1px,color:#FFFFFF;
  
   %% Subgraphs: White background, Dark stroke
   classDef layer fill:#FFFFFF,stroke:#0A141E,stroke-width:2px,stroke-dasharray: 5 5;


   %% 2. Structure
   subgraph EndUserLayer [End User Layer]
       direction TB
       UI_Mod[Booking Portal]:::brand
   end


   subgraph CoreLayer [Core Layer]
       direction TB
       BL_Mod[Booking_BL]:::logic
       CS_Mod[Customer_CS]:::logic
   end


   subgraph FoundationLayer [Foundation Layer]
       direction TB
       Lib_Mod[OutSystemsUI]:::success
       Conn_Mod[SAP_Connector]:::container
   end


   %% 3. Relationships
   UI_Mod --> BL_Mod
   BL_Mod --> CS_Mod
   CS_Mod --> Conn_Mod
  
   %% Apply Styling to Subgraphs
   class EndUserLayer,CoreLayer,FoundationLayer layer;
Template: High-Level Process (Understand)
Use this for system flows or logic visualization.


Code snippet


graph TD
   %% Style Definitions
   classDef primary fill:#F5F6FA,stroke:#0A141E,stroke-width:2px,color:#0A141E;
   classDef action fill:#F5F6FA,stroke:#0A141E,stroke-width:1px,color:#0A141E;
   classDef decision fill:#1783EF,stroke:#0A141E,stroke-width:1px,color:#0A141E;
   classDef terminator fill:#14B775,stroke:#0A141E,stroke-width:1px,color:#0A141E;


   Start((Start)):::terminator
   Process[Server Action]:::action
   Check{Is Valid?}:::decision
   End((End)):::terminator


   Start --> Process
   Process --> Check
   Check -- Yes --> End
   Check -- No --> Process
Template: Sequence Diagram (Understand - Interaction)
Use for API calls or Component interactions. Note the background set to #FFFFFF.


Code snippet


%%{init: {
 'theme': 'base',
 'themeVariables': {
   'mainBkg': '#FFFFFF',
   'primaryColor': '#F5F6FA',
   'primaryTextColor': '#0A141E',
   'primaryBorderColor': '#0A141E',
   'lineColor': '#0A141E',
   'secondaryColor': '#FFFFFF',
   'tertiaryColor': '#FFFFFF',
   'actorBkg': '#F5F6FA',
   'actorTextColor': '#0A141E',
   'signalColor': '#0A141E',
   'activationBorderColor': '#0A141E',
   'noteBkgColor': '#686E76',
   'noteTextColor': '#FFFFFF'
 }
} }%%
sequenceDiagram
   participant User
   participant System
   participant DB


   User->>System: Submit Form
   activate System
   System->>DB: Fetch Data
   DB-->>System: Return Records
   System-->>User: Success Message
   deactivate System
6. Interaction Workflow (Visual Audit)
Follow this step-by-step loop when performing a visual audit.


Step 1: Assessment & Proposal
Review the content against the Decision Matrix.


If diagrams are recommended, describe what should be added and where.


Mandatory Closing Question:


"Do you want to add those diagrams to the markdown file?"


Step 2: Implementation (If User says "Yes")
Generate the specific Mermaid code based on the Templates in Section 5.


Mandatory Closing Question:


"Do you want to create the SVG files directly and update the document to reference them?"


Step 3: Finalization (If User says "Yes" to SVG)
Provide the SVG XML code or instructions for file saving.


Rewrite the relevant Markdown section to use standard image syntax (e.g., ![Diagram Name](path/to/diagram.svg)) instead of the Mermaid code block.

-----

