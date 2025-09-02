---
summary: Current technical issues and recommendations in the migration of the OutSystems O11 apps to ODC, with recommendations how to address the issues where possible.
locale: en-us
guid: 84c331ff-513c-4e1f-ae7c-df9dfaac44f1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
coverage-type:
  - remember
tags: migration, technical issues, odc, o11, forge components
audience:
  - platform administrators
  - full stack developers
  - architects
outsystems-tools:
  - lifetime
  - forge
---
# Known issues

This page outlines the current known issues of the Migration Kit. OutSystems development teams are actively working to address these issues.

## Discrepancies with the latest app version in development only

The latest version of the app you want to migrate is in the development environment but not in production.

### Impact

Having the latest app version only in the development environment can cause discrepancies. This can happen because the migration process fetches the app from production.

### How to fix

Ensure that both the development and production environments are running the latest version.

## Forbidden access to LifeTime

This error shows in logs and means the service account cannot reach LifeTime to fetch data. You define this service account in the ODC Portal, during the setup of the Migration Assessment Tool.

### Impact

You can't initiate the migration because ODC cannot connect to O11 LifeTime.

### How to fix

Reset the service account for the Assessment Tool.

1. Go to LifeTime Access and access the page `https://<LifeTime_server>/lifetime/troubleshoot.aspx`. 
1. In the **Effective Permission Status** section, find the **AssessmentTool**(`service_account_name`).
1. Select the button **Clean up** in the same line.
