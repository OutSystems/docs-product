---
summary: Release notes for ML Builder.
tags:
---

# Release notes

These are the release notes for ML Builder.

Each section in this document contains:

* **Title**. The date when ML Builder received updates.
* The **What's new** section. Updates about new features and improvements.
* The **Bug fixes** section. The list of resolved issues.

## Release Mar 11 2021

ML Builder updates for the release of March 11, 2021.

### What's new

* ML Builder now shows the score for each attribute about how useful the attribute is for the prediction. Only available for new models.
* Improved the AI provider setup to define the storage container automatically.
* New popup for attributes in the review and model details pages.
* Reviewed and improved text in the "Tips" section.

### Bug fixes

* Fixed the model performance score to show correctly after training a model.
* Fixed the delete button in the model details screen.
* Fixed delete and deploy model popup size.
* Fixed popups to prevent clipping of the content.
* Fixed the position of the starting guide topics.

## Release Feb 24 2021

ML Builder updates for the release of February 24, 2021.

### What's new

* Starting Guide. Use the Starting Guide to guide you through the main ML Builder concepts.
* New Welcome page experience.
* Removed unnecessary paddings from the right sidebar.
* Minor improvements in user experience.
* The right sidebar now is open by default in the model training flow.

### Bug fixes

* Fixed CSV generation issue by enclosing fields that have commas in quotes.
* Fixed CSV format by the encoding to UTF-8 as default.
* Fixed scroll to top in the model review screen.

## Release Feb 10 2021

ML Builder updates for the release of February 10, 2021.

### What's new

* You can now delete your models through the ML Builder. Deleting obsolete models is important to avoid additional costs in your Azure subscription.
* In the AI provider setup now you don't have to register Azure resources before fetching the workspace. This lets you set up the tool faster.

### Bug fixes

* Fixed an issue that prevented training more than two models in parallel, in the same cluster.
* Fixed the cluster name so it can accept more than 16 characters.
* Fixed the decimal score representation so it doesn't show as a set of characters but the decimal value.

## Release Dec 7 2020

ML Builder updates for the release of December 7, 2020.

### What's new

* ML Builder is now a SaaS tool. Having the tool in the cloud reduces the installation efforts and provides a scalable solution for public availability.
* Now the training and deploy of a model are separate stages. The separation of stages lets you have a better overview and cost control of your Azure subscription.
* ML Builder user interface is a Reactive Web App with OutSystems UI. The newer UI framework provides a more straightforward and modern user experience.
* Improved CSS across the user interface.

### Bug fixes

No bug fixes in this release.
