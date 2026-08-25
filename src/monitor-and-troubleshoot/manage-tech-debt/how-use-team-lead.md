---
tags:
  - Infrastructure
  - IT Teams
  - Monitoring
  - Technical Debt
summary: 'Code Quality team lead workflow in OutSystems 11 (O11): check app and module debt, filter findings, update finding status, and use the Infrastructure overview dashboard.'
locale: en-us
guid: efc039d9-67e7-4824-a8fb-5e65418db58c
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=928%3A595&mode=design&t=rzWSTBJIapfhmERp-1
audience:
  - Developer
  - Platform administrator
  - Tech lead
outsystems-tools:
  - code quality
  - lifetime
coverage-type:
  - understand
  - apply
isautopublish: true
---

# Getting started as a team lead

<div class="info" markdown="1">

AI Mentor Studio is now Code Quality.

</div>

As a team lead, **Code Quality** provides you with an overview of the technical debt of organization's technical debt as well as detailed overview of the technical debt of your teams's apps.

From the Apps canvas, you can drill down into the team's problematic modules, and take the necessary steps to reduce the technical debt score for these areas.

This guide assumes the following:

* Your infrastructure is already set up in Code Quality.

* Your IT user is already associated with Code Quality.

* You have the **Administrator** role in LifeTime.

After logging into [Code Quality](https://codequality.outsystems.com/), follow these steps:

## Check the technical debt of your team apps

The Apps page gives you an overview of all the apps on your infrastructure.

To only see apps from your team, select your team from the **Teams** dropdown.

![Screenshot showing how to select a team from the Teams dropdown in Code Quality](images/use-team-ams.png "Team Selection in Code Quality")

Each square is an app. It shows the app name and the app type.

The color of each app shows you how high or low the technical debt is in that app.
Technical debt tells you how difficult or easy it is to change and maintain an app or module.

![Color-coded scale indicating the level of technical debt for apps in Code Quality](images/use-debt-scale-ams.png "Technical Debt Scale")

Red means the app has high technical debt.

## Check the technical debt of the modules of the app

To get an overview of all the modules of an app, double-click the app.  

![Screenshot of the Code Quality interface showing an overview of an app's modules](images/use-overview-app-ams.png "App Modules Overview")

Selecting a module gives you detailed information on the left panel, as well as access to the module findings.

![Detailed view of a selected module showing dependencies and information in Code Quality](images/use-module-dependencies-ams.png "Module Dependencies and Details")

## Find and understand the causes of technical debt in an app

To go back and see all the apps of your team, click **Back to Apps** and select the app again. Make sure you don't double-click the app this time.

To see the causes of technical debt in the app, click the **Open app report** button in the side panel.

![Screenshot showing the 'Open app report' button in the side panel of Code Quality](images/use-open-app-report-ams.png "Open App Report Button")

You can filter the findings based on your team(s), a specific app, module, category, when it was analyzed, the findings status, as well as specific users.

![Screenshot of the filter options available in the app findings of Code Quality](images/use-filters-ams.png "Findings Filters")

To see the details about a code pattern that causes technical debt, click **Impact**. The **Impact** information details why a code pattern creates technical debt.

![Screenshot showing the 'Impact' section of a code pattern that causes technical debt in Code Quality](images/use-report-impact-ams.png "Findings Impact Details")

To check how to resolve the code pattern, click **How to resolve**. You can also use this information to understand the effort involved in fixing a code pattern.

![Screenshot of the 'How to resolve' section for a code pattern causing technical debt in Code Quality](images/use-report-fix-ams.png "How to Resolve Code Patterns")

The **Findings** section displays all the occurrences of the code pattern. To see in which module and element each finding occurs, click the path icon.

![Screenshot of the 'Findings' section displaying occurrences of code patterns in Code Quality](images/use-findings-ams.png "Findings Section")

You can change the status of the findings individually or in bulk.

![Screenshot showing how to select multiple findings for bulk status change in Code Quality](images/bulk-selection-ams.png "Bulk Selection of Findings")

After selecting one or multiple findings, you can change the status of the findings depending on your action:

* If you fix the finding, set the status to **Already fixed**. This lets other developers in your team know it's fixed. After the next synchronization, if you have solved the finding correctly, it disappears. Otherwise, the finding reverts to **Open**.

* If the finding is a false positive, set the status to **False positive**. After the next synchronization, the finding is not counted toward the total technical debt score.

* If the finding isn't a false positive, set the status to **Won't fix** and detail the reason for not fixing it. After the next synchronization, the finding is not counted toward the total technical debt score.

* To temporarily remove the finding from the total debt calculation, set the status to **Remind me later**. After the next synchronization, and during the next 30 days, the finding is not counted toward the total technical debt score.

## Get an overview of the technical debt of your team apps

The **Infrastructure overview** dashboard gives you an understanding of the current state, distribution, and evolution of the technical debt across all the apps of your team.

![Screenshot of the Infrastructure overview dashboard in Code Quality showing technical debt across all apps](images/overview-dashboard-ams.png "Infrastructure Overview Dashboard")

To access the **Infrastructure overview** dashboard, click the **Overview** tab in **Code Quality**.

![Screenshot highlighting the 'Overview' tab button in Code Quality](images/overview-dashboard-button-ams.png "Overview Dashboard Access Button")

Filter the analysis data by team, application, code pattern category, or date range, to get the data that you require to do the proper follow up. You can identify, for example, the apps and modules of your team that contribute more to your technical debt.

See this article, [Get an overview of the overall technical debt](overview-dashboard.md), for more details.
