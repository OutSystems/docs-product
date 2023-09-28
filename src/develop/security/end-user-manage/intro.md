---
summary: Learn about end user licensing on OutSystems.
tags: support-Mobile_Apps; support-webapps
locale: en-us
guid: 907b0fd3-bc46-4391-aae2-673296d795d9
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# End Users
An end user is a unique individual who uses your OutSystems apps. Each non-anonymous end user who interacts with your apps counts toward the end user capacities established on your subscription. People who develop your OutSystems apps but do not use them are not considered end users.

## Internal and external end users
You license internal and external end user capacities separately on your subscription. Each end user of your OutSystems applications is classified as either internal or external. Internal is intended for employees and contractors of your organization. External is for your customers, partners, or other external parties who use your OutSystems apps.

By default in OutSystems, all end users are classified as internal until you configure the domains that you own. You only need to configure your domains when you license external end user capacity on your subscription, because doing so allows you to track the internal and external end user counts separately. Within Service Center (for OutSystems 11) or within the ODC Portal (for OutSystems Developer Cloud) you can configure domains that you own. When you do this, all end users with email addresses belonging to these domains are classified as internal, and all end users with email addresses outside these domains are classified as external. For example, if your organization owns `example.com` and the end user's email is `adam@example.com`, then the end user will be classified as internal. Make sure to configure all the email domains used by employees who use your apps, including domains owned by your parent or affiliate organizations.  

In OutSystems 11, when an end user has no email address stored on their profile, such as when you only capture a mobile phone number for the end user, this is counted as an internal end user. All users in OutSystems Developer Cloud must have an email address.

Independent Software Vendors (ISVs) and Managed Services Providers (MSPs) delivering apps to their clients should configure the domains of their clients (rather than the domains of their own company) as internal within Service Center or the ODC Portal. Internal and external end users are from the perspective of the client that is licensing usage of apps from the ISV or MSP, not from the perspective of the ISV or MSP that is licensing the OutSystems platform.

## Anonymous end users
Anonymous end users don't count toward the end user capacities specified in your subscription. Users who use your apps and who don't log in and also don't share any personally-identifiable information (name, email, mobile phone, etc.) are anonymous. For example, people who visit your website (that is an OutSystems app) and just browse the information without logging in or providing personal information are anonymous end users.

## End user limits
OutSystems subscriptions typically include rights to run applications serving up to a specific number of internal end users and a specific number of external end users, with options for upgrading these end user capacities that vary by subscription. When you exceed the internal or external end user capacities specified on your subscription, you need to upgrade to remain in compliance with the license terms. Please contact your OutSystems sales representative for assistance.

Some customers have more than one production runtime in the same OutSystems 11 infrastructure where their apps are hosted and delivered to end users. Each production runtime in OutSystems 11 has its own independent database that tracks the end users who access apps hosted on that runtime. When the same individual accesses apps hosted on multiple runtimes, this individual is tracked as an end user in each and contributes to the reported end user count in each. Nonetheless, customers only need to license end user capacities sufficient to cover the *unique* end users accessing apps within the same OutSystems 11 infrastructure.

## Managing your end users
You may periodically de-activate end users who you know will not continue to use your applications and these users, upon de-activation, will going forward no longer count toward your licensed end user capacities. For example, when an employee quits, you would de-activate this user because they will no longer need access to apps you've built for your employees.

For OutSystems 11:
- [Manage end users](accessing-users.md) through the **Users** console, which is available at `http://<environment address>/Users`.
- Manage end users programmatically using the [Users API](../../../ref/apis/auto/users-api.final.md)

For OutSystems Developer Cloud:
- [User management](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/)

## Older subscription models
Installations of OutSystems 11.6 and earlier do not support classifying internal vs. external end users, so customers should update to the latest version to take advantage of this. Also, in the past, some OutSystems subscriptions only licensed "named" users which did not require end users to be classified as internal or external.

## Related resources
* [Classify Users as Internal Users](classify-internal-users.md): includes information on configuring your email domains, for purposes of classifying users as internal or external
* [End User Authentication](end-user-authentication/intro.md): information on external authentication methods
* [Managing IT users](../../../managing-the-applications-lifecycle/manage-it-teams/intro.md): manage developer access, administrators, and other roles with access to OutSystems management tools
* [Group management](groups.md): creating and managing groups of users
* [Multi-tenant applications](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/How_to_Build_a_Multi-tenant_Application#Managing_Tenants_and_End-Users): managing different cohorts of users from different tenants
