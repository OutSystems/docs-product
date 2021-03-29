---
summary: Use deployment plans to take changes done in applications from one environment to another.
---

# Deployment Plans

A **deployment plan** allows you deploy application changes like new features and fixes, performed in one environment, to a different environment, for example from Development to QA.

A deployment plan can contain:

* Applications
* Version tag information
* Deployment notes
* Settings like [Site Property values](tp-configure-site-properties-during-deploy.md)

You can create deployment plans in LifeTime, on the **Deployment Plans** screen, under the **Applications** area.

You can also create a deployment plan by [reusing a finished plan](#reuse) or [retrying an aborted plan](#retry).

## The Deployment Plans screen

The **Deployment Plans** screen contains a list of past and current deployment plans in LifeTime, along with their status and details.

Open the Deployment Plans screen by clicking **Deployment Plans** under the **Applications** area.

![](images/deployment-plans-option-lt.png)

From this screen you can perform several operations like retrying an aborted deployment plan and reusing a finished deployment plan. The available operations on each plan depend on the plan's status.

![](images/deployment-plans-list-lt.png)

## Reusing a deployment plan { #reuse }

Reusing a deployment plan will get you faster deployments by not having to create deployment plans from scratch. You can reuse any finished deployment plan that was not aborted.

 This operation is especially useful in the following situations:

* **You are deploying to sequential environments in your infrastructure.** For example, you first deployed from DEV to QA and now you wish to deploy the same applications and versions from QA to PRD.  
    In this case you will reuse a recently finished plan to deploy applications to the next environment.

* **You are creating a new deployment plan very similar to a previous one.** Reusing an existing plan helps you reduce the risk of making mistakes, since you will not have to create the deployment plan from scratch.  
    In this case you will search for the desired plan in the Deployment Plans screen and choose the "Reuse Plan" operation.

The new deployment plan, reused from an existing one, will have the same applications (if they're available in the selected source environment) and, optionally, the same tagged versions of those applications.

To reuse a deployment plan from the Deployment Plans screen do the following:

1. Open the Deployment Plans screen from the Applications screen.

    ![](images/deployment-plans-option-lt.png)

1. Find the plan you wish to reuse in the plan list. You can search for the plan using several criteria, and use the **Advanced filters** for more search options.

    ![](images/deployment-plans-list-lt.png)

1. Click **Reuse Plan**. This operation is available for all finished plans that were not aborted.

1. In the pop-up window, choose the **source** and **target** environments for the new plan.

    ![](images/deployment-plans-reuse-popup-lt.png)

You can choose to keep the tags that were in the source plan by selecting **Keep the tags used in the original plan**.  
In this case, if some of the tagged versions of the original plan are not available for deployment (for example, if the version is not available in the selected source environment or if there's a more recent version of an application in the selected target environment), you will get a feedback message stating this situation, and you will be able to adjust the new deployment plan accordingly.  

If you don't select this option, the plan will contain the same applications but with the latest tags available for deployment.

**Notes:**

* The Reuse Plan operation is only available for finished deployment plans that were not aborted. For aborted plans, use the [Retry Plan](#retry) operation.

* You can select any source and target environments, as long as the source environment has at least **one** application contained in the source plan. When you select a source environment that doesn't contain **any application** from the source plan, the pop-up will show a warning and you will not be able to move forward.

* When you select a source environment that doesn't contain **some** of the applications in the source plan, the pop-up will show a message telling you that those applications will not be available in the new plan.

## Retrying an aborted deployment plan { #retry }

A deployment plan can be aborted manually by an operator or by the OutSystems platform, due to some issue that occurs during deployment.

When this happens, you don't need to create a new deployment plan from scratch to try to execute the same deployment operation, i.e. a deployment with the same applications and the same versions. In these situations you can **retry the deployment plan**, which is an operation available for all aborted deployment plans.

The retry operation does the following:

1. Creates **a copy** of the aborted deployment plan in an unsaved state, with the same applications and tagged versions and between the same source and target environments as the original deployment plan.  

1. Navigates to the new deployment plan detail screen, allowing you to make some adjustments to the plan before executing it.

To retry a deployment plan from the Deployment Plans screen do the following:

1. Open the Deployment Plans screen from the Applications screen.

    ![](images/deployment-plans-option-lt.png)

1. Find the aborted plan you wish to retry in the plan list. You can search for the plan using several criteria.

    ![](images/deployment-plans-list-lt.png)

1. Click **Retry Plan**. This operation is available for all aborted plans.

**Notes:**

When you're retrying a deployment plan the following situations may arise due to changes in the source or in the target environment:

* If the source environment no longer contains **some** of the applications in the original plan, LifeTime will show a pop-up with a message telling you that those applications will not be available in the new plan.

* If the source environment no longer contains **any** application from the original plan, LifeTime will show a pop-up with a warning and you will not be able to move forward.

* If some of the **tagged versions** are not available for deployment anymore when you retry the plan (for example, if a more recent version of an application was already deployed to the target environment), LifeTime will show you a feedback message stating this situation and you will be able to adjust the new deployment plan accordingly.
