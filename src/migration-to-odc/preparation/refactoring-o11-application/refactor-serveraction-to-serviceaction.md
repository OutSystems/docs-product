---
summary: This article outlines how to refactor server actions in your O11 apps to service actions for compatibility with OutSystems Developer Cloud (ODC).
locale: en-us
guid: bf0d4524-95c4-477b-9254-1e369a3f1f80
app_type: traditional web apps, mobile apps, reactive web appsc
platform-version: o11
figma: 
---

# Refactor server actions to service actions

In ODC, server actions can only be public in libraries but not in apps. Hence, you must refactor server actions on O11 apps to [service actions](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/app_architecture/service_actions/#) to avoid encountering broken references on migration. For example, in your O11 app, if there is a producer module exposing a server action and a consumer module consuming that server action action then, on migrating these modules to ODC apps, you will encounter broken references because the server actions are not public in ODC apps.

 Exposing a Service Action generates a weak dependency from the consumer to the producer module in a loosely-coupled way. Each time the implementation of an exposed service action changes, that change takes immediate effect in the consumer modules. 
 
 For large factories, you must ensure that your O11 app portfolio architecture follows a domain-driven design aligned with the to-be ODC architecture, which mandates that boundaries between domains must be loosely coupled. In such scenarios, you must refactor your O11 app to use service actions, as only weak references are allowed between ODC applications. For detailed information on using service actions and understanding best practices, refer to [use services to expose functionality](../../../develop/reuse-and-refactor/services.md).

 You must refactor your O11 app to use service actions, as only weak references are allowed between ODC applications. 
