---
summary: Performance Analytics for Reactive and Mobile apps explains how SPA architecture affects screen load timing, parallel requests, and sampling in O11.
tags:
  - Mobile app
  - Monitoring
  - Performance
locale: en-us
guid: a7f3c1d0-5e2b-4a6f-8b9c-2d5e7a1f3c9b
app_type: reactive web apps, mobile apps
platform-version: o11
figma:
audience:
  - Architect
  - Developer
  - Tech lead
outsystems-tools:
  - lifetime
coverage-type:
  - understand
  - apply
isautopublish: true
---

# Performance Analytics for Reactive and Mobile apps

<div class="info" markdown="1">

**Beta feature.** Behavior and UI may change before general availability. For more information, refer to [Technical Preview Features](https://success.outsystems.com/support/release_notes/technical_preview_features/).

</div>

You can monitor your Reactive and Mobile apps using performance analytics in LifeTime to understand server-side bottlenecks, client-side performance, and infrastructure impact. This allows you to compare metrics across all your app types in a single interface to identify patterns.

## What you can monitor

With performance analytics you can monitor and analyze the following:

* **Real-time performance data:** Latency and error rates for your app screens and services

* **Client-side and server-side metrics:** Track both client-side actions and server-side request performance

* **Screen loading behavior:** Understand the actual timing from screen initialization to readiness, accounting for parallel requests

* **Historical trends:** Track performance over time to detect degradation early

## How single-page architecture affects your metrics

Reactive and Mobile apps use a single-page application (SPA) architecture, which affects how performance analytics measures and interprets your app's performance:

* **Traditional page navigation:** Reactive and Mobile apps don't use traditional page navigation. Instead, screen updates happen dynamically in the browser, with performance measured from `OnInitialize` (when the screen starts loading) to `OnReady` (when the screen is ready for interaction).

* **Parallel server requests:** When a screen loads, multiple requests (such as aggregates and data actions) run simultaneously. Screen load time is determined by the longest-running request, not the sum of all requests.

* **Error rate measures server-side failures only:** Metrics only capture server-side activity, not client-side exceptions. If error rate is 0% but users report failures, your app is likely handling errors client-side.

* **Head-sampling is automatic:** Performance analytics automatically samples 20% of requests by default to maintain system performance. Sampling adjusts based on your LifeTime environment load. You can adjust the sampling rate if you need more or less data detail.

## Next steps

To start monitoring your Reactive and Mobile apps, follow [How to enable Performance Analytics for Reactive and Mobile apps](lifetime-analytics-reactive-apps-enable.md).

## Related resources

* [The APDEX Performance Score](../the-apdex-performance-score.md): Learn how OutSystems measures and interprets performance metrics.
