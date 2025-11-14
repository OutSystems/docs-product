---
guid: 279b1c31-1194-4d52-920e-6a950ed056f3
locale: en-us
summary: Learn more about handling the URLs of consumed REST API endpoints after converting to ODC.
figma: https://www.figma.com/design/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?m=auto&node-id=2861-240&t=sgPICOBjMsyBDjny-1
coverage-type:
  - unblock
topic:
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - backend developers
  - full stack developers
  - tech leads
tags: rest api, url handling, code conversion, odc, backend development
outsystems-tools:
  - service studio
  - odc studio
helpids:
---

# Update the URLs of consumed REST API endpoints

When converting simultaneously O11 modules that expose and consume REST API endpoints between themselves, the URL of the exposed endpoint automatically updates to reflect the converted asset's name. However, the Base URL of the consumed endpoint and the URL Path of consumed methods aren't automatically updated to reflect the name change in the converted assets.

![Screenshot of the properties of a consumed REST API in ODC Studio](images/rest-consume-odcs.png "Properties of a consumed REST API in ODC Studio")

<div class="info" markdown="1">

This behavior applies both to modules of the same app and modules of different apps that are converted to ODC at the same time.

</div>

## How to solve

You must solve this in ODC after proceeding with the code conversion.

### Solve in ODC

After converting your assets to ODC, check the properties of the consumed REST API and its methods in ODC Studio:

1. Update the **Base URL** of the consumed REST API to reflect the exposed REST API after conversion.

    ![Screenshot of the properties of a consumed REST API in ODC Studio](images/rest-consume-url-odcs.png "Properties of a consumed REST API in ODC Studio")

    Note that the Base URL you define in ODC Studio is the default URL. To learn how to define the actual Base URL for each stage, refer to [Configure API base URL and basic authentication](https://success.outsystems.com/documentation/outsystems_developer_cloud/integration_with_external_systems/use_rest_apis_in_your_app/consume_one_or_more_rest_api_methods/#configure-api-base-url-and-basic-authentication).

1. For each consumed method, update also the **URL Path** to reflect that change.

    ![Screenshot of the properties of a GET method in ODC Studio](images/rest-method-url-odcs.png "Properties of a GET method in ODC Studio")

<div class="info" markdown="1">

In ODC, the best practice is to use an ODC library to implement the communication with the REST API and then consume that library instead. Library encapsulation facilitates reusing the REST integration in multiple ODC apps and allows version management.

</div>
