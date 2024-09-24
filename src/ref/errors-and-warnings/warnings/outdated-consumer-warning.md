---
locale: en-us
guid: 00c4300a-4dd9-4770-a540-ddec24bc8d79
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Outdated Consumer Info

<a id="helpid-30181"></a>

Message
:   `Consumer module '<module>' is outdated.`

Cause
:   You changed a module that exposes functionality used by other module (consumer). The changes you performed are compatible with the consumer, but the consumer is now running an outdated version of your module. This situation applies only to [strong dependencies](../../../building-apps/reuse-and-refactor/strong-weak-dependencies.md#strong-dependencies). For [weak dependencies](../../../building-apps/reuse-and-refactor/strong-weak-dependencies.md#weak-dependencies), changes in the producer implementation take immediate effect in the consumer.

Recommendation
:   To start using the latest implementation of your producer module, the consumer module must be republished, otherwise the consumer will keep using the previous version. The consumer has no need to refresh the producer dependencies.

