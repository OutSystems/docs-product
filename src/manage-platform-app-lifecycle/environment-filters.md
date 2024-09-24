---
summary: Using filters allows you to create a custom view in your environments.
tags: support-Application_Lifecycle; support-Cloud_Platform; support-devOps
locale: en-us
guid: 9A82CE12-91D7-45F3-9C28-0F2D00A486B4
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=2186%3A6469&mode=design&t=rzWSTBJIapfhmERp-1
---
# LifeTime environment filters

<div class="info" markdown="1">

 While not a prerequisite, some knowledge on the following topics is helpful for anyone using the environment filter feature:

* OutSystems infrastructure and environment:

    * [Setting Up OutSystems](../setup-infra-platform/setup/intro.md)

    * [Managing Your OutSystems Infrastructure](initial-setup-of-an-infrastructure.md) (namely, adding or removing and reordering environments in an infrastructure)

* [Deployments and stagings with OutSystems](https://www.outsystems.com/evaluation-guide/how-does-outsystems-handle-deployment-and-staging/)

</div>

The landing page of the **LifeTime Management Console** (**Applications** list screen) gives IT users a high-level view of the state of their application portfolio. It provides information on the state of existing applications across the different environments that compose the infrastructure and it's the starting point for many  business needs, such as checking application details, staging application versions across environments up to managing user permissions, and infrastructure-level configurations.

![Screenshot of the LifeTime Management Console Applications list screen showing the state of applications across different environments](images/applications-lt.png "LifeTime Management Console Applications List")

## Benefits of using environment filters

With time, you might add new environments to your growing infrastructures and have to accommodate different CI/CD needs. For example, you might have a new specialized environment for integration testing, or you need a segmented app portfolio for separate delivery lines, depending on the target audience of the apps, such as internal facing apps versus external facing ones.

Infrastructure growth makes it difficult to monitor different CI/CD pipelines efficiently when the console displays the whole infrastructure, as opposed to a segmented one that suits your business needs.

To deal with this increased complexity, as of **LifeTime version 11.15.0**, OutSystems allows you to create custom views of the infrastructure, or environment filters. 

An environment filter is a subset of the infrastructure environments that you define, which helps you to focus on specific business cases, as opposed to the whole infrastructure. Create, edit, and delete as many environment filters as you need, and switch between them on the **Applications** list screen in LifeTime. Examples include creating a filter for your internal environments and another for your external ones. 

## Real-life examples of using environment filters

Here are 2 business cases that showcase the benefits of the new filters feature:

1. In a factory with multiple delivery lines, **an app deployer creates a filter that enables them to** select and focus only on the environments of the pipeline that are currently relevant for their work.

1. **A developer** that usually works with a small set of environments (out of the many that compose a factory) **creates a filter that enables them to** focus only on those, instead of having the whole factory visible by default.

### Creating an environment filter

**Prerequisite**: IT users require read access to the environment they want to create a filter for. 

To create an environment filter, follow these steps in LifeTime:

* In the **Applications** list screen, expand the environment dropdown list and select the option to create an environment filter.

    ![Step-by-step process showing how to create an environment filter in the LifeTime Management Console](images/create-filter-1-lt.png "Creating an Environment Filter in LifeTime")

* Enter a name for the filter and select the environments that you want to display in this new filter. Then, choose whether you want this filter to be the default screen for your applications list, and click **Create**.

    ![Dialog box for entering a name for the new environment filter and selecting environments to include](images/create-filter-2-lt.png "Environment Filter Configuration")

As a result, the new filter is available to use. Edit or delete filters, as needed.

![Notification of successful creation of a new environment filter with the filter list visible](images/result-successful-filter-list-lt.png "Successful Creation of Environment Filter")
![Options to edit or delete environment filters in the LifeTime Management Console](images/edit-delete-filter-lt.png "Edit and Delete Environment Filters")

Each time you switch filters, the view is automatically updated to the selected filter.

![LifeTime Management Console view filtered to show only internal environments](images/internal-filter-lt.png "Internal Environment Filter View")
![LifeTime Management Console view filtered to show only external environments](images/external-filter-lt.png "External Environment Filter View")

## Conclusion

Ultimately, environment filters provide you with a customized view of your environments, thus giving you better visibility and oversight of your environments to better manage your pipelines and application lifecycle within each pipeline. Futhermore, using smaller environment filters can provide better response times for loading the applications list screen.
