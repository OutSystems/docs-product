---
summary: 
locale: en-us
guid: d7657c47-7cd9-4bc1-a8be-54d25c20233d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30537
---
# Asset consuming an extension

An [Extension](../../integration-with-systems/integration-studio/getting-started/extension.md) is a set of actions, structures, and entities, defined in Integration Studio, that allows integration with external systems and the usage of custom C# code.

<div class="info" markdown="1">

If you are only preparing your code for the migration, at present, OutSystems recommends not making any changes to O11 extensions. OutSystems is working on automating the conversion of O11 Custom Code to ODC Custom Code.

For Extensions with external database connections, in order to take full benefit of ODC data fabric it's highly recommended that all external database connections are reviewed.

For Extensions with Custom C# code, ODC custom code runs under different premises than O11 custom code, and we highly recommend that a deeper analysis is done to ensure that the code run as expected in ODC

</div>

## How to solve

You must solve this pattern in ODC, after proceeding with the code migration to ODC.

### Solve in ODC

<div class="info" markdown="1">

If you are only preparing your code for the migration, at present, OutSystems recommends not making any changes to O11 extensions. OutSystems is working on automating the conversion of O11 Extensions to ODC custom code or external data connections.

</div>

If you want to manually implement your Extension's functionality in ODC, solve this pattern in one of the following ways:

* If you Extension connects to an [external data source that's supported in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/integrate_with_external_data_sources/#supported-systems), create the [integration with external data sources in ODC](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/integrate_with_external_data_sources/).

* If you Extension extends your apps with custom C# code, create and release an ODC Library that [extend your apps with external logic using custom code](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/). You must use the external SDK libraries to port your extension code to be [compatible with .NET 8.0 libraries](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_readme/#prerequisites).
