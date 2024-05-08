---
summary: Learn how to deploy a single module in OutSystems 11 (O11) to enhance deployment efficiency for Traditional Web apps.
tags: runtime-traditionalweb
locale: en-us
guid: ee8de340-e9d3-4392-8c8e-a2f3d2c02340
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=257:54
---

# Deploy a Single Module

<div class="info" markdown="1">

Applies only to Traditional Web apps.

</div>

To decrease the deployment time, it's sometimes useful to deploy a single module of an application, instead of [deploying the entire application](<deploy-an-application.md>). This feature is only available for Web applications.

Here's an example of how to do it.

## Deploy one module of an app to Quality

In this example, MyBigWebApp is a web application with several modules. It has changes in one module (MyBigWebApp4) and we only want to deploy this module to Quality.

### Choose the module to deploy

In the 'Application' tab, click the **Deploy...** green button between Development and Quality.

In the MyBigWebApp application, click the **Do Nothing** dropdown menu, and select **Deploy Custom...**.

![Screenshot showing the Deploy Custom option in the MyBigWebApp application to select a single module for deployment](images/deploy-a-single-module-1.png "Selecting a Single Module for Deployment")

A pop-up opens, displaying all modules of the MyBigWebApp application. Notice the modules with a '+'(plus) sign, signaling that they have been changed.

Check the MyBigWebApp4 module to deploy its latest version to Quality. Confirm the choice by pressing **Done**.

![Pop-up window displaying all modules of MyBigWebApp with the MyBigWebApp4 module checked for deployment](images/deploy-a-single-module-2.png "Module Selection Pop-up")

### Deploy the Module

Back to the deployment screen, click **Validate Now** to validate if just deploying module MyBigWebApp4 from MyBigWebApp has no impact on other applications in Quality. All it's OK, so click on the **Continue** button to review the deployment plan. 

![Deployment screen with Validate Now and Continue buttons highlighted, indicating the process to deploy module MyBigWebApp4](images/deploy-a-single-module-3.png "Deployment Validation and Execution")

Add a note like 'Deploying module MyBigWebApp4 from MyBigWebApp' and click on **Deploy Now**.
