---
guid: b3984bcd-0e7f-4b53-8238-83823091dbfc
locale: en-us
summary: Learn how to unblock the O11 to ODC conversion of an app consuming a REST API using multipart request format.
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: mobile apps, reactive web apps
platform-version: o11
audience:
  - full stack developers
tags: rest api, rest consume, outsystems conversion, odc conversion
outsystems-tools:
  - conversion assessment tool
helpids: "30690"
---

# Asset consuming REST API with multipart request

Currently, ODC doesn't support consuming REST APIs with a multipart/form-data request format. If your ODC asset is mapped to O11 apps that [consume a REST API with a multipart or form data method](../../integration-with-systems/rest/consume-rest-apis/consume-multipart-form-data.md), you can't proceed with the conversion of that asset.

## How to solve

If you want to convert the ODC asset, you must delete this pattern in O11 before proceeding with the code conversion to ODC.

### Solve in O11

To proceed with the conversion of the ODC asset, remove the consumed REST API call that uses a multipart request from your O11 app.

If you want to keep the same REST integration after converting your app to ODC, implement an alternative way to consume the REST API. ODC doesn't yet support the multipart/form-data request format.

<div class="info" markdown="1">

In ODC, you can create the body of a multipart/form-data message using the Forge components [Multipart/form-data (ODC)](https://www.outsystems.com/forge/component-overview/16944/multipart-form-data-odc) and [MultipartFormDataParser (ODC)](https://www.outsystems.com/forge/component-overview/16945/multipartformdataparser-odc). Please note that these components are not supported by OutSystems.

</div>
