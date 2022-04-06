---
tags:
summary: 
en_title: Avoid inline JavaScript or inline style
---


# Avoid inline JavaScript or inline CSS style

JavaScript code or CSS styles can be defined inline inside Screens and WebBlocks by using unescaped Expressions elements or via the Extended Properties window of Service Studio.

During development cycles developers frequently resort to inline style for a specific Screen or Block (for example, to quickly adjust the padding of an element or to define a small on-click JavaScript function).

## Impact

While the usage of inline styles or code can accelerate development, given how easy they can be defined, it can lead to significant impacts in the long run. Having code scattered throughout the application instead of centralized in one place, compromises maintainability and reliability.

The build-up of the inline CSS styles often translates into code duplication, making the project harder to maintain when the same style needs to be changed in several places. The same applies to the inline JavaScript snippets, as they cannot be reused across Screens or Web Blocks.

From the performance point-of-view, the usage of inline styles or scripts degrades performance as the page size increases. Also, the elements can't be cached unless the whole page is cached. The impact is greater with the inline scripts because the page rendering is halted while the inline code is interpreted.

Finally, and given the typical motivation behind using inline styles or scripts, they will probably be left undocumented, thus hindering code readability as well.

## Best practices

In accordance with the principle of separating content and style, both CSS styles and JavaScript code should be decoupled from HTML code and moved to a separate location, such as CSS stylesheets or JS file. The resources then can be easily cached and reused.

Given that each Screen or Web Block can have its own custom CSS or JavaScript file, the developers must be careful to avoid escalating the number of resources needed to render a given page.

In order to address this issue, you should have a theme hierarchy that promotes reusability. Also, place your JavaScript API’s in the module file.

JavaScript code should be minified to reduce network traffic/payload. For debugging and troubleshooting purposes, minification should be applied in Production environments only.
