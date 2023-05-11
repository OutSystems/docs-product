---
locale: en-us
guid: 5a57bbea-d8d7-44d5-921e-07aec6c1f705
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Download

Use the Download Tool to send a file to a user. This is an element that ends the action flow, so it is not possible to define new actions after it.

This Tool is available in Reactive Web Apps only.

<div class="info" markdown="1">

This element is processed on the client-side (browser) and it uses the browser's memory to receive the data (from the server) before it creates the file to be downloaded. This may fail depending on the size of the file and on how the browser manages its memory. For very large files (bigger than 250 MB) the likelihood of a failure increases, but the results vary significantly between browsers. The behavior of each browser is not controlled by the OutSystems Platform.

</div>

## Properties

|Name|Description|Mandatory|Default value|Observations|
|--- |--- |--- |--- |--- |
|File Content|Holds the file selected by the user.|Yes|||
|File Name|Text literal or expression with the name of the file, including the extension.|Yes|||


