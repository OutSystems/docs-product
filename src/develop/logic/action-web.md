---
summary: Learn more about the Actions you can create and use in your web applications.
tags: runtime-traditionalweb; support-webapps; support-webapps-overview
locale: en-us
guid: 8536c396-e702-492a-8a07-ab8c8bc0334c
app_type: traditional web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=266:0
---

# Actions in Web Applications

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

In OutSystems web applications you can create the following Actions:

* Preparation
* Screen Actions
* Server Actions
* Service Actions

## Preparation Actions

When you have for example a web screen that lists Contacts, you will need to execute some logic before the screen is displayed to fetch the list of Contacts from the database.

In OutSystems, you execute that logic in a **Preparation** action:

![Diagram illustrating the Preparation action in OutSystems, which is executed before a web screen is rendered.](images/preparation.png "Preparation Action in OutSystems")

You don't have to explicitly invoke the **Preparation** action because it is automatically executed before a screen is rendered. It is right place to add all the logic you want to execute before the screen is displayed, such as setting values to variables and fetching data from the database.

You can also add a **Preparation** action to your Web Blocks.


## Screen Actions

In a web screen to update a Contact, for example, you will need to define an action that reacts to the user interaction of clicking the "Save" button and execute the logic to update the Contact. In OutSystems web applications you do this in a **Screen Action**:

![Flowchart showing a Screen Action in OutSystems that responds to user interaction such as clicking a 'Save' button.](images/screen-action.png "Screen Action in OutSystems")

**Screen Actions** allow you to run logic when the user interacts with the screen, such as clicking on a button or a link.

You can also add **Screen Actions** to your Web Blocks.


## Server Actions

An application typically has its own business rules. In OutSystems you can create **Server Actions** to encapsulate the logic that implements the business rules of your application and use them in other actions, such as Preparation actions, Screen Actions or other **Server Actions**:

![Visual representation of a Server Action in OutSystems, used to encapsulate business logic for reuse in various parts of the application.](images/server-action-web.png "Server Action in OutSystems")

You can set a **Server Action** as a function and use it directly in expressions. 

## Service Actions

This action is like a server action. But it has a loosely dependency with the producer. Means when any changes made to this action in producer module, consumer module need not be refreshed.

![Visual representation of a service action in outsystmes.]
(images/ServiceAction.png "Service Action in Outsystems")
