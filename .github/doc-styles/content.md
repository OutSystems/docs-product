# Grammar and content

Write clearly and consistently.

## Tone and voice

Write in a friendly, direct, and precise voice. For the full guidance, including the calibration table and self-check, refer to [tone.md](tone.md#tone-and-voice).

Your content must be:

* Clear and concise
* Inclusive and respectful
* Free of jargon, sales talk, and marketing talk

## Avoid conversational language

Technical content is friendly but structured and precise. It doesn't read as spoken conversation. Avoid casual connectors, hedging phrases, and slang verbs that creep in from everyday speech, and don't address the reader as if chatting with them.

**Language to avoid:**

* **Casual connectors:** so, well, now, just, basically, actually (as sentence openers)
* **Hedging phrases:** it's worth noting that, keep in mind that, as you might expect
* **Casual or slang verbs:** wire up, spin up, hook up, tackle
* **Enthusiasm:** exclamation points, "Great!", "Awesome,"
* **Rhetorical questions:** "Wondering how to configure X?"

**Examples**

**No:** The cache expires after 10 minutes, so requests made after that trigger a new query.
**Yes:** The cache expires after 10 minutes. Requests made after that trigger a new query.

**No:** Now you need to wire up the database connection.
**Yes:** Configure the database connection.

**No:** Just add the following code to your module.
**Yes:** Add the following code to your module.

**No:** Great! You're ready to deploy the app.
**Yes:** You can deploy the app.

**No:** Wondering how to reset your password? Here's how.
**Yes:** To reset your password, do the following.

## Be brief and concise

Write short sentences and well-structured paragraphs. Don't repeat yourself.

**Example**

**Yes:** The style guide is a document with your brand colors and patterns. The style guide is important for user interface usability and consistency, as well as for adherence to your brand rules.

**No:** The Style Guide is a document with your brand theme colors and patterns ready to use to create a consistent user experience on your applications. It is an essential piece to ensure adherence to your brand rules, user interface consistency, and foster usability. It is designed to guide you through all delivery assets to optimize the development process and user experience.

## Use American English

Use American English. This applies to spelling, word use, and writing dates.

## Use the present tense

Use the present tense whenever possible. Using the present tense helps make sentences clear and straightforward to understand.

**Example**

**Yes:** Click the Save button. The data updates immediately.

**No:** Click the Save button. The data will be updated.

## Use contractions

Use common contractions instead of full forms. Some of the common contractions you need are: it's, doesn't, there's, can't/cannot.

Contractions keep sentences natural and direct. Full forms read as stiff in technical content. Avoid making contractions from a noun and a verb, especially with nouns denoting OutSystems products.

**Examples**

**Yes:** Don't use this function to encode text that might get executed as part of the SQL statement.

**No:** Do not use this function to encode text that might get executed as part of the SQL statement.

**Yes:** Iterating more than once over a query result isn't a good practice.

**No:** Iterating more than once over a query result is not a good practice.

**Yes:** LifeTime is an OutSystems management console.

**No:** LifeTime's an OutSystems management console. (No contractions with a noun, here a product name.)

## Use the active voice

The active voice makes the sentence dynamic and clear. It also makes it clear who (the user, the system, and so forth) is doing what.

**Example**

**Yes:** After you validate the new SQL element, delete or deactivate the original Aggregate.

**No:** The original Aggregate is kept in the flow editor for your manual deletion after validating the new SQL element.

## Lead with the condition or goal

Start the sentence with the circumstance, condition, or goal, and follow it with the action or result. Readers can then tell whether the sentence applies to them before they read the instruction, and they can skip it when it doesn't.

This applies in three situations:

* **Cross-references:** Put the purpose before the link.
* **Instructions:** Put the goal before the action.
* **Conditions:** Put the condition before the consequence.

**Examples**

**Yes:** For more information, refer to [Asset portfolios](portfolios-overview.md).

**No:** Refer to [Asset portfolios](portfolios-overview.md) for more information.

**Yes:** To implement your workflow, use the workflow editor.

**No:** Use the workflow editor to implement your workflow.

**Yes:** To delete the entire document, click **Delete**.

**No:** Click **Delete** if you want to delete the entire document.

**Yes:** If an app consumes service actions from an app in another portfolio, refactor the dependency into a REST API.

**No:** Refactor the dependency into a REST API if an app consumes service actions from an app in another portfolio.

Keep the opening clause short. If the condition is long, split it into its own sentence.

## Be careful with modal verbs

This section applies to the modal verbs can, could, may, might, will, shall, would, should, and must. Modal verbs describe what you believe or think of the product, or they denote an ability or obligation. In contrast, technical content confidently describes what the product does. Using a modal instead of a stronger structure creates a weak and wordy sentence. It also makes your readers less confident about the content.

**Modals we use:**

* **can** — for genuine ability or a real choice the reader has
* **must** — for a genuine requirement or obligation
* **will**, used sparingly — use, for example, when pointing forward to something the reader needs later in a procedure, never as a softer substitute for the present tense

**Modals to avoid:** could, may, might, shall, would, should. These introduce uncertainty, formality, or hedging that technical content doesn't need. Rephrase with can, must, the present tense, or a direct statement instead.

**Examples**

**Yes:** You can export the report as a CSV or PDF file.

**No:** You may export the report as a CSV or PDF file. ("May" suggests permission or uncertainty. This is a straightforward choice the reader has, so use "can".)

**Yes:** OutSystems handles unforeseen or unhandled errors in apps.

**No:** OutSystems handles unforeseen or unhandled errors that might occur in apps. (If errors do happen, there's nothing hypothetical about their existence.)

**Yes:** You must configure a valid license before deploying to production.

**No:** You should configure a valid license before deploying to production. ("Should" makes a requirement sound optional.)

**Yes:** The migration deletes all records in the staging table.

**No:** The migration will delete all records in the staging table. (Use the present tense for actions that happen as part of the current step, even if they technically run after you trigger them.)

## Use second person

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

## Be clear and precise

The language in technical content must be clear and precise. Clarity and precision make content useful for the audience. The following examples demonstrate how being vague, blaming users, or taking their time and skills for granted weakens clarity.

**Examples**

**Yes:** Do the following in all of your apps.

**No:** Some tasks must be used as a rule of thumb (they apply to all kinds of applications). ("Some" and "all kinds of" are vague.)

**Yes:** With this approach, you're not adding styles that can break the look and feel other developers created.

**No:** With this approach, you're not forcing things that people may not want in a particular scenario. (It's not clear what "thing" or "people" are.)

**Yes:** Error. The library uses an API that's not available.

**No:** Error. The library might be using an API that's not available. ("Might" introduces doubt and doesn't make it clear whether the API is available or not.)

**Yes:** You must create a package with all the apps, and deploy the package to your enterprise infrastructure.

**No:** Just create a package with all the apps, and deploy it to your enterprise infrastructure. ("Just" makes this task appear quicker to do than it seems. Using "simply" would imply the same false assumption.)

**Yes:** If you activate this option, and your connection is poor, debugging takes longer.

**No:** By activating this option, it's possible that the debugger will feel slower. (Using the verb "feel" is claiming that the slower performance is a subjective observation. It's not subjective.)

## Use objective language

Technical documentation describes how a product works. State facts and provide instructions rather than making subjective claims or value judgments.

**Why this matters:** AI-assisted writing tools tend to produce promotional-sounding content. Review generated text for subjective language and replace it with factual descriptions.

**Language to avoid:**

* **Superlatives:** best, most, optimal, ideal, ultimate
* **Subjective modifiers:** powerful, robust, seamless, intuitive, elegant, cutting-edge
* **Unverifiable claims:** easy, simple, straightforward, effortless, quick
* **Unnecessary intensifiers:** very, really, highly, extremely, significantly

**Examples**

**No:** This powerful feature lets you build apps faster.
**Yes:** This feature reduces the number of steps to build an app.

**No:** Follow these best practices to create high-quality applications.
**Yes:** Follow these practices to create applications.

**No:** The seamless integration makes connecting to external services easy.
**Yes:** The integration connects to external services using REST APIs.

**No:** This is the most efficient way to deploy your application.
**Yes:** Deploy your application as follows.

**Exceptions:**

Descriptive language is acceptable when:

* Comparing with measurable criteria (for example, "processing 1000 requests per second")
* Referring to established technical terms (for example, "high-availability mode")
* Quoting UI labels or product names as they appear

Focus on what the product does and how to use it, not on how good it is.

### Avoid figurative jargon

Use plain, literal verbs instead of figurative or trendy jargon. Figurative verbs are vague about what actually happens, and they're one of the more recognizable signs of unedited AI-generated text.

| Words to avoid | Words to use instead |
|---|---|
| leverage | use, apply |
| unlock | enable, provide access to |
| harness | use |
| scaffold | set up, create |
| delve into, dive into | describe, cover |
| supercharge, turbocharge | speed up, improve |
| streamline | simplify, reduce the number of steps |

Use "streamline" only for the literal act of simplifying a specific step.

For "wire up", refer to [Avoid conversational language](#avoid-conversational-language).

**Examples**

**No:** Leverage the Data Grid component to unlock advanced filtering.
**Yes:** Use the Data Grid component to add advanced filtering.

**No:** This script supercharges the database connection setup.
**Yes:** This script reduces the steps to set up the database connection.

**No:** Let's dive into how log streaming works.
**Yes:** Log streaming works as follows.

### Avoid colons that join sentences

Use a colon only to introduce a list, a code block, or a definition in the `**Term**: definition` form. Don't use a colon to join two clauses. Write each idea as a complete sentence, or connect the clauses with a conjunction or a relative clause. Colons that join clauses are a recognizable sign of unedited AI-generated text.

**Patterns to avoid:**

* **Explanation colon:** a statement, a colon, then the explanation, as in "X is Y: it does Z."
* **Reveal colon:** a fragment, a colon, then the point, as in "The result: faster builds."

**Examples**

**No:** The cache improves speed: it stores results in memory.
**Yes:** The cache stores results in memory, which improves speed.

**No:** There's one requirement: the app must be published.
**Yes:** The app must be published.

**No:** Configuration is simple: add the key to the file.
**Yes:** Add the key to the file.

**Exceptions:**

A colon is acceptable when:

* It follows an introductory sentence before a list or code block. Refer to the list rules in [structure.md](structure.md).
* It separates a term from its definition in the `**Term**: definition` form.
* It appears in a time or ratio, such as 10:30 or 3:1.

## Write for the user's problem, not the feature {#user-problem-first}

Lead with what the reader needs to accomplish or the problem they're facing. Describe what the capability does for the user before, or instead of, describing how the capability itself works or what it's made of.

**Why this matters:** A feature-first description reads as marketing copy and forces the reader to work out the relevance themselves. A problem-first description lets the reader immediately confirm this page answers their question.

**Examples**

**Yes:** If you need to detect suspicious account activity in real time, stream your transaction logs to your APM tool so you can flag unusual patterns as they happen.

**No:** Log streaming is a feature that continuously sends log data from OutSystems to a third-party APM tool using the OpenTelemetry protocol.

**Yes:** When a deployment fails partway through, roll it back instead of troubleshooting a partially deployed application.

**No:** The rollback feature reverts a deployment to its previous state.

This applies across document types, not only overview pages:

* An overview leads with the problem the capability solves, not a description of the capability's parts.
* A procedure's intro sentence states what the reader accomplishes by completing it, not just the mechanism they're using.
* A troubleshooting doc's Symptoms section describes the impact on the user, not the internal cause (causes belong in the Causes section).

**Exception:** Reference documentation describes settings and fields factually, since the reader has already found the specific item they need. Don't force a "why" framing onto a settings table.

## Keep accessibility in mind

Your content should be accessible to all people, to those without and with disabilities. Be mindful of:

* How you refer to people with disabilities. Use inclusive language.
* How you describe interactions with the user interface. Consider providing alternative methods or steps.
* How you use words to indicate a location (left, right, top, below, up, down) on screen. Provide more context for people using screen-readers.
* How you use the words "easy" and "simple". What may be simple to do for some people may not be simple to do for all.

**Yes:** For more information about accessibility, refer to [Writing for all abilities](https://docs.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).

**No:** For more information about accessibility, see [Writing for all abilities](https://docs.microsoft.com/en-us/style-guide/accessibility/writing-all-abilities).

## Don't use the words "sorry" and "please"

**Examples**

**Yes:** To view the document, click **View**.

**No:** To view the document, please click **View**.

## Use sentence case for titles

Capitalize the first letter in titles.

**Examples**

**Yes:** Configure application settings after deployment.

**No:** Configure Application Settings After Deployment.

**Yes:** Use Actions to encapsulate logic

**No:** Use Actions to Encapsulate Logic

**Yes:** Bootstrap an Entity using an Excel file

**No:** Bootstrap an Entity Using an Excel File

## Avoid overusing parentheses

Don't put important information in parentheses. Some readers ignore any information that appears in parentheses.

Whenever you're inclined to use parentheses, consider whether they're necessary. The sentence often works as well if you remove the parentheses and set off the phrase with commas or split it into two sentences.

If you need to include parentheses in the middle of a sentence, keep the information in the parentheses short. Otherwise, consider using two sentences.

**Examples**

**Yes:** Enter a six-digit hex number, and then click **OK**. For example, if you want the color forest green, enter `228B22`.

**No:** Enter a six-digit hex number (for example, if you want the color forest green, enter `228B22`), and then click **OK**.

## Serial comma

In a series of three or more items, use a comma before the final and or or to avoid potentially changing the meaning of the sentence. This comma is called a *serial comma*.

**Examples**

**Yes:** Consider an infrastructure with the following environments: development, preproduction, and production.

**No:** Consider an infrastructure with the following environments: development, preproduction and production. (It may seem that there are two environments, the first running the apps in "development" and the second in "preproduction and production". However, there are three different environments.)

**Yes:** The sync client action sends the added, changed, and deleted local records to the server.

**No:** The sync client action sends the added, changed and deleted local records to the server. (The reader may understand that the local records need to be both changed and deleted before the client action sends the records to the server. However, both modification and deletion qualify a local record for a sync.)

**Yes:** Service Center provides a set of metrics regarding a specific environment. It provides access to:

* Application logs and errors
* Web and mobile requests
* Integration calls
* Business processes
* Security audits

**No:** Service Center provides a set of metrics regarding a specific environment. It provides access to application logs and errors, web and mobile requests, integration calls, business processes, and security audits. (There are many items, and a list works better here.)

## Keep it international and straightforward to translate

Ensure your content is accessible to people of different cultures and speakers of various levels of the English language. The following are some guidelines to help you with that:

* Use plain English.
* Be consistent.
* Be inclusive. Inclusiveness also implies creating accessible content.
* When providing examples, whether visual or textual, be aware that not all examples work well across different cultures.
* Don't try to be funny. Humor doesn't work well in technical content.
* Don't use idioms. Idioms are difficult to translate, and not all people know them.

**Example**

Here's an example of a copy: "It takes 23 years to become a Jedi, but it takes a lot less to master OutSystems, and it won't cost you an arm and a leg, or even a hand."

In Japan, the translators and editors removed the idiom "cost an arm and a leg" and the humorous addition "or even a hand". They kept the Jedi reference, as it works well for their audience: "It takes 23 years to become a Jedi, but learning OutSystems takes less time. And you don't have to make a big sacrifice."

## Use gender-inclusive language

You should make the gender visible only if it's important to understand the content. This means you shouldn't use words like he/she, himself/herself, man/woman, unless you're referring to a particular individual. Instead, use a non-gender alternative, like plural forms and "they". Furthermore, you shouldn't use language that reinforces stereotypes.

For more details, refer to [Bias-free communication](https://docs.microsoft.com/en-us/style-guide/bias-free-communication) by Microsoft.

**Examples**

**Yes:**

* When developers download a Forge component, they can install it in Service Studio. (Use plural to avoid referring to gender.)
* When a developer downloads a Forge component, they can install it in Service Studio. (Use "they" to refer to a single person without mentioning their gender.)
* When you download a Forge component, install it in Service Studio. (Are your target readers developers? If yes, then "you" is a better choice.)

**No:**

* When a developer downloads a Forge component, he can install it in Service Studio. (Service Studio is not used exclusively by male developers or developers who identify as men.)

## Use standardized example domains

When providing examples of domain names, use one of the domains reserved for such use. For example, example.com. Don't use other domains nor any of our customer domains.

Refer to [RFC 6761 - Special-Use Domain Names](https://tools.ietf.org/html/rfc6761) for more information.

**Example**

**Yes:** Enter the email address, for example, john.smith@example.com.

**No:** Enter the email address, for example, john.smith@outsystems.com.

## Check the readability scores

A readability score shows the estimated education level needed to understand a given text. Content must be understandable to high school graduates.

## Don't announce features and updates

Don't use documentation, training videos, or other technical content to inform users about future developments. Users need support with the product that is available to them.

**Example**

**Yes:** This feature has the following limitations. For more information about updates, refer to the release notes.

**No:** This feature currently has the following limitations that will be removed next month, in version 11.9.

## Avoid Latin abbreviations

Use "that is" instead of "i.e." and "for example" or "such as" instead of "e.g.".

**Examples**

**Yes:** Design the process behavior, that is, the process flow.

**No:** Design the process behavior, i.e., the process flow.

**Yes:** Make sure the Textarea Input has the Name property set (for example, myTextArea).

**No:** Make sure the Textarea Input has the Name property set (e.g., myTextArea).

## Limit the git commit subject line to 50 characters

When writing git commit messages, be brief and limit the subject line (often the first line) to 50 characters. The subject line is visible in many places, and it's useful to know what the changes are by reading a one-line summary.

## Timeless documentation

* Avoiding time-based words and phrases: Do not use words like new, now, currently, latest, or future when describing a product's features. These words quickly become outdated and require maintenance.
* Focusing on the current state: The documentation should describe how a product works as if it is the current, stable state, not a recent change.
* Providing a specific reference point (if necessary): If you absolutely must refer to a new feature, provide a specific reference point like a version number or a date.

**Yes:** You can configure LinkedIn as your Identity Provider using the provided accelerator.

**Yes:** From Lifetime Release 11.27.1, You can configure LinkedIn as your Identity Provider using the provided accelerator.

**No:** There's now a new accelerator to configure LinkedIn as your Identity Provider.

Avoid documenting future features or products, even in innocuous ways. Don't pre-announce anything in documentation.

## Rules for Pronouns

For when to use "you" and singular "they", refer to [Use second person](#use-second-person) and [Use gender-inclusive language](#use-gender-inclusive-language).

### Ensure pronoun references are unambiguous
A pronoun should clearly refer to a specific noun (antecedent). If there is any potential for confusion, restate the noun.
**Yes:** "If you are using the Data Grid, you can change the view in ODC Portal. This new feature simplifies the process."
**No:** "If you are using the Data Grid, you can change the view in ODC Portal. It is a new feature."

### Use `that` and `which` correctly
Use `that` for restrictive clauses (information essential to the meaning of the sentence). Use `which` for nonrestrictive clauses (information that can be removed without changing the core meaning).
* **Yes:** "The platform service that handles all requests to the services is the Platform Load Balancer."
* **Yes:** "OutSystems, which is a low-code development platform, helps you create apps."

### Use "who" for people
The pronoun `who` should be used when referring to a person or people.
* **Yes:** "The person who configures the security settings should be an administrator."
* **No:** "The person that configures the security settings should be an administrator."