---
summary: This article provides guidelines for mapping O11 vertical and horizontal domains to OutSystems Developer Cloud (ODC) apps and libraries, aligning with their business domain characteristics and dependencies.
locale: en-us
guid: 2b5fc18e-70df-4b15-9046-7bb3de66b6c9
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?type=design&node-id=6%3A249&mode=design&t=blNAbpnofC4dwbOh-1
tags: outsystems, odc architecture, business domains, application lifecycle, component reusability
audience:
  - full stack developers
  - architects
  - backend developers
  - frontend developers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
---

# Map O11 domains to ODC apps and libraries

In ODC, you can create apps or libraries. An app can be a web, tablet, or mobile app. An ODC app encapsulates business concepts, UI, logic, and data of a specific business context. The ODC apps are loosely coupled and have independent lifecycles.

Libraries are a collection of reusable components used across multiple apps. They are used to implement business-agnostic components such as themes, integration wrappers, and logic utilities. They are strongly coupled with ODC apps and are packaged into a version included inside the application container.

For detailed information on ODC apps and libraries, refer to [ODC application architecture](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/app_architecture/).

O11 domains have similar characteristics to ODC apps since they are both loosely coupled by definition and have a close match, with most of the referencing rules. ODC Libraries share  similarities with O11 Foundation apps and can be extracted from these foundation apps. Based on these principles, here are some recommendations to map O11 vertical and horizontal domains to ODC apps and libraries:

* Convert vertical domains to an ODC app, as both represent a business domain and have loosely coupled properties with the same type of possible dependencies.

    ![Diagram illustrating the conversion of vertical domains to an ODC application.](images/vertical-domain-to-application-diag.png "Mapping Vertical Domains to ODC Application")

* Convert vertical domains with foundation apps consumed only in a vertical to an ODC app and one or more libraries from the foundation app(s).

    ![Diagram showing the conversion of vertical domains with foundation apps to an ODC app and libraries.](images/vertical-domain-to-library-diag.png "Mapping Vertical Domains to ODC Libraries")

* Convert horizontal domains containing shared business logic, shared technical services, and data to ODC apps.

    ![Diagram depicting the conversion of horizontal domains containing shared services to ODC apps.](images/horizontal-to-application-diag.png "Mapping Horizontal Domains to ODC Apps")

*  Convert horizontal domains with foundation apps consumed across multiple verticals to one or more ODC libraries.

    ![Diagram representing the conversion of horizontal domains with foundation apps to ODC libraries.](images/horizontal-to-library-diag.png "Mapping Horizontal Domains to ODC Libraries")
