---
tags: 
summary: Learn how to find and fix technical debt in an app.
locale: en-us
guid: 8b0d91f3-f1ee-48c2-8b7e-8a82aeb27ae3
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=928:596
---

# Getting started as a developer

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>

As a developer, **AI Mentor Studio** provides you with an overview of the organization's technical debt. It also provides you with a detailed overview of the technical debt of the apps in the infrastructure that need to be fixed so that the overall technical debt score is reduced.

This guide assumes the following:

* Your infrastructure is already set up in AI Mentor Studio.

* Your IT user is already associated with AI Mentor Studio.

## Check the technical debt of the modules of an app

The apps page gives you an overview of the apps in the infrastructure that you have access to.

Each square is an app. It shows the app name and the app type.

The color of each app shows you how high or low the technical debt is in that app.

Technical debt tells you how difficult or easy it is to change and maintain an app or module.

![Screenshot showing the technical debt scale with apps color-coded by debt level in AI Mentor Studio](images/use-debt-scale-ams.png "Technical Debt Scale in AI Mentor Studio")

Red means the app has high technical debt.

To get an overview of the modules of an app, double-click the app.  

![Screenshot of an app overview displaying modules and their technical debt in AI Mentor Studio](images/use-overview-app-ams.png "App Overview in AI Mentor Studio")

Selecting a module gives you detailed information on the left panel, as well as access to the module report.

![Screenshot showing module dependencies and detailed information panel in AI Mentor Studio](images/use-module-dependencies-ams.png "Module Dependencies in AI Mentor Studio")

Click **Open Module report** in order to see the causes of technical debt in the module (seen in the next section).

![Screenshot of the 'Open Module report' button in AI Mentor Studio for analyzing technical debt causes](images/open-module-report-ams.png "Open Module Report in AI Mentor Studio")

## Find and understand the causes of technical debt in the module

After clicking **Open Module report** you can examine the causes of technical debt in the module.

![Screenshot of the technical debt report interface in AI Mentor Studio with various metrics and details](images/use-report-ams.png "Technical Debt Report in AI Mentor Studio")

You can filter the report based on your team(s), a specific app, module, category, when it was analyzed, the findings status, as well as specific users.

![Screenshot showing different filters for the technical debt report in AI Mentor Studio](images/use-filters-ams.png "Report Filters in AI Mentor Studio")

To see details about a code pattern that causes technical debt, click **Impact**. The **Impact** information details why a code pattern creates technical debt.

![Screenshot highlighting the 'Impact' section of a technical debt report in AI Mentor Studio](images/use-report-impact-ams.png "Report Impact Details in AI Mentor Studio")

To check how to fix the code pattern, click **How to fix**. You can also use this information to understand the effort involved in fixing a code pattern.

![Screenshot showing the 'How to fix' section with instructions for resolving technical debt in AI Mentor Studio](images/use-report-fix-ams.png "How to Fix Technical Debt in AI Mentor Studio")

## Fix and resolve technical debt findings

The **Findings** section displays all of the occurrences of the code pattern. To see in which module and element each finding occurs, click the path icon.

![Screenshot of the 'Findings' section displaying code pattern occurrences in AI Mentor Studio](images/use-findings-ams.png "Findings Section in AI Mentor Studio")

To open **Service Studio** and navigate to the element where a code patterns occurs, click the **Open in Service Studio** icon.

![Screenshot of the 'Open in Service Studio' icon used to navigate to elements with technical debt in AI Mentor Studio](images/use-finding-open-ams.png "Open in Service Studio from AI Mentor Studio")

Your browser may ask you to confirm that you want to open **Service Studio**. In Chrome, confirm that you want to open **Service Studio** by clicking **Open Service Studio**.

You can change the status of the findings individually or in bulk.

![Screenshot showing the bulk selection feature for managing findings status in AI Mentor Studio](images/bulk-selection-ams.png "Bulk Selection of Findings in AI Mentor Studio") 

After selecting one or multiple findings, you can change the status of the findings depending on your action:

* If you fix the finding, set the status to **Already fixed**. This lets other developers in your team know it's fixed. After the next synchronization, if you have solved the finding correctly, it disappears. Otherwise, the finding reverts to **Open**.

* If you don't fix the finding because the finding is a false positive, set the status to **False positive**. After the next synchronization, the finding is not counted toward the total technical debt score.

* If you don't fix the finding, but the finding isn't a false positive, set the status to **Won't fix** and detail the reason for not fixing it. After the next synchronization, the finding is not counted toward the total technical debt score.

* To temporarily remove the finding from the total debt calculation, set the status to **Remind me later**. After the next synchronization, and during the next 30 days, the finding is not counted toward the total technical debt score.
