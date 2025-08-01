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

This page outlines the current technical limitations of migrating the OutSystems 11 apps to ODC. OutSystems development teams are actively working to address the issues.

## Dependency warnings for Forge components after migration to ODC

Some apps referencing Forge components show errors due to different identifiers in ODC and O11. This happens with the Forge components that don't have an equivalent and compatible version in ODC.

### Impact

After migration from O11, you can't publish the apps in ODC due to invalid and outdated references to the Forge components.

### How to fix

Install a compatible Forge component in ODC, change the references, and publish the app. Alternatively, if there are no compatible components, consider removing their functionalities to publish the app.

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

## Static entities with auto-number not supported

After conversion, you might receive the error message "StaticEntity Auto Number not supported in this version." This issue occurs because the system hides static entities with auto numbers in references.

### Impact

The migration process cannot migrate data in the static entities.

### How to fix

Remove the hidden references that contain static entities with auto numbers. This requires a trial-and-error approach until the references containing the hidden entities are no longer present. You can also contact Early Access Program representatives and open a Support ticket requesting more information about the hidden entities.
