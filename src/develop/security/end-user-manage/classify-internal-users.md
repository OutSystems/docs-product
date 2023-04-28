---
summary: End user classification
locale: en-us
guid: 8cb73d92-a60d-4133-9f95-67ef4505932d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# End user classification: internal or external

By default, all end users are considered internal until you configure specific domains that you own within Service Center. When you specify the domains that you own, any users with an email address matching those domains will be classified as internal, and any other email domains will be classified as external. Users without an email on their profile are classified as internal. This is important since you license internal and external end user capacities separately. [Learn more](intro.md)

## How to configure your domains

1. Open the Service Center management console.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

1. Under **User Classification Rules**, select **Only users registered with these domains count as Internal** and enter the domain names that you own. 

    ![](images/sc-user-classification-rules.png?width=900)

1. Click **Save**.

After saving your changes, OutSystems starts the process of calculating the current internal and external end users, which might take a few minutes. The totals are recalculated periodically using a timer process. The **Last update on** indicates the last time the user counts were calculated.

## How end users are counted when using different authentication providers 

It is possible to have apps that each use different authentication providers, such as one app using internal authentication (the built-in authentication offered with OutSystems) and another using Okta or Azure Active Directory. In this situation, you might have a user who logs into one app using their identity stored in the built-in authentication provider, and then logs into another app using their Okta identity, but both identities use the same email. Starting with Platform Server version 11.11.3, this is counted as one user. Prior to that version, these were counted as separate users.

### Related pages
[Manage end users](add-delete-users.md)

[Users application](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/Access_the_Users_application)
