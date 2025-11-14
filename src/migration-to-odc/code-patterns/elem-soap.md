---
summary: This article provides guidelines for handling SOAP integrations before converting O11 apps to OutSystems Developer Cloud (ODC).
locale: en-us
guid: 6c7adafe-3611-4fd7-86b8-156a3828a1a1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30540
tags: api integration, rest services, soap conversion, integration platforms, outsystems developer cloud
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - backend developers
  - architects
outsystems-tools:
  - service studio
  - integration builder
coverage-type:
  - unblock
  - understand
---

# The Asset cannot contain SOAP

SOAP is an integration technology that has seen a significant reduction in its use over time. So at this point, ODC does not support SOAP (consumption or exposure).

## How to solve

If you have access to the [O11 to ODC App Conversion Kit EAP](https://www.outsystems.com/o11-odc-migration/), and want to proceed with the conversion of other ODC assets without SOAP, follow the steps in the following sections.

### SOAP Expose

Consider replacing SOAP Expose with REST Expose.

### SOAP Consume

Consider the following options:

* Use an integration platform such as Enterprise Service Bus (ESB) or an API Gateway Management that can translate between different systems. Use REST on the OutSystems side to connect to the integration platform and continue to use SOAP between the integration platform and the external system.

* In ODC, implement the SOAP Consume using [ODC custom code](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/supporting_soap_in_odc/).

Ensure the O11 modules with findings for this code pattern aren't mapped to any ODC Assets. Either move the module with SOAP Consume to an app that isn't mapped to an ODC Asset, or replace the SOAP Consume usage with a placeholder action that you can later replace in ODC.
