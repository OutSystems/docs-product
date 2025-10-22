---
summary: Learn more about configuring your app settings once they've been converted to ODC
tags: app conversion, configuration management, cloud services, security, custom domains
guid: 024212bc-2069-42b6-ac89-aa024b0e9410
locale: en-us
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?m=auto&node-id=2150-444&t=HG8PieYurYat1wsj-1
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - service studio
  - portal
coverage-type:
  - apply
---

# Configure converted apps

<div class="info" markdown="1">

This article only applies to customers with access to the App Conversion Kit.

</div>

After converting your apps, you may need to configure some settings to ensure the apps work correctly.

You must have [converted your apps](execute-about-migrate-code.md).

![A diagram displaying the current state of app conversion, highlighting the 'Execute app conversion' step.](images/execute-config-migrated-apps-diag.png "Diagram of App Conversion Process")

You may need to configure the following:

* Review the [ODC app and library properties](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/libraries/edit_app_and_library_properties/). The code conversion merges multiple O11 modules into a single ODC app or library. Although most properties are inherited from the main O11 module into which the others are merged, there isn't a deterministic way to decide which O11 module's properties should take precedence in the resulting ODC app or library.

* Review the [On Application Ready](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/application_logic/on_application_ready/) and the [On Application Resume](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/application_logic/on_application_resume/) actions of your ODC apps. During the code conversion, when merging multiple O11 modules into a single ODC app, only one instance of each of these system event actions is preserved in the converted ODC app. The instance is chosen from one of the O11 modules. All other instances from the remaining O11 modules are deleted during the conversion.

* If the O11 apps used Site Properties (Settings in ODC) and Timers, configure them in Portal, refer to [Configuration management](https://success.outsystems.com/documentation/outsystems_developer_cloud/managing_outsystems_platform_and_apps/configuration_management/).

* In O11, Site Properties that are set as **secret** are converted as non-secret values. You must set these values as Settings in ODC and manually set them as Secret. To set app Configurations as secrets, refer to [Set as a secret](https://success.outsystems.com/documentation/outsystems_developer_cloud/security_of_outsystems_developer_cloud/set_as_secret/).

* To configure custom domains, refer to [Configure custom domains](https://success.outsystems.com/documentation/outsystems_developer_cloud/managing_outsystems_platform_and_apps/configure_custom_domains_for_apps/).

* Configure the access to external databases by referring to [Integrate with external data sources](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/integrate_with_external_data_sources/).

* In ODC Portal, configure the endpoint of consumed REST services across the stages.

* If your apps need to access resources that aren't publicly accessible, like private REST endpoints or private external databases, [configure the private gateways](https://success.outsystems.com/documentation/outsystems_developer_cloud/managing_outsystems_platform_and_apps/configure_a_private_gateway_to_your_network/).

* If your converted apps use emails, configure the SMTP server in Portal, refer to [Configure emails](https://success.outsystems.com/documentation/outsystems_developer_cloud/managing_outsystems_platform_and_apps/configure_emails/).

## Next steps

* Test your apps before deploying them to the QA and Production stages.
* Deploy your apps to the stages where you want to migrate data to.
* Delete any testing app data you added to the converted ODC apps.
* [Migrate data](execute-about-migrate-data.md).
