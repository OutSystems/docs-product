---
summary: Learn how to test and fix accessibility issues on your OutSystems Reactive Web applications.
tags: runtime-reactiveweb
locale: en-us
guid: 4d847458-cdd8-40ec-848a-aa9af7e1d2ea
app_type: reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=186:22
---

# Testing and fixing accessibility issues

During the development of an accessible application, OutSystems recommends you to test for accessibility issues and fix them early. This sections shows a quick example of using the [WAVE accessibility evaluation tool](https://wave.webaim.org/), identifying issues, and addressing them in Service Studio. WAVE shows issues as visual markers on the page, which lets you focus on the low-code approach of the app development. You can also audit your apps with Lighthouse, integrated in the Chrome DevTools.

## Build a page

In Service Studio create a screen, publish the app, and open it in your browser. Here is an example of a simple screen with a title and an image.

![Example of a simple OutSystems Service Studio screen with a title and an image](images/a-sample-page-ss.png "Sample OutSystems Service Studio Screen")

## Test for accessibility

To test your page for accessibility, do the following steps:

1. Load the page.
1. Click on the WAVE extension (1) to start testing.
    The existing issues show on top of the page elements.
1. Click an error marker (2) to open a pop-up box with the notes. In this example, a page title is missing.
1. Click the reference link (3) to see which success criteria the issue affects. In this example it's the "2.4.2 Page Titled" rule, which is the Level A success criteria (4).

![WAVE tool showing accessibility issues on a web page with error markers and pop-up notes](images/test-for-accessibility.png "Testing for Accessibility with WAVE Tool")

There are other issues with this page. There is no heading, and the image is missing the alternative text.

<div class="info" markdown="1">

The accessibility analysis shows page structural elements and ARIA annotation. These elements and annotations come from the OutSystems UI by default.

</div>

## Fix the accessibility issues

To fix all the issues from this example, follow the instructions in the [Basic accessibility settings](https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Accessibility#Basic_accessibility_settings) section. After some quick edits, the page now has a title, the language definition, and the image has an alt text. If you check the page again, the report shows zero errors.

![Web page with fixed accessibility issues, including a page title, language definition, and alt text for an image](images/fixing-accessibility-issues.png "Fixed Accessibility Issues on a Web Page")
