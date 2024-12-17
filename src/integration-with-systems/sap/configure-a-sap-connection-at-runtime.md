---
summary: OutSystems 11 (O11) allows dynamic configuration of SAP connections at runtime to adapt to different environments without republishing modules.
tags: sap integration, environment configuration, dynamic configuration, service center, runtime configuration
locale: en-us
guid: ef8e199e-6f48-4a7a-8084-6e0cd1d5a532
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - backend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - service center
coverage-type:
  - apply
---

# Configure a SAP Connection at Runtime

When developing an application integrated with SAP, you define a default connection. However, you can configure specific connections to SAP in different environments, which override the default connection. This allows your application to use specific SAP systems in certain environments, without having to change or republish the module.

The steps to configure a SAP connection in an environment at runtime are the following:

1. Go to the management console of your OutSystems environment (Service Center). 
1. Go to Factory section and open your application. 
1. Open the module containing your SAP integration. 
1. Select the Integrations tab and click on the SAP connection name to edit it. 
1. Configure the SAP connection to point to the SAP system you want. 
1. Click Apply. 

Your SAP integration will start using the SAP connection you have just configured.
