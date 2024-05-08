---
tags:
summary: Explore how OutSystems 11 (O11) leverages AI Mentor Studio to manage and reduce technical debt across applications.
locale: en-us
guid: 5771d1af-cf5a-4e5c-a4c7-79f03a5f99ef
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=928%3A594&mode=design&t=rzWSTBJIapfhmERp-1
---

# Getting started as an architect

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>

As an architect, the AI Mentor Studio provides you with an overview of your organization’s technical debt.

From the Apps canvas, you can check the technical debt of all the apps in your infrastructure and take the necessary steps to reduce the technical debt score for problematic areas. 

This guide assumes the following:

* Your infrastructure is already set up in AI Mentor Studio.

* Your IT user is already associated with AI Mentor Studio.

* You have the **Administrator** role in LifeTime.

After logging into [AI Mentor Studio](https://aimentorstudio.outsystems.com/), follow these steps:

## Check the technical debt of all your apps

The Apps canvas gives you an overview of all the apps on your infrastructure.

![Screenshot of the Apps canvas in AI Mentor Studio showing an overview of apps with their names and types.](images/use-overview-infra-ams.png "Apps Canvas Overview")

Each square is an app. It shows the app name and the app type.

The color of each app shows you how high the technical debt is in that app.
Technical debt tells you how difficult or easy it is to change and maintain an app or module.

![Image displaying the technical debt scale with different colors indicating the level of debt in apps.](images/use-debt-scale-ams.png "Technical Debt Scale")

## Find an app with high technical debt

Red means the app has high technical debt.

Select a red app. If there's no red app, select another app, preferably orange or yellow.

![Illustration of selecting a red app indicating high technical debt in the AI Mentor Studio.](images/use-select-app-ams.png "Selecting an App with High Technical Debt")

## Check the dependencies of the app

Selecting an app highlights the dependencies of that app. Use this information to help you decide which apps should be improved first.

![Screenshot showing how selecting an app in AI Mentor Studio highlights its dependencies.](images/use-app-dependencies-ams.png "App Dependencies Highlight")

## Find out which team owns the app

On the side panel, check the team that owns the app. You can use this information to ask for improvements to the app.

![Image of the side panel in AI Mentor Studio displaying the team that owns a selected app.](images/use-app-team-ams.png "App Ownership Information")

## Check how technical debt has changed with time

The mini chart shows how technical debt has changed over time.

![Screenshot of a mini chart in AI Mentor Studio showing the trend of technical debt over time for an app.](images/use-mini-chart-ams.png "Mini Chart of Technical Debt Over Time")

To get more details, click the mini chart.

![Detailed chart in AI Mentor Studio showing the technical debt trendline and trend value over time.](images/use-chart-ams.png "Detailed Technical Debt Chart")

The technical debt chart is a 100% stacked chart with a trend value (X axis) indicating the level of technical debt and a trendline (Y axis) that tells you whether your technical debt is increasing or decreasing with time. 

Ideally, you want your technical debt chart all green with a horizontal trendline. Or, a chart that's not so green but has a high negative trendline which indicates that the technical debt is being actively worked on.

To get information for a specific date, hover your mouse over the chart.

![Image of a technical debt chart with a cursor hovering over a specific date for detailed information.](images/use-chart-date-ams.png "Technical Debt Chart with Date Information")

You can also select another date range.

![Screenshot illustrating the selection of a different date range on the technical debt chart in AI Mentor Studio.](images/use-chart-range-ams.png "Selecting a Date Range on Technical Debt Chart")

## Get an overview of the technical debt across all factory

The **Infrastructure overview** dashboard gives you an understanding of the current status, distribution and evolution of the technical debt across all the apps in your factory.

![Screenshot of the Infrastructure overview dashboard in AI Mentor Studio showing technical debt across all apps.](images/overview-dashboard-ams.png "Infrastructure Overview Dashboard")

To access the **Infrastructure overview** dashboard, click the **Overview** tab in the AI Mentor Studio.

Filter the analysis data by team, application, code pattern category, or date range, to get the data that you require to do the proper follow up. You can see, for example, which code patterns of a specific category contribute more to the technical debt of your factory.

![Image showing how to filter analysis data by team, application, and other criteria on the AI Mentor Studio dashboard.](images/architect-get-overview-ams.png "Filtering Analysis Data on Dashboard")

[See here](overview-dashboard.md) more details about the Infrastructure overview dashboard.

## Remove modules from technical debt score

You can remove specific modules from the technical debt calculation for your infrastructure, by setting them as **Ignored Modules**.  
To set a module as ignored, follow these steps:

1. Click the **Maintenance** tab.

    ![Screenshot of the AI Mentor Studio with the Maintenance tab highlighted for user access.](images/use-username-maintenance-ams.png "Accessing Maintenance Tab")

1. On the **Maintenance** screen, set the **Module status** filter to **All status**.

    ![Image of the Maintenance screen in AI Mentor Studio with the Module status filter set to All status.](images/use-maintenance-status-all-ams.png "Maintenance Screen with Module Status Filter")

1. Select the module you want to remove from the technical debt calculation, and then select **Change to Ignored**.

    ![Screenshot showing the process of selecting a module to change its status to Ignored in AI Mentor Studio.](images/use-ignore-module-ams.png "Ignoring a Module in Technical Debt Calculation")

After completing these steps and after the next synchronization occurs, the findings associated with the ignored module are resolved and removed from the technical debt score.
