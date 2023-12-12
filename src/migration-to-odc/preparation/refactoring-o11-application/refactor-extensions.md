---
summary: This article guides how you can refactor extensions and extend your ODC applications with external logic.
locale: en-us
guid: d7657c47-7cd9-4bc1-a8be-54d25c20233d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: 
---

# Extend ODC apps with external logic

<div class="info" markdown="1">

If you are only preparing your code for the migration, at present, OutSystems recommends not making any changes to O11 extensions. Since, we are working to automate the conversion of O11 Custom Code to ODC Custom Code.

</div>

An [extension](../../../extensibility-and-integration/integration-studio/getting-started/extension.md) is a set of actions, structures, and entities, defined in Integration Studio, that allows integration with external systems. In ODC, you can use external logic to [extend your apps](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/) with custom C# code.  This code is run in an isolated microservice function.

You must use the external SDK libraries to port your extension code to be compatible with .NET 6.0 libraries. For detailed information on using external logic, best practices, and external logic architecture, refer to [external libraries SDK readme](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/external_libraries_sdk_reference/).

