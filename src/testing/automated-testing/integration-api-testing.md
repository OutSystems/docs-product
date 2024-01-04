---
en_title: Integration/API Testing
guid: c3feac47-4625-4632-a11f-6bbcba99482b
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Integration/API Testing

Integration/API testing is often a good target for automation. There's no user interface to perform manual tests, and testers often need to invest a lot of time setting up each individual test, which leaves small room for exploratory testing. Integration/API tests can include both integration with external systems and integration with loosely coupled services exposed by other OutSystems applications. Here are recommended practices on how to build integration tests with OutSystems.

Before we drill down into more detail, it's important to highlight a few points related to integration testing: 

1. **Don't test business logic with integration testing**. Unit and component tests aim to test and validate correctness on the business logic level. Integration tests are more aimed at correctness of request/responses, service availability. and performance.

1. **Keep in mind that when integration tests fail, it doesn't mean you have a bug in the business logic of your code**. You should analyze the component/unit tests for that integration, and if there are issues with the business logic, those tests should flush the issues out. When the issue is not flushed by component/unit tests for the integration, then probably the test failure has something to do with changes on the environment level that need readdressing.

1. **Integration tests aren't exclusive for API testing**. Software often depends on complex ecosystems that include virtualization tools, databases, mail servers, load balancers, DNS servers, and proxy servers, to name a few. Therefore, whenever possible, also aim to automate this kind of integration check.

## Integration Test Design Patterns

As mentioned above, integration tests don't focus only on API tests. Given this complex nature, we identify two main areas to address when implementing your integration tests:

1. API integration tests 
1. Other integration tests, i.e. virtualization tools, external databases, mail servers 

### API Integration Tests 

APIs can be exposed by either external systems such as SAP, Jira, Google Drive, or by other OutSystems applications. Many tools allow scanning [WSDL](https://www.w3.org/TR/2001/NOTE-wsdl-20010315) and/or [Swagger](https://swagger.io/docs/specification/about/) files (for SOAP and REST, respectively) to automatically generate all of the API endpoints as test objects or modules to later build your test cases or reusable test blocks.

This way, it's recommended that you generate WSDL or Swagger documentation for your APIs, whenever possible. When this documentation isn't available, most tools also provide API scanning tools that allow you to scan each API endpoint to generate the required test objects/modules that will help you build your tests. But keep in mind that this approach is costly because it requires scanning each individual endpoint manually.

After having your test objects or modules set up, it is time to start building your API integration test cases. Here, you can implement different types of tests on your APIs: 

* **Syntax testing** — Verifies how endpoints behave with valid and invalid input parameters and how the response is generated on incorrect or invalid inputs. It should also validate if the API behaves as expected regarding mandatory and optional inputs.

* **Test scenarios** or **integrated testing** — Combines two or more different requests to create a test scenario. This may include some E2E tests, as well. As an example, think of multiple operations over a single entity. First make a request to create a record, then use the search/find requests to ensure you can find the record where expected. Then make requests to update values on the entity, using search/find requests again to check that data was correctly updated. Finally make a delete request and ensure the record was deleted as expected.

When implementing your tests, it's a good practice to keep a few things in mind:

* **Design for Reuse** — Of all the principles in programming, **Don't Repeat Yourself** (DRY) is perhaps one of the most fundamental. Duplication always results in increased probability of bugs and adds undesired complexity, making the system tests harder to maintain. Whenever you have a number of common test steps between different test cases, create a reusable test block or test case that you can set up and reuse in multiple test cases. This helps  ensure maintainability and scalability for your test framework. Remember that if something changes in those common steps, having them wrapped in a reusable test block or test case allows you to update the changes once, and immediately ensures that all tests going through that flow are up-to-date. 

* **Implement Data Driven Tests** — You'll often have different scenarios to test each individual endpoint of your APIs. If your test cases are designed in a way they can be steered using data sets that set up endpoint inputs and expected outputs for all those scenarios, you will end up with a way more maintainable and scalable test framework. Following this approach can often simplify how to handle a new scenario with a simple new line in your data set. On the other hand, keep in mind that implementing data-driven tests is not always the best solution. If your test needs to perform a very simple and specific set of verifications, turning it into a data-driven test might result in overkill.

    Take into account the data quality for the data sets: Can they run with random seeded data? Should they use data that's close to production for better integrity checks?

## Other Integration Tests 

To automate your other integration tests, it's crucial to have a clear infrastructure design and identify your most critical failure points so you can target them for automation.

Automating integration tests to perform verifications on those points can be of great help for ops team members when an unexpected problem occurs. Mainly, it can reduce the time wasted finding where the issue comes from.

If you have a good set of integration tests to verify your typical and critical failure points, running these tests when problems occur can either pinpoint the source of the issue, or immediately discard these typical and critical failure points as suspect. It allows you to focus on other possible causes, provided none of these tests fail.

If your tests couldn't spot the problem and, after the issue is found, its verification can be automated, it's a good practice to add this verification to your automated integration tests. 
