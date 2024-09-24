---
summary: Overview of options, resources, and tools to implement automated testing in your OutSystems environment .
tags: 
locale: en-us
guid: 319b0b59-b9cc-48d8-a776-ea8c0b564711
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---
# Testing apps

As your applications grow in scale and complexity, validating them can take longer, especially if validation is manual. If not addressed, more time for testing can slow the pace of delivery. Automated testing is one way software teams can shorten delivery timelines and ensure application code works as designed.

OutSystems provides tools, guidance, and best practices for implementing automated testing in your environment. Documentation on [testing guidelines](automated-testing/testing-guidelines.md) covers a number of topics related to strategy, tools, and test types. 

## Component testing with BDDFramework tools
Component testing is the process of testing Actions and exposed Services that make up an application's logic. Component testing in OutSystems spans multiple test types, including unit, integration, and API tests. BDDFramework is the recommended tool for planning and executing component testing. The following resources provide more information.

* [Component testing with BDDFramework tools](testing-bdd-framework.md) -- Introduction to BDDFramework tools that includes installation and getting started steps
* [Your Complete Guide to BDD Testing in OutSystems](https://www.outsystems.com/blog/posts/bdd-testing/) -- Comprehensive blog post describing how to use the BDDFramework for server-side testing 
* [Component testing](automated-testing/component-testing.md) -- Best practices for implementing component tests


## UI and load testing
OutSystems generates standard mobile and web apps with a .NET web stack on the server side. Therefore, you can use most standard testing tools for UI or load testing. Considerations to keep in mind when choosing a tool appear in this best practices article on [automated testing tools](automated-testing/automated-testing-tools.md).

## Integration and API testing
You can find guidelines for [integration and API testing](automated-testing/integration-api-testing.md). This best practices article covers considerations for planning and implementing API integration tests. It also briefly covers other types of integration testing. 

## Web UI testing
Considerations and best practices for [web UI testing](automated-testing/web-ui-testing.md) cover design patters and considerations for choosing a testing tool and designing tests. 

## More information and training 
The following resources provide general information about planning and executing tests with OutSystems.

* [Developing for testability](develop-test.md) -- Conceptual information to help you integrate testing with the development process
* [Becoming a Tester in OutSystems](https://www.outsystems.com/training/paths/10/becoming-a-tester-in-outsystems) -- Guided path training on implementing tests and testing strategy  
* [Test automation in the delivery life cycle](test-automation-in-delivery-lifecycle.md) -- 
Considerations when implementing test automation, including acceptance criteria and definition of ready and definition of done
