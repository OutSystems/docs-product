---
summary: Use Download Tool in a Flow to send file to the browser, so the users can download the file through the browser built-in download feature.
tags: support-application_development; runtime-traditionalwebandreactiveweb;
locale: en-us
guid: c434b127-7855-4ec0-9c5d-e484eff41e63
app_type: traditional web apps, reactive web apps
---

# Download a file through browser

<div class="info" markdown="1">

Applies only to Traditional Web Apps and Reactive Web Apps.

</div>

You can send binary content to the browser, which makes the browser initiate the download. In some browsers or devices the download may begin immediately, while some first open a save dialog.

To send the file to the browser, use the **Download Tool**, and pass it the values for:

* **File Content** - the binary content of the file
* **File Name** - the name of the file that will be downloaded

For example, you can create a **DownloadImageOnClick** action that takes the image binary and file name as the input parameters, and then pass those parameters to the Download Tool at the end of the Flow:

![Adding link](<images/download-binary-example.png?width=600>)
