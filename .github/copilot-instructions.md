##  General guidelines for grammar and content

### Tone and voice

Use the appropriate tone and voice in your content. Your content must be:

- Friendly and straightforward
- Clear and concise
- Inclusive and respectful
- Free of jargon and sales talk

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
* A specific instance of a common noun

#### Don't capitalize common nouns

Don't capitalize generic technical terms unless they're part of a proper noun:

* environment, application, module, screen, action
* database, server, cloud, platform
* developer, user, administrator

**Examples**

* **Yes**: 
  1. Configure application settings after deployment
  1. Click the Save button
    For more information, refer to the troubleshooting guide

* **No**: 
  1. Configure Application Settings After Deployment
  1. Click the save button
    For More Information, Refer To The Troubleshooting Guide

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

### Keep accessibility in mind

Your content should be accessible to all people, to those without and with disabilities. Be mindful of:

- How you refer to people with disabilities. Use inclusive language.
- How you describe interactions with the user interface. Consider providing alternative methods or steps.
- How you use words to indicate a location (left, right, top, below, up, down) on screen. Provide more context for people using screen-readers.
- How you use the words "easy" and "simple". What may be simple to do for some people may not be simple to do for all.

**Yes:** For more information about accessibility, refer to [Writing for all abilities](https://docs.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).

**No:** For more information about accessibility, see [Writing for all abilities](https://docs.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).

### Use sentence case for headings and titles

Capitalize the first letter in headings and titles.

**Examples**

**Yes:** Configure application settings after deployment.

**No:** Configure Application Settings After Deployment.

**Yes:** Use Actions to encapsulate logic

**No:** Use Actions to Encapsulate Logic

**Yes:** Bootstrap an Entity using an Excel file

**No:** Bootstrap an Entity Using an Excel File

### Use gender-inclusive language

You should make the gender visible only if it's important to understand the content. This means you shouldn't use words like he/she, himself/herself, man/woman, unless you're referring to a particular individual. Instead, use a non-gender alternative, like plural forms and "they". Furthermore, you shouldn't use language that reinforces stereotypes.

For more details, see [Bias-free communication](https://docs.microsoft.com/en-us/style-guide/bias-free-communication) by Microsoft.

**Examples**

**Yes:**

- When developers download a Forge component, they can install it in Service Studio. (Use plural to avoid referring to gender.)
- When a developer downloads a Forge component, they can install it in Service Studio. (Use "they" to refer to a single person without mentioning their gender.)
- When you download a Forge component, install it in Service Studio. (Are your target readers developers? If yes, then "you" is a better choice.)

**No:**

- When a developer downloads a Forge component, he can install it in Service Studio. (Service Studio is not used exclusively by male developers or developers who identify as men.)

### Avoid Latin abbreviations

Use "that is" instead of "i.e." and "for example" or "such as" instead of "e.g.".

**Examples**

**Yes:** Design the process behavior, that is, the process flow.

**No:** Design the process behavior, i.e., the process flow.

**Yes:** Make sure the Textarea Input has the Name property set (for example, myTextArea).

**No:** Make sure the Textarea Input has the Name property set (e.g., myTextArea).

### Timeless documentation

- Avoiding time-based words and phrases: Do not use words like new, now, currently, latest, or future when describing a product's features. These words quickly become outdated and require maintenance.
- Focusing on the current state: The documentation should describe how a product works as if it is the current, stable state, not a recent change.
- Providing a specific reference point (if necessary): If you absolutely must refer to a new feature, provide a specific reference point like a version number or a date.

**Yes:** You can configure LinkedIn as your Identity Provider using the provided accelerator.

**Yes:** From Lifetime Release 11.27.1, You can configure LinkedIn as your Identity Provider using the provided accelerator.

**No:** There's now a new accelerator to configure LinkedIn as your Identity Provider.

Avoid documenting future features or products, even in innocuous ways. Don't pre-announce anything in documentation.

### Rules for pronouns

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

## General guidelines for the structure of a document

### Put critical information first

Similarly to putting the most important information first in a sentence, put the most important information first in a paragraph. Don't hide the key point of a paragraph at the end of the paragraph. Readers don't read every word.

### Lists

#### Types of lists

Choose one of the following list styles. 

#### Numbered list

A set of items where the sequence is significant, such as ordered steps, phases, or priorities. The following is an example of a numbered list:

To install OutSystems in your infrastructure, follow these steps:

1. Download the Platform Server installation binaries.  
2. Install the Platform Server.  
3. Download the LifeTime installation binaries.  
4. Install the LifeTime in a dedicated environment.  
5. Configure the infrastructure management console.  
6. Install and configure the development tools.

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
2. Set up the [OpenTelemetry Collector](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/introduction_to_log_streaming/configuring_the_log_streaming_service_in_lifetime/set_up_the_opentelemetry_collector/) with Datadog as the exporter.  
3. Get the OpenTelemetry Collector endpoint and authentication credentials.

Here are some examples of events that can occur in an app:

* A sensor detects a temperature change.  
* A customer is submitting a loan application.  
* A server reaching 80% of its capacity.

**No:**

To stream logs to Datadog, 

1. Get the Datadog API key.  
2. Set up the [OpenTelemetry Collector](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/introduction_to_log_streaming/configuring_the_log_streaming_service_in_lifetime/set_up_the_opentelemetry_collector/) with Datadog as the exporter.  
3. Get the OpenTelemetry Collector endpoint and authentication credentials.

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

## General guidelines for procedures

### Use task-based headings for procedural content

* Start with a verb in the imperative mood (for example, "Create a screen" or "Install a Forge app").
* Avoid gerunds (for example "Creating a screen").

### Include an introduction

* Provide a brief overview of the procedure, explaining what the user will achieve and why it is important.
* Identify the audience or skill level (for example, beginner or experienced developer).

### Place prerequisites at the top

* List any requirements (for example, tools, permissions, or prior steps) before the procedure begins.
* Ensure prerequisites are clear and concise.

### Use numbered steps

* Write steps in a logical order, using numbers to indicate sequence.
* Each step should describe a single action.

### Follow the 3w rule

* **Why**: Explain the purpose of the step (optional).
* **Where**: Indicate the location or context for the action.
* **What**: Specify the action to be performed.

### Limit the number of steps

* Aim for 7–9 steps per procedure. If more steps are needed, break the procedure into smaller sections or sub-procedures.

### Add content after headings

* Include at least one sentence after a heading to introduce the content that follows (for example, images, tables, or steps).

### Use infoboxes sparingly

* Highlight critical information (for example, warnings or tips) only when necessary to avoid overuse.

### Use links judiciously

* Limit the number of links in the procedure to avoid distractions.
* Place additional resources in a **Related Resources** section at the end.

### Add a summary

* Provide a brief summary at the end of the procedure, recapping the key points or outcomes.

### Add rationales for steps

* When necessary, explain why a step is important to help users understand its purpose.

These rules ensure that procedures are user-friendly, consistent, and easy to follow. Let me know if you need further assistance!
