---
summary: Introduces component testing using the BDDFramework tools.
tags: 
---

# Component testing with BDDFramework tools
 
This article describes how to install and start using the BDDFramework tools to implement automated and structured component testing. Component testing in OutSystems covers testing **Actions** and exposed **Services** that make up an application's logic. 

Component testing in OutSystems includes the following standard test types:

* Unit Tests, which developers maintain, focus on individual units of code or components that a single team owns 
* Integration Tests, which test whether two or more components work together; these touch a broader application scope than unit testing and the tested code usually belongs to two or more teams
* API Tests, which verify the contract between consumer and provider and the behavior of your application's existing API endpoints

The [BDDFramework for Client-Side tool](https://www.outsystems.com/forge/component-overview/10917/bddframework-client-side) allows you to test public Client Actions, and it provides the following features:

* Tests use Gherkin-like syntax and offer a visual representation of test execution
* You create the test structure using UI Blocks that the tool provides
* Test code is implemented through actions that are bound to each Block
* Test Blocks are organized into screens called Test Suites

## Installing the BDDFramework

You can install the BDDFramework client-side tool in your OutSystems infrastructure, just as you would other Forge components. Install it directly through Service Studio (the OutSystems IDE) or from the online [Forge portal](https://www.outsystems.com/forge/).

To install from Service Studio: 

1. Open **Service Studio**.
2. In the main menu bar at the top of Service Studio, click the **Forge** tab.
3. In the search box on Forge, type **BDDFramework Client Side**.  
4. Select **BDDFramework Client Side** from the results.
5. Click **Install**. If you see a confirmation message, confirm the installation.

Once you complete the installation, it's time to start implementing tests.

## Getting started 

The following steps walk through creating a test application.

### Create a test application and module

1. In Service Studio on the Development tab, click **New Application**.
1. Select **Start from scratch**, and click **Next**.
1. Select **BDD Framework Client Side** as the application type, and click **Next**.
1. Type the app name, for example, **App-Name-1** and click **Create App**.
1. On the **App-Name-1** page, under **Modules**, change the module name to **AppName1-TESTS**, and leave the module type as **BDD Framework Client Side**.

    ![](images/create-bdd-module-xplat.png)

1. Click **Create module**. The module imports all the building blocks you need, and the test module is connected to the app you created.

## Add a test to your test module

1. On the **Interface** tab menu on the right, go to **AppName1TESTS** > **UI Flows** > **TestFlow**.  

1. Right-click **TestFlow** and select **Add Screen**.

    ![](images/testflow-1-xplat.png) 

    You may see a message that new templates are loading.

1. Select **New Test Suite**, type **MyFirst_TestSuite** in the name field, and click **Create Screen.**
 
    ![](images/new-test-suite-xplat.png)

    The screen contains a test structure that's added to the UI Flow.

1. Start implementing the code for your test. See [Your Complete Guide to BDD Testing in OutSystems](https://www.outsystems.com/blog/posts/bdd-testing/) for more information on creating specific tests.

## Learn more about component testing

If you're interested in learning more about component testing and about best practices, see the following resources. These pages provide information to help you master the art of automated testing.

* [Component Testing Best Practices video](https://www.outsystems.com/training/courses/180/component-testing/?LearningPathId=10) -- A video detailing best practices for structuring and organizing test code for component tests.
* [Your Complete Guide to BDD Testing in OutSystems](https://www.outsystems.com/blog/posts/bdd-testing/) -- A thorough how-to guide on implementing your first test case with the BDDFramework 
* [BDDFramework for Client-Side documentation page]( https://www.outsystems.com/forge/Component_Documentation.aspx?ProjectId=10917&ProjectName=bddframework-client-side) -- A summary of the latest changes and features for the client-side tool
