# Documentation formatting rules

Use these rules when writing or reviewing documentation in this repository.

## Markdown and layout

* **Unordered lists**: Use `*` for bullets.
* **Nested unordered lists**: Indent by 4 spaces.
* **Ordered lists**: Prefix every item with `1.`.
* **Headings spacing**: Leave an empty line before and after a heading.
* **Headings and visuals**: Add at least one sentence between a heading and an image or table.
* **Code blocks**:
    * Use fenced code blocks (triple backticks).
    * Specify the language when it adds value (for example, `javascript`).

## Typographical emphasis

* **Bold**: Use for UI elements (labels, buttons, links) and occasional emphasis.
* _Italic_: Do not use italic.
* **Underline**: Do not use underline.

## UI elements, user input, and properties

* **UI labels**: Use **bold** (for example, **New Application** window, **Save** button).
* **User input**: Use `inline code` for text the user must type (for example, enter `display-flex`).
* **Property names**: Use **bold** (for example, **Name** property).
* **Typed values**: Use `inline code` (for example, enter `Yes`).
* **Selected values**: Use **bold** (for example, select **Yes**).
* **Keyboard shortcuts**: Use bold and sentence capitalization (for example, select **Ctrl+N**).

## Lists and punctuation

* **Parallel syntax**: Use the same grammatical structure for each item in a list when possible.
* **List punctuation**:
    * Start each item with a capital letter.
    * End each item with a period unless it is:
        * A single word.
        * Missing a verb.
        * Entirely code font.
        * Entirely link text.

## Links and cross-references

* **Write descriptive link text**: Use short, unique, descriptive phrases. Do not use "click here".
* **Introduce cross-references consistently**:
    * Use "For more information, refer to ...".
    * Use "For more information about ..., refer to ... ." when needed to clarify the purpose.
    * Use "about" (not "on").
    * Use "refer to" (not "see") for cross-references.

## Placeholders

Format placeholders consistently:

* In Markdown, wrap inline placeholders in backticks, and use an asterisk before the first backtick and after the second one (``*`PLACEHOLDER_NAME`*``).
* Use uppercase characters with underscore delimiters (for example, `*API_NAME*`).
* Explain the placeholder the first time you use it.

## Warnings and info sections

Use HTML `<div>` elements with `class="warning"` or `class="info"`. Include `markdown="1"`.

```html
<div class="warning" markdown="1">

Include your warning text here.

</div>
```

## Images and screenshots

* Use standard Markdown image syntax: `![alt text](images/my-image.png)`.
* Do not use the `?width=` parameter (deprecated).
* Include screenshots only when needed to guide users through complex procedures.

## File, folder, and image naming

* **Files and folders**: Use lowercase, numbers, and hyphens only. Do not use spaces or underscores (for example, `my-new-topic.md`).
* **Images**:
    * Use lowercase, numbers, and hyphens.
    * Include a suffix identifying the source:
        * `ss` (Service Studio)
        * `odcs` (ODC Studio)
        * `lt` (LifeTime)
        * `sc` (Service Center)
        * `pl` (ODC Portal)
        * `usr` (Users)
        * `fg` (Forge)
