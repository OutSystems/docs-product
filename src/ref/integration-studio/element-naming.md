---
locale: en-us
guid: 17d3cb2c-81bd-4784-aacf-7c382295c1a0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
summary: OutSystems 11 (O11) Integration Studio enforces naming conventions and character limits for elements.
tags: ide usage, reactive web apps, tutorials for beginners, integration studio, naming conventions, database compatibility
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - integration studio
coverage-type:
  - remember
---

# Naming Elements in Integration Studio

An **element name** is a sequence of characters [Aa-Zz], numbers, and/or the character "\_"; spaces are not allowed. The name of the element must start with a character [Aa-Zz]. Any character that is not allowed, for example "space" or "ç", is automatically translated, by Integration Studio, to "\_".

The maximum number of characters allowed depends on the element you are handling:

* **Entity attribute name**: 28 characters.

    ![Warning icon indicating a message about reserved words in Oracle databases](images/warning-icon.png "Integration Studio Warning") If you are using an Oracle database, there are some reserved words that cannot be used as attribute names: `timestamp`, `number`, `blob`, `clob` and `varchar2`. Integration Studio presents a warning message notifying you that the attribute name must be changed.

* **Any other element**: 50 characters.

If the name is bigger than the maximum allowed, Integration Studio presents an error message and you must follow these limits in order to proceed.
