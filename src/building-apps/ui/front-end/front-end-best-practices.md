---
summary: Explore front-end architecture best practices and scalable design patterns in OutSystems 11 (O11).
guid: 1ee12745-d16e-4b0b-bbd5-0c1fd820cbef
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: front-end development, css best practices, scalability, style guide, architecture patterns
audience:
  - frontend developers
  - full stack developers
  - ui designers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
topic:
  - front-end-architecture
---

# Front-end architecture best practices

## Rules to build your scalable front-end architecture

* Define the HTML Layout structure without style rules, as a skeleton to start working from.
* Build without business logic. Use functional logic only.
* Avoid using animations in Javascript. Build these in CSS, so it can be easily overridden. By doing this the work of processing animations is done in the Graphics Processor Unit instead of the CPU.
* Avoid manipulating the attribute style in elements. Add classes instead, and document it. With this approach, you are not forcing things that people may not want in a particular scenario, and you avoid cleaning all the attributes by mistake.
* Avoid polluting your structure with elements just to cover a specific case. Instead, use pseudo-elements. With this approach, you keep the same structure applied in different themes, and some of them will use pseudo-elements to cover specific cases.
* Control your CSS base.
* Use Patterns.
* Define your own rules for scalability.
* Create a platform to centralize all information (aka Style Guide aka Docs).

## The 3 sacred don’ts while building a scalable pattern

The following 3 rules follow the same baseline: abstract your pattern, think in structure only,

1. Don’t add inline style in elements.

    * Don’t stick with a style forever. If you need to change it later, you need to go to the screen and deploy it again.

    * If you want to override a rule, you need to add `!important` to your rule (use `!important` just to ensure factual cases, like a disabled button - it is always disabled)

1. Don’t add classes that are objective, like color names (`.Black`), measures (`.Width20px`), styling (`.Bold`) or sizing (`.fontSize15`).

    * In the future, if those classes don’t make sense in a project, they need to be overridden. For example, imagine a class `.Bold` rule says that the font-weight is normal. This would sound strange, right?

1. Don’t put business logic in these patterns.

    * They should be clean and ready to use for every project, regardless of the business.

    * Only aggregate the functional logic if needed.
