---
summary: Explore how OutSystems 11 (O11) manages application themes to ensure consistent enterprise look & feel while allowing customization.
guid: 5a065377-1843-4d63-b7b9-135f9de77886
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/rdSCF3WV51agwVCcEFkx2I/App-architecture?node-id=1-1739&t=WkNS4cBkPZHvTban-1
tags: enterprise architecture, ui design, theme customization, css, layout design
audience:
  - frontend developers
  - full stack developers
  - ui designers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
  - understand
---

# Isolating an application Theme

In an enterprise installation, applications usually share the same corporate look & feel. Being a shared component, it is key to correctly position a global Theme module in the enterprise architecture.

A Theme module includes the following components:

* The theme itself (the CSS)
* Layout *Blocks,* to define screen or screen section patterns
* Logo images
* ![Diagram illustrating login flow and exception handling components in an application theme.](images/isolating-app-theme_0.png "Login Flow and Exception Handling Components") Login flow and exception handling
* ![Diagram showing menu and navigation support logic within an application theme.](images/isolating-app-theme_1.png "Menu and Navigation Support Logic") Menu and navigation support logic
* Transversal roles (normally job roles like Manager or Employee) that can be reused in any application. This roles may influence the menu entries to be displayed.

<div class="warning" markdown="1">

The Theme module should be restricted to global look & feel elements and never be used as a global repository of assets and utilities.

</div>

## Same look and feel, menu and login flow

The following example shows a Global theme that is reused by several applications, supplying a common menu and login flow. This scenario makes sense if all the applications belong to a common Portal.

![Architecture diagram depicting global theme reuse across multiple applications, with common services and system components.](images/isolating-app-theme_2.png "Global Theme Reuse Across Applications")

It is based on one of the built-in themes supplied in OutSystems UI.

If the Common services supply UI components (*Blocks*), they should be based on the built-in base theme, since they are reusable by other applications that might be using a different look & feel.

A *Block* will assume the CSS of the consuming module, thus adapting to the look & feel of the final application.

Services inside each application are specific for that application, hence they can safely use the Global theme.

## Same look and feel, different menus and login flows

If the applications are independent from each other and all they need is to share the global look & feel, then each application must have its own theme module.

![Architecture diagram showing independent application themes inheriting from a global theme, with separate app themes and common services.](images/isolating-app-theme_3.png "Independent Application Themes Inheriting Global Theme")

In this case, each application theme inherits the common global theme, but defines its own menu and/or login flow.

Any overall change to the look & feel is performed in the Global theme module. Specific menus and login mechanisms (integrated, federated, different user provider, among others) are specialized in each application theme.

## More information

To learn more about how to design your application architecture check the [Designing the architecture of your OutSystems applications](../intro.md) guide.

You can also check for further recommendations on how you should [compose your application landscape](06-app-composition.md).
