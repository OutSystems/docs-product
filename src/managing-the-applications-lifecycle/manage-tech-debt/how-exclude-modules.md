---
tags: Architecture Dashboard; how-to; manual
summary: You can exclude classes of modules from tech-debt analysis in Architecture Dashboard.
en_title: How to exclude modules from tech debt analysis  
---

# Excluding modules from tech debt analysis

**Architecture Dashboard** provides an integrated, bird’s eye view of technical debt across an entire portfolio of applications and the interdependencies between modules in the developers’ environment.

However, analyzing every module in a factory can result in a misleading technical debt score. To help your development team get a realistic picture of the portfolio's technical debt, you can ignore certain modules from the analysis.

Modules that might be ignored include:

* Proof-of-concept or demo applications
* Applications that have not changed for an extended period of time, possibly because development was halted
* Experimental or preliminary applications that are not meant for production
* Forge components integrated, as is, into applications

**Architecture Dashboard** gives architects and team leads the ability to ignore individual modules—or to bulk-select whole classes of modules—so they will be excluded from the technical debt evaluation of your factory’s portfolio.

<div class="info" markdown="1">

For more information about permissions to access this feature, see [How does Architecture Dashboard work](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Manage_technical_debt/How_does_Architecture_Dashboard_work#Permissions).

</div>

To select modules for exclusion:

1. Go to the **Maintenance** tab of **Architecture Dashboard**.
    ![Select Maintenance tab](images/ad-autoclass-1.png)
1. On the **Maintenance** page, click **Ignored Modules** to get a list of all modules in your infrastructure, which includes filtering options for finding specific modules to ignore.
    ![Ignored modules page](images/ignored-modules-main-page-ad.png)

You can use the following filters to fine-tune your choices, and then sort the results by the column headers.

* Teams
* Apps
* Modules
* Modules status
* Types


## Batch selection of modules

In some cases, **OutSystems** recommends excluding entire classes of modules from technical debt analysis, such as demo apps that are not meant to be released to production.

Ignoring **[Forge](https://www.outsystems.com/forge/)** components in **Architecture Dashboard** is another good practice. **OutSystems** developers rely on the **Forge** to accelerate the design process. Components that are used as-is do not have to be included when calculating your infrastructure’s technical debt.

To ignore **Forge** components in technical debt analysis:

1. Go to the **Maintenance** tab.
1. Click **Ignored Modules**.
1. Select **Forge components** from the **Types** dropdown.
    ![Ignore Forge components](images/ignore-forge-components-ad.png)
1. Click the select all box in the header. 
    This selects all of the components on the current page.
    ![Ignore Forge components](images/bulk-actions-ad.png)
1. The information area under the filters tells you how many modules have been selected on the current page. Click **Select all &lt;n> items on this list** to add **Forge** components on all pages to the selection.
    ![Select all components](images/select-all-ad.png)

1. The information area now tells you that all components on all pages have been selected. Click **Change to Ignored**. 
    ![Select all components](images/change-to-ignored-ad.png)
1. Click **Change to Ignored** in the popup window that asks you to confirm that you want to ignore all of the selected components, including those beyond the displayed page.
    ![Confirm Ignore Forge components](images/bulk-actions-confirm-ad.png)

All of the selected components/modules are marked to be ignored during future technical debt evaluations.


## Excluding individual modules

In some cases you may wish to fine-tune your selections. As one example, you may exclude old or discontinued modules, as follows:

1. In the **Maintenance** page click **Clear all** if the **Ignored Modules** page shows the results of a previous search.
1. Sort the modules by the **Last analyzed on** column (or the **Status changed on** column, depending on what criteria you wish to use).
1. Click the specific modules to exclude from analysis.
1. Click **Change to ignored**.
    ![Ignored modules page](images/individually-ignored-modules-ad.png)
    <div class="info" markdown="1">
    When all modules in an app are changed to **Ignored**, the app itself is also ignored during analysis. In a like manner, if one or more modules of a previously ignored app is changed to **Analyzed** the app itself will also be analyzed.
    </div>
