---
summary: Explore the standard toolkit for debugging and troubleshooting in OutSystems 11 (O11), featuring native tools and modern web browsers.
tags: debugging, best practices, troubleshooting, code reviews, learning and development
guid: 6419e85e-475e-4e4e-a5ee-b4d85ea5e3ac
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - ai mentor studio
coverage-type:
  - evaluate
  - apply
---

# Suggested standard toolkit

When it comes to troubleshooting and debugging, the OutSystems platform and a modern web browser like Chrome or Safari already give you a significant amount of capabilities. This is a "standard Toolkit." 

This fact alone should allow you to successfully vanquish the majority of bugs found. In this article, you can find a high-level recap of this Toolkit's capabilities.

## Before you begin

Keep in mind that "an ounce of prevention is worth a pound of cure." This means that squashing a bug is satisfying, but given the choice, working on building new features and apps is time better spent.

So, before taking a detailed look into the Tools, you can do a couple of things that go a long way to ensure you can spend more time on building new apps:

1. Spend time learning about and following recommended [Best Practices](https://success.outsystems.com/Documentation/Best_Practices) for the development of [Mobile](https://success.outsystems.com/Documentation/Best_Practices/Development/OutSystems_Mobile_Best_Practices) and [Reactive Web](https://www.outsystems.com/learn/lesson/2073/reactive-web-overview-and-best-practices) Apps. 
    
    Also, invest some more in a great Tech Talk about [developing Mobile apps](https://www.outsystems.com/learn/lesson/1737/developing-mobile-apps).

1. Make code reviews, especially code reviews with peers, a part of your standard development workflow (if you really don’t have anyone available, you can also try [explaining your code to a rubber duck](https://en.wikipedia.org/wiki/Rubber_duck_debugging). This is actually a valid techinique).

1. Leverage tools like [AI Mentor Studio](https://success.outsystems.com/Documentation/Architecture_Dashboard/Introduction_to_Architecture_Dashboard) that can perform automated analysis of your code base and flag potential issues before you deploy code beyond your development environment.

1. Test as you develop your code, whether manually ([OutSystems Now](https://success.outsystems.com/Documentation/11/Delivering_Mobile_Apps/Test_Your_Mobile_App_in_the_Device_Using_OutSystems_Now) is a nice stop-gap solution for quick testing of Mobile apps) or by investing in [testing automation](https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Testing_Guidelines).

<div class="info" markdown="1"> 

[Using OutSystems Now in iOS](https://www.outsystems.com/forums/discussion/52566/outsystems-now-app-is-out-of-apple-store/) requires a couple more steps.

</div> 

## Standard tools

The Tools that comprise the standard Toolkit are a mix between OutSystems native Tools and 3rd party Tools. Here, you can find detailed information on their capabilities.

### Service Studio debugger

The debugger included in Service Studio is an extremely powerful Tool, so you should take the time to familiarize yourself with all [its capabilities](https://success.outsystems.com/Documentation/11/Developing_an_Application/Troubleshooting_Applications/Debugging_Applications). The debugger enables you to:

* Jump from client-side code to server-side code as you step through code

* Look at the output of an Aggregate after it executes (in the ‘In Use’ tab of the Debugger panel)

* While the debugger is running

    * Make a change to your code and publish that change, then continue debugging

    * Add/remove breakpoints (incl. breakpoints in events handlers)

* Examine the values of the output parameters of a Plugin

* Debug across multiple modules (don’t forget to set the [correct entry point](https://success.outsystems.com/Documentation/11/Developing_an_Application/Troubleshooting_Applications/Debugging_Applications/Debugging_Producer_Modules)).

### OS platform logs/Service Center monitoring/LifeTime analytics

By default, the OutSystems platform generates a rich set of logs that provide detailed information related to platform operations and applications execution. Applications are also instrumented by default, and prebuilt, low-code elements are available if you want to [generate extra logging information](https://success.outsystems.com/Documentation/11/Developing_an_Application/Troubleshooting_Applications/Log_Information_in_Action_Flows).

You can examine different [types of logs](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot/View_the_Environment_Logs_and_Status) either via [Service Center or the LifeTime console](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot/View_the_Environment_Logs_and_Status). These logs provide information about many aspects of your applications, including:

* Errors logs 

* General logs

* Service Actions logs

* Integrations logs

Other logs are also generated, but tipically these are the most commonly used. 

<div class="info" markdown="1">

Note that Error and General logs include entries generated by the Native App Shell that underlines each OutSystem Mobile application, giving you some visibility into Mobile applications operations. 
Unfortunetly Mobile Apps don't generate entries in these logs when they operate in offline mode, so a different logging strategy might be required for offline applications. You can find more infomration on this in the [Extending your toolbox](extended-toolkit.md) article.

</div>

### Chrome or Safari developer tools

The last component of your standard Toolkit is your favorite modern web browser. Both [Chrome](https://developers.google.com/web/tools/chrome-devtools/) and [Safari](https://support.apple.com/guide/safari-developer/safari-developer-tools-overview-dev073038698/mac) offer powerful Developer Tools that allow you to easily perform many sophisticated troubleshooting activities.

One great benefit of the fact that Mobile and Reactive Web Apps share a good portion of their underlying technology stack is that you can run your OutSystems Mobile Apps directly in an instance of Chrome or Safari on your computer. This execution model has some limitations (For example, plugins aren't available), but it still provides a first quick and easy way to start troubleshooting a Mobile App.

## Process tip

When troubleshooting a Mobile App, it's almost always a good idea to try to run the app directly in your computer browser first. Just to see if you can reproduce the issue there, because it's simpler to investigate with the app running in the browser. 

However, keep in mind that **fixing your code and testing it in your browser only won’t suffice. Always test it in a real device, as the behavior might be different**.

In addition, the Chrome Dev Tools also allow you to inspect and debug the contents of the WebView displaying your Mobile App, while the app is running on a mobile device connected to the machine on which Chrome is running. You can find and overview of the related capabilities [here](https://success.outsystems.com/Documentation/11/Developing_an_Application/Troubleshooting_Applications/Advanced_Mobile_App_Troubleshooting_Using_Chrome).

Becoming proficient in the numerous capabilities offered by Chrome and Safari Developer Tools is a clear advantage when debugging Mobile and Reactive Web Apps.
