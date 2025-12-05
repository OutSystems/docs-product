---
summary: Discover UI performance optimization techniques for OutSystems 11 (O11), including AJAX moderation, viewstate reduction, and strategic caching.
guid: eda645ae-a7e2-4844-af65-4b45d8d69b18
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: ui optimization, performance improvement, ajax optimization, viewstate management, caching strategies
audience:
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
---

# Best practices for enhancing UI performance

There are no fast applications with slow user experiences. To promote the adoption and keep the end users satisfied, the application has to respond fast. Don’t discard usability issues, but don’t compromise the performance just to have a nicer way to present the data.

## Avoid using preparation data in screen actions

### Description

Avoid using preparation data in screen actions; most of the time it's better just to fetch the data again.

### Solution

Avoid using data created in the screen preparation in the screen actions. For instance, instead of using the tablerecord record data, use only the ID of the row and fetch the data from the database again is needed.

### Importance

Page size affects usability since it will increase the time to submit a form. If you use screen preparation data on screen action, that data will be saved on the page viewstate. Since the viewstate is a part of the page it is sent to the client with every requested page. The viewstate is also sent to the server on a post, postback and AJAX request. So avoid using preparation data in screen actions otherwise the size and loading time of the page can increase dramatically.

## Use AJAX with care and in moderation

### Description

AJAX is a great tool to improve usability and user interaction but needs to be used with care to avoid performance issues.

### Solution

You should not abuse AJAX when you are designing a new page. Only after you have the full idea of what you need to improve on regarding user interaction should you start adding localized AJAX patterns. Remember that each AJAX request to the server takes the entire page viewstate, so you should avoid including unnecessary things in the viewstate (don't use records or list records from the preparation in the screen actions, etc.).

### Importance

Most of performance problems are detected due to the impact that they have on the end user. The other best practices improve the performance perceived by the end user by reducing the server side time of processing and the amount of resources used (processor, database, etc.). This best practice, on the other hand, tries to maximize the improvement in the performance perceived by the end user, at the expense of server performance, that should be minimized. So, when other best practices cannot be used because things cannot be further optimized, you can use AJAX to hide the processing time from the perception of the user.

### Remarks

AJAX is a powerful weapon, and like all powerful weapons, should be used with extreme care. When you start using it, the risk of overdoing it is high, and it will have the opposite effect, worse performance and worse usability.

## Split large Screens

### Description

Split large screens to reduce Viewstate size and the number of queries in the preparation.

### Solution

Splitting large screens (using server side tabs for instance) will reduce the page information and therefore reduce the size of the Viewstate and the size of the page itself.

### Importance

Using many records and record lists, will cause the page Viewstate to grow considerably, increasing the HTML rendered page size, increasing page network transmission time, and increasing screen processing time. All these add up to slow screens since the records/record lists are serialized and deserialized during the page generation and on submit at the server side.

### Remarks

When splitting screens, the customer needs and the whole application logic must be accounted for. Logic must be reused and it's possible that just splitting the screen by half won't do the trick. Splitting in more than two parts, or unevenly, may be the best way to do it.

## Cache, baby, cache!

### Description

Use cached WebScreens/WebBlocks when repeated use yields the same result therefore saving the cost of processing the screen/block over and over again. Particularly useful in AJAX queries that retrieve lookup data.

### Solution

If the operation is executed via web screen, cache the entire contents of the screen. Keep in mind that this is based on parameters and these should vary as little as possible. This is particularly useful in AJAX queries that are used for retrieving long lived information like lookups.

### Importance

Every time a request is served from the cache the client gets the response faster and most importantly the server spends fewer resources that can be used to respond to other requests.

### Remarks

Caching is a double edged sword. While it can significantly boost the performance of certain operations always keep in mind that information is cached. Every time a change to that information is required it will either take longer to be available or you have to use cache invalidation mechanisms. Also, caching will not run any logic, which means no updates will be performed for a cached element.

## Minimize screen parameters

### Description

Reduce the number of screen parameters and their sizes to a minimum to improve performance and memory.

### Solution

Avoid passing lots of information using screen parameters. Try to pass only entity identifiers and user inputs between screens to improve performance.

### Importance

When a large amount of data is passed through screen input parameters, it increases the page request and consequently page size, causing general slowness in overall user experience. This is especially important when dealing with network latency or when suffering from server side memory shortage.

### Remarks

Note that if only passing entity IDs, you will need to do another query to the database to get the data you need. So one should consider the pros and cons of having large page sizes v. extra queries to the database.

## File your JavaScript

### Description

Avoid the use of JavaScript in screen expression; place JavaScript code in files included through extensions or module resources.

### Solution

Avoid using large JavaScript in screen expressions. Always place it in a file and include it through extensions or module resources, placing a link script to it.

### Importance

Placing large chunks of JavaScript code in your screen through expressions will significantly increase the screen size causing poor user experience during page load.

### Remarks

This is a good idea because it enables reusability between modules and encapsulates the JS logic. Always use it on the JavaScript frameworks. However, for custom JavaScript, it may be a problem when you need to use local widget ids.

## JavaScript Loading Delay

### Description

Move the JavaScript that is not needed at load time to the bottom of the page to make the page load faster.

### Solution

Consider moving the JavaScript that is not needed at load time to the bottom of the page to make the page load faster.

### Importance

Moving the JS to the end of the page will ensure the browser will display what is needed first and load the JavaScript later on.

### Remarks

This is fundamental rule especially in homepages that need a small load time - it might be harder to maintain but it is well worth the effort. You can use a static resource manager to deal with file inclusions. You need to be careful to make sure you do not execute any JavaScript that requires the files before they are loaded though.

## CSS sprite images

### Description

Use CSS sprites that replace several images to reduce the number of server requests and improve screen load times.

### Solution

Combine images frequently used on the same screen in a single image (CSS sprite) making use of CSS background-image and background-position properties to display the desired image segment.

Learn more with the [full description of the technique](http://www.websiteoptimization.com/speed/tweak/css-sprites/).

### Importance

When using sprites the number of HTTP requests to fetch images are significantly reduced allowing for faster screen loading.

### Remarks

This best practice should only be used for high traffic public facing applications with a large number of images.

The effort required to build and maintain CSS sprites is not negligible. Furthermore using CSS sprites is more error prone than individual images.

## JavaScript minification

### Description

Whenever possible use minified JavaScript in production environments.

### Solution

All major JavaScript libraries supply minified versions. For custom JavaScript, minification tools can be used to obtain minified versions.

### Importance

Minification reduces the JavaScript size by removing unnecessary characters and even when using compression it still has some impact on JavaScript size.

### Remarks

Minified JavaScript is extremely hard to read so any JavaScript problem in the production environment will be especially hard to diagnose. Furthermore there is some effort involved in maintaining development (non-minified) and production (minified) versions. Stable JavaScript libraries like JQuery and Prototype shouldn't pose any problems. For custom JavaScript, only public high traffic application will yield positive payoffs in using this technique.
