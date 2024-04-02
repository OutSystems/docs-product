---
summary: Applications secured with authentication can be subject to brute force attacks that systematically try to guess user passwords. OutSystems provides a built-in protection mechanism that allows taking countermeasures against these attacks.
tags: support-Security-overview
locale: en-us
guid: 12783fed-7ac1-41f3-8d46-544892ff8b58
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=267%3A99&mode=design&t=wnuT61gSaBFQZ5jn-1
---

# Protection against Brute Force Attacks

Applications secured with authentication can be subject to brute force attacks that systematically try to guess user passwords. OutSystems provides a built-in protection mechanism that lets you take countermeasures against these attacks.

* **User-level Attack:** The attack is perpetrated with a user from a specific IP address. In this case, that user is blocked from logging in from the attacker IP address. The legitimate user can still login from an IP address that wasn't used for the attack.

* **IP-level Attack:** The attacker has a list of users and tries to guess their passwords from a specific IP address. In this case, the attacker IP address is blocked. By blocking the IP address, the platform doesn't let the attacker go through all the users and flood the application with requests. This could also lead to a **Denial-of-Service (DoS)** attack.

![User and IP level protection mechanism against brute force attacks](images/protection-against-brute-force-attacks-0.png "Brute Force Attack Protection Mechanism")

## How the protection works

The countermeasure OutSystems provides consists of a two-step backoff mechanism:

1. **The first backoff:** If the number of failed login attempts reaches a limit within a period of time, the following happens:

     * **User-level attack:** The user gets blocked for that IP address and can't log in from there for a short time (a few minutes).
     * **IP-level attack:** The IP address gets blocked and users can't log in from there for a short time (a few minutes).

    In both cases, the error message changes from **Invalid username or password** to **Too many failed login attempts. Please try again in a few minutes.**

1. **The second backoff:** If the attack continues and a second limit is reached, the login is blocked for a long time (about an hour). The error message changes to: **Too many failed login attempts. Please try again in 60 minutes.**

<div class="info" markdown="1">

## Protecting Application Users and IT Users

The protection against brute force attacks for **application users**, for instance, end users of your applications, is available for all applications configured with Users as their User Provider or when using a custom User Provider cloned from Users.

To learn how to configure this protection for IT users, refer to [Configure Brute Force Protection for Application Users](<#configure-brute-force-protection>).

The same brute force attack protection is available by default for **IT users** when logging in to Service Center and LifeTime. To learn how to configure this protection for IT users, refer to [Configure Brute Force Protection for IT Users](#configure-brute-force-protection-it-users).

</div>

## Unblocking Application Users

Users and IP addresses can get blocked even if they're legitimate, for example:

* Forgetting the password and trying too many login attempts.
* A brute force attack that blocks an IP address, for example, an ISP that is also used by many legitimate users.

To unblock users/IP addresses and restore the normal login process, refer to the Users management console at `http://<yourserver>/Users`).

To unblock an **end user**, do the following:

1. Log in to the **Users** application.
1. Go to the User details page and scroll down to the bottom of the page to s the **Blocked Login Attempts** section.
1. If the user is blocked, an entry is added to this section specifying the number of attempts, the IP address used, and the timestamp of the last attempt.
1. Click the  **Unblock** link to restore the normal login process for this specific end user.

To unblock an **IP address**, do the following:

1. Log in to the **Users** application.
1. On the right side of the screen, click the **Blocked Addresses** link to check if there are any blocked IP addresses.
1. Click the **Unblock** link to restore the normal login process for all users in the unblocked IP address(es).

## Unblocking IT Users

LifeTime and Service Center are protected against brute force attacks, which means its users can get blocked. When they get blocked use LifeTime to unblock them or, if not installed, use Service Center.

### For on-premise installations

To unblock IT users in environments that are registered in **LifeTime**, do the following:

1. Log in to **LifeTime** with a user who has permissions to manage users and teams.
1. Go to the ****Infrastructure** tab.
1. Go to the **Blocked Addresses** sub tab.
1. Click **Unblock** to restore the normal login process for all users in the desired IP address(es)

![blocked address](images/blocked-address-lt.png "identify blocked address")

<div class="info" markdown="1">

If the environment is not registered in LifeTime, then the unblock process occurs in **Service Center**:

1. Log in to **Service Center** with a user who has permissions to manage users.
1. Go to the **Monitoring** section.
1. Select the **Security** option, which displays a list of blocked IP addresses.
1. Check the IP address(es) for which you want to restore the normal login process for all users.
1. Click the **Unblock Selected** button.

</div>

![user test](images/user-test-sc.png "identify blocked login attempts")

### For Cloud installations

To unblock IP Addresses in **Cloud** environments, do the following:

1. Log in to **LifeTime** with a user who has permissions to manage users and teams.
1. Go to the **Environments** tab.
1. From the **Options** button, select **Blocked Addresses**
1. Click **Unblock** to restore the normal login process for all users in the desired IP address(es).

![Unblocking blocked addresses to restore normal login process on Cloud](images/environments-lt.png "Unblocking blocked addresses from Cloud")

## Check for Possible Brute Force Attacks

The environment management console (Service Center) provides logs with information that you can use to monitor possible brute force attacks.

![two-step backoff mechanism for brute force protection](images/protection-against-brute-force-attacks-1.png "Brute Force Protection Countermeasures")

To access the log, do the following:

1. Log in to **Service Center** and go to the **Monitoring** section.
1. Select the **Errors** option.
1. Filter by **Login** in the Source.

When an IP address is blocked due to a possible brute force attack, the information  displays in the following format:

![Log entry for blocked user or IP address due to a brute force attack](images/protection-against-brute-force-attacks-2.png "Blocked User or IP Address Log Entry")

* The timestamp of the login attempt
* The user who attempted the login
* The IP address from where the login attempt was made
* The approximate time that elapsed since the last login attempt
* When was the last login attempt
* The count of login attempts

If a failed login attempt hasn't triggered blocking the IP address yet, the information displays as follows:

![log entry for failed login attempt that does not configure attack](images/protection-against-brute-force-attacks-3.png "Failed Login Attempt Log Entry")

* The timestamp of the login attempt
* The user who attempted  the login
* The count of login attempts at the user-level and IP-level

## Configure Brute Force Protection for Application Users { #configure-brute-force-protection }

<div class="info" markdown="1">

The configuration in this section is only applicable to **application users** and not to IT users. Therefore, it doesn't affect the protection of LifeTime and Service Center.

To learn how to configure this protection for IT users, refer to the [Configure Brute Force Protection for IT Users](#configure-brute-force-protection-it-users).

</div>

The protection of OutSystems applications against brute force attacks is configurable. To change the behavior, do the following:

1. Log in to **Service Center**.
1. Go to the **Factory section** and select the **Modules** option.
1. Search for the **Users** module and open the page with the details.
1. Select the **Site Properties** tab.
1. Configure the protection in the **Site Properties** using the information in the following table.

|Site Property                              |Description               |
|-------------------------------------------|--------------------------|
|EnableBruteForceProtection                 |Enables brute force login protection at user level.|
|MaxUsernameAttemptsFirstBackoff            |The maximum number of login attempts for a user after which the first backoff protection is triggered.<br/>The default value is 3 times.|
|MaxUsernameAttemptsSecondBackoff           |The maximum number of login attempts for a user after which the second backoff protection is triggered.<br/>The default value is 6 times.|
|UsernameAttemptsFirstBackoffDelayInSeconds |After hitting the first backoff, it's the time that login attempts are blocked for a user.<br/>The default value is 30 seconds.|
|UsernameAttemptsSecondBackoffDelayInSeconds|After hitting the second backoff, it's the time that login attempts are blocked for a user.<br/>The default value is 1800 seconds.|
|EnableBruteForceProtectionPerIP            |Enables brute force login protection at IP level.|
|MaxIPAttemptsFirstBackoff                  |The number of login attempts for an IP address after which the first backoff is triggered.<br/>The default value is 20 times.|
|MaxIPAttemptsSecondBackoff                 |The number of login attempts from an IP address after which the second backoff is triggered.<br/>The default value is 50 times.|
|IPAttemptsFirstBackoffDelayInSeconds       |After hitting the first backoff, it's the time that login attempts are blocked for an IP address.<br/>The default value is 300 seconds.|
|IPAttemptsSecondBackoffDelayInSeconds      |After hitting the second backoff, it's the time that login attempts are blocked for an IP address.<br/>The default value is 3600 seconds.|
|InvalidLoginCheckWindowInMinutes           |Time frame in minutes in which failed attempts are accounted.<br/>Default value is 60 minutes.|

## Configure Brute Force Protection for IT Users { #configure-brute-force-protection-it-users }

The protection against brute force attacks is available by default for **IT users** when logging into Service Center and LifeTime. To change the default behavior, use the [Factory Configuration](https://www.outsystems.com/forge/component-overview/25/factory-configuration) application, available from OutSystems Forge, in **all environments**.

To configure the brute force protection for IT users, do the following in **all application environments and in the LifeTime environment**:

1. Download and install the [Factory Configuration](https://www.outsystems.com/forge/component-overview/25/factory-configuration) application.

1. Go to the Factory Configuration application (`https://<environment_name>/FactoryConfiguration`) and change the Brute Force Protection settings.

    ![Brute Force Protection settings in Factory Configuration application](images/protection-against-brute-force-attacks-4.png "Brute Force Protection Settings in Factory Configuration")

1. Click  **Apply**.

Make sure the Brute Force Protection settings are **the same across all environments**.
