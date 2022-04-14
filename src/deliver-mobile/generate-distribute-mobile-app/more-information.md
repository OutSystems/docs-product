---
summary: In this article you can find more information about tasks associated with generating and publishing iOS and Android mobile apps.
tags: runtime-mobile; support-mobile
locale: en-us
guid: 952b6539-a884-4fed-bcdd-90d4145d41b7
---

# More Information on Generating and Distributing Mobile Apps

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

In this article you can find more information about tasks associated with generating and publishing iOS and Android mobile apps:

* For iOS, check how you can enroll as an Apple Developer, and learn more about creating certificates and provisioning profiles. 
* For Android, check how to create a keystore and some of the best practices for managing one. 

## For iOS

### Enroll as an Apple Developer

The first step to generate an iOS app package (IPA) is to register as an [Apple Developer](https://developer.apple.com/programs/). You have two types of developer programs that you can choose according to your requirements:

* **Apple Developer Program** &#8211; The standard Apple Developer account allows you to build applications and distribute them on the public App Store, potentially reaching millions of end users all over the world. Your applications must follow specific guidelines in order to get approved by Apple. 

    [Learn more about the Apple Developer Program](https://developer.apple.com/programs/).

    [Learn more about App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).

* **Apple Developer Enterprise Program** &#8211; With the Enterprise Developer Account, you are not obliged to follow the App Store Guidelines, but you can only distribute your applications to employees within your organization. The apps cannot be submitted to the public App Store, they should be distributed by an internal enterprise store or an MDM (Mobile Device Management) solution. 

    [Learn more about the Apple Developer Enterprise Program](https://developer.apple.com/programs/enterprise/).

After understanding the differences between Apple Developer and an Apple Developer Enterprise program, you should enroll in one of them. If you have requirements for both use cases, you can create two different accounts, one for the Developer Program and one for the Enterprise Program. Then, depending on the application you want to build, you should use one or the other.

You can also enroll as an individual or an organization. If you wish to enroll as an organization you must provide additional information and the process can take a little longer but allows you to publish applications on behalf of your organization. If you choose the Apple Developer Enterprise Program, you must always enroll as an organization. Note that enrolling as an individual or organization has different annual fees.

To learn more about the iOS Apple Developer account, read the OutSystems post in Medium "[Cruising through the Complexities of Signing Native Mobile Apps](https://medium.com/outsystems-engineering/cruising-through-the-complexities-of-signing-native-mobile-apps-cc123eb2814b)" or check the [iOS official documentation](https://developer.apple.com/programs/).

### Create a Certificate

Log in your [Apple Developer account](https://developer.apple.com/account) and select the option **Certificates, IDs & Profiles**.

The certificates you can use:

* For a development certificate, use the `iOS App Development` certificate type. 
* For a production certificate, select the `App Store and Ad Hoc` (for Apple Developer Program) or the `In-House and Ad Hoc` certificate type (for Apple Developer Enterprise Program). 

To create the certificate (`.p12` extension format):

**Generate the Certificate Signing Request (CSR) File**

To create your certificate you need to provide a CSR file. Apple will provide you with instructions on how to create one if you have an Apple machine, but if you don't have a Mac here's how you can do it on a Windows machine:

1. Download the most recent version of [OpenSSL](http://slproweb.com/products/Win32OpenSSL.html). 
1. Start a new command prompt (Start > Run > `cmd.exe`). 
1. Execute the command to set the folder used on the OpenSSL installation: 

        set OPENSSL_CONF=<path_to_openssl_bin>\openssl.cfg

    where `<path_to_openssl_bin>` can be `C:\OpenSSL-Win32\bin` or `C:\OpenSSL-Win64\bin`.

1. Now call the OpenSSL to create the CSR and the private key: 

        <path_to_openssl_bin>\openssl.exe req -out <CSR_file_name>.csr -new -newkey rsa:2048 -nodes -keyout <privateKey_name>.key 

    where `<CSR_file_name>` is the name for the CSR file and `<privateKey_name>` is the name for the private key file.

After you run the command on your computer, it will generate a new CSR file with a public key embedded and a private key.

**Download the CER and Create the P12 Certificate**

Now that you have created the CSR file, go back to the Apple Developer Portal and upload the file. Follow the next steps on Apple's page to create a new Certificate (CER file format). This certificate includes both public and private keys and can be used for multiple apps.

<div class="warning" markdown="1">

Back up the CSR and the CER files in a safe place.

</div>

If you're using a Mac, download the CER file, install it and export to the P12 file format. If you are using a Windows machine, open the command prompt and execute the following commands:
    
    <path_to_openssl_bin>\openssl.exe x509 -in <certificate_cer>.cer -inform DER -out <app_pem_file_name>.pem -outform PEM 

where `<certificate_cer>` is the name of the certificate downloaded from Apple and `<app_pem_file_name>` is the name for the PEM file.

Now you'll need to use the file you've just generated to run the following command and create the P12 file:
    
    <path_to_openssl_bin>\openssl.exe pkcs12 -export -inkey <privateKey>.key -in <app_pem>.pem -out <app_p12>.p12

where `<privateKey>` is the file generated when creating the CSR file, `<app_pem_filename>` is the name of the created PEM file in the command executed before and `<app_p12>` is the name you want for the P12 file.

You will be asked for a password, create one and remember or store it somewhere &#8212; you'll need to insert it in OutSystems. The P12 file created in the last step is the certificate to generate the iOS app.

If you are creating the P12 file with OpenSSL 3.0, add the flag `-legacy` to the previous command. If OpenSSL is not installed system-wide, the command returns the error "pkcs12: unable to load provider legacy". If that happens, you can either add the flag `-provider-path <openssl_path>/providers` to the previous command or set the environment variable `OPENSSL_MODULES` to point to the directory `<openssl_path>/providers`. The command should look like the following:

    <path_to_openssl_bin>\openssl.exe pkcs12 -legacy -provider-path <openssl_path>/providers -export -inkey <privateKey>.key -in <app_pem>.pem -out <app_p12>.p12

### Create a Provisioning Profile

A provisioning profile allows your application to be launched on Apple devices and use app services like Apple Pay or push notifications.

The provisioning profiles you can use are:

* **iOS App Development**: this Development Provision Profile allows you to generate a development version (containing debug information) of your mobile app that can be installed and launched in a given set of devices for development tests. Only the devices specified for the provisioning profile will be able install and launch the app. If a given user's device is not authorized to install the app, the user will get an "Unable to Download App" alert message. 

* **Ad Hoc**: this Distribution Provisioning Profile allows you to generate a release version of your mobile app that can only be used in a limited list of devices. Use this profile to distribute your application to a limited group of end users. Only the devices specified for the provisioning profile will be able install and launch the app. If a given user's device is not authorized to install the app, the user will get an "Unable to Download App" alert message. 

* **App Store**: this Distribution Provisioning Profile, available for the Apple Developer Program, allows you to generate a release version of your mobile app that can be published and distributed through the App Store. Use this profile when your application has been thoroughly tested and is ready to be made available to everyone through the App Store. 

* **In-House**: this Distribution Provisioning Profile, available for the Apple Developer Enterprise Program, allows you to generate a release version of your mobile app with no limitations on which devices it will run. Use this profile when your mobile app will only be distributed inside your company. It will not be subject to review by Apple because you will not be able to submit it to the App Store. However, you will have to handle the app distribution on your own. 

To create a provisioning profile (`.mobileprovision` extension format):

1. Access your [Apple Developer account](https://developer.apple.com/account) and select the option **Certificates, IDs & Profiles**.

1. Select **Provisioning Profiles**.

1. Select the type of provisioning profile you want to generate, as explained above.

1. Provide the information requested during the generation process. You will have to enter an App ID, which certificates to include in the profile and, for some types of provisioning profiles, which specific iOS devices will be allowed to launch mobile apps associated with the provisioning profile being generated. Note that if you later register additional devices in your Developer Account or add any app services, you will need to create a new provisioning profile and generate the mobile app again to propagate your changes.

1. At the end of the generation process, you will be able to download the generated provisioning profile for later use. 

In order to generate iOS mobile apps in OutSystems you will be asked to provide a provisioning profile along with one of the certificates that you associated with it in the steps described above.

### Renew a Provisioning Profile

To check the validity of your provisioning profile:

* Access your Apple developer portal, go to **Account -> Certificates, Identifiers & Profiles -> Profiles**, and check the expiration date of the desired provisioning profile.
* Open the provisioning profile in a text editor and look for the **ExpirationDate** key that contains information about the expiring date.

To renew your provisioning profile, follow these steps:

1. Log in to your [Apple Developer account](https://developer.apple.com/account).
1. Select **Certificates, Identifiers & Profiles**.
1. Click **Profiles**.
1. Select the provisioning profile to be renewed.
1. Click **Edit**.
1. Select the certificate(s) you want to associate with the profile.
1. Click **Generate**.
1. Download the renewed provisioning profile.
    

## For Android

### Create a Keystore

A keystore is a file that stores a security key. You can use it to sign your Android apps. Signing the app is the way to identify the author of the application for an Android app. Check more information about it in the official documentation.

To create a new keystore, you can use the [keytool](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/keytool.html) command interface. Ensure that you have [Java](http://www.oracle.com/technetwork/java/javase/downloads/jre8-downloads-2133155.html) installed since this command interface is available in the "bin" directory of your Java installation.

After you verify the availability of the keytool command, open a computer command prompt (Start > Run > `cmd.exe`) and, if the keytool command is not available in the path, navigate to the Java "bin" directory. Execute:
    
    keytool -genkey -v -keystore <keystore_name>.keystore -alias <alias_name> -keyalg RSA -keysize 2048 -validity 10000 -storetype jks

where:

* `<keystore_name>` is the name you want to give to the keystore
* `<alias_name>` is the identifier name for your key

Throughout the command execution, it will ask you some questions. Two of the questions are the keystore password and the alias password. The rest of the answers identify the owner of the apps using this keystore.

After the command executes, a new file named `<keystore_name>.keystore` is going to be present in the folder location where you've executed the command.

### Keystore File Recommended Practices

* Store the keystore file in a place where you'll remember it because you'll need to use the same keystore to sign the app when updating it to publish to the Google Play store. 

* Create your keystore with a long validity (in the command example we are extending the validity of the keystore till 2044). If your keystore expires, you can't renew it and so you won't be able to update your app. 

* Keep your keystore file in a safe place. In case a third-party has it can sign and distribute apps under your identity. 

For more information, check the [Android official documentation](https://developer.android.com/studio/publish/app-signing.html#considerations).
