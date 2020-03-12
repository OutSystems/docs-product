---
summary: Check how to collaboratively create a deployment plan, that can later be executed by other team to deploy your applications.
tags: support-Application_Lifecycle-featured
---

# Plan a Deployment for the Operations Team

This topic describes how to collaboratively create a deployment plan, that can later be executed to deploy your applications.

In this example the eCommerce and Customer Portal apps are developed by two different teams. The teams have finished the last developments, and the apps are ready to be tested in Quality Assurance.

Each team leader adds their application to the deployment plan, but only the operations team has permissions to deploy applications to Quality Assurance.

## Create a Deployment Plan

After reaching a stable new version, the eCommerce team leader prepares the deployment plan for the eCommerce application.

On the deployment summary screen, fill-in the deployment notes, and choose **Save Plan &amp; Notes**. Notice that even though team leaders have no permissions to deploy to Quality Assurance, they can still create deployment plans.

![](images/plan-a-deployment-for-the-operations-team-1.png)

## Edit a Deployment Plan

Later on, the Customer Portal team leader edits the existing plan.

Click on the **Saved** blue button between Development and Quality Assurance, and set Customer Portal to **Tag and Deploy 0.6**.

![](images/plan-a-deployment-for-the-operations-team-2.png)

On the deployment summary screen, edit the deployment notes to include more comments. You can then save the plan for the operations team.

## Execute the Deployment

Now the operations team just needs to review the plan and execute it, since only they can deploy applications to Quality Assurance. Click on the **Saved** blue button between Development and Quality Assurance.

Click the **Continue** button to review the deployment plan.

![](images/plan-a-deployment-for-the-operations-team-3.png)

Review the application versions and deployment notes. Click **Deploy Now**.

The deployment begins, and you can check the deployment logs to see if everything went according to the plan.

![](images/plan-a-deployment-for-the-operations-team-4.png)
