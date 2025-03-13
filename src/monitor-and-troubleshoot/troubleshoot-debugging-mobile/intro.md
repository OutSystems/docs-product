---
summary: Explore debugging and troubleshooting for mobile and reactive web apps using OutSystems 11's integrated tools and extensive documentation.
tags: debugging, troubleshooting, application logs, developer tools, documentation
guid: 3ccd01d8-e072-4219-8547-cb105941bfca
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
  - service center
coverage-type:
  - evaluate
  - apply
---

# Debugging and troubleshooting mobile and reactive web apps

OutSystems provides rich capabilities to develop Mobile Applications and Reactive Web applications. These two application types each have a few unique characteristics, but they also share a common modern technology stack and development model. 

Applications consist on a combination of client-side code and server-side code, which are both key to a great user experience, but can also make investigating and correcting unexpected behavior a bit more involved in certain scenarios.

The OutSystems platform comes with a very powerful debugger (integrated with Service Studio) and detailed, configurable built-in logging right out of the box. Application logs are accessible via the monitoring section of Service Center. 

These Tools, combined with the Developer Tools offered by modern browsers like Chrome and Safari, provide an excellent starting point for applications troubleshooting and debugging. 

Ample documentation on how to take advantage of this Toolset is available in the [Troubleshooting Applications](https://success.outsystems.com/Documentation/11/Developing_an_Application/Troubleshooting_Applications) and [Monitor and Troubleshoot](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot) (Note that the monitoring capabilities of LifeTime **aren't available** for Reactive and Mobile Apps) sections of the [public platform documentation](https://success.outsystems.com/Documentation/11/New_in_OutSystems_11).

Beyond this standard Toolkit, there's the possibility to add additional Tools into the mix to address more complex analysis needs. This section describes some of these Tools and related advanced troubleshooting and debugging techniques.

This section's articles address the following topics:

* [A general discussion of the troubleshooting and debugging **process**.](troubleshooting-process.md)

* [A quick refresher on the main capabilities of the standard troubleshooting and debugging **Toolkit**](standard-toolkit.md) 
    (For example: Service Studio and its integrated debugger + Service Center logs & reports + Chrome / Safari Developer Tools).

* [A list of **additional Tools** that can help you when the standard Toolkit isn't enough.](extended-toolkit.md)

* [Some common **examples** of how to use these additional Tools in certain scenarios.](debug-examples.md)

Also, along the way, learn how the similarities of Mobile and Reactive Web applications allows you to share most of tools and techniques, and where differences between the two may require an application type-specific approach.
