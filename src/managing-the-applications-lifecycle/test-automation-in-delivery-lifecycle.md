# Test Automation in the Delivery Lifecycle

Introducing automated testing as part of the development-and-release lifecycles can mean changes in the way the application are developed and delivered. Some of these changes come from DevOps culture, which incorporates vertical teams. Vertical teams participate from the point of the business idea through to application deployment and monitoring in production. Tasks in the release cycle are automated to accelerate lead times. 

## Putting a Team Together

Because teams are responsible for the entire application lifecycle, there are no longer individualized roles such as  Product Owner (PO), Business Analyst (BA), Development (DEV), Quality Assurance (QA),or Operations. Instead, there will be a single Product team responsible for every aspect related to all applications under its domain. This team has at least one member for each role just described, but all members work together in each aspect to build the application with quality, deliver it to production as soon as possible, and maintain it.

In the context of automated testing, QA has a big impact. QAs define test strategies, identify risks and test scenarios, and say where test efforts should be directed. They can even have a say in how to design the application architecture so that it can be more easily tested.

We're not saying that the QA role is the only role responsible for everything related to Automated Testing, or even that the DEV role only cares about implementing, or that the POs and BAs look only at the requirements. Just as in any Agile methodology, the team is responsible for all aspects of the application as a whole. Think of it as each role having its own mindset. Each mindset brings its own point of view and strengths to the table,  improving the application under development.

What we're saying is that you must bring Testing and QA processes to the table from the very beginning, as soon as the user story definition/drill down starts. The effective communication between every team member ensures that your business objectives keep aligned.

## The Three Roles Involved in the Process

If you don't team up the way we just proposed, the following workflow is what usually happens.The PO or BA adds the acceptance criteria when he first writes the user story and hands it over to developers.

When developers pick it up, they have a lot of questions about eventual behaviors that are not strictly described. So they hand the user story back to clarify their questions and possibly translate them into new acceptance criteria scenarios.

Then there are testers who probably have additional insights into potential scenarios that nobody had considered, and the user story goes back and forth between everyone until finally they are all happy with the acceptance criteria, and the user story can finally enter the sprint and start.

Other than that, we commonly observe an anti-pattern where this process doesn't even take place before the sprint — it happens during and after the sprint, when specific scenarios are only identified during development or testing, which is likely to require more rework.

With the proposed team organization, acceptance criteria is defined  in the earliest collaborative sessions between all three roles (PO, DEV, and QA — commonly called "the three amigos.") This streamlines the process and avoids stumbling during the development and test stages, or misinterpreting expected outcomes. The discussions between the three roles are at the core of [Behavior-Driven Development (BDD.)](https://www.agilealliance.org/glossary/bdd/) The aim is to build software that not only works correctly, but serves business needs.

Those discussions should happen during the [backlog refinement sessions](https://www.agilealliance.org/glossary/backlog-grooming/), where the teams already discuss the development details of their user stories to ensure that they are ready for sprint. This way, a test definition, which includes acceptance criteria, design for testability, and test strategies, will be just another subject added to the details of a user story.

It is important to define testing as a detail of the user story rather than leaving it till the end of the meeting. Not foregrounding testing makes it a second-tier concern that doesn't get the attention it deserves.

## Top-Notch Acceptance Criteria

Writing top-notch acceptance criteria is one of the keys for effective software delivery. Acceptance criteria specifies rules for a given user story and requires them in t evaluating the code produced by your DEV team.

There are multiple ways to write acceptance criteria, but we recommend using the **Given-When-Then** format introduced as part of the BDD methodology, it follows the **Specification By Example** approach.

This approach comes very naturally to people. Our human brains really know how to derive concepts from examples. And the more examples we find, the better we understand the problem at hand and its scope.

The Given-When-Then format obviously has three main sections, explained further here:

* **Given** — Inputs/Preconditions. Describes the state of the world before you begin the behavior you're specifying in this scenario. You can think of it as the preconditions to the test. 
* **When** — Functionality. Runs the behavior that you're specifying. 
* **Then** — Assertions. Describes the changes you expect due to the specified behavior.

You can string together multiple preconditions, actions, and assertion by using Chaining, or **And**.

Here's a scenario in this particular format:

**Scenario:** User requests a sell before close of trading  
**Given** I have 100 shares of MSFT stock  
**And** I have 150 shares of APPL stock  
**And** the time is before close of trading  
**When** I ask to sell 20 shares of MSFT stock  
**Then** I should have 80 shares of MSFT stock  
**And** I should have 150 shares of APPL stock  
**And** a sell order for 20 shares of MSFT stock should have been executed  

This example does not contain any technical information related to technologies, systems, screen interactions, or APIs. That's because that information describes the behavior expected by the business user for the functionality delivered, but not how it will actually get there.

Remember that. Really. It facilitates discussions with the business user by making it independent of the technical solution. The scenario is still valid even if refactoring is done in the future, and focuses on what really matters — the behavior.

Notice as well that there are no IFs or ORs in the example. A test scenario must be clear and explicit and have no conditional logic written in its definition. If you feel the need to add an IF or OR anywhere, then what you actually have is a new scenario, and as such you should write a separate test scenario to validate it.

### A Few Too Many

After writing the acceptance criteria, maybe the user story will end up having too many scenarios. Well, odds are that you can break it up into multiple user stories. So, split it up and make sure that each user story stands for the smallest deliverable unit of business value.

### Definition of Ready/Definition of Done

As automated tests are introduced into the team workload, review the [Definition of Ready (DoR)](https://www.agilealliance.org/glossary/definition-of-ready/) and the [Definition of Done (DoD)](https://www.agilealliance.org/glossary/definition-of-done/) to ensure compliance with them. You should only accept a user story as ready if it has the right acceptance criteria defined and if everyone agrees on the corresponding tests identified.

Now that it's a team-wide task, implementing tests should be reflected in the DoD. So create separate technical stories to implement tests for E2E scenarios that depend on multiple user stories. Do not use any additional business logic other than what was already implemented in the user stories. With this approach, the DoD of your user stories will never be compromised because of dependency issues.

In the DoR, consider adding a clear definition of quality test data required for the new test scenarios. You may also want to identify the existing tests that may require review. Here's a list of items you should consider for the DoR/DoD.

#### Definition of Ready

* It's written down in the form: "As a &lt;user role&gt; I want to &lt;activity&gt; so that &lt;benefit&gt;".
* [INVEST](https://www.agilealliance.org/glossary/invest/) principles are achieved: Independent, Negotiable, Valuable, Estimable, Small, and Testable. 
* It's mapped as a step in a business process diagram. 
* Business context and value are clear. 
* It's prioritized, based on MoSCoW for example.
* Conversations have happened to clarify the User Story so Business, IT, DEV, and QA teams (including everyone) are aligned on what exactly to build. 
* Details are captured in acceptance criteria, both functional and nonfunctional.
* Everyone's involved in the Acceptance Criteria definition. 
* Wireframes/mockups are drawn or reviewed for major US. 
* It's validated by business. 
* Test cases/scenarios are captured. 
* Meaningful and comprehensive test data is available. 
* New manual or automated tests are clearly identified and categorized (UI, API, Component, and so on.)
* Existing tests potentially impacted by the User Story are identified for review. 
* It's estimated at a high level and fits in a Sprint. 

#### Definition of Done

* Code is complete and adheres to IT guidelines, so it's published. 
* Unit tests are completed successfully by developers and confirmed by DM. 
* Test cases for acceptance criteria are executed with success. 
* Reviewed and approved by EM.
* Usability and performance tests are performed. 
* Intermediate demo (preview) is done, and a plan is in place to address its feedback during stabilization, before demo to business. 
* All existing tests that required revision were updated and eventually passed. 
* The new code does not break any regression tests. 
