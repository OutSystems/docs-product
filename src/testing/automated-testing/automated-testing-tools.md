---
en_title: Automated Testing Tools
guid: 33518ed5-11df-42fe-8cba-daa3622ea514
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Automated Testing Tools

## Choosing Your Testing Tool

OutSystems generates 100% standard mobile and web apps, with a standard .NET web stack on the server side. As such, most testing tools on the market can be used for UI testing and load testing. For this reason, we won't recommend any specific tool here, but we'll focus on the aspects you should keep in mind to pick the best tool for your context.

### Your Team Coding Skills

You should look for a tool that responds to your team's capabilities. If your team has low or no coding skills, then choose a no-code/low-code tool.

Regardless of the tool type you choose, never underestimate the need for a tool expert in your team. That person should know how to leverage the tool capabilities for your needs.

Keep all of your questions in mind when choosing your testing tool. Do you need API tests? Do you need UI testing? Is it a web application? A mobile application? Does it have lots of performance/availability requirements? Some tools only allow a specific kind of test, while others are much more comprehensive, covering multiple test types. Choose wisely to ensure you have the right tools for all your test types.

Keep in mind that the more tools you use, the wider the skill set your team needs to have, which can result in bigger costs and lower productivity.

### Complex Applications

If you have a large number of UI tests, an application with a complex UI, or one that changes often, it is important to choose a tool for UI testing that allows you to implement the Page Object Model pattern. This will enable you to build maintainable and scalable test framework to implement your UI tests in an efficient way.

### Budgeting and Versioning

Licensing costs for testing tools can range from free to expensive. Obviously, costs will rise with the number of "out of the box" features that each tool provides. Try to find the most adequate balance for your needs.

Don't go for overkill.You may end up investing a lot for features you don't use or even need. Also avoid making "0" investment in testing tools if that may result in hidden development costs for setting up your test framework.

Besides that, usually for each specific application version, you'll have a bundle of automated tests that perform the required checks to validate the quality of your application. Remember to match the application version and the test application version. Having said that, it's important to take into account that not all testing tools in the market will allow you to do versioning for your tests.

### Data-Driven Tests

Not all tools in the market allow you to perform data-driven testing.  And even then, not all of them are equal, so be sure to choose one that meets your specific needs. Following are some guidelines to keep in mind.

### Testing Across Different Technologies

For instance, you may need your testing tools to work across your whole software stack. Not all tools allow for API testing, or desktop application testing, so keep this in mind. Analyze your technology needs thoroughly.

### Recording Tests

Recording features will allow you to start automating your UI tests quickly. However, you'll soon understand that they do not promote reusability, and you'll have a hard time maintaining your tests as your test base grows bigger.

## Testing Tools 

There are many  tools available for test automation. But we recommend [BDDFramework](https://www.outsystems.com/forge/component-overview/1201/bddframework) for component or integration testing.

For test management, most UI testing tools have their own management capabilities. For component testing, assuming a CI/CD practice is in place for OutSystems, the CI engine will be able to manage those types of tests.

However, if you believe you'd better manage these tests in a dedicated tool, go for another Forge tool called [Test Framework](https://www.outsystems.com/forge/component-overview/2464/test-framework). Another alternative, since BDD Framework exposes an API to execute Test Suites, would be an external tool with API testing capabilities.

We want to share with you the results from rehearsing a few tools with different characteristics, analyzing how their capabilities fit test automation with OutSystems. We hope to help you identify common practices and patterns that will optimize their usage to build a scalable and maintainable test framework.

### Ghost Inspector®

Ghost Inspector is a SaaS Web UI-only test automation tool. It offers an easy-to-use interface, with the possibility to create test cases manually or with a recorder utility that scans the user interaction with the application screens and saves that interaction as a test case. Although behind the scenes it uses Selenium® to steer the test cases, one of its best features is that it abstracts the user from the actual script. Instead, the tester can select the interactions from dropdown lists (i.e. click, type, drag) and type some CSS selectors to build tests. 

It does allow for test reusability, but it doesn't follow a page object model-based approach, and hence may not be an advisable option if you need a lot of UI test scenarios. Because it is a SaaS, it's probably also not a good choice if there are strict security restrictions in allowing access to OutSystems applications from outside the organization. It is for UI tests only, so BDDFramework tests would need to be integrated into another tool. 

### Katalon® 

Katalon is a free tool that provides a complete web testing solution. The tool allows setting up test projects and creates test suites and test suite collections, test cases, test objects for UI or API testing, custom keywords, test data files, and reporting. It easily integrates with Git for versioning and has plugins for integration with other tools like Jira®, Jenkins®, and Slack®.

Test implementation using katalon is keyword-driven and requires some coding/scripting skills. You can build custom keywords and reusable test cases to accelerate test design and ease test framework scalability. The tool also allows you to set up your test project data files to enable data-driven testing for both UI and API tests. 

This tool fits very well with OutSystems applications, for UI and API test implementation. As it makes it possible to easily use/build API test objects, it can also be used, together with BDD Framework API, to steer your BDD Framework component tests.

### Tricentis Tosca® 

Tricentis Tosca is a full-fledged automated testing platform that offers a comprehensive technology support portfolio for technologies such as Web, SAP, API, ServiceNow®, and Oracle®. It can map the entire testing process, which means test planning, requirements mapping, test coverage, test case definition, test data management, and test execution.

Tosca is a no-code solution that follows a model-based approach to all types of testing. It has the capability to manage the entire testing process from one single platform. Licensing is at the high-end of the budget scale.

Tosca would be a viable option when there are no technical skills among the testers, with a big set of test cases to manage that span multiple technologies.It would still be a good idea to have a Tosca expert in the team to guide the testers in how to leverage the tool's capabilities. Otherwise, there's a risk of misuse, which can affect speed, usefulness, and adoption.

### BDDFramework (Forge Component)

This tool enables test scenarios for OutSystems applications that conform to the principles of Behavior-Driven Development. Test scenarios are built by dragging and dropping web blocks (Scenario + Given / When / Then clauses) on a regular web screen. Each test step is then implemented using its own action, making sure that steps are sequential and occur in the same request.

BDDFramework is particularly suitable for exercising, on the business logic layer, the acceptance criteria of the application's main features. This way it promotes a TDD/BDD approach during the delivery cycle.

BDDFramework is recommended when automating the delivery pipeline. It provides a REST API for running tests and obtaining results that can be easily integrated with an external CI/CD orchestrator, such as Jenkins®. Read [Component Testing](component-testing.md)​ for usage guidelines.

Major benefits of using this tool for component testing include: 

* **Test suite capability** — a way of logically grouping tests, on a single test screen 
* **Faster execution** — this can be achieved leveraging test suite capabilities. 
* **Reduced consumption of AOs** — especially compared to other ways of component testing implementation in OutSystems, like using UTF or exposing dedicated services
* **Visual test representation** — easy-to-read test definition and execution, based on Gherkin syntax (Given, When, Then) 
* **Faster error analysis** — errors in BDDFramework assertion can be easily identified either in the screen execution or via API. 
* **CI/CD integration** — easy integration with CI/CD best practice for OutSystems 
* **Community support** — the component testing tool used as part of OutSystems platform development process, which is widely used by OutSystems customers 

### Test Framework® (Forge component)

Provides simple management and automated execution of OutSystems component and integration tests. For component tests, Test Framework can automatically import and run tests built using BDD Framework, validating test results on every run.

Using Test Framework, delivery teams can specify their own test suites and execute them manually or periodically, on a given schedule. It grants them an automated regression-testing capability to incorporate in their delivery cycles.

Additionally, Test Framework acts as a factory quality monitor by providing a dashboard where IT teams can monitor the execution of test suites. It can give them a clear understanding of whether their tests are designed for maintainability, or if applications increasingly have more quality and fewer regressions. 

### JMeter

JMeter may be used for load testing. Since OutSystems applications are standard web applications, any strategy or tool currently used to test traditional web apps can apply. OutSystems recommends the following webinars explaining how to implement simple load testing scenarios using the open-source tool JMeter, for both web and mobile applications (server-side only):

* [How to set up a load test in 5 minutes](https://learn.outsystems.com/training/journeys/tester-654/how-to-set-up-a-load-test-in-5-minutes/o11/2467)
* [Load testing applications expert talk](https://www.outsystems.com/training/courses/161/load-testing-applications-expert-talk/)

### AppFeedback 

To improve the quality of the information when doing functional tests, developers and/or business users can use the [OutSystems AppFeeback​](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Gather_user_feedback) feature.

This feature allows end-users of OutSystems applications to share feedback with contextual information from within the app itself, therefore shortening the feedback cycle.

One of this feature's advantages is its ability to report defects or suggest improvements during test cycles in QA.

The AppFeedback feature can be enabled per OutSystems environment, per application, and even per user group (for a given application). Just use the AppFeedback back-office located at `https://<environment_url>/ECT_Provider`.

Collected feedback can be managed directly in the AppFeedback back-office. It can also be synchronized with an external tool, such as a defect management tool, leveraging in-house feedback management workflows.

The [AppFeedback Connector](https://www.outsystems.com/forge/Component_Details.aspx?ProjectId=1966) Forge component provides the engine to synchronize AppFeedack data. On top of this, there are several connectors to other ticketing tools:

* [App Feedback to JIRA](https://www.outsystems.com/forge/component-overview/2153/app-feedback-to-jira) 
* [App Feedback to VSTS](https://www.outsystems.com/forge/component-overview/3081/app-feedback-to-vsts) 
* [App Feedback to Asana](https://www.outsystems.com/forge/component-overview/2107/app-feedback-to-asana) 
* [ECT Trello Connector](https://www.outsystems.com/forge/component-overview/1514/ect-trello-connector) 
