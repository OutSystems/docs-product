---
summary: JavaScript in OutSystems 11 (O11) overview for Traditional Web, Reactive Web, and Mobile apps, covering when and how to add custom client-side code.
tags:
  - Front-End
  - JavaScript
  - Mobile app
  - Traditional Web
locale: en-us
guid: 863ded76-6477-4f45-9677-b6d0cad1972c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - understand
isautopublish: true
---

# JavaScript

You can use JavaScript in OutSystems to extend the behavior of your applications when the built-in visual logic and UI features aren't enough for a specific requirement.

The way you add and run JavaScript depends on the type of app you're building:

* **Traditional Web Apps** let you define JavaScript in modules, screens, and blocks, and run it in the browser through supported mechanisms such as extended properties, unescaped expressions, or platform APIs.
* **Reactive Web Apps** and **Mobile Apps** let you use the **JavaScript** element inside client actions to run custom client-side code.

Use JavaScript when you need to:

* Add custom client-side behavior to the UI.
* Call browser APIs or external JavaScript libraries.
* Reuse existing JavaScript code.
* Complement OutSystems logic with code that runs directly in the browser or device web view.

## Choose the right article

For detailed instructions, see the article that matches your app type:

* Traditional Web Apps: [Extend your Traditional Web App using JavaScript](./web/intro.md)
* Reactive Web Apps and Mobile Apps: [Extend Your Mobile and Reactive Apps Using JavaScript](./mobile/intro.md)

## Before you use JavaScript

Before adding custom JavaScript, keep these recommendations in mind:

* Prefer built-in OutSystems features whenever they already solve the problem.
* Keep JavaScript focused and easy to maintain.
* Avoid duplicating the same code in multiple screens or blocks.
* Test your code in the browsers and devices supported by your app.
* Be careful when manipulating the DOM directly, especially in Reactive Web Apps and Mobile Apps, because direct DOM changes can interfere with the framework rendering lifecycle.

## Related topics

You may also want to check these related articles:

* [Use JavaScript Code from an External Library](./mobile/use-external-lib.md)
* [OutSystems JavaScript API Reference](../../ref/apis/javascript/intro.md)

## Next steps

Start with the article for your app type, then review any related guidance for external libraries or JavaScript APIs if your scenario requires them.
