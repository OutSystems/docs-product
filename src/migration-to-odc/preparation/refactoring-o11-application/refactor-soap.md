---
summary: This article outlines how to adapt SOAP connections in your O11 apps for compatibility with ODC, suggesting alternatives like ODC Custom Code.
locale: en-us
guid: 6c7adafe-3611-4fd7-86b8-156a3828a1a1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Refactor SOAP to be ODC-compatible

SOAP is an integration technology that has seen a significant reduction in its use over time. so at this point, ODC does not support SOAP (consumption or exposure). Therefore, you must consider the following alternatives to connect with the external systems instead of using SOAP protocol:

* Use an integration platform such as Enterprise Service Bus (ESB) or an API Gateway Management that can translate between different systems. Use REST on the OutSystems side to connect to the integration platform and continue to use SOAP between the integration platform and the external system.

* For SOAP consumption,use [ODC custom code](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/supporting_soap_in_odc/) and replace SOAP Expose with REST Expose.
