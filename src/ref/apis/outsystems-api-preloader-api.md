---
summary: A JavaScript API that allows you to prefetch static resources (css, js, png, gif. jpg, jpeg, woff) for a list of modules.
tags: runtime-traditionalweb; support-application_development; support-Front_end_Development; support-webapps
locale: en-us
guid: 46d68360-ea42-4078-8bc7-b8f9286e09e6
app_type: traditional web apps
---

# outsystems.api.preloader API

<div class="info" markdown="1">

Applies only to Traditional Web Apps.

</div>

A JavaScript API that allows you to prefetch static resources (css, js, png, gif. jpg, jpeg, woff) for a list of modules. This way, when the page needs a resource, it can be already in the browser's cache.

<div class="info" markdown="1">

We **don't recommend** using the outsystems.api.preloader API. It's a legacy feature superseded by the functionalities available in Mobile App and Reactive Web App.

</div>

The following files are prefetched:

* CSS styles and JavaScript code added to Web Blocks, Screens, and Themes
* Image files used in the application module
* Module resources with their 'Deploy Action' property set to 'Deploy to Target Directory', and that have the following file formats: 
    * css 
    * js    
    * gif, png, jpg, jpeg 
    * woff 
* If your module has a dependency to other modules: 
    * CSS of referenced Web Blocks and Themes
    * All referenced images

## Requirements

Include the _preloader.js file in your application. It needs to be added to the screen where you want to use the API. To do so, follow these steps:

1. Reference the [AddJavaScriptTag](<auto/httprequesthandler-api.final.md#AddJavaScriptTag>) of the [HTTPRequestHandler](<auto/httprequesthandler-api.final.md>) extension in your application. 
1. Use the 'AddJavaScriptTag' action in your application to import the `_preloader.js` file.   
Set the 'JavaScriptURL' parameter to `_preloader.js`.

## preloadApp Method

Prefetches static resources (css, js, png, gif, jpg, jpeg, woff) for a list of modules.

This way, when the page needs a resource, it can be already in the browser's cache.

### Input Parameters

`modules`
:   Array. A string array with the names of the modules from where resources are fetched.

`redirectUrl`
:   String. The URL to redirect to, after all static resources are prefetched.  
    If you pass an empty string, there is no redirection.

`locale`
:   String. Fetch resources in the language indicated by this locale code. Example: "en-US".  
    If you pass an empty string, the resources will be prefetched without any locale.

`ProgressCallback`
:   Function. Allows defining a JavaScript callback function. It is called each time a resource is loaded. Example: give visual feedback about the progress.  
    This callback function has a decimal input parameter, with the percentage of files prefetched from the server.

## Example

Users open the OrderManager app on their device by navigating to `http://example.com/OrderManager/`. When doing so, we want to prefetch the static resources of the 'CRM' and 'OrderManager' modules. This will speed up the navigation between screens, since images and scripts will be stored in the browser cache when they are needed.

While prefetching the static resources, we want to print on the console the percentage of the loaded files.

When finished, the user is redirected to the `http://example.com/OrderManager/Welcome.aspx` page.

To implement this, we add the following JavaScript code to the OrderManager default screen, where we want to prefetch the resources:

```javascript
// A list of modules to prefetch resources.
var modulesToPrefetch = ["CRM", "OrderManager"];

// The URL to redirect to after prefetching the resources.
var redirectUrl = "http://example.com/OrderManager/Home.aspx";

// The locale of the resources to fetch.
var locale = "en-US";

// The code to be executed when receiving an update about
// the progress. It prints the progress on the console.
function PreloadProgress(percentage) {
    console.log(percentage*100 + "%");
};

// Prefetches the static resources from the 'CRM' and 'OrderManager' modules.
outsystems.api.preloader.preloadApp(modulesToPrefetch, redirectUrl, locale, PreloadProgress);

// This example prints the following on the console:
// 10%
// 20%
// ...
```
