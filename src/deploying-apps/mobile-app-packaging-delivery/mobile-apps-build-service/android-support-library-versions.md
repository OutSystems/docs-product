---
summary: Learn about different Android support library versions, how these versions are handled by MABS and how they should be handled by customers and plugin developers.
tags: runtime-mobile
locale: en-us
guid: 8734c248-e81d-4d5b-a3a2-323a0373c188
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=313:3
---

# Android Support Library Versions for MABS

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

<div class="warning" markdown="1">

Starting with version 10, MABS no longer replaces the legacy packages from Support Library. AndroidX packages must be used instead. For more details, please check the **[release notes](https://success.outsystems.com/support/release_notes/mobile_apps_build_service_versions/mabs_10_release_notes/#breaking-changes)**.

</div>

Whenever the target Android SDK is changed for a version of MABS, the version for the support libraries reflect this change as well. This affects the core and supported mobile plugins as well as the third-party plugins available in the Forge. For instance, with MABS 5, the target Android SDK has been raised to 28.

## Scenarios of plugins using different versions of support libraries

The different scenarios of version resolution, version incompatibility and SDK incompatibility for MABS 5 are described in the following sections.

### When does version resolution take place?

Plugins that use different versions of the same library (with the exact same name) can coexist. If two plugins use `com.android.support:support-v4` but one uses version 23 and the other uses version 28, the higher version will be used.

![Flowchart illustrating the version resolution process when plugins use different versions of the same Android support library](images/android-support-library-versions-2-diag.png "Version Resolution Process")


### When does version incompatibility occur?

However, version resolution does not occur when libraries that depend on each other are used. MABS builds always reference `com.android.support:support-v4` and `com.android.support:support-annotations`. Thus, libraries associated to these must be handled carefully to ensure that the different versions match.

For instance, `com.android.support:support-core-utils` is referenced by `support-v4`. A mobile plugin that uses version 25 of this library is incompatible with the `support-v4` reference and the build fails in both MABS 4 and 5.

![Diagram illustrating version incompatibility when using support-core-utils library with different versions of support-v4](images/android-support-library-versions-3-diag.png "Version Incompatibility with Support Core Utils Library")

Another example is `com.android.support:exifinterface`, which references `support-annotations`. A mobile plugin that uses version 25 of this library is incompatible with the `support-annotations` reference and the build fails in both MABS 4 and 5.

![Diagram showing version incompatibility with exifinterface library that references different versions of support-annotations](images/android-support-library-versions-1-diag.png "Version Incompatibility with Support Annotations Library")

In both scenarios, if the version used is 26 instead of 25, the build works in MABS 4. Similarly, the build works in MABS 5 for version 28 support libraries.
It should be noted that this type of incompatibility is not unique to support libraries.

### When does SDK incompatibility occur?

The version for the support libraries cannot be higher than the target SDK. An app that is built with MABS 4 (SDK 26) cannot use plugins that make use of version 28 support libraries and any such build made will fail.

## How different kinds of plugins handle different versions of support libraries 

The following sections describe how different kinds of plugins handle the changes in MABS versions and support library versions.

### Core plugins

Core plugins are already associated with the current MABS version and thus do not require any further action. MABS 4 uses plugins that have support libraries of version 26 and MABS 5 uses plugins that have support libraries of version 28.

### Supported plugins

There are multiple versions of supported plugins that use supported libraries in Forge. The plugin versions that use version 28 support libraries cannot be used by MABS 4 or other older MABS versions due to SDK incompatibility. Plugins that target MABS 4 and older MABS versions may be used with MABS 5. 

However it is recommended to update these plugins to the newer versions. Using older versions of some plugins and newer versions of others can cause version incompatibility, especially when paired with third party plugins.

The following table provides information about the recommended versions for plugins that use support libraries.

|Plugin Name|Version for MABS 4	|Version for MABS 5|
|---|---|---|
|**Barcode Plugin**|3.0.1|4.0.0|
|**Camera Plugin**|4.0.0|5.0.0|
|**Local Notifications Plugin**|5.0.0|6.0.0|
|**OneSignal Plugin**|2.1.0|3.0.0|
|**PushWoosh Plugin**|3.1.0|4.0.0|

### Third-party plugins

Third-party plugins that use support libraries should be aligned with core and supported plugins. Follow these guidelines while creating new plugins:

* Reference `com.android.support:support-v4` directly instead of using libraries that are referenced by `com.android.support:support-v4`.

* Use version 26 if you want to target MABS 4 or version 28 if you want to target MABS 5.
