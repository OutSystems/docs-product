---
summary: Explore app development options in OutSystems 11 (O11) for various platforms, including Reactive Web Apps and Mobile Apps, to suit different project needs.
tags: support-application_development; support-Mobile_Apps-overview; support-webapps-overview
locale: en-us
guid: 1945689d-cfc3-497f-b313-a8cf051a18d9
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/mDMvfanpcaW6fqmEKxjvMQ/Getting%20Started?node-id=1:89
---

# Choose the right app for your project

You can create several types of apps in OutSystems. Here's an overview to help you choose a new app in the **New Application** window:

* To create an app that users run mostly in a desktop browser, select **Reactive Web App**.
* To create an app and submit it to the Apple App Store or Google Play, as a mobile app for users to download, select **Phone App** or **Tablet App**.
* To create a lightweight app and share it as a progressive web app (PWA) from your website and let users put the app icon on their mobile home screens, select **Phone App** or **Tablet App**.

<iframe src="https://player.vimeo.com/video/977630610" width="750" height="601" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="">Video showing the process of selecting an app type in the New Application window of OutSystems</iframe>

## What's a Reactive Web App?

In OutSystems, a Reactive Web App is an app with a responsive interface that runs in the browser. The user experience is excellent across many types of devices and screen sizes. You develop with the OutSystems visual language and interact with the device hardware by extending the app logic with HTML5 and JavaScript.

Reactive Web App helps you unify development experience. Develop with a single language, and create and promote components that work across apps.

When you develop a Reactive Web App:

* You have one development paradigm for web and mobile.
* You can build apps using the client-side runtime and create responsive UX.
* Your apps run on a modern stack.

If you haven't developed OutSystems apps that focus on the client-side development paradigm, you can check the explanation about [Screen and Block lifecycle Events](<../building-apps/logic/screen-block-lifecycle-events.md>) and these notes about [best practices](https://success.outsystems.com/documentation/best_practices/development/outsystems_mobile_best_practices/).

![Diagram illustrating the concept of a Reactive Web App in OutSystems](images/reactive-web-app-diag.png "Reactive Web App Diagram")

![Diagram highlighting the characteristics of a Reactive Web App in OutSystems](images/reactive-web-app-characteristics-diag.png "Reactive Web App Characteristics")

<div class="info" markdown="1">

Check the blog post <a href="https://www.outsystems.com/forums/discussion/52761/reactive-web-the-next-generation-of-web-apps/">The Next Generation of Web Apps</a> to read more about Reactive Web Apps.

</div>

## What's a Mobile App?

In OutSystems, a Mobile App is an app that compiles to a native mobile Android/iOS app. The app uses Apache Cordova and wraps a web app that you develop with the OutSystems visual language. The user experience focuses on mobile and the app logic can access the device hardware, such as sensors, by using plugins. The app works offline because it caches data in the local storage. You can develop for iOS and Android at the same time, as the underlying code is cross-platform. The default app templates of this type are **Phone App** and **Tablet App**.

There are two ways you can distribute a Mobile App, as:

* **Native app package**. A dedicated OutSystems cloud service generates native mobile builds for you, to distribute your app in the app stores or internally to a group of users.

* **Progressive web app (PWA)**. PWAs are lightweight apps that have a look and feel of native mobile apps. They're quick to distribute and install directly from your website, as they don't depend on the app stores.

![Diagram comparing mobile apps and web apps in OutSystems](images/mobile-vs-web-diag.png "Mobile vs Web App Diagram")

## Comparison Between Reactive Web App and Mobile App

Here is a table with a comparison of features between Reactive Web App and Mobile App. In a default OutSystems installation, you can create a Reactive Web App by selecting **Reactive Web App** in the **New Application** window. For Mobile App choose **Phone App** or **Tablet App**.

|**Reactive Web App** <br/><br/>![Diagram showing features of Reactive Web App in OutSystems](images/mobile-vs-web-web-diag.png "Reactive Web App Features")|vs|**Mobile App**<br/><br/>![Diagram showing features of Mobile App in OutSystems](images/mobile-vs-web-mobile-diag.png "Mobile App Features")|
|:-:|:-:|:-:|
|![Diagram depicting code reusability for all devices and screen sizes in Reactive Web App](images/mobile-vs-web-code-reusability-web-diag.png "Code Reusability in Reactive Web App")<br/>Common logic for all devices and screen sizes.|**Code Reusability**|![Diagram depicting code reusability for all supported native mobile platforms in Mobile App](images/mobile-vs-web-code-reusability-mobile-diag.png "Code Reusability in Mobile App")<br/>Common logic for all supported native mobile platforms, and supported browsers for PWAs.|
|![Diagram showing that Reactive Web App runs in a browser without installation](images/mobile-vs-web-runs-in-web-diag.png "Reactive Web App Runtime Environment")<br/>A browser.<br/>No installation is needed.|**Runs in**|![Diagram showing that Mobile App runs in Android and iOS devices and as PWAs in supported browsers](images/mobile-vs-web-runs-in-mobile-diag.png "Mobile App Runtime Environment")<br/>Native mobile apps run in Android and iOS devices. PWAs run in any device with a supported browser.|
|![Diagram illustrating the responsive layout for all screen sizes and types in Reactive Web App](images/mobile-vs-web-user-experience-web-diag.png "User Experience in Reactive Web App")<br/>Responsive layout for all screen sizes and types.|**User Experience**|![Diagram illustrating dedicated mobile UI patterns and experiences in Mobile App](images/mobile-vs-web-user-experience-mobile-diag.png "User Experience in Mobile App")<br/>Dedicated mobile UI patterns and experiences.|
|![Diagram showing performance design for the client side with optimization mechanisms in Reactive Web App](images/mobile-vs-web-performance-web-diag.png "Performance in Reactive Web App")<br/>Performance designed for the client side, with smart mechanisms to optimize the data transfer.|**Performance**|![Diagram showing performance design for the client side with optimization mechanisms in Mobile App](images/mobile-vs-web-performance-mobile-diag.png "Performance in Mobile App")<br/>Performance designed for the client side, with smart mechanisms to optimize the data transfer.|
|![Diagram indicating HTML5 supported device capabilities in Reactive Web App](images/mobile-vs-web-access-device-web-diag.png "Device Hardware Access in Reactive Web App")<br/>HTML5 supported device capabilities.|**Access to device hardware**|![Diagram showing that native mobile apps access a range of device capabilities through Cordova plugins](images/mobile-vs-web-access-device-mobile-diag.png "Device Hardware Access in Mobile App")<br/>Native mobile apps access a range of device capabilities through Cordova plugins. PWAs use dedicated plugins, which by design can access only hardware that the browser running the PWA is allowed to access.|
|![Diagram stating no offline capabilities for Reactive Web App](images/mobile-vs-web-offline-web-diag.png "Offline Capabilities in Reactive Web App")<br/>No offline capabilities.*|**Offline capabilities**|![Diagram showing offline data storage using local storage for native mobile apps and browser storage for PWAs](images/mobile-vs-web-offline-mobile-diag.png "Offline Capabilities in Mobile App")<br/>For storing offline data, native mobile apps use local storage and PWAs use browser storage.|
|![Diagram explaining that updates in Reactive Web App are automatic when users refresh the browser page](images/mobile-vs-web-deployments-web-diag.png "Deployment and Updates in Reactive Web App")<br/>Updates are automatic when users refresh the browser page.|**Deployment and updates**|![Diagram explaining that native mobile apps can update automatically and PWAs update when a new version is detected](images/mobile-vs-web-deployments-mobile-diag.png "Deployment and Updates in Mobile App")<br/>Native mobile apps can update automatically, and users need to install a new version only when you change the native shell. PWAs update automatically when the app detects a new version.|
|![Diagram showing that Reactive Web App can be shared via a link with users](images/mobile-vs-web-distribution-web-diag.png "Distribution of Reactive Web App")<br/>Share the app link with users.|**Distribution**|![Diagram showing distribution options for native mobile apps and PWAs](images/mobile-vs-web-distribution-mobile-diag.png "Distribution of Mobile App") ![Diagram showing that Reactive Web App can be shared via a link with users](images/mobile-vs-web-distribution-web-diag.png "Distribution of Reactive Web App")<br/>You can distribute native mobile apps in-house or through the app stores. Users can run a PWA directly from your website, and add the app icon to the device home screen.|

(*) Currently not available.

## What's a Traditional Web App?

Traditional Web App is an earlier type of OutSystems app with a focus on server-side development. You may know this app as app templates **Top Menu** or **Lisbon**.

## What's a Service?

As your app grows, you can use [Services](../building-apps/reuse-and-refactor/services.md) to abstract specific core concepts and expose functionality to other applications, following a service-oriented architecture.
