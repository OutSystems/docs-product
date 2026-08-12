# Documentation structure rules

Use these rules when writing or reviewing documentation in this repository.

## Headings and title

Use sentence case for headings and titles. Use descriptive headings and titles because they help a reader navigate their browser and the page. It's easier to jump between pages and sections of a page if the headings and titles are unique.

Write section headings based on the type of content that's in the section.

For a task-based heading, start with a [*bare infinitive*](https://wikipedia.org/wiki/Infinitive#English), also known as a *plain form* or [*base form*](https://wikipedia.org/wiki/English_verbs#Base_form) verb. In English, the *imperative mood* also uses the base form verb, so it looks the same as the bare infinitive.

Task-based headings are frequently used in procedures

**Yes:** Create an app

**No:** Creating an app

For a conceptual and overview or non-task-based heading, use a [*noun phrase*](https://wikipedia.org/wiki/Noun_phrase) that doesn't start with an *\-ing* verb.

Noun-phrase headings are frequently used in concept documentation.

**Yes:** Workflows in ODC

**No:**  Using workflows in ODC

When possible, avoid using *\-ing* verb forms as the first word in any heading or title.

**Yes**: Transfer data sets

**No**: Transferring data sets

An *\-ing* verb form is a present participle or gerund. These verb forms are inconsistently translated when they're used as the first word in a title, and they increase character count in limited spaces.

## Heading and title format

* Use sentence case for headings and titles. That is, capitalize only the first word in the title, the first word in a subheading after a colon, and any proper nouns or other terms that are always capitalized a certain way. Even though you're using sentence case, don't put a period at the end of a title or heading.  
  
* Don't include numbers in headings to indicate a sequence of sections. 
   
* Use punctuation in headings sparingly, if at all. Punctuation can be a sign that your heading is too complicated. Consider rewriting.  
  
* Only use an abbreviation of a word in a page title or heading if it's the more commonly known version of the word. If you do use an abbreviation in the page title or heading, the first instance of the word in a paragraph needs to be defined. You can define the abbreviation in the page title or heading, but consider if the additional length adds value. For SEO, use the more prominent version of the term in headings. For more information, see [Abbreviations](https://developers.google.com/style/abbreviations).  
  
* For ease of comprehension and translation, include definite and indefinite articles (*a*, *an*, and *the*) in your writing. Don't skip articles for brevity, including in headings and titles.  
  
* Use heading tags to structure your content hierarchically—for example, `<h1>`, `<h2>`, and `<h3>` in HTML, or `#`, `##`, and `###` in Markdown.  
* Don't put a link in a heading because it can easily be confused as a style applied to a heading instead of a link.  
  
* Use a heading hierarchy and take the following items under consideration:  
  * Ensure that each page in your project includes a unique level-1 heading.   
  * Don't skip levels of the heading hierarchy. For example, put an `<h3>` tag only under an `<h2>` tag.
  * Use heading levels to show the relationship of ideas and to enable readers to easily scan and read selectively. Limit headings to three levels. Avoid using more than three levels of headings. If you think that you need more levels to structure the content, consider separating the content into smaller documents. 
* Add at least a sentence between a heading and an image or table, describing what follows. Introduce images and tables, so users know what they are looking at.  

### Headings in markdown

Headings are defined using one or more # (hash) characters placed in the first column of a given line. The number of # characters define the heading level.

General rules for headings:

* Use only one Heading 1 in a topic, because Heading 1 defines the topic title. Titles must only contain letters from the English alphabet, numbers, dashes, and periods.
  
* Don't skip heading levels. For example, don't use a Heading 3 right after a Heading 1, without a Heading 2 in-between.
  
* Always leave an empty line before and after a heading line.

*Example*

A Markdown snippet with three headings:

```markdown
# Heading 1

This is content under Heading 1.

## Heading 2

This is content under Heading 2.

### Heading 3

This is content under Heading 3.
```

## Paragraphs

Break up your paragraphs to aid in the scannability of the page and to avoid walls of text. Readers scan for information and read on different devices with different screen sizes. Each paragraph should address a single idea in the fewest words and in the fewest sentences possible.

Don't make sentences longer in order to limit the number of sentences in a paragraph. Use shorter sentences and paragraphs.

A paragraph longer than 5 or 6 sentences is often an indication that the paragraph is trying to convey too much information. If so, break the paragraph into smaller paragraphs or remove some content. However, don't break paragraphs up if they contain a single idea. It's OK to have a paragraph with one sentence, and it can be OK if it's longer than 6 sentences as long as it's still about one idea.

## Put critical information first

Similarly to putting the most important information first in a sentence, put the most important information first in a paragraph. Don't hide the key point of a paragraph at the end of the paragraph. Readers don't read every word.

## Lists

## Types of lists

Choose one of the following list styles. 

### Numbered list

A set of items where the sequence is significant, such as ordered steps, phases, or priorities. The following is an example of a numbered list:

To install OutSystems in your infrastructure, follow these steps:

1. Download the Platform Server installation binaries.  
2. Install the Platform Server.  
3. Download the LifeTime installation binaries.  
4. Install the LifeTime in a dedicated environment.  
5. Configure the infrastructure management console.  
6. Install and configure the development tools.

### Bulleted list

A set of items that's not a sequence, such as a set of nonsequential options or examples. Make sure it's clear whether or not every item is required. The following is an example of a bulleted list: 

Here's some of the benefits of using workflows: 

* Streamline tasks that require manual intervention. 
  
* Automate repetitive tasks and notifications, leading to faster response times and better operational efficiency. Include multiple conditional paths that route your business process based on specific criteria. 

### Description list that uses bulleted run-in headings

A set of introductory terms or phrases, each followed by a description, definition, or explanation. Use this type of list if you want to highlight and explain several concepts or save space. 

The following is an example of a description list that uses bulleted run-in headings:

OutSystems allows you to deploy your apps in the following ways:

* **Public cloud:** Leverage the scalability and reach of public cloud providers.  

* **On-premises (self-managed):** Maintain full control over your infrastructure within your own data center.  

* **Hybrid cloud:** Combine public cloud and on-premises environments for a flexible solution.

## Introductory sentences for lists

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

### Numbered, lettered, and bulleted lists

Start each list item with a capital letter, unless case is an important part of the information conveyed by the list—such as in a list of glossary terms.

End each list item with a period or other appropriate sentence-ending punctuation, except in the following cases:

* If the item consists of a single word, don't add end punctuation.  
* If the item doesn't include a verb, don't add end punctuation.  
* If the item is entirely in code font, don't add end punctuation.  
* If the item is entirely link text or a document title, don't add end punctuation.

If you end up with inconsistent punctuation in your list, then either rewrite your list to use [parallel construction](https://developers.google.com/style/lists#parallel) or add end punctuation to every list item for consistency.

## Comma-separated lists

When you write a list in a paragraph, use [serial commas](https://developers.google.com/style/commas#serial-commas) to separate the items.

Avoid ending a list with *etc.* or phrases like *and so on*. Instead, introduce the list in a way that makes it clear that the list isn't all-inclusive.

**Yes**: The service processes data such as event logs, clickstream data, social network interactions, and e-commerce transactions.

**No**: The service processes data like event logs, clickstream data, social network interactions, e-commerce transactions, etc.

**No**: The service processes data such as event logs, clickstream data, social network interactions and e-commerce transactions.

## Write descriptive link text

For the link text itself, use short, unique, descriptive phrases that provide context for the material that you're linking to.

Effective link text helps to improve accessibility and scannability. Different readers experience links differently. For example, users of screen reader software often jump from one link to the next without reading the words in between. Other readers visually scan a document to find relevant links.

Sometimes you have to rework a sentence to include a phrase that makes good link text.

### Two options for effective link text

For your link text, use either the exact page title or a descriptive phrase, as described in the following sections.

#### Page titles as link text

One option for effective link text is to match the link text to the page title or heading that you're referencing.

**Yes**: For more information, refer to [Worflows in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/).

#### Descriptive phrases as link text

Another option for effective link text is to use a description of the destination page, capitalized as if it's part of the sentence.

When you write a descriptive phrase as link text, help readers quickly determine whether the link is relevant to them:

* Place important words at the beginning of the link text.  
* Don't use the same link text in the same document for different target pages.  
* Keep link text short where possible. Don't write lengthy link text such as a sentence or short paragraph.

**Yes**: You can [configure log streaming to DataDog tool](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/introduction_to_log_streaming/configuring_the_log_streaming_service_in_lifetime/stream_logs_to_datadog/) from your O11 app.

**No**: To configure log streaming to Datadog tool, see [this article](https://success.outsystems.com/documentation/11/monitoring_and_troubleshooting_apps/introduction_to_log_streaming/configuring_the_log_streaming_service_in_lifetime/stream_logs_to_datadog/).

### Avoid vague link text

Write link text that makes sense without the surrounding text. Don't use phrases such as *this document*, *this article*, or *click here*.

## Write link introductions 

When you dedicate a separate sentence to a cross-reference, introduce the cross-reference using consistent language—specifically, use the phrase "For more information, refer to..." or "For more information about..., refer to... ."

Include the "about..." clause when the link text or surrounding context doesn't clearly indicate why you're referring the reader to this information. 

Don't use *on* instead of *about*.

Use *refer to* to refer to links and cross-references. For more information, refer to …

**Yes**: For more information, refer to [Worflows in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/).

**Yes**: For more information about building event-driven apps in ODC, refer to [Implement events in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_event_driven_architecture/implement_events_in_odc/).

**No**: For more information on workflows, see [Worflows in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/about_business_processes/workflows_in_odc/).

## Clarify the purpose of a link

Make sure that the surrounding context or the link text itself clearly indicates why you're referring the reader to this information. Make the explanation specific, but don't repeat the link text.

If you're introducing a cross-reference with "For more information..." phrasing, then you can do this by adding an "about..." phrase. 

**Yes**: For more information about OAuth authentication and authorization, refer to

## 

## Formatting placeholders

Placeholders in sample code and commands represent values that the reader must replace when they use the sample input. Placeholders in example output can also represent other values that vary. 

For example, the placeholder `PROJECT_ID` represents a project ID in
sample code, commands, and example output.

In example output, the placeholder `HTTP_RESPONSE_CODE` represents an
HTTP response code; the reader isn't expected to set this to a specific value.

## Placeholders

When you create placeholders follow this general guidance around using the letter *x*:

* In general, don't use a single *x* or a series of *x*'s as placeholders; use a more informative placeholder.  
* In some contexts (such as HTTP status codes), a series of *x*'s is the standard, so it's OK to use (for example) *xx* in those cases.  
* In Markdown, wrap inline placeholders in backticks only
  (`PLACEHOLDER_NAME`).
* If your placeholders are in a block of code, wrap the code block in a code
  fence (\`\`\`).
* Inside a code fence, you can't apply formatting like bold or italic.
* For a single placeholder explanation, use this format:
  `Replace \`PLACEHOLDER_NAME\` with a description of what the
  placeholder represents.`
* Example: `Replace \`BUILD_ID\` with the ID of the 'WORKING' build that
  you copied in the preceding step.`
* For two or more placeholders:
    * Follow the command line with a descriptive list of the placeholders
      used in the command line.
    * Introduce this list with `Replace the following:`.
    * List the placeholders in the order in which they appear in the command
      line.
    * Explain what each placeholder represents, even if the placeholder value
      is intuitive.

### Placeholder text

**Use uppercase characters with underscore delimiters.**

**Yes**:

* `API_NAME`
* `METHOD_NAME`

**No**:

* `API-NAME`
* `METHOD NAME`

If the context in which your placeholders appear makes using uppercase characters with underscore delimiters a bad idea, use something else that makes sense to you, but be internally consistent.

**Don't include possessive adjectives in placeholders.**

**No**:

* `.../<var>MY_API_NAME</var>`  
* `.../<var>YOUR_API_NAME</var>`

## Explain placeholders

When you use a placeholder in text or code, explain the placeholder the first
time you use it. It's not necessary to repeat the explanation in the document
unless doing so might benefit the reader, for example in circumstances such as
the following:

* Your document is lengthy.
* You've introduced several other placeholders in a long procedure.
* Your document isn't intended to be read from beginning to end.

