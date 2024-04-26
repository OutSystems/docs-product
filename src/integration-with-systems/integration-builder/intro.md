---
summary: Integration Builder allows anyone to implement complex integrations between an OutSystems application and your enterprise Systems of Records like SAP or Salesforce.
locale: en-us
guid: 7d1ada04-3931-44d4-9dc1-654ed40f16f2
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/jSgZ0l0unYdVymLxKZasno/Extensibility%20and%20Integration?node-id=410:58
---

# Create connectors with Integration Builder

Integration Builder is a Software as a Service (SaaS) that allows you to implement complex integrations between an OutSystems application and your enterprise Systems of Records like SAP or Salesforce.

Allowing business to break enterprise data silos and use them across the enterprise ecosystem (cross-departmental) is fundamental in modern times, where companies want to:

* Increase departmental efficiency, by allowing data to flow seamlessly between different departments, avoiding human intervention, and reducing manual input processes, which eventually lead to data duplication and errors

* Optimize business processes, by allowing them to build complex workflows that leverage data siloed in different systems

* Increase business agility, by allowing businesses to quickly adjust IT systems based on new market trends and demand

![Screenshot of the Integration Builder login interface](images/login-ib.png "Integration Builder Login Screen")

Integration Builder removes the complexity of integrating with existing systems while allowing developers to quickly link their apps to data stored in those systems. It allows you to reduce development time and address complex integration scenarios with ease.

Integration Builder allows you to:

* Create integrations for existing systems like SAP and Salesforce using a wizard-like interface.
* Create plug-and-play integrations that you can reference in your OutSystems apps.
* Edit previously created integrations to add support to additional entities and attributes of the external system.

The generated integrations have the following features:

* Follow the OutSystems development best practices.
* Support several authentication methods out-of-the-box (depending on the target system).
* Edit in Service Studio for further customization.

Currently Integration Builder supports:

* [Salesforce integrations](connectors/integration-salesforce.md)
* [SAP OData integrations](connectors/integration-sap.md)
* [Microsoft Dataverse integrations](connectors/integration-ms-dataverse.md)
* [Microsoft Dynamics 365 integrations](connectors/integration-ms-dynamics.md)
* [SharePoint Online integration](connectors/integration-ms-sharepoint.md)
* External databases, check [Integrate with an external database using Integration Builder](../external-database/integrate-external-db-ib.md) for a list of supported databases.

## Start using Integration Builder

Check [how Integration Builder works](works.md) and [how to set up Integration Builder](set-up.md). When everything is ready, check out how to [create and use integrations](use.md).
