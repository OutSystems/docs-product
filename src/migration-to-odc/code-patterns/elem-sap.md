---
guid: 4a785cf2-70c2-4085-9923-7d5ac1d1eb6f
locale: en-us
summary: Learn how to handle SAP connections after migrating from O11 to ODC.
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - frontend developers
  - mobile developers
  - full stack developers
tags: sap integration,integration platforms,outsystems developer cloud
outsystems-tools:
  - service studio
helpids: 30632
---

# Asset with SAP BAPI connection

The Business Application Programming Interface (BAPI) is a standard SAP API designed to seamlessly connect non-SAP applications with SAP business processes.

In ODC, you can use [OutSystems Data Fabric](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/integrate_with_external_data_sources_using_data_fabric/) to integrate with SAP using a SAP BAPI connector.

## How to solve

You must solve this pattern in ODC, after proceeding with the code migration to ODC.

### Solve in ODC

Recreate your SAP integration in ODC using [OutSystems Data Fabric](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/integrate_with_external_data_sources_using_data_fabric/):

1. In the ODC Portal, [create your SAP BAPI connection](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/integrate_with_external_data_sources_using_data_fabric/create_connections_to_external_data_sources/) and select the specific BAPIs relevant to your use case.

1. In ODC Studio, use Aggregates to fetch the data in your app.
