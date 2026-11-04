---
summary: AppShield plugin for OutSystems 11 (O11) protects Android and iOS apps with runtime checks, obfuscation, configuration, and certificate whitelisting.
tags:
  - Android
  - Forge
  - iOS
  - Lifecycle
  - Mobile app
  - Plugins
  - Security
locale: en-us
guid: bacbf600-bd10-4caf-820a-205c16a58691
topic:
  - appshield-hardening
app_type: mobile apps
platform-version: o11
figma: https://www.figma.com/file/RizSdkiVSDYFb97Vqvc7oj/Delivering%20Mobile%20Apps?node-id=313:21
audience:
  - Developer
  - Platform administrator
outsystems-tools:
  - forge
coverage-type:
  - understand
  - apply
  - remember
isautopublish: true
---

# Harden the protection of mobile apps with AppShield

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

**OutSystems AppShield** is a licensed plugin available from the **Forge**. **AppShield** lets you harden the protection of your native Android and iOS apps. **AppShield** integrates with the Mobile Apps Build Service (MABS version 6.3 or later) and adds app protection at runtime and rest.

<div class="info" markdown="1">

To use **OutSystems AppShield**, you must have a license. If you don't already have a license, contact the sales team.

</div>

**AppShield** prevents code injection, screenshots of app data, and data hijacking.

When the user launches a hardened app, the app performs multiple checks, including root and repackaging detection. These checks increase the app launch time, especially the first time the app starts. The start time varies depending on multiple factors, such as device hardware and app complexity.

To ensure your app users have protection against the latest security vulnerabilities, **OutSystems** provides continuous updates to **AppShield**.

## Understanding the AppShield life cycle

Before you install and use **AppShield**, it's important to understand the release cycle and how it improves security. For example, suppose you have a mobile banking application and your app data must always be secure, but your version of **AppShield** isn't current. OutSystems regularly updates **AppShield** and strongly recommends that you always install the latest version of **AppShield** in your environment. Then release a new build of your app to your users.

To identify the **AppShield** plugin releases, OutSystems uses the following tags:

* Stable
* Current
* Expiring
* Discontinued

The following list describes the tags:

* **Stable and Current** - This is the active version and has up-to-date protection. OutSystems **supports** this version and highly recommends that you install and use this version.
* **Stable** - You can use this version, but the protection isn't current. OutSystems **doesn't support** this version. You can build an app, but you get a warning message when you try to build the app.
* **Stable and Expiring** - This version becomes discontinued in three months. OutSystems **doesn't support** this version, but you can build an app with it. If you use this version, a warning message displays advising you to update to the most current version before the expiration date. Once this version is **discontinued**, you won't be able to build your app with it.
* **Discontinued** - This plugin version is out of date. OutSystems security mechanisms prevent you from creating a new build for your users. OutSystems **doesn't support** this version.

The following diagram shows how release versions work in **AppShield**.

![Diagram illustrating the release life cycle of the AppShield plugin with various version tags such as Stable, Current, Expiring, and Discontinued.](images/life-cycle-diag.png "AppShield Release Life Cycle Diagram")

<div class="warning" markdown="1">

To keep your apps and data secure, OutSystems recommends that you always use the current version of the **AppShield** plugin. Go to the [Versions tab of the plugin Forge page](https://www.outsystems.com/forge/component-versions/9379) to get the current version.

</div>

## Prerequisites

To ensure the integrity and protection of your apps with **AppShield**, you must meet the following requirements:

* You have a license for **AppShield**.

* You're using MABS 6.3 or later.

    For more information about the supported operating systems, refer to [MABS and mobile operating systems life cycles](https://success.outsystems.com/Support/Release_Notes/Mobile_Apps_Build_Service_Versions).

* The OutSystems Platform Server is running on version 11.

## Enable AppShield on your mobile apps

To protect your mobile app using the AppShield plugin, follow these steps:

1. **Install the AppShield** plugin in your environment.

    To download the plugin, go to [OutSystems AppShield](https://www.outsystems.com/forge/component-overview/9379/) in Forge.

    ![Image showing the process of installing the AppShield plugin from the OutSystems Forge.](images/install-appshield-fg.png "Install AppShield Plugin")

1. **Add the dependencies for AppShield** plugin on each mobile app you want to protect.

    ![Screenshot depicting how to add dependencies for the AppShield plugin in a mobile app project.](images/add-dependencies-ss.png "Add Dependencies for AppShield Plugin")

1. **Generate and distribute a new mobile package** protected with AppShield.

    ![Image illustrating the steps to generate and distribute a new mobile package protected with AppShield.](images/distribute-app-sc.png "Generate and Distribute Mobile Package")

Note the following:

* AppShield enables all capabilities by default, except [Screen reader](protection-features-description.md#android-screen-reader), [Keylogger](protection-features-description.md#keylogger-protection), [Tapjacking](protection-features-description.md#tapjacking-protection), and [Private space](protection-features-description.md#private-space-detection) detection.
* You can set additional configuration in the [Configuration](#configuration) section.
* Hardening increases the app file size.
* MABS takes more time to create a hardened build.

<div class="info" markdown="1">

For more information about adding mobile plugins to your app, refer to [Adding plugins](../../integration-with-systems/mobile-plugins/intro.md#adding_plugins).

</div>

## Supported features

These are the features you can use with the current release of the **AppShield** plugin.

### Android

AppShield provides the following protections for Android builds:

* Root detection
* Repackaging detection
* Code obfuscation
* Code injection protection
* Debugger protection
* Emulator detection
* Key logger protection
* Screen reader detection
* Untrusted keyboard detection
* Screenshot protection
* Task hijacking protection
* Tapjacking protection
* Private space and work profile security enforcement

### iOS

AppShield provides the following protections for iOS builds:

* Jailbreak detection
* Repackaging detection
* Code injection protection
* Debugger protection
* Screen mirroring detection
* Screenshot protection

## Configuration

**AppShield** is on by default when you install the plugin. You can turn it off in one or more environments for testing purposes.

* To turn off **AppShield** in one or more environments, edit the **Extensibility Configuration** settings in **LifeTime** for the environment. Disabling the plugin in the development environment, for example, lets you run the app in emulators or debug the app.

* To turn off **AppShield** globally, edit the **Extensibility Configuration** settings **in Service Studio**. **LifeTime** copies configuration from **Service Studio** to other environments during deployment.

<div class="info" markdown="1">

The following rules apply when you work with **AppShield** JSON for extensibility configuration:

* Specific settings in **Extensibility Configuration** override global extensibility configuration settings.
* **Extensibility Configuration** settings in LifeTime override the extensibility configuration in **Service Studio**.

</div>

The following example shows the JSON for **Extensibility Configurations**. You can use different sections for iOS and Android.

```
{
    "preferences": {
        "global": [
            {
                "name": "DisableAppShielding",
                "value": "false"
            },
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "false"
            },
            {
                "name": "ExitOnURL",
                "value": "https://example.com/protectionblocker/landing-page"
            }
        ],
        "android": [
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "true"
            },
            {
                "name": "AllowPrivateSpace",
                "value": "false"
            },
            {
                "name": "AllowTapjacking",
                "value": "false"
            },
            {
                "name": "AllowScreenshot",
                "value": "false"
            },
            {
                "name": "BlockUntrustedKeyboards",
                "value": "true"
            },
            {
                "name": "BlockUntrustedScreenreaders",
                "value": "true"
            }
        ],
        "ios": [
            {
                "name": "AllowJailbrokenRootedDevices",
                "value": "true"
            },
            {
                "name": "AllowScreenshot",
                "value": "false"
            }
        ]
    }
}
```

### Configuration reference

The following table lists the values available in the **AppShield** configuration JSON.

| Configuration | Type | Default value | OS | Description |
| ------------------------------- | ------------ | ------------- | ------------ | ------------------------------------------------------------------------------------------------- |
| `AddTrustedKeyboardSigner` | Text | | Android | If `BlockUntrustedKeyboards` is set to `true`, this option can whitelist a third-party keyboard. This option must be added for each keyboard software that you want to add to the whitelist. |
| `AddTrustedScreenReaderSigner` | Text | | Android | If `BlockUntrustedScreenreaders` is set to `true`, this option can whitelist a third-party screen reader. This option must be added for each screen reader software that you want to add to the whitelist. |
| `AllowJailbrokenRootedDevices` | Boolean | `false` | iOS, Android | If set to `true`, users can run the app on the jailbroken devices. |
| `AllowPrivateSpace` | Boolean | `true` | Android | If set to `false`, the application is blocked from running if the application was started from a private space or a work profile. |
| `AllowScreenshot` | Boolean | `false` | iOS, Android | If set to `true`, users can take screenshots of the app. |
| `AllowTapjacking` | Boolean | `true` | Android | If set to `false`, the application will detect tapjacking attempts and remove the malicious overlay entirely for apps running on Android 12 and above or block inputs to the overlay for versions below Android 12. |
| `AllowIOSAppOnMacOSX` | Boolean | `false` | iOS | If set to `true`, the application is allowed to run on macOS via Catalyst or as an iPhone app on Mac. When set to `false` (default), the application exits when it detects it is running on macOS. You can configure an exit URL to redirect users when the app exits. For more information about configuring an exit URL, refer to [Configuring an exit URL for a blocked app](ExitOnUrl.md). macOS provides greater access to debugging and reverse engineering tools than a standard iOS device. Enable only if your app is designed to support macOS and your target audience requires it. |
| `ApplicationSignerCertificate` | Text(Base64) | | iOS, Android | Adds the given certificate to the accepted signers whitelist of the final package. This option must be added for each certificate that you want to add to the whitelist. |
| `AppShieldDebugMode` | Boolean | `false` | iOS, Android | If set to `true`, the shielding process is applied in debug mode, keeping debugging options used in Debug and Development builds. Used for extended developer troubleshooting. Builds with this option can't be uploaded to the Store, and, on Android, they need to be installed using `adb install` with the `-t` option. |
| `AppShieldObfuscationRules` | Text(base64) | | Android | Custom rules for obfuscation. For more information, refer to [Creating custom obfuscation rules](obfuscate-custom-rules.md). |
| `BlockDeveloperMode` | Boolean | `false` | iOS, Android | If set to `true`, the application is blocked from running on iOS devices that have Developer Mode enabled and Android devices with Developer Options unlocked. |
| `BlockUntrustedKeyboards` | Boolean | `false` | Android | If set to `true`, untrusted keyboards are detected and blocked. |
| `BlockUntrustedScreenreaders` | Boolean | `false` | Android | If set to `true`, untrusted screen readers are detected and blocked. Screen readers that come preinstalled on the device as system apps, such as TalkBack, are always trusted and are not blocked. Screen readers installed from an app store or other sources are checked and blocked if untrusted. |
| `BlockMemoryScan` | Boolean | `true` | Android | If set to `true`, the application shuts down when it detects unauthorized memory scanning or dumping activity. This protects sensitive data stored in memory, such as encryption keys or session tokens, from being extracted or manipulated by attackers. |
| `BlockUnlockedBootloader` | Boolean | `true` | Android | If set to `true`, the application exits when it detects that the device bootloader is unlocked. An unlocked bootloader may indicate the device is running a custom or potentially malicious OS. You can optionally configure an exit URL to redirect users when the app exits. For more information about configuring an exit URL, refer to [Configuring an exit URL for a blocked app](ExitOnUrl.md). |
| `BlockCodeTraceDetection` | Boolean | `true` | Android | If set to `true`, the application terminates when it detects runtime code tracing activity. Code tracers follow application threads at runtime to capture native instructions, and are commonly used to reverse engineer apps and extract business logic. |
| `BlockNonSystemOverlays` | Boolean | `true` | Android | If set to `true`, the application prevents non-system overlays from appearing over it and removes any existing non-system overlays while the app is in use. This protects against tapjacking attacks, where malicious overlays trick users into interacting with hidden content. |
| `BlockEmulator` | Boolean | `true` | iOS, Android | If set to `true`, the application exits when it detects it is running in an emulator or simulator. You can optionally configure an exit URL to redirect users when the app exits. For more information about configuring an exit URL, refer to [Configuring an exit URL for a blocked app](ExitOnUrl.md). Developers and testers commonly use emulators and simulators during development. Enable this in production builds where emulator access is not expected or permitted. |
| `BlockEmulatedInput` | Boolean | `false` | Android | If set to `true`, the application blocks inputs injected to the screen by emulated or automated sources. You can also configure the app to exit when emulated input is detected by setting an exit URL. For more information about configuring an exit URL, refer to [Configuring an exit URL for a blocked app](ExitOnUrl.md). Some accessibility tools, such as switch access or assistive input devices, rely on emulated input methods and may be incorrectly blocked when this setting is enabled. Enable this only if your target audience does not rely on such tools. |
| `BlockScreenMirroring` | Boolean | `false` | Android | If set to `true`, the application detects when the device screen is being mirrored to an external display and blocks it by drawing a blank view on secondary displays. Users who legitimately cast their screen, such as for presentations or streaming to a TV via Chromecast or MiraCast, will have their mirrored display go blank while the app is in use. Enable this only if your app handles sensitive data that must be prevented from appearing on external displays. |
| `BlockVPN` | Boolean | `false` | iOS, Android | If set to `true`, the application exits when it detects that a VPN is active on the device. You can optionally configure an exit URL to redirect users when the app exits. For more information about configuring an exit URL, refer to [Configuring an exit URL for a blocked app](ExitOnUrl.md). Enterprise users or users who rely on VPNs for privacy may be unexpectedly blocked. Enable this only if your app operates in environments where VPN usage is not permitted. |
| `BlockHiddenSEPolicyArtifacts` | Boolean | `false` | Android | If set to `true`, the application verifies the device's SELinux policy artifacts. If hidden artifacts indicating a tampered or compromised security policy are detected, the app will close. This covers advanced rooting and root-hiding techniques, including Magisk and KernelSU setups with modules such as TrickyStore. Note: all LineageOS devices ship with a modified SELinux policy. When this setting is enabled, end users on LineageOS devices will be blocked, including on unrooted devices. |
| `DisableAppShielding` | Boolean | `false` | iOS, Android | Activates or deactivates App Shield. |
| `ExitOnURL` | URL value | | iOS, Android | If an app feature is blocked due to a configured policy of the **AppShield** plugin, the default browser opens the URL where the problem may be explained. For more information, refer to [ExitOnURL](ExitOnUrl.md). |
| `RemoveQueryAllPackagesPermission` | Boolean | `true` (`false` for versions below 1.5.1) | Android | If set to `true`, AppShield removes the app's ability to check other installed applications. For more information, refer to [Query All Packages permission in Android apps using AppShield](query-all-packages.md). |
| `android` | JSON value | | Android | The key denoting values that apply to Android devices. |
| `global` | JSON value | | iOS, Android | Settings in this section apply to both Android and iOS builds. |
| `ios` | JSON value | | iOS | The key denoting values that apply to iOS devices. |

## Check that an app with AppShield builds successfully

To ensure that your build passed the shield phase, check your [app’s build logs](../../deploying-apps/mobile-app-packaging-delivery/generate-distribute-mobile-app/intro.md#download-mobile-app-build-logs).

When you trigger a build with AppShield enabled and correctly configured, MABS includes a **shield phase** while generating the app's mobile package.

The shield phase occurs after the build phase, and a message at the end of the log file lets you know if the shield phase is successful.

![Screenshot of the AppShield shield phase in the mobile app build logs indicating a successful shield operation.](images/appshield-log-sc.png "AppShield Shield Phase Log")

## Obfuscation

Obfuscation has the following limitations:

* Obfuscation applies only to the supported **OutSystems** mobile plugins.
* Obfuscation of JavaScript files isn't supported.
* Obfuscation of native iOS bitcode isn't supported.
* Deobfuscation of the native Android logs that the plugin obfuscates in Service Center requires an external tool.
* Access to the mapping files requires contacting Support.

### String binding

On Android apps, bindings are created between AppShield and the app so that the presence of AppShield is required for the app to execute normally. The binding process modifies classes by extracting and removing values (i.e., constants) from the application code. When the app launches, AppShield provides these values to the app only if the app satisfies the configured AppShield security policy.

The strength of the binding depends on the number of constants removed from the app and the distribution of removed constants across the code base. AppShield adds the removed constants to the encrypted runtime data.

By default, Android apps have the binding active. For more information about configuring string binding, refer to [Creating custom obfuscation rules](obfuscate-custom-rules.md).

## Whitelist signing certificates

If you re-sign your app with a different certificate after you build it, **AppShield** repackaging detection treats the app as repackaged. The app then crashes on startup with a repackaging exception. To prevent this, whitelist the certificate that re-signs the app.

Repackaging detection is one of the security features of **AppShield**. It flags packages signed with an unrecognized certificate. For example, Google Play App Signing re-signs the app with a different certificate when you upload an `.aab` file to the Google Play Store. **AppShield** whitelists the certificate of the keystore provided to MABS automatically. Whitelist only the certificates that re-sign the app afterward.

When you whitelist a certificate, **AppShield** considers packages signed with that certificate safe during the repackaging analysis.

### Obtain the signing certificate {#obtain-the-signing-certificate}

To get the certificate value, export the certificate to a `certificate.pem` file, and then copy the certificate text from that file. The export steps depend on the platform and on where the certificate is stored.

#### Export the certificate for iOS

If you have the PKCS12 file, do the following:

1. Export the certificate to a `certificate.pem` file by running the following command:

    ```
    keytool -storetype PKCS12 -keystore PKCS12_FILE -storepass STORE_PASSWORD -alias ALIAS -exportcert -rfc > certificate.pem
    ```

    Replace the following:

    * `PKCS12_FILE`: The path to the PKCS12 file
    * `STORE_PASSWORD`: The password of the PKCS12 file
    * `ALIAS`: The alias of the certificate in the PKCS12 file

1. Optional. To use `openssl` instead of `keytool`, run the following command:

    ```
    openssl pkcs12 -in PKCS12_FILE -nokeys -password pass:STORE_PASSWORD -out certificate.pem
    ```

    Some certificates and openssl versions require the `-legacy` option.

Continue with [Copy the certificate value](#copy-the-certificate-value).

#### Export the certificate for Android

If you have the keystore file, do the following:

1. Export the certificate to a `certificate.pem` file by running the following command:

    ```
    keytool -keystore KEYSTORE_FILE -storepass STORE_PASSWORD -alias ALIAS -exportcert -rfc > certificate.pem
    ```

    Replace the following:

    * `KEYSTORE_FILE`: The path to the keystore file
    * `STORE_PASSWORD`: The password of the keystore file
    * `ALIAS`: The alias of the certificate in the keystore file

If the certificate is the **App Signing Certificate** from the Google Play App Signing feature, do the following:

1. In Google Play Console, download the **App Signing Certificate** from the **App Signing** section. The downloaded file has the `.der` extension.

1. Convert the downloaded file to a `certificate.pem` file by running the following command:

    ```
    openssl x509 -inform der -in DER_FILE -out certificate.pem
    ```

    Replace `DER_FILE` with the path to the downloaded `.der` file.

Continue with [Copy the certificate value](#copy-the-certificate-value).

#### Copy the certificate value {#copy-the-certificate-value}

The `certificate.pem` file contains the certificate between a `-----BEGIN CERTIFICATE-----` line and a `-----END CERTIFICATE-----` line. To get the value for the `ApplicationSignerCertificate` preference, do the following:

1. Open the `certificate.pem` file in a text editor.

1. Copy the text between the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` lines. Don't include these two lines.

1. Remove the line breaks so the copied text is a single line.

### Whitelist the signing certificate

You can whitelist signing certificates using the `ApplicationSignerCertificate` preference. Set the value of the preference to the certificate value that you get by following the steps in the [Obtain the signing certificate](#obtain-the-signing-certificate) section.

Add the `ApplicationSignerCertificate` preference once for each certificate that you want to whitelist. **AppShield** treats applications signed with any of those certificates as secure.

**AppShield** whitelists the certificate of the keystore provided to MABS automatically. You can install the app retrieved from MABS directly on any device.

In the [Extensibility Configurations JSON](../../deploying-apps/mobile-app-packaging-delivery/customize-mobile-app/extensibility-configurations-json-schema.md), add the preference to the `android` section for an Android certificate, or to the `ios` section for an iOS certificate. Set `name` to `ApplicationSignerCertificate` and `value` to the certificate value. For more information about where to edit the Extensibility Configurations, refer to [Configuration](#configuration).

The following example whitelists two certificates for Android and one for iOS:

```javascript
{
    "preferences": {
        "android": [
            {
                "name": "ApplicationSignerCertificate",
                "value": "ANDROID_CERTIFICATE_VALUE_1"
            },
            {
                "name": "ApplicationSignerCertificate",
                "value": "ANDROID_CERTIFICATE_VALUE_2"
            }
        ],
        "ios": [
            {
                "name": "ApplicationSignerCertificate",
                "value": "IOS_CERTIFICATE_VALUE"
            }
        ]
    }
}
```

Replace the following:

* `ANDROID_CERTIFICATE_VALUE_1`: The certificate value of the first Android certificate
* `ANDROID_CERTIFICATE_VALUE_2`: The certificate value of the second Android certificate
* `IOS_CERTIFICATE_VALUE`: The certificate value of the iOS certificate

After you update the Extensibility Configurations, generate a new build of your mobile app.

## Limitations {#limitations}

**AppShield** isn't compatible with the Automatic Protection service of Google Play. The service injects additional code into the app, which makes **AppShield** trigger a repackaging exception. Disable Automatic Protection in Google Play for apps that use **AppShield**.
