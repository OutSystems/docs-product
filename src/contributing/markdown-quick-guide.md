# Markdown language hints

The following hints cover the basics of markdown making you able to edit almost everything in our documentation. If you need/want to know about markdown extensively, check this guide.


## Headers
To create headers just use the following syntax:
Level 1 heading - # your H1 title
Level 2 heading - ## your H2 title
Level 3 heading - ### your H3 title
…

## Images
Use the inline syntax to add images to your topic:

`![alt text](image_path/image_name)`

Note: Currently, we don’t use the reference-style syntax for including images. Reference-style image syntax looks like this:

`![alt text][image_id]`

`[image_id]: image_path/image_name`

Where “id” is a string of your choosing that identifies this image in the current topic.


**Notes:**
> Put all the images related to a given topic under an images/ folder inside the topic folder.

> Name the images, if any, [topic name]-n (with n starting in 0 for the first image in the topic and finishing in the highest digit needed for the last image in the topic).

 
*Example:*

For an image called “hello-world-0.png” the right way to put it in the topic is:

`![Hello World](images/hello-world-0.png)`

## Cross references/links
Add links using the inline syntax:

This is [an example](http://success.outsystems.com/Documentation/11/Developing_an_Application) link to an absolute URL.
A [relative link](sibling.md) to a Markdown file stored in the same folder.
A [relative link](../parent-topic.md) to a file stored in the parent folder.

Use Linux-like relative paths (i.e. paths using forward slashes ‘/’ when needed) when linking to Markdown files stored in the same Git repository, either in the same folder, parent folder, or a subfolder. Do not include the “./” prefix when linking to topics in the same folder.

Use absolute URLs pointing to the final topic location (after publishing) when linking to topics whose source is not stored in the same Git repository as the current topic.

## Code Samples
To highlight a line of code in the middle of a sentence do the following:

`code line`

If you want to highlight a block of code:

```
<beginning of code lines>
Code lines
</end of code lines>
```

Note: This second syntax only works when not indented. When inside a list, indent the code one more level than the list level to turn it into a code block.
Example: 

1. My numbered list item here.

    This becomes a second paragraph inside the same list item because it only has one level of indentation (4 spaces). It’s not rendered as a code block.

        Since the indentation in this third paragraph is one level above the list level (8 spaces, when list item paragraphs are indented with 4 spaces), this paragraph is rendered as a code block.

When using the second syntax you can additionally define the language of the code block:

```
```javascript
var myVar = 1;
```

This activates syntax highlighting for the specified language when the article is published.

Available languages: html, xml, css, javascript, json, sql, csharp

## Tables

To add a table, use three or more hyphens (---) to create each column’s header, and use pipes (|) to separate each column.

| Heading1 | Heading 2 |
|----------|-----------|
| Text 11 | Text 21 |
| Text 12 | Text 22 |

## Infos/Warnings
Create Info and Warning sections using HTML. Use HTML tags directly in the Markdown file, leaving a blank line above and below the DIV tags:

Info:

<div class="info" markdown="1">

Info text

</div>

Warning:

<div class="warning" markdown="1">

Warning text

</div>

**Note:** By including the markdown="1" attribute you can use Markdown syntax inside the DIV element.

## Definition Lists
Even though Markdown doesn’t support definition lists by default, we use an extension to add support for rendering this HTML element.

Example:

Term
:   This is the description of the term. Start with a colon and add 3 spaces.

Second term
:   Another definition here.

    It can have a second paragraph, as long as it’s indented with 4 spaces after a blank line.


This is rendered as:

Term
    This is the description of the term. Start with a colon and add 3 spaces.

Second term
    Another definition here.
    It can have a second paragraph, as long as it’s indented with 4 spaces after a blank line.

**Note:** Definition lists are not supported when previewing Markdown files in GitHub!
