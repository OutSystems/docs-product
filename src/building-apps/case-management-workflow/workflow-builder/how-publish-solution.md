---
tags: solution deployment, service center, deployment process, outsystems service studio, outsystems deployment
summary: Explore how to publish a solution in an environment using OutSystems 11 (O11).
guid: 375789e9-8e68-42e9-abf8-731bc1fdc1c1
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - service center
  - case management framework
coverage-type:
  - apply
---

# How to publish a Solution in an Environment

To publish a Solution in an Environment follow these steps:

1. In the Service Center console of the target environment (`https://<environment>/ServiceCenter`), go to **Factory**.
1. Go to **Solutions**.
1. Select **Upload & Publish a Solution**.
1. Select **Choose File** and select the **Case Management Framework.osp** file.
1. Select **1-Click Publish**.

![Service Center console showing the process of uploading and publishing a solution in an environment](images/deploy-apps-sc-6.png "Uploading and Publishing a Solution")

Validate if the Solution is successfully published by checking for a **Done: The solution was successfully published.** message.

![Confirmation message indicating successful publication of the solution in Service Center](images/deploy-apps-sc-7.png "Successful Solution Publication Confirmation")
