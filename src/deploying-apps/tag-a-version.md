---
summary: Explore how OutSystems 11 (O11) facilitates application version tagging and deployment through its LifeTime interface.
tags: support-Application_Lifecycle-featured
locale: en-us
guid: d97b99fb-75a2-453c-a20d-d4270e09c8ed
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=257:3
---

# Tag a Version

Tagging an application version in LifeTime means that a snapshot of the development state of the application is taken and a version number is associated to it. When [deploying the application](<deploy-an-application.md>), just select the tagged version and LifeTime deploys the application in the exact development state in which it was tagged.

A typical situation of tagging an application is when it reaches a development milestone:

1. The application is tagged
2. The development continues
3. The tagged version of the application is deployed to another environment for tests

When tagging a mobile app, there is an extra section called Mobile Versions that allows tagging the mobile package. That operation isn't frequently needed because the platform automatically updates the app without generating new packages. In some [update scenarios](<mobile-app-packaging-delivery/mobile-app-update-scenarios.md>) new packages have to be tagged and generated.

Here's an example of tagging applications.

## Tag a Web and a Mobile Application

In this example, there are two applications in Development environment:

* A mobile app (MyApp)
* A web application (MyWebApp)

They have reached a development milestone and must be tagged.

![Screenshot of the OutSystems LifeTime interface showing the application tagging process with a plus sign indicating changes since the last tag.](images/tag-a-version-1.png "Application Tagging Interface")

The plus ('+') sign means the applications have changed since their last tag.

### Tag the Mobile App

To tag the mobile app, do the following:

1. Click on **MyApp** to show its details.
    
    ![Screenshot of the OutSystems LifeTime interface displaying details for the mobile app 'MyApp' with the 'TAG VERSION' button highlighted.](images/tag-a-version-2.png "MyApp Details")

1. Click the **TAG VERSION** button for the Development environment.

1. Set the Version to **0.2** and type a description. In the Mobile Versions section, there's also a plus ('+') sign for the Android platform, meaning that the [changes in the app](mobile-app-packaging-delivery/mobile-app-update-scenarios.md) require the tagging and generation of a new mobile package. Set also the mobile version for the native platform. Make sure the mobile version [is higher than any previous version](#mobile-package-version).
    
    ![Screenshot of the OutSystems LifeTime interface with the 'TAG VERSION' dialog for 'MyApp' where the version is set to 0.2 and a description is added.](images/tag-a-version-3.png "Tagging Mobile App Version")

1. Click the **TAG VERSION** button to finish.
    
    ![Screenshot of the OutSystems LifeTime interface confirming that the mobile app 'MyApp' has been successfully tagged with version 0.2.](images/tag-a-version-4.png "Mobile App Tagged")

The mobile app is now tagged and can be [deployed](<deploy-an-application.md>) to Quality at any time.

<div warning="info" markdown="1">

Note that the mobile version will only be updated in other environments if the application  **is deployed through LifeTime**. Publishing the same version in other environments directly in Service Center or Service Studio will not update the mobile version.

</div>

If you need to install and test the tagged application version in a mobile device still in the Development environment, you can [generate a new mobile package](mobile-app-packaging-delivery/generate-distribute-mobile-app/intro.md) before proceeding with the deploy to Quality. Otherwise, OutSystems generates a new mobile package during the deployment process.

#### Mobile package versions { #mobile-package-version }

In [update scenarios](<mobile-app-packaging-delivery/mobile-app-update-scenarios.md>) that require the generation of a new mobile package, you need to set the new mobile version for the package during the tagging operation in LifeTime. This **new mobile version** must be **higher than any previous version**.

LifeTime applies this restriction to the mobile version to comply with the same restriction in public app stores, where you can't publish a new version of your mobile app using a version number lower than the current one. As LifeTime can't validate which versions were already published in the app stores, the tagging operation restricts lower mobile versions.

To cope with this limitation, during the development cycle between app store releases, the developers should increment the mobile version below the next version value for the new app store release.

Take the following example:

* You release your mobile app to app stores with **version 1.0**. The next release in the stores should be **version 2.0**.

* During the development cycle of version 2.0, the development team needs to generate new mobile packages.

* Therefore, every time the developers need to generate a new mobile package during the development cycle, the mobile version must be **lower than 2.0**. For example, you can use the following version numbers: 1.1, 1.2, 1.3, or 1.0.1, 1.0.2, 1.0.3, depending if there is the possibility of intermediate releases.

* You should use the mobile version 2.0 only when the new release of your application is ready to publish in the app stores.

### Tag the Web Application

To tag the web application, do the following:

1. Click on **MyWebApp** to show its details.

    ![Screenshot of the OutSystems LifeTime interface displaying details for the web application 'MyWebApp' with the 'TAG VERSION' button highlighted.](images/tag-a-version-5.png "MyWebApp Details")

1. Click the **TAG VERSION** button for the Development environment.

1. Set the Version to **0.3** and type a description. 

    ![Screenshot of the OutSystems LifeTime interface with the 'TAG VERSION' dialog for 'MyWebApp' where the version is set to 0.3 and a description is added.](images/tag-a-version-6.png "Tagging Web Application Version")

1. Click the **TAG VERSION** button to finish.

    ![Screenshot of the OutSystems LifeTime interface confirming that the web application 'MyWebApp' has been successfully tagged with version 0.3.](images/tag-a-version-7.png "Web Application Tagged")

The web application is now tagged and can be [deployed](<deploy-an-application.md>) to Quality at any time.
