---
en_title: Web UI Testing
guid: 7b8f66bb-5f78-4ff7-8248-85d4a25b6589
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Web UI Testing

There are three major techniques for UI testing: **scripted testing**, **exploratory testing**, and **user experience testing**.

In **scripted testing**, software testers focus on designing and executing preplanned scripts to uncover defects and verify the **System Under Test** (SUT) does what it's supposed to do.

In **exploratory testing**, rather than follow pre-written test scripts, testers rely on their knowledge and experience about the SUT, designing tests and immediately executing them. Exploratory tests are a very effective way of discovering lack of test coverage.

This kind of testing should always be performed manually, though some exploratory tests will eventually be automated. As an example, if issues are found during exploratory testing, it's best practice to create automated tests that detect the issues found. Then after the issues found are solved, their validation will completed through automation, preventing the need for manual regressions. Using exploratory testing in combination with automation for the issues found can be a very effective technique to incrementally improve test automation coverage. 

**User experience testing** is all about gathering information from actual end users, or a select group of end users. Subjects can include its ease of use, how it fits their needs, what they use the most, how visually appealing it is, and so on.

By definition, user experience testing determines the best way for a website and its elements to interact with its audience. This kind of testing can provide important feedback to the business to help continuously improve the SUT, based on user inquiries, user monitoring, or other possible methods.

## Automation 

If you've ever dealt with UI test automation, you probably know it can be very hard to build, scale, and maintain. There's actually a rule of thumb that states you should minimize the number of automated UI Tests, giving higher priority to unit and integration tests. Learn more about the testing pyramid in [OutSystems Testing Guidelines](testing-guidelines.md#segregating-automated-tests).

Some common pitfalls when building UI tests are:

* **UI Automation tests are difficult to maintain** — The reason teams prioritize unit/component tests over UI is because these run faster, are more stable, and are closer to the code. Still, these simple low-level tests can't simulate the way users actually use their applications. To model these scenarios, you need to implement tests that fully exercise your UI and backend logic (E2E testing.) Given the complexity of these scenarios and the fact that they depend on UI, which can change frequently, these tests are bound to be slower and break easily.

* **Poorly written locators can break UI testing** — Well-written CSS and XPath locators (or proper module element identification) are crucial for UI testing. Still, these alone are not enough, since often the required elements lack an ID. It's always recommended that developers set proper IDs on all actionable elements. Learn more about Widget Naming in [Developing for Testability —  Web UI Simulation](https://success.outsystems.com/Documentation/11/Developing_an_Application/Developing_for_Testability#web-ui-simulation).

Because of the complexity and challenges of building UI tests, there are a number of test design patterns that aim to avoid common pitfalls. These can help build a scalable and maintainable UI test framework. 

## Web UI Testing Design Patterns

Doing test automation generally consists of two concepts: **building your testing framework** and **automating the tests you need**.

Building a proper UI test framework is essential for both maintainability and scalability.You want to keep your tests clean, maintainable, and easy to write. There are some identified techniques and patterns that can help achieve this goal.

From the many automation design patterns for UI testing, we will focus on the Page Object Model pattern for UI test design. It's important to take into account that depending on the testing tool you choose, you may not be able to apply this pattern. For instance, Ghost Inspector® doesn't allow it. If you're going to have a lot of UI tests to manage, choose a tool that enables this pattern, i.e. Tricentis Tosca® or Katalon Studio®, but there are many others.

### Page Object Model (POM)

For the test framework, begin by defining proper page objects. As we are talking about UI, these pages are basically your test objects. There is no recipe for this; it all depends on the application you need to test.

Just as you have web blocks to build your pages in OutSystems, you'll need your page blocks to build tests. Choosing these blocks is not hard if you follow the **Don't Repeat Yourself** (DRY) principle. Identify elements or groups of elements that you will need to use repeatedly, or that repeat themselves across multiple pages. Example elements include header, footer, menu, widgets. Design these for reuse in the first place.

The page object model pattern also focuses on page flows and verifications. Once you have your page objects, you need to think about what each page's interactions: Do you have usage patterns, such as a search pattern or an auto-complete pattern? Do they repeat? Based on the answers to those questions, build reusable test blocks according to your needs.

Following this approach helps you build a framework that will enable you to write your tests in a much easier and readable way. Also, if you have multiple tests that use the same widget, and that widget has changes in the UI, all you need to do is update your page object. Additionally, if there's some behavior pattern change, just update the pattern — all your tests will be updated.

The Page Object pattern also states operations and flows in the UI should be separated from verification because this separation keeps your test code cleaner and easier to maintain and scale.

Given this principle, the baseline to build our test framework is based on the different groups of reusable test objects listed below.

### Page Widgets

Page widgets can represent simple or complex page elements. As an example, you can have simple page widgets to represent inputs, buttons, or links.But you can also have complex page widgets that represent a specific form with multiple inputs, dropdowns, save, and cancel buttons.

You can create page widgets composed by a mix of other page widgets. As an example, you can have a page widget to represent any input by ID and another to represent a button by ID. Later, you identify you have a common pattern across multiple application pages where you have a search input and a search button to perform on each of these pages.

In this context, it might make sense to create another page widget to represent a generic search pattern that would be composed of the previous two-page widgets (input and search button). This way, whenever you wish to instantiate a specific search pattern to perform a search on a page, you just need to provide the IDs of the input and button for that page into this composed object. This will steer it to perform searches in that page.

### Interactions 

Many tools already have multiple actions built in for simple page elements such as click, set text, and double click. Still, when you build your own complex page widgets, it might make sense to also build your custom interactions for those page widgets.

Imagine a scenario where you want to select an element from an autocomplete widget. You would have to click the widget, wait for the dropdown, do your search, and then send “Enter.” Instead of building your test with all these individual interactions, you can build a reusable interaction test object that does all these steps for the value given in just one test step.

Those encapsulated complex interactions allow you to modify them once after a change in behavior, instead of forcing you to review all test cases where you were using it.

### Assertions

Just as with interactions, many tools already have multiple assertions built in to perform UI checks, such as verify text and verify visible. Still, when you have your own custom and complex page widgets, it makes sense to also encapsulate assertions into reusable test objects, where you can set up your assertions for those widgets. As an example, imagine a typical scenario of search and verify in a list. If you need to perform this kind of check in multiple different test cases, you should design a reusable test object that implements this assertion pattern and reuse it on each of those test cases.

### Templates

Many tools also support conditional logic inside your test cases, but they should be avoided when possible because tests will run slower. To overcome this, a few testing tools also allow for the creation of test templates. You can use templates for the instantiation of multiple slightly different test cases without conditional logic, based on inputs and on the conditional logic implemented and configured with parameters.

An example would be an E2E test where, depending on the profile of your user, some steps might not exist or some assertions might be slightly different. In such cases, it would be possible to create a template that describes the whole test. This would include all the required actions and assertions for all user types, with some conditions to perform (or not) specific test steps, depending on the user type.

Then, you would set up data files with the possible user types. By applying the file to the template, you can instantiate each test case, i.e. for each user type based on one unique template.

When it's possible to use templates, you can really improve your test framework maintainability because you can easily update your template with whatever changes are required and just re-instantiate your multiple test cases. All test scenarios are updated with the required changes. 

### Test Data Quality

We include this topic because it is also an important subject regarding UI testing that shouldn't be underestimated. Always take into account the data quality for your tests. For instance, can tests be run with random seeded data? Or should they use data that is close to production for your integrity checks? 
