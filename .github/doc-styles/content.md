# Grammar and content

Write clearly and consistently.

## Tone and voice

Use the appropriate tone and voice in your content. Your content must be:

* Friendly and straightforward
* Clear and concise
* Inclusive and respectful
* Free of jargon and sales talk

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

Contractions help create friendlier and informal sentences, as full forms are generally reserved for formal writing. Avoid making contractions from a noun and a verb, especially with nouns denoting OutSystems products.

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

## Be careful with modal verbs

This section applies to the modal verbs can, could, may, might, will, shall, would, should, and must. Modal verbs describe what you believe or think of the product, or they denote an ability or obligation. In contrast, technical content confidently describes what the product does. Using a modal instead of a stronger structure creates a weak and wordy sentence. It also makes your readers less confident about the content.

**Examples**

**Yes:** OutSystems lets you create several app types.

**No:** There are several app types you can create. (Here, "can" means ability, all people are able to create an app.)

**Yes:** All customers with a valid and active Subscription are eligible for OutSystems Support.

**No:** All customers with a valid and active Subscription can contact OutSystems Support. (All people can dial a phone number.)

**Yes:** OutSystems handles unforeseen or unhandled errors in applications.

**No:** OutSystems handles unforeseen or unhandled errors that might occur in applications. (If errors do happen, there's nothing hypothetical about their existence.)

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

The language in technical content must be clear and precise. Clarity and precision make content useful for the audience. Check out the examples that demonstrate how being vague, blaming users, or taking their time and skills for granted weakens clarity.

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

**Yes:** To view the document, click *View*.

**No:** To view the document, please click *View*.

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

Don't put important information in parentheses. Unfortunately, some readers ignore any information that appears in parentheses.

Whenever you're inclined to use parentheses, consider whether they're necessary. Maybe the sentence might work just as well if you remove the parentheses and set off the phrase or sentence by using commas, dashes, or periods.

If you need to include parentheses in the middle of a sentence, keep the information in the parentheses short. Otherwise, consider using two sentences.

**Examples**

**Yes:** Enter a six-digit hex number, and then click *OK*. For example, if you want the color forest green, enter `228B22`.

**No:** Enter a six-digit hex number (for example, if you want the color forest green, enter `228B22`), and then click *OK*.

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

For more details, see [Bias-free communication](https://docs.microsoft.com/en-us/style-guide/bias-free-communication) by Microsoft.

**Examples**

**Yes:**

* When developers download a Forge component, they can install it in Service Studio. (Use plural to avoid referring to gender.)
* When a developer downloads a Forge component, they can install it in Service Studio. (Use "they" to refer to a single person without mentioning their gender.)
* When you download a Forge component, install it in Service Studio. (Are your target readers developers? If yes, then "you" is a better choice.)

**No:**

* When a developer downloads a Forge component, he can install it in Service Studio. (Service Studio is not used exclusively by male developers or developers who identify as men.)

## Use standardized example domains

When providing examples of domain names, use one of the domains reserved for such use. For example, example.com. Don't use other domains nor any of our customer domains.

See [RFC 6761 - Special-Use Domain Names](https://tools.ietf.org/html/rfc6761) for more information.

**Example**

**Yes:** Enter the email address, for example, john.smith@example.com.

**No:** Enter the email address, for example, john.smith@outsystems.com.

## Check the readability scores

A readability score shows the estimated education level needed to understand a given text. Our content should be understood by high school graduates.

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

### Use "you" to address the reader
The primary voice for documentation should be the second person ("you") to speak directly to the user. Avoid using "we" or "I."
* **Yes:** "You can upload files up to 90 MB when creating an external library."
* **No:** "We have made it possible to upload files up to 90 MB."

### Use singular "they" as a gender-neutral pronoun
When referring to a generic person, such as a user, use "they," "them," or "their." This avoids gender-specific pronouns like "he" or "she."
**Yes:** "When a user logs in, they can access their assigned resources."
**No:** "When a user logs in, he can access his resources."

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