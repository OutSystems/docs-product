---
summary: Explore mobile development best practices in OutSystems 11 (O11) to enhance app performance and user experience.
guid: 35d524c9-ab83-4f6e-b3fe-b2a89b2ff7af
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/iBD5yo23NiW53L1zdPqGGM/Developing-an-Application?node-id=5593-486&t=dmWMuLk1wDbU6pmJ-1
tags:
  - Best Practices
  - JavaScript
  - Mobile app
  - Optimization
  - OutSystems UI
  - Performance
  - Troubleshooting
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - apply
  - evaluate
isautopublish: true
---

# OutSystems mobile best practices

Mobile apps bring a completely [new mindset for the development model](https://www.outsystems.com/blog/posts/convert-website-to-app-what-to-consider/). On the one hand, users have very high expectations regarding their experience with mobile apps. On the other hand, device limitations together with network restrictions can have a major impact on that experience. No matter the circumstances or limitations, users expect mobile apps to work like a charm!

If you want to develop a mobile app that offers your users the best mobile experience, keep these key rules in mind:

* **Focus on mobile use cases to guide your development**: Choose the best use cases for a great mobile experience. Start small and iterate. Use less and optimized content. Show what's more important first. Use common mobile patterns such as the ones provided by the [OutSystems UI](https://www.outsystems.com/outsystems-ui/) framework.
* **Keep heavy logic on the server side**: Keep client-side information as simple as possible. Execute complex data processing and calculations on the server side, using the minimum number of server requests as possible. Cache your results on the client side.
* **Choose OutSystems low-code over JavaScript**: OutSystems automatically optimizes the code for the best runtime performance. Use JavaScript only if it cannot be done with the OutSystems low-code language or in advanced extensibility scenarios.
* **Test your app in real world scenarios**: Understand how your mobile app is used and thoroughly test it before deploying to production. Ensure that device limitations, [network restrictions](https://www.outsystems.com/blog/posts/low-bandwidth-lie-fi/), or [offline periods](https://www.outsystems.com/blog/posts/offline-mobile-apps/) don't prevent users from having a great experience.

This article builds on these ground rules with best practices that help you avoid common pitfalls. The pitfalls covered here typically impact user experience and app performance.

If you haven't done so already, start with the [Becoming a Mobile Developer](https://learn.outsystems.com/training/journeys/mobile-developer-679) online training to learn how to develop high-quality mobile apps.

We'll be updating and adding new content to this article along the way!

## User interface

A [great UI experience](https://www.outsystems.com/blog/posts/mobile-look-and-feel/) increases the user perception of a fast and fluid mobile app. This section presents a set of best practices to improve the UI experience of your OutSystems mobile app.

### Discover and use OutSystems components

Developing common mobile patterns from scratch takes a huge effort and feels like reinventing the wheel.

Use the [OutSystems UI](https://www.outsystems.com/outsystems-ui/) framework or other [OutSystems Forge](https://www.outsystems.com/forge/) components, which provide you with a large set of common mobile patterns. Remember to keep them up to date to benefit from the latest improvements.

### Design an empty state for content being fetched

When a user navigates to a screen, the static content is usually rendered first. The dynamic content takes more time because it is [fetched asynchronously](../ui/screens/screen-block-lifecycle-events.md). The result is a poor UI experience: an incomplete screen with content moving around as the dynamic data renders.

Improve the user experience by [designing and displaying an empty state image](https://success.outsystems.com/documentation/how_to_guides/front_end/how_to_improve_list_slowness_on_low_end_devices/) while the dynamic content is being fetched. A couple of good examples are Facebook or LinkedIn.

![Example of a mobile app screen displaying an empty state design while content is being fetched.](images/OutSystems-Mobile-Best-Practices-0.png "Empty State Design Example")

This strategy is valid for all dynamic content in the screen such as blocks, cards or list items. When the empty state turns into the fetched content you may experience some flickering. To avoid flickering when the empty state turns into the fetched content, choose one image that assures a smooth transition, such as a blurred gray line or a spinner.

### Prioritize screen content rendering

By default, OutSystems mobile apps fetch screen data without a specific priority. If your screen has content that is more relevant and should be displayed first but you are not prioritizing its rendering, it may lead to a bad user experience. For example, displaying an advertising banner before the main information of the screen.

Delay the rendering of the secondary content so that the main content is rendered first. To do this:

1. Place the secondary content in a Block inside the _True_ branch of a*n If w*idget. The Block must enclose all the logic to fetch the secondary content so that data fetching of the secondary content only runs when the Block is rendered.

1. On the*False*branch of the _If_ widget, place [an empty state](#design-an-empty-state-for-content-being-fetched) to avoid content from moving around when the secondary content is fetched.

1. Set the _If_ condition to a variable holding _False_ by default.

1. In the On Render event of the screen, add logic to set the variable to _True_ so that the secondary content starts to render.

![Illustration of prioritizing content rendering in an OutSystems mobile app using conditional blocks.](images/OutSystems-Mobile-Best-Practices-1.png "Content Rendering Priority in OutSystems")

### Set the width and height of image widgets

If you do not set the width and height of an Image widget, the user can get a flickering effect while the final image is being downloaded. For example, not setting the image height might cause the total height of the screen to change until the image loads completely. The widget height changes from 0px to the height of the final image.

Set the width and height of the Image widget to the expected size of the final image.

![Screenshot showing how to set width and height properties for an image widget in OutSystems.](images/OutSystems-Mobile-Best-Practices-2.png "Setting Image Widget Dimensions")

## Performance

Handling data or implementing logic specifically for mobile scenarios can have a significant impact on a mobile app performance. Follow the best practices in this section to develop performant mobile apps. Also check the other sections for best practices that, although not directly related to performance, can contribute to improving it.

### Fix the performance warnings

OutSystems automatically detects potential performance issues while you are developing your mobile app in Development Environment. Not paying attention to them may result in a bad performance of the application.

![OutSystems development environment interface displaying performance warnings.](images/OutSystems-Mobile-Best-Practices-3.png "OutSystems Performance Warnings")

Check the performance warnings displayed in the TrueChange tab and fix them.

### Design a lightweight local storage { #lightweight-local-storage }

Keeping a large amount of data in the device's local storage, for example in offline or cache scenarios, might become a performance killer in low-end devices, causing `Failed to allocate X bytes` errors.

Use the following techniques to design a lightweight local storage:

* Design the local storage data model using only the attributes that you need, instead of all attributes of the corresponding server entity. Consider [denormalizing](https://en.wikipedia.org/wiki/Denormalization) the local data model to avoid complex queries like having multiple JOINS.
![Diagram comparing server database and optimized local storage data models in OutSystems.](images/OutSystems-Mobile-Best-Practices-4.png "Local Storage Data Model Design")

* Identify the best [data synchronization patterns](../data/offline/intro.md) for your use case and define exactly when to run them.

* Keep only the entity records you need for your use case in the local storage, instead of all records. For example, get only the open tasks for a given time period, instead of all tasks.

* Consider synchronizing data in small chunks, starting with the most relevant data first (e.g. synchronize only text information first; photos and other images can be synchronized later).

* If your synchronization process must include images, try to compress them.

### Keep the splash screen simple and fast

When your mobile app starts, it displays a splash screen while internal operations are running. Adding heavy or lengthy operations to the splash screen increases the time that the users must wait to use the app. Additionally, if the splash screen has a complex UI, the users may see a blank screen before the splash screen renders.

![Example of a simple and fast-loading splash screen for a mobile app.](images/OutSystems-Mobile-Best-Practices-5.png "Splash Screen Best Practices")

To keep the splash screen simple and fast to load you should avoid:

* Requests to the server

* Heavy logic

* Complex UI, namely too many Blocks

For example, consider the following possible approaches:

* Make server requests preferably in an event handler run at a later stage, like On Ready. If you really need to obtain server data in the app initialization stage, minimize the number of server calls (e.g. by obtaining several pieces of data using a single server action designed for the loading stage).

* Do not perform lengthy operations when the mobile app starts. For example, if you must synchronize data that is used in the first screen of the app, keep the data transfer to a minimum and postpone the transfer of secondary data.

**Tip**: To provide an amazing user experience, we also recommend that you [customize the native splash screen](../../deploying-apps/mobile-app-packaging-delivery/customize-mobile-app/use-custom-splash-screens.md).

### Optimize Fetching Server Data for a Screen

Using the On After Fetch of server aggregates to execute other aggregates in sequence generates several server requests and slows down the application.

Create a Data Action containing aggregates in the correct order. This action runs in the server in a single request and returns all data.

![Flowchart demonstrating optimized server data fetching for a screen in OutSystems.](images/OutSystems-Mobile-Best-Practices-6.png "Optimized Data Fetching for a Screen")

### Fetch list data on demand

Lists involve fetching and rendering multiple records at the same time. If not done carefully, the experience can become cumbersome, especially on low-end devices or with bad network connectivity.

Fetch records as you need them instead of all at once. Start with a minimum set, for example, 10 records. As the user scrolls down, use the On Scroll Ending event to fetch the next set of records — for example, the following 10 records.

To understand how this works, scaffold a list on a screen and this mechanism is provided by default.

### Keep list items simple

Avoid designing list items with complex logic or complex widgets like JavaScript to load a map from Google Maps, for example. That complexity is multiplied by the number of items being rendered in the list.

### Avoid expanding content in list items

Do not design list items with content that can be expanded, such as a description that is trimmed and has a 'Show All...' link. This impacts the behavior of the list while rendering. Use OutSystems UI patterns such as [MasterDetail](../ui/patterns/mobile/adaptive/masterdetail.md) instead.

### Fine-tune how lists fetch data on demand

Adjust the number of records that are initially loaded, the increment when scrolling down, and the scroll threshold to trigger the On Scroll Ending event. This provides a better user experience when using lists by avoiding visual glitches and slow list scrolls.

The values to use depend on the size of the records:

* The **initial number of fetched items** should ensure a balance between a fast data fetch and a sensible amount of scrolling until a request for more data occurs.
* The **incremental number of fetched items** triggered by scrolling should generally be similar to the initial amount of fetched items, but you may need to tune it according to the usage of your app. If users frequently use the list to search for entries, your app should be prepared to fetch data faster and load more items at a time.
* The **scroll threshold** that triggers fetching new items is the distance in pixels before the scroll hits the end of the list and should be set to 2000 pixels. If you need to tune this threshold to improve the usability of your application, you can add the attribute `infinite-scroll-threshold` to the list widget with a new integer value in pixels.

The next picture shows examples of values to use in different situations. Start with these as initial guidelines and then test and adjust to your specific case.

![Table with examples of initial records, increment, and scroll threshold values for list optimization.](images/OutSystems-Mobile-Best-Practices-7.png "List Fetching Optimization Parameters")

### Provide visual feedback while fetching list data

Users need a clear indication that the list has more items to show and that it's actually doing something. An animated image should be enough to provide this message to the user. Even so, as a performance target, keep in mind that during typical application usage the users should never hit a loading wall at the end of a list.

### Optimize the file size of images

Big image files can increase download time or even block the download. They lead to poor performance, especially on older devices or in low connectivity scenarios. They also consume storage space and might be too big for the screens of mobile devices, even high-DPI models.

Reduce image size (in bytes) and adapt its dimensions (height/width) considering your target user's experience — follow [Google's Image Optimization](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/image-optimization) recommendations. Also, consider delaying the fetch of images to a later stage. Refer to the best practice to [Prioritize Screen Content Rendering](#prioritize-screen-content-rendering).

## JavaScript

OutSystems generates mobile apps with fast and optimized JavaScript code. You should carefully assess whether to add your own JavaScript code. To help you with that, follow these guidelines:

* **Use OutSystems low-code instead of custom JavaScript**: The most common components for implementing a mobile app are provided in [OutSystems UI](https://www.outsystems.com/outsystems-ui/) and in the [OutSystems Forge](https://www.outsystems.com/forge/). You can probably find the ones you need for your scenario and customize them accordingly.
* **Use JavaScript if strictly necessary and follow the best practices**: Keep in mind that OutSystems low-code is more performant, but if you decide to use your own JavaScript, it's important that you read and follow the best practices in this section.
* **Use the OutSystems public [JavaScript API](../../ref/apis/javascript/intro.md) and not internal APIs**: Internal APIs are not supported and can change in any upgrade, thus breaking your JavaScript code.

### Follow the industry JavaScript best practices

When writing JavaScript, make sure you know the code you're implementing and how it affects the app.

Follow the best practices for JavaScript development like the ones described in [W3Schools](https://www.w3schools.com/js/js_best_practices.asp) or these [JavaScript Coding Standards and Best Practices](https://github.com/stevekwan/best-practices/blob/master/javascript/best-practices.md).

For example, use performant [JavaScript selectors](https://www.w3schools.com/w3js/w3js_selectors.asp) to obtain elements from the DOM, and avoid [properties and methods](https://gist.github.com/paulirish/5d52fb081b3570c81e3a) that trigger the browser to recalculate geometric information for the elements — known as [Layout or Reflow](https://developers.google.com/web/fundamentals/performance/rendering/avoid-large-complex-layouts-and-layout-thrashing).

![Badge symbolizing best practice standards for JavaScript development.](images/OutSystems-Mobile-Best-Practices-8.png "JavaScript Best Practice Badge")

### Avoid using external JavaScript libraries

External JavaScript libraries can be too complex to run on mobile devices.

Find OutSystems components in [OutSystems UI](https://www.outsystems.com/outsystems-ui/) or in the [OutSystems Forge](https://www.outsystems.com/forge/) and use them instead of external JavaScript libraries.

However, if it is clear that you really need to [use the JavaScript library](../../integration-with-systems/javascript/mobile/use-external-lib.md), use it in a Script element and not in JavaScript nodes.

![Diagram showing the correct way to implement JavaScript libraries in OutSystems.](images/OutSystems-Mobile-Best-Practices-9.png "Using JavaScript Libraries in OutSystems")

Using JavaScript code in Script elements allows:

* A cleaner implementation of JavaScript libraries in your app.

* Having a single source for each JavaScript library, thus avoiding multiple parses of the same JavaScript code.

### Refactor JavaScript Code into Client Actions

Repeating the same JavaScript code in several JavaScript nodes increases maintainability efforts and makes your app more prone to errors.

Encapsulate the repeated JavaScript code in a JavaScript node inside a client action. Call this client action whenever you need to run that JavaScript. This way, the JavaScript code is in a single place which improves the maintainability of the app.

For example, encapsulate troubleshooting JavaScript functions such as console.log(), console.error() and alert() in client actions.

![Illustration of refactoring repeated JavaScript code into a client action in OutSystems.](images/OutSystems-Mobile-Best-Practices-10.png "Refactoring JavaScript Code into Client Actions")

### Avoid manipulating the DOM

OutSystems mobile apps use React and manipulating the DOM with JavaScript can lead to unpredictable or undesirable behaviors.

Do not use JavaScript that manipulates the DOM. This is only for advanced use cases.

If you are implementing a known mobile pattern, look for it in [OutSystems UI](https://www.outsystems.com/outsystems-ui/) or the [OutSystems Forge](https://www.outsystems.com/forge/).

![Warning sign indicating to avoid direct DOM manipulation in OutSystems applications.](images/OutSystems-Mobile-Best-Practices-11.png "Avoid DOM Manipulation Warning")

### Avoid using global objects

OutSystems uses [single-page applications](https://en.wikipedia.org/wiki/Single-page_application) to optimize the runtime execution of mobile apps. As such, the window object isn't cleared between navigations and global objects are not destroyed, increasing memory usage in the long run.

Avoid using objects that get attached to the window object, like global variables, cache objects, or listeners. Do the following instead:

* Use browser features like [localStorage and sessionStorage](https://www.w3schools.com/html/html5_webstorage.asp) objects.

* Use the 'var' keyword when declaring JavaScript variables to limit their scope.
![Code snippet demonstrating the use of 'var' to declare a variable in JavaScript.](images/OutSystems-Mobile-Best-Practices-12.png "JavaScript Global Object Usage")

### Change widgets style using OutSystems low-code

Using JavaScript to add or remove CSS classes can cause several problems. These include reduced code visibility and integrity, and flickering while rendering.

Use the Style Classes property of widgets to change the CSS classes applied to them. In this property you can use expressions that are evaluated at runtime to change the styles dynamically.

![Screenshot showing how to dynamically change widget style classes using OutSystems low-code.](images/OutSystems-Mobile-Best-Practices-13.png "Dynamic Style Classes in OutSystems")

### Use CSS for Animations instead of JavaScript

JavaScript animations typically run on the device's Central Processing Unit (CPU) with direct impact on the mobile app performance.

Use OutSystems low-code and style classes to run animations on the device's Graphics Processing Unit (GPU) and remove load from the CPU. For example, in [Making Magic with WebSockets and CSS3](https://www.outsystems.com/blog/posts/swipe-effect-with-websockets-and-css3/), cards are animated using CSS.

![Code example of using CSS for animations in an OutSystems application.](images/OutSystems-Mobile-Best-Practices-14.png "CSS Animations in OutSystems")

Learn more about how to properly animate elements in your mobile apps in [Smooth as Butter: Achieving 60 FPS Animations with CSS3](https://medium.com/outsystems-experts/how-to-achieve-60-fps-animations-with-css3-db7b98610108) and [FLIP Your 60 FPS Animations, FLIP 'Em Good](https://www.outsystems.com/blog/posts/flip-animation-60-fps/).

However, if you really must use JavaScript, use the window.requestAnimationFrame() method to run the animation using the GPU.

## Troubleshooting

Understanding bugs in your mobile apps can sometimes be a hard task, but there are [a few techniques](../../monitor-and-troubleshoot/solve-common-mobile-app-development-issues.md) that facilitate that troubleshooting process. Also following the development guidelines presented below allows you to more easily replicate and fix a problem in your mobile app.

### Define fallbacks for your native plugins

When you are troubleshooting your app in a desktop browser, the native plugins aren't available. This might prevent you from troubleshooting issues detected in real mobile devices.

Include sensible fallbacks in your apps to account for when the plugins are missing or do not work. This helps ensuring that apps can be tested using desktop browsers. You can do so by wrapping your plugin calls in client actions that return an error (or mock data for testing purposes instead) when a given plugin is not available.

In the following example, the AddToContacts action of the Contacts native plugin was wrapped in a client action called AddToContacts_Safe that first validates if the plugin is available:

![Flowchart showing how to define fallbacks for native plugins in OutSystems.](images/OutSystems-Mobile-Best-Practices-15.png "Fallbacks for Native Plugins in OutSystems")

Having these fallbacks in place also helps avoiding issues in the apps running in devices that do not support a given plugin.

### Create a simple client-side logging system

Client-side issues can be hard to troubleshoot, especially when they seem to occur in a single user's device in production. If you cannot replicate the issues, finding and fixing them is much more difficult.

OutSystems provides [a way for you to log information](../../monitor-and-troubleshoot/log-information-in-action-flows.md) in a mobile app. However, you can also create your client-side logging system that stores log entries in local storage. Then provide a way for the user to upload these logs in case of errors. This allows you to analyze what might have caused an issue in that specific user's device.
