---
guid: 8e949f41-0b7b-48ac-aebb-e4691e2cc790
locale: en-us
summary: Solve the O11 to ODC code conversion warning that reports a producer asset missing elements that a consumer asset uses.
figma:
coverage-type:
  - unblock
topic:
  - troubleshoot-code-conversion
app_type: mobile apps, reactive web apps, traditional web apps
platform-version: o11
audience:
  - Developer
  - Platform administrator
tags:
  - Libraries
  - Troubleshooting
outsystems-tools:
  - odc portal
  - odc studio
helpids: 30810
isautopublish: true
---

# Missing elements in converted producer assets

When a code conversion ends with the **Finished with warnings** status and the conversion log reports that a producer is missing elements used by a consumer, the conversion couldn't update the consumer's dependency on that producer. This page explains why the warning occurs and how to solve it.

The warning in the conversion log reads "[Producer] is missing elements used by [Consumer]", where the bracketed values are the names of the producer and consumer assets.

## What happens during the conversion

During code conversion, the tool updates the dependencies of each consumer asset so that they point to the ODC asset that now provides the elements of the O11 producer module. If the ODC producer doesn't contain an element that the consumer uses, the dependency update for that consumer fails.

The conversion still generates the consumer, and you can download it. However, the conversion doesn't update the consumer's dependency on the producer. None of the consumer's references to that producer are updated, not only the references to the missing elements. When you open the consumer in ODC Studio, these references appear as TrueChange errors.

## When the warning occurs

The warning typically occurs in the following scenarios:

* **The producer evolved in O11 after its conversion.** You converted and published the producer, then developers added elements to the O11 producer module. Consumers that use those elements fail the dependency update when you convert them.

* **The producer changed in ODC.** Developers changed the converted producer in ODC, so it no longer has all the elements of the O11 producer module. Consumers that use the missing elements fail the dependency update when you convert them.

* **The producer was converted in a mode that removes elements.** You converted the producer in the **Data and logic** or **Data** mode, which don't convert all the elements of the O11 producer module. A consumer gets the warning only if it still uses the removed elements after its own conversion. For example, a producer converted in the **Data** mode has no service actions. A consumer that uses one of those service actions only in a screen gets the warning in the **Full** mode. In the **Data and logic** or **Data** mode, the conversion removes the consumer's screens, so no warning occurs. For more information, refer to [Choose a conversion mode](../plan/plan-map-in-tool.md#choose-a-conversion-mode).

## Solve the warning

The dependency update of the consumer succeeds only if the published ODC producer contains all the elements that the consumer uses. To solve the warning, bring the missing elements from the O11 producer module into the published producer, and then convert the consumer again.

To do this, follow these steps:

1. In the ODC Portal, open the conversion plan that includes the producer and click **Convert code**.

1. Download the converted producer and open it in ODC Studio.

1. Merge the missing elements into the published revision of the producer.

1. Publish a new revision of the producer.

1. Open the conversion plan that includes the consumer and click **Convert code**.

For more information about converting code, refer to [Code conversion using the tool](execute-how-to-migrate-code.md#code-conversion).

These steps work only if the conversion mode of the producer converts the missing elements. A producer converted in the **Data and logic** or **Data** mode doesn't receive the elements that its mode removes.
