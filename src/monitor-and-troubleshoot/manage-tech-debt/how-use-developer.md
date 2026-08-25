---
tags:
  - Mentor
  - Mentor Studio
  - Monitoring
  - Quality Assurance
  - Refactoring
  - Technical Debt
summary: 'OutSystems 11 (O11) Code Quality developer guide: check module technical debt, analyze findings impact, and resolve issues by setting finding status.'
locale: en-us
guid: 8b0d91f3-f1ee-48c2-8b7e-8a82aeb27ae3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=928:596
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - code quality
coverage-type:
  - understand
  - apply
isautopublish: true
---

# Getting started as a developer

<div class="info" markdown="1">

AI Mentor Studio is now Code Quality.

</div>

As a developer, **Code Quality** provides you with an overview of the organization's technical debt. It also provides you with a detailed overview of the technical debt of the apps in the infrastructure that need to be fixed so that the overall technical debt score is reduced.

This guide assumes the following:

* Your infrastructure is already set up in Code Quality.

* Your IT user is already associated with Code Quality.

## Check the technical debt of the modules of an app

The apps page gives you an overview of the apps in the infrastructure that you have access to.

Each square is an app. It shows the app name and the app type.

The color of each app shows you how high or low the technical debt is in that app.

Technical debt tells you how difficult or easy it is to change and maintain an app or module.

![Screenshot showing the technical debt scale with apps color-coded by debt level in Code Quality](images/use-debt-scale-ams.png "Technical Debt Scale in Code Quality")

Red means the app has high technical debt.

To get an overview of the modules of an app, double-click the app.  

![Screenshot of an app overview displaying modules and their technical debt in Code Quality](images/use-overview-app-ams.png "App Overview in Code Quality")

Selecting a module gives you detailed information on the left panel, as well as access to the module findings.

![Screenshot showing module dependencies and detailed information panel in Code Quality](images/use-module-dependencies-ams.png "Module Dependencies in Code Quality")

Click **Open Module findings** in order to see the causes of technical debt in the module (seen in the next section).

![Screenshot of the 'Open Module findings' button in Code Quality for analyzing technical debt causes](images/open-module-report-ams.png "Open Module Findings in Code Quality")

## Find and understand the causes of technical debt in the module

After clicking **Open Module findings** you can examine the causes of technical debt in the module.

![Screenshot of the technical debt findings interface in Code Quality with various metrics and details](images/use-report-ams.png "Technical Debt Findings in Code Quality")

You can filter the findings based on your team(s), a specific app, module, category, when it was analyzed, the findings status, as well as specific users.

![Screenshot showing different filters for the technical debt findings in Code Quality](images/use-filters-ams.png "Findings Filters in Code Quality")

To see details about a code pattern that causes technical debt, click **Impact**. The **Impact** information details why a code pattern creates technical debt.

![Screenshot highlighting the 'Impact' section of a technical debt findings entry in Code Quality](images/use-report-impact-ams.png "Findings Impact Details in Code Quality")

To check how to resolve the code pattern, click **How to resolve**. You can also use this information to understand the effort involved in fixing a code pattern.

![Screenshot showing the 'How to resolve' section with instructions for resolving technical debt in Code Quality](images/use-report-fix-ams.png "How to Resolve Technical Debt in Code Quality")

## Fix and resolve technical debt findings

The **Findings** section displays all of the occurrences of the code pattern. To see in which module and element each finding occurs, click the path icon.

![Screenshot of the 'Findings' section displaying code pattern occurrences in Code Quality](images/use-findings-ams.png "Findings Section in Code Quality")

To open **Service Studio** and navigate to the element where a code patterns occurs, click the **Open in Service Studio** icon.

![Screenshot of the 'Open in Service Studio' icon used to navigate to elements with technical debt in Code Quality](images/use-finding-open-ams.png "Open in Service Studio from Code Quality")

Your browser may ask you to confirm that you want to open **Service Studio**. In Chrome, confirm that you want to open **Service Studio** by clicking **Open Service Studio**.

You can change the status of the findings individually or in bulk.

![Screenshot showing the bulk selection feature for managing findings status in Code Quality](images/bulk-selection-ams.png "Bulk Selection of Findings in Code Quality")

After selecting one or multiple findings, you can change the status of the findings depending on your action:

* If you fix the finding, set the status to **Already fixed**. This lets other developers in your team know it's fixed. After the next synchronization, if you have solved the finding correctly, it disappears. Otherwise, the finding reverts to **Open**.

* If you don't fix the finding because the finding is a false positive, set the status to **False positive**. After the next synchronization, the finding is not counted toward the total technical debt score.

* If you don't fix the finding, but the finding isn't a false positive, set the status to **Won't fix** and detail the reason for not fixing it. After the next synchronization, the finding is not counted toward the total technical debt score.

* To temporarily remove the finding from the total debt calculation, set the status to **Remind me later**. After the next synchronization, and during the next 30 days, the finding is not counted toward the total technical debt score.
