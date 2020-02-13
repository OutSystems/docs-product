---
summary: Learn what is the right app for your project. Know the difference between web and mobile apps in OutSystems and what to choose for your needs. 
tags: support-application_development; support-devOps; support-Infrastuture_Architecture; support-Mobile_Apps; support-webapps; support-Mobile_Apps-overview; support-webapps-overview
---

# Choose the Right App for Your Project

When creating a new app in OutSystems and according to your project's requirements, you need to select the type of application you want to develop. For each development scenario, different tools and features are available.

![](images/right-app-1.png?width=600)

## What is a Reactive Web App?

<div class="info" markdown="1">

Check our blog post <a href="https://www.outsystems.com/forums/discussion/52761/reactive-web-the-next-generation-of-web-apps/">The Next Generation of Web Apps</a> to read more about Reactive Web Apps!

</div>


In OutSystems, a Reactive Web App is an application with a responsive interface that runs in the browser, displaying a user experience adapted to all kinds of devices and screen sizes. It is developed using the OutSystems visual language. You can interact with the device's features and capabilities by extending the application code using HTML5 and JavaScript. You need only a browser to run it. This type of app is mostly used for displaying a high volume of data, like dashboards and tables, and it's crucial when targeting web desktops and responsive apps.

Reactive Web App is based on new Reactive Modules that helps unify development experience. Use Reactive Web App to develop with a single language, and to create and promote components that work across apps.

This means that with a Reactive Web App application:

* You have one development paradigm for web and mobile.
* You can build apps using the client-side runtime and create responsive UX.
* Your apps run on a modern stack.

If you haven't developed OutSystems apps that focus on the client-side development paradigm, you can check the explanation about [Screen and Block lifecycle Events](<../develop/logic/screen-block-lifecycle-events.md>) and these notes about [best practices](<https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Mobile_Best_Practices>).

![](images/mobile-vs-web-what-is-web.png)

## What is a Mobile App?

In OutSystems, a Mobile App is a native app shell, developed using Apache Cordova, that wraps a web app developed using the OutSystems visual language. The app has user experience that is mobile-optimized and can access the device's capabilities and features using plugins. It can work offline and have data-caching features thanks to access to the device's local storage. The developed code is cross-platform, this means that you only have to develop one project and the application works on all the supported mobile platforms (iOS and Android). You can generate application packages and distribute them in the stores or you can distribute them to a set of users.

![](images/mobile-vs-web.png)



## Comparison Between Reactive Web App and Mobile App  

<table border="1" cellpadding="1" cellspacing="1" markdown="1" class="mt-responsive-table" style="border:none;">
<thead>
<tr>
<th class="mt-bgcolor-ffffff" scope="col" style="border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;">
<p><span class="mt-font-size-20"><strong>Reactive Web</strong></span></p>
<p>![](images/mobile-vs-web-web.png?width=126)</p>
</th>
<th class="mt-bgcolor-ffffff" scope="col" style="border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;"><span class="mt-font-size-20"><strong>vs</strong></span></th>
<th class="mt-bgcolor-ffffff" scope="col" style="border-bottom:1px solid #E7ECED;text-align:center;">
<p><span class="mt-font-size-20"><strong>Mobile</strong></span></p>
<p>![](images/mobile-vs-web-mobile.png?width=126)</p>
</th>
</tr>
</thead>
<tbody>
<tr>
<td class="mt-bgcolor-ffffff" data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-code-reusability-web.png?width=150)</p>
<p>One codebase for all devices and screen sizes.</p>
<p> </p>
</td>
<td class="mt-bgcolor-ffffff" data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;vertical-align:middle;"><strong>Code Reusability</strong></td>
<td class="mt-bgcolor-ffffff" data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-code-reusability-mobile.png?width=132)</p>
<p>One codebase for all supported mobile platforms.</p>
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
<p>Mobile devices. Needs to be installed and is not supported in the browser.</p>
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
<p>Dedicated mobile UI patterns and experiences, such as animations and screen transitions.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-performance-web.png?width=232)</p>
<p>Performance optimized for the client side. App logic can run on the device and the data exchange with the server is reduced.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Performance</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-performance-mobile.png?width=164)</p>
<p>Performance optimized for the client side. App logic can run on the device and the data exchange with the server is reduced.</p>
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
<p><strong>Access to Device <span style="line-height:inherit;">Capabilities</span></strong></p>
</td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-access-device-mobile.png?width=172)</p>
<p>Access to full range of device capabilities (using Cordova plugins).</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-offline-web.png?width=240)</p>
<p>No offline capabilities*</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Offline capabilities</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-offline-mobile.png?width=180)</p>
<p>Using local storage for storing offline data. Client logic running on the device.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-deployments-web.png?width=240)</p>
<p>Automatic update on browser page refresh.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;vertical-align:middle;"><strong>Deployments/Updates</strong></td>
<td data-th="Mobile" style="border:none;border-bottom:1px solid #E7ECED;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-deployments-mobile.png?width=143)</p>
<p>Most updates are made automatically on screen change. New installation required only when changing the native shell.</p>
<p> </p>
</td>
</tr>
<tr>
<td data-th="Web" style="border:none;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-distribution-web.png?width=264)</p>
<p>Share the app’s link with users.</p>
<p> </p>
</td>
<td data-th="vs" style="border:none;background:#fff;text-align:center;vertical-align:middle;"><strong>Distribution</strong></td>
<td data-th="Mobile" style="border:none;background:#fff;text-align:center;">
<p> </p>
<p>![](images/mobile-vs-web-distribution-mobile.png?width=265)</p>
<p>In-House or via Mobile app stores.</p>
<p> </p>
</td>
</tr>
</tbody>
</table>

(*) Currently not available.

## What is Traditional Web?

Traditional Web is an earlier type of OutSystems app that is focused on the server-side development. You may know this app under names such as Top Menu or Lisbon.

## What is a Service?

As your application grows, you can use [Services](../develop/reuse-and-refactor/services.md) to abstract specific core concepts and expose functionality to other applications, following a service-oriented architecture.
