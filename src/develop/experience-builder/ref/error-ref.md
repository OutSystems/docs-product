---
tags: Experience Builder; Mobile.
summary: Learn more about the issues that can occur while publishin an Experience Builder app. This topic includes a list of all the warning and blockers in Experience Builder.
---

# Experience Builder blockers and warnings

Experience Builder validates your app before publishing it to the environment.

If the validation fails, Experience Builder lists the issues it found in your app or environment.
Issues belong to one of the following types:

* **Blockers** are issues that you need to solve before publishing the app.

* **Warnings** are issues that may affect the experience of your app, but you don't need to solve them to publish the app.

An issue may include a **Fix it now** link that helps you solve you the issue. Selecting this link takes you to the location in Experience Builder where you can fix it.

## Blockers reference

A blocker is an issue with your environment or with your app that blocks the publishing of the app.

Experience Builder lists blockers in the publish dialog after **Before publishing the app, please review the following:**.

### We can't publish your application, because the dependency "&lt;dependency-name&gt;" has version &lt;outdated-version&gt; and the required version is &lt;current-version&gt;

Your environment doesn't have the correct version of a dependency of the app. 

[Update the dependency](../how-update-dependency.md).

### We can’t publish your app. There’s a missing required dependency in your environment: "&lt;dependency-name&gt;"

Your environment doesn't have a required dependency installed.

[Install the dependency](../how-update-dependency.md).

### You haven’t added any screens.

Your app must have screens, otherwise you can't test it.

Add flows to your app.

### Not enough flows. Add flows to your app.

Ensure that your app has at least two flows.

### Missing menu items. Add menu items to your app.

In the **Menu** canvas, add a menu icon and connect it to a flow.

### Menu items are missing links. Add destination links to your app's menu items.

In the **Menu** canvas, link at least one menu item to a flow.

### Missing flows. Add a Login or Onboarding flow.

Your app needs a default screen to act as the entry point. Experience Builder uses either a login or onboarding flow as the default screen of your app.

In the **Flow** canvas, select **Add flow**, search for `Login`or `Onboarding`, and add a login or onboarding flow to the app.

### Too many login flows. Add only 1 login flow per app.

Your app can only have one login flow.

In the **Flow** canvas, delete the login flows until your app only has one login flow.

## Warnings reference

A warning lets you know about issues that can compromise the experience of testing the app.

Experience Builder lists warnings in the publish dialog after **It looks like your app isn't ready to be published... You might want to:**.

### There’s a missing dependency in your environment: "&lt;dependency-name&gt;"

Your environment doesn't have an optional dependency installed.

Install the missing dependency in one of the following ways:

* [Install the dependency component package](../how-update-dependency.md)  associated with the missing component.

* Select **Fix it now**, download the dependency from Forge, and install it in the environment using Service Studio.

### Unlinked menu items. Connect menu items to destination flows.

When using the app, selecting the unlinked menu entries won't take you anywhere in the app.

Connect menu items to flows.

### Can't access the "&lt;flow-name&gt;" flow.

When using the app, you won't be able to access the screens in the &lt;flow-name&gt; flow since no flow or menu item connect to the &lt;flow-name&gt; flow.

Connect the end point of another flow or a menu item to &lt;flow-name&gt; flow.

### That doesn't look right. Your login flows isn't connected to another flow. Connect the flow so user can log in and use your app.

You must connect the exit point of the login flow to another flow, otherwise end users can't test the rest of the app.

### Adding flows would improve navigation.

You only added onboarding and login flows to your app and you won't be able to test your app.

Add flows of other types, and make sure the login or oboarding flows connect to the flows you added.

### You've added flows that required registered users. Add a login flow.

Some flows in the app are only accessible to registered uses, which means the app must be able to authenticate users using a login flow.

### You've added a passcode login flow. Add a signup flow.

Passcode information isn't available by default in end-users created using Users.
All the singup flows in Experience Builder let the end-user set a passcode.
