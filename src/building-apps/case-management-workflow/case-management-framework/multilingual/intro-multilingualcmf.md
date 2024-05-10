---
tags: Case Management; Case Management framework; Multilingual Case Management framework
summary: Explore the multilingual capabilities of the Case Management framework in OutSystems 11 (O11), supporting multiple languages for application development.
guid: 2e31ca9c-b4b9-4e3a-9ed3-81172a775fd4
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4376:1907
---

# Introduction to multilingual Case Management framework

Case Management framework (CMf) now includes multilingual capabilities allowing you to build OutSystems Case Management (CM) applications in different languages. 

The supported languages are:

* English
* Portuguese
* Arabic
* Japanese
* Spanish
* Italian
* Dutch
* German

## Process Overview

To build translated Case Management applications on top of the framework, first you need to create the CM app and then translate the UI content, business data, and any of the following CMf static entities in Service Studio:

* CaseDefinitionConfiguration
* CaseStatusConfiguration
* Milestones (if applicable)
* CaseActions (if applicable)

The CMf APIs return data translated to the current locale language selected at the application level. Following this, the setup timer **Bootstrap_CaseConfiguration** must be adapted to include the translations and it then needs to be executed. Finally, CMf processes the setup data and stores the translations.

A typical process flow is shown in the diagram below.

![Diagram illustrating the process flow for setting up a multilingual Case Management framework](images/cmf-mlingual-flow-diag.png "Multilingual Case Management Framework Process Flow")

The full procedure on how to [enable Multilingual CMf can be found here](enabling-multilingualcmf.md).
