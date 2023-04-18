---
summary: 
tags:
locale: en-us
guid: 9a5711af-7947-4f71-9569-ae016863db49
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Lifecycle Management and Data Protection

This article addresses what personal data OutSystems system applications collect, where this personal data is kept and provides some examples on how to obfuscate or remove this personal data.

Personal data includes any information that can directly or indirectly identify an individual, whether it relates to their private, professional or public life. It can be a name, a photo, an email address, location, user-name, computer IP address, and so on.

## Service Center and LifeTime { #service-center-and-lifetime }

### IT user management

Service Center and LifeTime are both OutSystems management consoles, and as so, they are responsible for managing IT Users.
In scenarios where LifeTime is not available, Service Center is the one responsible for creating and managing IT users; otherwise this management is performed in LifeTime (using Service Center in the background).

In order to manage IT Users, both Service Center and LifeTime store the following information for each user in the **User** system entity (physical table name: **ossys\_User**):

* Name (for example, Amos Tesen)
* Username (for example, amos.tesen)
* Mobile Phone [only in Service Center] (for example, +1-800-555-0000)
* Email (for example, amos.tesen@example.com)

### Protection against brute force attacks

Service Center and LifeTime have a system that protects against brute force attacks that systematically try to guess user passwords.

This system offers protection against two levels of attacks, user-level attacks and IP-level attacks (more details [here](secure-the-applications/protection-against-brute-force-attacks.md)); and needs to store some personal user data in order to be functional. The personal information stored in **LoginAttempt** system entity (physical table name: **OSSYS\_LOGIN\_ATTEMPT**) is:

* Username (for example, Amos Tesen)
* IP Address (for example, 192.0.2.0)

### LifeTime audit events

LifeTime has an audit system that logs every operation performed by IT users in the infrastructure. These logs relate to operations performed in Applications, Deployment Plans, Users, Teams, and Roles screens.

These logs may contain some personal information such as the name or username of the users and also client IPs. The information is stored in **AuditEvent** entity [**OSLTM\_AUDITEVENT**], in Message and ClientIP attributes.

For performance reasons, LifeTime deletes the audit logs older than one year. By default, this deleting process runs daily at 7:30 AM (database time).

### LifeTime Analytics

LifeTime Analytics allow users to configure automatic performance reports regarding their applications. These reports can be sent to a registered user or to an isolated email.

This contact list is stored in the platform database in **PerformanceReportConfiguration** entity of the **LifeTimeAnalytics** module (physical table name:**OSLTM\_REPORTCONF**).

### Emails

OutSystems provides a feature to send emails from a web application. This mechanism requires some metadata that may contain personal information related with users.
Users data is necessary to send the emails (email address), and may be present in the email content itself.

All this data is present in System entities: **Sent\_Email** (physical table name: **OSSYS\_EMAIL**) and **Email\_Content** (physical table name: **OSSYS\_EMAIL\_CONTENT**).

### Logs

Service Center logs the user logins in General log. These logs have the following format:

    Login (user: '<username>'). 

This information may be present in all General log tables (**oslog\_General\_0**, **oslog\_General\_1**, **oslog\_General\_2**, …).

## Users

**Users** is the application used by default to manage end users. It contains the same information related with users already referred to in the [Service Center and LifeTime section](#service-center-and-lifetime), namely:

* Name (for example, Amos Tesen)
* Username (for example, amos.tesen)
* Mobile Phone (for example, +1-800-555-0000)
* Email (for example, amos.tesen@example.com)

The entity where this information is stored is the same entity used by Service Center and LifeTime (**User** system entity), but uses a different tenant identifier.

Also, **Users** uses the previously described brute force attack protection system. This system stores some personal user information:

* Username (for example, amos.tesen)
* IP Address (for example, 192.0.2.0)

**Users** uses a different entity to store this information, the **LoginAttempt** entity of the **Users** module (physical table name: **OSUSR\_&lt;PREFIX&gt;\_LOGINATTEMPT**).

**Note:** If you created a new user provider by cloning **Users** the same mechanisms may be in place in your user provider.

## App Feedback

**App Feedback** is a system application for gathering user feedback by allowing users to share written and oral feedback while using your mobile and/or web applications. 
Furthermore, when feedback is submitted the tool captures a screenshot of what is being displayed on the user's screen at that moment.
Therefore, the tool may capture sensitive information depending on the type of application.

For instance, if a user is using a directory type application and submits feedback for the contacts list screen, the tool collects all the contacts that are listed at that moment as a screenshot or HTML code. As a result some personal information may be stored in the **App Feedback** database.

This data may be stored in the following Attributes of the following entities of the **ECT\_Provider** module:

* **Feedback** entity
    * `originalHTML` (used in Web Applications) – The screen's HTML.
* **WebpageContent** entity
    * `Content` (used in Web Applications) – All the resources referenced in HTML when the user submitted the feedback.
* **FeedbackScreenshot** entity
    * `ImageBinary` (used in Mobile Applications) – A screenshot of the users screen when the feedback was provided.
* **FeedbackSoundMessage** entity
    * `SoundBinary` (used in Mobile Applications) – Sound recorded when the feedback was provided.

Apart from the user feedback itself, the tool also stores some more metadata in order to provide as much context as possible. This information includes:

* User's Name
* User's Username
* User's Email
* Browser used
* Device used (in mobile apps)
* Operating System used

## Examples of personal data obfuscation/removal

There are certain scenarios, outside of production environments, where collected personal data (like the name of an end user) is irrelevant and as such should be masked or removed. For example, you may want to use a clone of a real production database for troubleshooting purposes or you may want to use real production data in pre-production environments to perform testing of new features.

The following examples show how to replace or remove personal data collected by OutSystems systems applications in such situations:

### Users

The following SQL snippet masks the `Name`, `Username`, `Email` and `MobilePhone` number from the User entity:

```sql
UPDATE ossys_User
SET
    NAME =  CONCAT('User_', ID),
    USERNAME = CONCAT('User_', ID),
    EMAIL = CONCAT('user_', ID, '@email.com'),
    MobilePhone = ''
WHERE
    USERNAME <> 'admin';
```

Note: `admin` is an internal platform user that cannot be updated, otherwise the platform will create a new one.

<div class="warning" markdown="1">

Do not use this SQL snippet in your Production environment. All the end users usernames and emails will be modified and the end users will not be able to login without your assistance.

</div>

### System Login Attempts

The following SQL snippet deletes all log-in attempt logs from the **LoginAttempt** system entity:

```sql
DELETE FROM OSSYS_LOGIN_ATTEMPT;
```

<div class="warning" markdown="1">

Do not use this SQL snippet in your Production environment.  
By deleting Login Attempts logs, you will clear personal data but you will also unblock all users/IPs that may have been blocked before by the system that protects against brute force attacks.

</div>

### Users Login Attempts

Use the following SQL snippet to find the physical table name of the **LoginAttempt** entity of the **Users** module:

```sql
SELECT PHYSICAL_TABLE_NAME
FROM ossys_Entity
WHERE
    NAME = 'LoginAttempt'
    AND
    ESPACE_ID = (SELECT ID FROM ossys_Espace WHERE NAME = 'Users');
```

And then, use the physical table name with the following SQL snippet to delete all user login attempt logs:

```sql
DELETE FROM <found_PHYSICAL_TABLE_NAME>;
```

Where `<found_PHYSICAL_TABLE_NAME>` is the physical table name of the **LoginAttempt** entity of **Users** module that you found in the previous step.

<div class="warning" markdown="1">

Do not use this SQL snippet in your Production environment.  
By deleting Login Attempts logs, you will clear personal data but you will also unblock all users/IPs that may have been previously blocked by the system that protects against brute force attacks.

</div>

### Emails

The following SQL snippet deletes all the information and content of sent and unsent emails:

```sql
DELETE FROM OSSYS_EMAIL;
DELETE FROM OSSYS_EMAIL_CONTENT;
```

### Logs

The following SQL snippet deletes all login attempt log entries from all the general Service Center log tables:

```sql
DELETE FROM oslog_General_0
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_1
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_2
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_3
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_4
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_5
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_6
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_7
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_8
WHERE Message LIKE 'Login (%';
DELETE FROM oslog_General_9
WHERE Message LIKE 'Login (%';
```

### App Feedback

Use the following SQL snippet to find the physical table names of each of the App Feedback entities in the **ECT\_Provider** module that may contain personal information:

```sql
SELECT PHYSICAL_TABLE_NAME
FROM ossys_Entity
WHERE
    ESPACE_ID = (SELECT ID FROM ossys_Espace WHERE NAME = 'ECT_Provider')
    AND
    NAME IN ('Feedback', 'WebpageContent')
```

And then use each one of the physical table names with the following SQL snippet to delete all the data in each one of them:

```sql
DELETE FROM <each_found_PHYSICAL_TABLE_NAME>;
```

Where `<each_found_PHYSICAL_TABLE_NAME>` is the physical table name of each of the entities of **ECT\_Provider** module that you found in the previous step.

Note: The content of the **WebpageContent** entity must be the last one to be deleted due to foreign key referential constraints.
