---
summary: List of System Actions (both server actions and client actions) available in OutSystems, including list operations.
tags: support-application_development; support-Mobile_Apps; support-webapps
---

OutSystems provides a set of **System Actions** that you can use when designing the Actions to define the business rules of your application.

Run System Actions the same way as any other Action in your module. **System Actions** are available in the **Logic** tab, under the **System** module within the **Server Actions** folder.

If you are developing a mobile app, along with the System Actions available at the server side, you can use a set of System Actions to run at the client side. These **Client Actions** are available under the System module within the **Client Actions** folder.

Similarly to the Actions you design in your module, some Systems Actions are **defined as functions**, which you can use also within Expressions. They're available in the **User Functions** folder within the Scope Tree of the Expression Editor.

## Referencing Systems Actions in  module

Only a subset of the System Actions is by default available in your module. You can add other System Actions at any time by adding new dependencies from the System module. To edit which Systems Actions are available in the module, do the following:

1. Open the **Manage Dependencies** window (**Ctrl+Q**).

1. Click **(System)** in the left pane. The available actions show in the right pane.

    ![Systems Actions in Manage Dependencies window](images/reference-systems-actions-ss.png?width=600)

1. Browse the available actions, click the checkboxes next to the actions you want to reference, then click **Apply** to confirm and close the window.

