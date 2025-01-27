---
tags: user feedback management, application lifecycle management, environment configuration, permissions management, user experience
summary: OutSystems 11 (O11) streamlines user feedback management through its App Feedback application.
locale: en-us
guid: b8db2ed6-0551-41c8-b16d-3063670c0417
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=267:14
audience:
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - lifetime
coverage-type:
  - apply
---

# Handle the submitted feedback


When you [enable user feedback for your apps](user-feedback-enable.md), the App Feedback application collects all the feedback your users send for each app. To act upon the feedback received, follow the steps below.

1. Open the LifeTime console at `https://<your environment>/Lifetime`.

    <div class="info" markdown="1">

    If you don't have LifeTime installed, access the App Feedback application of your environment by visiting the URL `https://<your environment>/ECT_Provider`.

    </div>

1. In the Applications section, select the **App Feedback** option in the drop-down menu next to the environment for which you want to see the feedback items.

    ![Dropdown menu for selecting App Feedback in the LifeTime console](images/app-feedback-handle-3.png "App Feedback Selection")

1. Sign in with the credentials of a user account defined in the Users app (`https://<your environment>/Users`), that has Administrator or FeedbackManager permissions.

1. Click the **Feedback** section, to see a list of all the feedback submitted by users. 

1. On the right side of the screen, ensure the selection of the drop-down menu is **Open**. This option allows you to display open requests, closed ones, or both.

    ![Overview of feedback items in the App Feedback section](images/app-feedback-handle-overview.png "Feedback Overview")

1. Select one of the listed feedbacks to check the information provided by the user, and click **Open**.

    A window with the details opens, providing the feedback from the user and screenshot of the app screen.
    
    ![Detailed view of user feedback with screenshot in the App Feedback application](images/app-handle-feedback-details.png "Feedback Details")

1. To open the screen directly in Service Studio for acting upon the users' feedback, click **CHANGE THIS SCREEN**.

    1. Confirm this operation by clicking **Open Service Studio**. If you don't want to see this message again, click on the checkbox to automatically allow this operation.

        ![Confirmation dialog for opening Service Studio from the App Feedback application](images/app-handle-feedback-handle-ss-confirm.png "Open Service Studio Confirmation")

    1. Enter your environment address and login credentials to allow downloading the app module from Service Center to Service Studio, and click **LOG IN**.

        ![Login screen for downloading the app module from Service Center to Service Studio](images/app-feedback-handle-download-module.png "Download App Module")

    1. Implement the requested change or suggestion, publish your app, and test it.

1. To mark the feedback as closed, click **Close**. The request moves to the closed list.

    ![Feedback request marked as closed in the App Feedback application](images/app-handle-closed-request.png "Closed Feedback Request")
