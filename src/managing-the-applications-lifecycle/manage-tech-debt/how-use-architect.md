---
tags:
summary: Learn how to Check the technical debt of all the apps in your infrastructure.
locale: en-us
guid: 5771d1af-cf5a-4e5c-a4c7-79f03a5f99ef
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
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

![Overview of apps in infrastructure](images/use-overview-infra-ams.png)

Each square is an app. It shows the app name and the app type.

The color of each app shows you how high the technical debt is in that app.
Technical debt tells you how difficult or easy it is to change and maintain an app or module.

![Technical debt and agility color scale](images/use-debt-scale-ams.png)

## Find an app with high technical debt

Red means the app has high technical debt.

Select a red app. If there's no red app, select another app, preferably orange or yellow.

![Select app with high technical debt](images/use-select-app-ams.png)

## Check the dependencies of the app

Selecting an app highlights the dependencies of that app. Use this information to help you decide which apps should be improved first.

![Check app dependencies](images/use-app-dependencies-ams.png)

## Find out which team owns the app

On the side panel, check the team that owns the app. You can use this information to ask for improvements to the app.

![Check app owner](images/use-app-team-ams.png)

## Check how technical debt has changed with time

The mini chart shows how technical debt has changed over time.

![Mini technical debt chart](images/use-mini-chart-ams.png)

To get more details, click the mini chart.

![Expanded technical debt chart](images/use-chart-ams.png)

The technical debt chart includes a technical debt trendline and a trend value. This information tells you whether your technical debt is increasing or decreasing with time. 
To get information for a specific date, hover your mouse over the chart.

![Get technical debt chart details on a date](images/use-chart-date-ams.png)

You can also select another date range.

![Change chart time frame](images/use-chart-range-ams.png)

## Get an overview of the technical debt across all factory

The **Infrastructure overview** dashboard gives you an understanding of the current status, distribution and evolution of the technical debt across all the apps in your factory.

![overview dashboard](images/overview-dashboard-ams.png)

To access the **Infrastructure overview** dashboard, click the **Overview** tab in the AI Mentor Studio.

Filter the analysis data by team, application, code pattern category, or date range, to get the data that you require to do the proper follow up. You can see, for example, which code patterns of a specific category contribute more to the technical debt of your factory.

![overview dashboard](images/architect-get-overview-ams.png)

[See here](overview-dashboard.md) more details about the Infrastructure overview dashboard.

## Remove modules from technical debt score

You can remove specific modules from the technical debt calculation for your infrastructure, by setting them as **Ignored Modules**.  
To set a module as ignored, follow these steps:

1. Click the **Maintenance** tab.

    ![Select Maintenance](images/use-username-maintenance-ams.png)

1. On the **Maintenance** screen, set the **Module status** filter to **All status**.

    ![Set status](images/use-maintenance-status-all-ams.png)

1. Select the module you want to remove from the technical debt calculation, and then select **Change to Ignored**.

    ![Setting a module as ignored](images/use-ignore-module-ams.png)

After completing these steps and after the next synchronization occurs, the findings associated with the ignored module are resolved and removed from the technical debt score.
