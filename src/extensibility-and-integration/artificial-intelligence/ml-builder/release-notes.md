---
summary: Release notes for ML Builder.
tags:
---

# Release notes

These are the release notes for ML Builder.

## Release May 13 2021

ML Builder updates for the release of May 13, 2021.

### What's new

* Now you have the mini-hub in the header to help you browse the OutSystems cloud tools.
* Now you can request to receive a notification when the training is finished.
* New copy and images in the screen **Choose a use case**.
* In Service Studio, a new alert message when you try to call a model that's not deployed.
* In Service Studio, a new alert message when you try to call a model without all required parameters in the request.

## Release Apr 8 2021

ML Builder updates for the release of April 8, 2021.

### What's new

* Added a new and guided tutorial with a sample dataset and a demo app. Together, they let you train and integrate your first model.
* Now the ML Builder sets the number of the experiments automatically.
* On the review model page, added new instructions explaining how to obtain the relative path to a remote CSV file.
* We reviewed and improved the parameter descriptions of the public action of ML Builder Plugin v1.0.2.
* Added a success message for connection string validation during the AI provider setup.

### Bug fixes

* Fixed how the locations list show when configuring a new workspace. Now ML Builder shows only the valid locations for the subscription.
* Fixed the delete model button that was not appearing in certain use cases.
* Fixed the duplicated **Set up environment** title in the homepage.

## Release Mar 25 2021

ML Builder updates for the release of March 25, 2021.

### What's new

* All attributes now show during the attribute selection. Invalid attributes are disabled by default.
* Added the **Retry** button to the **Create a cluster** action. Use the button to retry the action if there's timeout while the cluster templates load.
* Improved the performance of loading cluster templates during the AI provider setup.
* Added an overview area for text classification and attribute prediction on the screen where you select a use case.
* Now the tips area is highlighted in the first training.
* Minor UX improvements.
 
### Bug fixes

* Fixed a sync issue where the workspace was registered in the database before getting the API response.
* Fixed the screen auto-refresh to prevent unnecessary refreshes.
* Fixed the display of a new workspace when the creation process starts.
* Fixed the provisioning cluster message display during the creation of a workspace.

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
