---
summary: Explore best practices for building mobile apps with multiple independent teams using OutSystems 11 (O11).
tags: mobile app development, mobile architecture, team collaboration, native plugins, offline support
guid: eeb1ecc6-8b4e-4c29-8f20-9c811cb1a65b
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
topic:
  - scale-development-strategy
---

# Building mobile apps with multiple independent teams

This series of articles helps you on providing guidelines and best practices on how you can leverage the power of having multiple independent development teams working on the same mobile apps, avoiding common mistakes and maximizing their productivity.

## What’s the challenge?

As you know by now, there are several differences between developing a traditional web and a mobile application in OutSystems. 

First of all, the mobile application lifecycle is completely different. There is no preparation, but there are several events to fetch data or initialize variables. The mobile application has local storage to speed up common operations or to support offline navigation, which is an additional aspect to take into consideration.

There are also several plugins to interact with device native capabilities as well as other user-developed functionalities.

It has a dedicated JavaScript node that allows you not only to run any snippet you create, but also to use input and output parameters to send or receive information related with the code snippet.

Several dedicated widgets are exclusive to the mobile version and were optimized for mobile usage.

Also, the architecture of such applications must also be approached in a very different level. 

Having to deal with all this while having different teams developing, it's huge. That's why we recommend you to understand about:

* [Architecture best practices](bp-architecture.md)
* [Development best practices](bp-development.md)
* [Best practices with multiple teams](bp-multiple.md)

Besides this section we recommend checking the following resources:

* [Mobile Tech Talks](https://learn.outsystems.com/training/journeys/odc-2018-mobile-551)

* [Mobile Architecture Tech Talk](https://learn.outsystems.com/training/journeys/odc-2018-architecture-547/-odc-2018-mobile-architecture/o11/2474)

* [Mobile Application Architecture Training](https://learn.outsystems.com/training/journeys/mobile-app-architecture-411)

