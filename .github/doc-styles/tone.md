# Documentation tone and language rules

Use these rules when writing or reviewing documentation in this repository.

## Tone and voice

Write in a friendly, direct, and precise voice, as a knowledgeable colleague explaining how the product works. Your content must be:

* Friendly and straightforward.
* Clear and concise.
* Inclusive and respectful.
* Free of jargon and sales talk.

### Calibrate your voice

Aim for the middle column. Drafts, especially AI-generated ones, drift toward either of the other two.

| Too informal | Right | Too formal |
|---|---|---|
| Just wire up the connection and you're good to go! | Configure the connection. | The connection may be configured by utilizing the settings panel. |
| This feature is super powerful and makes building apps a breeze. | This feature reduces the number of steps to build an app. | This feature facilitates the expedited construction of applications. |
| Wondering how to reset your password? Here's how. | To reset your password, do the following. | The password reset procedure is described hereinafter. |

### What friendly means

* Friendly means addressing the reader as "you", using contractions, choosing plain verbs, and stating things directly.
* Friendly doesn't mean slang, enthusiasm, humor, filler politeness, or chatty connectors.

### Put clarity before personality

Readers scan to finish a task, so lead with what they need. Don't try to entertain or sell. Keep benefits factual.

### Avoid both extremes

* **Too informal:** hype, slang, exclamation marks, rhetorical questions, and words like "easy", "simple", "just", and "simply".
* **Too formal:** passive voice, stacked nominalizations ("the facilitation of the creation of"), and words like "via", "utilize", and "enables the acquisition of".
* **AI-generated text:** AI drafts tend toward promotional wording ("powerful", "seamless", "robust") or stiff, abstract wording. Replace both with plain statements of what the reader can accomplish and what the product does to support it.

### Keep writing natural and translatable

* Use plain, consistent words.
* Avoid idioms, clichés, pop-culture references, and culture-specific references.
* Avoid starting several sentences in a row the same way.
* Avoid strings of choppy sentences. Vary sentence structure while keeping sentences short.

### Describe behavior literally

State what the product does for the reader, not what it's like. Lead with the reader's goal or problem, then describe the behavior that addresses it. For more information, refer to [Write for the user's problem, not the feature](content.md#user-problem-first). Figurative comparisons, human traits, and absolute claims make a statement vague and hard to verify.

* **Figurative comparisons:** Don't use "as if", "like having", "think of it as", or similar phrases to describe product behavior.
* **Human traits:** Don't describe the product as if it were a person. Avoid verbs such as "remembers", "understands", "knows", "thinks", and "forgets" unless the UI uses them.
* **Unclear references:** Don't use "this" or "that" as a pointing word ("that conversation", "this feature") before you've named the noun. Introduce the noun first. This rule doesn't apply to "that" in restrictive clauses.

**No:** Mentor takes everything said since the beginning of that conversation into account, as if you never left the conversation.
**Yes:** Mentor retains the history of a conversation. When you continue a conversation, you don't need to restate earlier constraints, naming conventions, or decisions.

**No:** The editor understands your project and always suggests the right component.
**Yes:** The editor suggests components based on the elements in your project.

**No:** Think of the portfolio as a folder for your assets.
**Yes:** A portfolio groups assets and has its own set of stages.

### Self-check

Before you finish a draft, confirm the following:

* A busy developer can act on it quickly.
* The text describes behavior literally, without figurative comparisons, human traits, or unverifiable absolutes.
* It sounds like a colleague explaining the product, not a marketer or a legal document.
* A non-native English reader can understand it.

## Be brief and confident

* Write short sentences and well-structured paragraphs.
* Do not repeat yourself.
* Lead with what the reader needs to accomplish, then describe what the product does in confident, present-tense statements. Don't describe how good the product is.
* Hedging and unnecessary modal verbs weaken a statement. Treat them as a tone problem.

### Be careful with modal verbs

Use only the modal verbs can, must, and will. Use "can" for a real choice, "must" for a real requirement, and "will" sparingly. Avoid could, may, might, shall, would, and should. For details and examples, refer to [content.md](content.md#be-careful-with-modal-verbs).

* **Yes:** You can export the report as a CSV or PDF file.
* **No:** You may export the report as a CSV or PDF file.

## Language and grammar

* Use American English (spelling, word choice, and dates).
* Use the present tense when possible.
* Use contractions (it’s, don’t, there’s) unless the contraction would attach to a product name.
* Use the active voice.
* Use second person ("you") to address the reader. Do not use "we" to refer to OutSystems.
* Be clear and precise. Avoid vague language.

## Capitalization

* Do not capitalize common nouns unless they start a sentence.
* Capitalize proper nouns and brand names (product, company, and technology names).
* For APIs and endpoints, use the exact capitalization as defined in the API documentation.
* For code elements (variables, functions, classes), keep the original capitalization.

## Inclusive, accessible, and global writing

* Use gender-inclusive language.
* Avoid idioms and jokes.
* Do not describe locations using only directional words (left, right, above). Add context for screen readers.
* Avoid the words "easy", "simple", "just", and "simply". They make a task sound quicker or less demanding than it is for some readers.

## Avoid filler politeness

Avoid "sorry" and "please" in technical documentation.

* **Yes:** To view the document, click **View**.
* **No:** To view the document, please click **View**.

## Timeless documentation

* Avoid time-based words and phrases such as new, now, currently, latest, and future.
* Do not pre-announce features or products.
* If you must refer to a new feature, anchor it to a version number or date.

## Clarity rules for pronouns and clauses

* Ensure pronoun references are unambiguous. If there is potential confusion, restate the noun.
* Use `that` for restrictive clauses and `which` for nonrestrictive clauses.
* Use `who` for people.

## Style preferences

* Use a serial comma in lists of three or more items.
* Avoid putting important information in parentheses.
* Use `example.com` for domain examples. Do not use real customer domains.
* Avoid Latin abbreviations:
    * Use "that is" instead of "i.e.".
    * Use "for example" or "such as" instead of "e.g.".

## Readability

Content should be understood by high school graduates (readability score < 13).

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
