---
summary: Set of best practices and solutions for securing data in your mobile apps built with OutSystems.
tags: runtime-mobile; support-Security; support-Security-featured
locale: en-us
guid: 5b81d4aa-2da0-4e88-9d14-c17a753a79fa
app_type: mobile apps
platform-version: o11
---

# Secure the Data of your Mobile Apps

<div class="info" markdown="1">

Applies only to Mobile Apps.

</div>

This document presents a set of best practices and solutions for securing data in your mobile apps built with OutSystems.

## Avoid storing sensitive data on the device

We take our devices everywhere and install all kinds of apps. Their security can be easily compromised by theft or some malicious app we inadvertently install. Keeping sensitive data only on the server and requesting it to the device only when needed prevents third parties from accessing it by compromising your device storage. All connections from the device to the server are authenticated and run over HTTPS, so your sensitive data will be safe.

If you need your application to work offline, make an informed decision on what data to store locally on the device. Keep sensitive entities or attributes on the server database, and keep in Local Storage only the data that is non-sensitive and necessary for offline use of your application.

A good approach is to find the minimum subset of data your users will need to accomplish their tasks while in offline. This will help you trim down the data and remove all sensitive data.


## Store small snippets of sensitive information

In scenarios where you need to store small amounts of information, like a password or your user’s social security number, you can use the keystore of the device ("keychain" on iOS).

The keystore is an app provided by the device that stores small bits of sensitive information. The keystore secures data by encrypting the data before storing it, and the platform itself carefully controls access to stored items.

To safely store information in the keystore, you can use the [KeyStore Plugin](https://www.outsystems.com/forge/component-details/1550/Key+Store+Plugin/) available in the Forge.


## Store sensitive attributes in Local Storage Entities

If the offline operation of your application needs to hold sensitive information in a few entity attributes, you can create logic in your application to encrypt and decrypt those values as needed.

You may use a traditional JavaScript encryption framework (there are several [available here](https://gist.github.com/jo/8619441)) to encrypt the data before writing it to the Local Storage and decrypt it after reading from the Local Storage. The encryption key can be stored securely using the device keystore mechanism as described above.

## Store large amounts of sensitive information in Local Storage

If you have a lot of information on your Local Storage that is considered sensitive you can encrypt the whole Local Storage.

To cipher the Local Storage database, you can use the [Ciphered Local Storage Plugin](https://www.outsystems.com/forge/component-details/1500/Ciphered+Local+Storage+Plugin/) available in the Forge, and this will ensure secure 256-bit AES encryption of your data on the device.

Note that this extra security level may introduce a few performance overheads when reading and writing data to the Local Storage, so be sure to take this in consideration when using this approach.


## Re-validate data in the Server

All data sent from the app to the server should be re-validated in the server. This helps in keeping your server-side logic working over sound data and executing operations as expected. If a hacker is able to forge a request from your app to the server, it will bypass the app validations and can send incorrect requests. Not performing the required validations server-side may lead to data corruption (by replacing real data in the server with bogus data) or data leakage (by accessing data not intended for a specific user).
