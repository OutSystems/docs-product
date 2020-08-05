---
summary: Learn what is the right app for your project. Know the difference between web and mobile apps in OutSystems and what to choose for your needs. 
tags: support-application_development; support-devOps; support-Infrastuture_Architecture; support-Mobile_Apps; support-webapps; support-Mobile_Apps-overview; support-webapps-overview
---

# Choose the Right App for Your Project

When creating a new app, select the type of app that best fits your users' needs. Here's a quick start to help you choose a new app in the **New Application** window:

* To create an app that users run mostly in a desktop browser, select **Reactive Web App**.
* To create an app and submit it to the Apple App Store or Google Play, as a mobile app for users to download, select **Phone App** or **Tablet App**.
* To create a lightweight app and share it as a progressive web app (PWA) from your website and let users put the app icon on their mobile home screens, select **Phone App** or **Tablet App**.

![A new app window in Service Studio](images/new-app-window-ss.png?width=600)

## What's a Reactive Web App?

In OutSystems, a Reactive Web App is an app with a responsive interface that runs in the browser. The user experience is excellent across many types of devices and screen sizes. You develop with the OutSystems visual language and interact with the device hardware by extending the app logic with HTML5 and JavaScript.

Reactive Web App helps you unify development experience. Develop with a single language, and create and promote components that work across apps.

When you develop a Reactive Web App:

* You have one development paradigm for web and mobile.
* You can build apps using the client-side runtime and create responsive UX.
* Your apps run on a modern stack.

If you haven't developed OutSystems apps that focus on the client-side development paradigm, you can check the explanation about [Screen and Block lifecycle Events](<../develop/logic/screen-block-lifecycle-events.md>) and these notes about [best practices](<https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Mobile_Best_Practices>).

![Reactive App graph](images/mobile-vs-web-what-is-web.png)


<div class="info" markdown="1">

Check the blog post <a href="https://www.outsystems.com/forums/discussion/52761/reactive-web-the-next-generation-of-web-apps/">The Next Generation of Web Apps</a> to read more about Reactive Web Apps.

</div>

## What's a Mobile App?

In OutSystems, a Mobile App is an app that compiles to a native mobile Android/iOS app. The app uses Apache Cordova and wraps a web app that you develop with the OutSystems visual language. The user experience focuses on mobile and the app logic can access the device hardware, such as sensors, by using plugins. The app works offline because it caches data in the local storage. You can develop for iOS and Android at the same time, as the underlying code is cross-platform. The default app templates of this type are **Phone App** and **Tablet App**.

There are two ways you can distribute a Mobile App, as:

* **Native app package**. A dedicated OutSystems cloud service generates native mobile builds for you, to distribute your app in the app stores or internally to a group of users.

* **Progressive web app (PWA)**. PWAs are lightweight apps that have a look and feel of native mobile apps. They're quick to distribute and install directly from your website, as they don't depend on the app stores.

![Mobile and Reactive Web apps compared](images/mobile-vs-web.png)

## Comparison Between Reactive Web App and Mobile App

Here is a table with a comparison of features between Reactive Web App and Mobile App. In a default OutSystems installation, you can create a Reactive Web App by selecting **Reactive Web App** in the **New Application** window. For Mobile App choose **Phone App** or **Tablet App**.

<table border="1" cellpadding="1" cellspacing="1" markdown="1" class="mt-responsive-table" style="border:none;">
<thead>
<tr>
<th class="mt-bgcolor-ffffff" scope="col" style="border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;">
<p><span class="mt-font-size-20"><strong>Reactive Web App</strong></span></p>
<p>![](images/mobile-vs-web-web.png?width=126)</p>
</th>
<th class="mt-bgcolor-ffffff" scope="col" style="border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;"><span class="mt-font-size-20"><strong>vs</strong></span></th>
<th class="mt-bgcolor-ffffff" scope="col" style="border-bottom:1px solid #E7ECED;text-align:center;">
<p><span class="mt-font-size-20"><strong>Mobile App</strong></span></p>
<p>![](images/mobile-vs-web-mobile.png?width=126)</p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td class="mt-bgcolor-ffffff" data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-code-reusability-web.png?width=150)</p>
<p>Common logic for all devices and screen sizes.</p>
<p> </p>
</td>
<td class="mt-bgcolor-ffffff" data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;"><strong>Code Reusability</strong></td>
<td class="mt-bgcolor-ffffff" data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-code-reusability-mobile.png?width=132)</p>
<p>Common logic for all supported native mobile platforms, and supported browsers for PWAs.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-runs-in-web.png?width=239)</p>
<p>A browser.<br />
No installation is needed.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Runs in</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-runs-in-mobile.png?width=116)</p>
<p>Native mobile apps run in Android and iOS devices. PWAs run in any device with a supported browser.</p>
<p> </p>
</td>
</tr>
<tr>
<td class="mt-bgcolor-ffffff" data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-user-experience-web.png?width=240)</p>
<p>Responsive layout for all screen sizes and types.</p>
<p> </p>
</td>
<td class="mt-bgcolor-ffffff" data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;"><strong>User Experience</strong></td>
<td class="mt-bgcolor-ffffff" data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-user-experience-mobile.gif)</p>
<p>Dedicated mobile UI patterns and experiences.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-performance-web.png?width=232)</p>
<p>Performance designed for the client side, with smart mechanisms to optimize the data transfer.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Performance</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-performance-mobile.png?width=164)</p>
<p>Performance designed for the client side, with smart mechanisms to optimize the data transfer.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-access-device-web.png?width=187)</p>
<p>HTML5 supported device capabilities.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;">
<p><strong>Access to device hardware</strong></p>
</td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-access-device-mobile.png?width=172)</p>
<p>Native mobile apps access a range of device capabilities through Cordova plugins. PWAs use dedicated plugins, which by design can access only hardware that the browser running the PWA is allowed to access.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-offline-web.png?width=240)</p>
<p>No offline capabilities.*</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Offline capabilities</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-offline-mobile.png?width=180)</p>
<p>For storing offline data, native mobile apps use local storage and PWAs use browser storage.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-deployments-web.png?width=240)</p>
<p>Updates are automatic when users refresh the browser page.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Deployment and updates</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-deployments-mobile.png?width=143)</p>
<p>Native mobile apps can update automatically, and users need to install a new version only when you change the native shell. PWAs update automatically when the app detects a new version.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-distribution-web.png?width=264)</p>
<p>Share the app link of the app with users.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;background:#fff;text-align:center;vertical-align:middle;"><strong>Distribution</strong></td>
<td data-th="Mobile" style="border:none;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-distribution-mobile.png?width=265)</p>
<p>You can distribute native mobile apps in-house or through the app stores. Users can run a PWA directly from your website, and add the app icon to the device home screen. </p>
<p> </p>
</td>
</tr>
</tbody>
</table>

(*) Currently not available.

## What's a Traditional Web App?

Traditional Web App is an earlier type of OutSystems app with a focus on server-side development. You may know this app as app templates **Top Menu** or **Lisbon**.

## What's a Service?

As your app grows, you can use [Services](../develop/reuse-and-refactor/services.md) to abstract specific core concepts and expose functionality to other applications, following a service-oriented architecture.
