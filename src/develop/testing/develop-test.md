---
summary: Testing in OutSystems
tags:
locale: en-us
guid: a04eb23a-d3fe-4967-875b-02d15033b8cd
---

# Develop for Testability

Best practices in development and architecture apply to OutSystems as they would to any other programming language. Basically, you want to ensure that your developed code/module/application is reusable, maintainable, and scalable.

When introducing automated tests in OutSystems (UI, integration, or component tests) the concept of developing code that is testable reinforces some of those best practices. It also introduces some new ones.

You should develop every application to facilitate tests that validate its correctness. This overarching concept is completely independent of the technology involved.

In this article, we'll review some best practices to consider when implementing testable OutSystems applications. 

## Domain Isolation

OutSystems organizes business concepts and business logic into modules. Each module "owns" any concept or logic defined within it. As a result, modules can ensure that any use of their concepts or logic is correct according to their own internal business rules. [Domain-Driven Design (DDD)](https://dddcommunity.org/learning-ddd/what_is_ddd/) principles to promote code (and test) isolation are highly recommended. DDD drives the development of complex systems based on decoupled domains of technology artifacts. From a best practices perspective, OutSystems maps a domain to a LifeTime team. This team owns a set of applications for a business domain with an independent lifecycle from other teams (domains). Domains can be horizontal or vertical. Depending on the scenario, the level of decoupling between domains needs to be carefully evaluated.

If you want to learn more about DDD in OutSystems, see this great content describing its main concerns and principles:

* [Monoliths or Microservices: Make Both Your Domain](https://www.outsystems.com/blog/posts/monoliths-or-microservices-make-both-your-domain/) — Article

* [Domains and Services Architecture](https://www.outsystems.com/learn/lesson/1696/domains-and-services-architecture/) — OutSystems Developer Conference Talk 2018

With this introduction to the principles of DDD, you may notice some common pitfalls in implementing OutSystems applications. These will have an impact on application testability, so we’ll examine them further.

### Anti-Pattern #1: Validations at the UI Level Only

In the following image, the screen in the UI module displays a form to edit a concept owned by the Core module. When submitting the changes, all validations take place in the corresponding Screen Action, which then calls the action from the Core modimages/ule to save the record. The Core Action itself doesn't  perform any validation on the given input and serves mostly as a wrapper for the Create Action of the entity.

![Anti-Pattern #1 - Validations in the UI only](images/test-validation-only-ui-ss.png?width=800)

When testing the Core action, we can input any value into the action, and it will always succeed, barring any problems communicating with the database. Therefore, any test that uses this action in its execution loses its relevance.
To solve this problem, move all business validations to the Core action to ensure the provided inputs are valid according to the business rules for that module.

Keep in mind that the Core module action should be testable and take business validations/rules into account on its own. It should be possible to independently test it for validation/rule tests, without depending on a UI test. At the UI level, validations should focus more on user interaction than on business rules, and they should include simple input validation feedback.

In summary, UI testing should focus on validating user inputs. Consider these questions:

* Did the user input a value that exists in the autocomplete input options?

* Did the user fill in all mandatory input?

Core level testing should focus on validating business rules:

* Is the option selected from autocomplete a valid one in the current context?

* Is the value submitted for the mandatory input valid in the current context? 

### Anti-Pattern #2: Business Logic at the UI Level

The Screen Action to submit changes on a page has embedded business logic in its flow. In the example image, it creates a master record, then it creates or updates child records, and finally creates some notification. 

![Anti-Pattern #2 - Business logic in the UI](images/test-biz-logic-ui-ss.png?width=800)

If this logic needs to be tested as a whole, then one of two things will happen:

1. Either the test is forced into the UI level, which will make it potentially more expensive, especially because UI tests are generally harder to maintain and slower to run.

1. That logic would have to be replicated in the test logic, which is of course not desirable because the test would need an update every time the screen action changes.

The best way to handle this problem is to encapsulate the logic that needs to be tested in a public action at a Core module level, which will then be used in the screen action. This way, the business logic can be tested through component testing, without depending on the implementation of UI tests, which are much more expensive to produce and maintain.

### Anti-Pattern #3: Unsupported Cross-Domain Referencing

DDD recommends using Service Actions and Public Entities for dependencies between domains.

![Anti-Pattern #3 - Unsupported cross-domain dependencies](images/test-cross-domain-references-diag.png?width=600)

This decision about whether to directly reference Public entities between domains may impact the test data setup and therefore needs to be discussed here.

There are a couple of things you can do to sort it out. If cross-domain entities are referenced directly, that means there’s no possibility to mock data from the other domain. As a result, it is acceptable for test setup activities in the local domain to create any required data directly in the external domain.

However, if those entities are only referenced through APIs or Service Actions, that opens up the possibility to use mock services to simulate data from the external domain. This approach promotes test independence and reliability. In this scenario, it isn’t acceptable for test setup activities in the local domain to directly create any required data in the external domain. Instead, use mock services to get the data.
## Service API Isolation

Whenever an API service external to the current domain needs to be consumed, it should be done so in a wrapper module. This wrapper module should then expose a set of public actions to use that API, and all modules needing to access the API must go through the wrapper module.

Available since OutSystems 11, Service Actions are essentially remote calls available only to other OutSystems applications running in the same environment. They are used to create loosely coupled dependencies between applications, allowing them to break monoliths inside the OutSystems context. Because at runtime they are services, it also makes sense to apply this isolation for Service Actions that are referenced across different domains.

In this section, we will use the API to refer to or service actions.

### Anti-Pattern #4: Same API Consumed in Multiple Modules

In an OutSystems environment, there are multiple modules that consume the same API. When we’re in the scope of a test execution and need to use mock services to isolate the application under test from the remote system (where the API is exposed), we’ll have to change every single module that is consuming this specific API. Needless to say, this becomes a maintenance nightmare while also being error-prone, as the potential to forget to change one module increases.

![Anti-Pattern #4 - Same API consumed in multiple Modules](images/test-consume-api-several-modules-diag.png?width=500)

The best solution for you is to isolate the API consumption in a wrapper module that exposes the API methods through public actions. Core modules needing access to the API do it through the wrapper module. Later, in the scope of a test execution, when we need to point it to a mock service, that is done in one place only — the wrapper module.

In the case of APIs, the OnBeforeRequest event action available at the consumed definition can be used.

* For service actions, because they behave like public actions at development time, the wrapper should implement logic to return the output expected for the test instead of executing the service action call.

For more detail on mocking strategies, read [Mock Services for Integration Points](https://success.outsystems.com/Documentation/Best_Practices/Automated_Testing_Strategy#Mocking_Services_for_Integrations_Points).

## UI Simulation

### Widget Naming

The way automated UI testing works in applications is by simulating the user interaction through application screens in order to fulfill a specific user journey or functionality provided by the application. This simulation is done through scripting the various steps a user needs to perform on the screen elements. An example would be: Follow the home menu link; Click on the submit button; Enter the `email@example.com` into the email input.

This means that the UI script needs to uniquely identify the elements that the user is interacting with. The easiest way to uniquely identify an element in a screen is through its ID property. As such, and in the scope of OutSystems application screens, it implies that those widgets need to be properly identified in Service Studio.

When developing a screen, the developer should ensure that all elements that have some degree of user interaction, such as inputs, buttons, and links, have the name property assigned with a meaningful value. This facilitates the element identification in the generated screen code, since the element’s ID attribute will always terminate with the widget’s name property value. This will also avoid additional effort later on if a UI test finds that a specific element on the screen is not properly identified.

Eventually, it may be the case that a specific UI test will require additional elements on the screen, which will also need identifiers. However, by naming at least the widgets mentioned above, the developer minimizes the number of times that rework needs to be done. Saving some of this effort fosters a faster workflow when implementing UI testing.

Using the name as the basis of the selector also allows the platform to detect name collision inside the same screen. This is an added benefit. It does not allow two different widgets to have the same Name property, and so the second will add the suffix of "2", and so on.

Still, because OutSystems allows composing a screen with multiple Blocks, if we use the same name in two different Blocks for the same screen, this name collision will not be automatically addressed by Service Studio. Taking that into account, we recommend that when naming a widget in a block, developers should include the block name as a prefix to the name of the UI widget. This ensures that names will still be unique when a screen is composed by multiple, different Blocks.

And what if there is a need to have multiple instances of the same block on the same screen? In these scenarios, developers should wrap each block in a container with a specific ID for the screen, and then use that container ID to anchor each specific block instance in a unique way for that screen.

Testing tools usually use XPath or CSS selectors to identify each UI element. When following the approach mentioned above for UI element identification, these UI widgets will all have IDs, but the OutSystems platform will generate a "composed" ID that will only end with the actual name given to the widget inside Service Studio.

The following is a simple example of how you can identify these IDs that end with a given unique name. Remember, the name represents both CSS selectors and XPath selectors for an input with the name "UserNameInput" in Service Studio:


CSS Selector
:   `input[id$=UserNameInput]`

XPath Selector (1.0)
:   `//input[substring(@id, string-length(@id) - string-length('UserNameInput') + 1) = 'UserNameInput']`

XPath Selector (2.0) not commonly supported by testing tools
:   `//input[ends-with(@id,’UserNameInput’)]`

### Extended Property Alternative

As an alternative to using the name property to identify the elements, an extended property named "os-test-id" can be used as the identifier. For the same input in the previous example, add the "os-test-id" extended property with the value "UserNameInput" in Service Studio. In the generated HTML code, the platform will add an attribute with the mentioned name/value pair.

Then, the following selectors can be used to identify the element on the screen:

CSS Selector
:   `input[os-test-id=UserNameInput]`

XPath Selector
:   `//input[@os-test-id='UserNameInput']`

This approach allows for complete control identifying the elements in the screen, but it does come with some drawbacks.

First of all, developers need to start adding these extended properties to their widgets in Service Studio, which introduces more development effort. Naming widgets may feel much more natural.

In addition to that, the OutSystems platform doesn't provide any collision detection for extended properties, so it’s up to the developer to ensure it. This can be especially tricky to manage in complex screens.

### Mapping tests to the Architecture Canvas

![Architecture Canvas](images/test-4-layer-diag.png?width=800)

The [Architecture Canvas](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_the_architecture_of_your_OutSystems_applications/01_The_4_Layer_Canvas) is an OutSystems architecture tool to make the design of Service-Oriented Architectures simple.

Architecture Canvas promotes the correct abstraction of reusable (micro)services and the correct isolation of distinct functional modules. It's useful in cases where you are developing and maintaining multiple applications that reuse common modules.

Due to the nature of the functionalities implemented in modules at each layer, it is possible to map these layers to the types of functional tests that would make sense to implement at each level.

### Orchestration layer

<div class="warning" markdown="1">
The Orchestration layer is applicable only to versions prior to OutSystems 11.
</div>

#### Functionalities

Processes, dashboards, and portal home pages, mashing up information from different applications to provide a unified user experience.

#### Tests

##### Automated UI (end-to-end) Testing (user journeys)

Orchestrations modules often implement screens that are cross-application, which are more information-oriented and not so much form oriented. These provide links to access application screens built on the End-User Layer. This way, tests implemented on functionalities at this layer are full user journey UI tests that require moving between multiple applications. They validate both the navigation and how applications impact each other.

Example:

1. Access the Intranet portal.
1. Go to the Vacations app.
1. Submit a week’s vacation.
1. Go to the Allocation app.
1. Verify that the submitted week is blocked for vacations.

### End User Layer

#### Functionalities

User interfaces and processes, reusing Core and Library services to implement the user stories. 

#### Tests

##### Automated E2E UI Testing

End-user modules implement screens specific for a single application with a very well defined business domain. They tend to be more form oriented, or at least a mix of information/form. They also focus on the business functionality for that application. As such, tests implemented on functionalities at this layer are UI tests that will validate the implemented business logic of that application.

Example:

1. Login in the Vacations app.
1. Go to the Calendar screen.
1. Select a week in September and submit for approval.
1. Logout/Login in the Vacations app with the manager’s account.
1. Verify that the submitted request for vacations is in the “To Approve” list.

### Core Layer

#### Functionalities

Services around business concepts, exporting reusable entities, business rules, and business widgets.

Core modules implement business concepts and logic. Because horizontal references are allowed at the core layer, it actually establishes a hierarchy between core modules. Consequently, depending on how high or low a core module sits in that hierarchy, it is possible to implement different types of tests for it. The lower the level, the closer the test will be to a unit test, while higher levels promote end-to-end tests that may have dependencies on concepts from multiple modules and even integrate with external systems.

#### Tests

##### Automated End-to-End Testing (non-UI)

Non-UI end-to-end tests validate business logic by calling the OutSystems code directly without going through the application screens and asserting expected outputs. They actually test multiple components in the application. There are two dimensions that can be explored here:

1. Explicitly calling multiple business actions in a logical sequence — simulating the sequence of actions that a user would follow through the UI — to assert a final outcome.

1. Calling a single business action that encapsulates the orchestration of multiple concepts from different modules to achieve a full user interaction validation.

##### Automated API Testing

API tests are used to validate the correctness of exposed APIs, according to specification. These can either be APIs that are exposed from external systems and consumed inside the OutSystems platform, or APIs that are exposed by the OutSystems module to be consumed externally by other applications or systems. These tests are usually defined by a set of inputs for the API and the corresponding expected outputs.

##### Automated Unit/Component Testing

Unit/component tests validate business logic on the lower-level code modules. They are self-contained and have almost no dependencies (or none at all) to other core modules. For this reason, these modules typically contain the business logic specific for the set of concepts defined, with no context of any other concepts or higher level logic. This makes them the smallest testable business part of an OutSystems application.

### Library Layer

#### Functionalities

Business-agnostic services to extend the framework with highly reusable assets, UI patterns, connectors to external systems, and integration of native code.

#### Tests

##### Automated API Testing

API tests validate the correctness of exposed APIs. These can be either APIs that are exposed from external systems and consumed inside the OutSystems platform, or APIs that are exposed by the OutSystems module to be consumed externally by other applications or systems. These tests are usually defined by a set of inputs for the API and the corresponding expected outputs.

##### Automated Unit/Component Testing (non-business)

Library modules are by definition business-agnostic. This way, they contain no business logic. But because they provide highly reusable assets that may be used throughout all OutSystems applications, it may be useful to test the functionalities provided by these modules. Examples of such libraries include auditing subsystems, where every action performed by a user on any application is logged in an Audit entity.
