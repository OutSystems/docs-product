---
summary: How to define user classification rules for identifying Internal Users.
---

# Classify Users as Internal Users

<div class="info" markdown="1">

Applies to OutSystems licenses purchased after January 2020.

</div>

OutSystems identifies two different types of registered end users for licensing purposes: [**Internal Users** and **External Users**](intro.md#internal-external).

You can classify all Registered Users whose email address contains a specific domain (e.g., `mycompany.com`) as Internal Users, while all other Registered Users are considered External Users.

The list of one or more domains used to identify users as Internal Users is defined in **classification rules**. All users whose email address contains one of the domains contained in the classification rules are considered **Internal Users**. Every other Registered User is considered an **External User**.

For example, if you set the classification rules to `mycompany.com`:

* A Registered User whose email address is `scott.green@mycompany.com` is considered an Internal User.
* A Registered User whose email address is `scarlett.doe@outsourcing.com` is considered an External User.

The user classification rules are checked against the user's email address field, if it contains a value, or to the username, if the field value contains an email address. Any Registered Users that do not have a valid email address in one of these fields are classified as Internal Users. 

The configuration of classification rules is done per environment in Service Center, and you can configure different classification rules in different environments. OutSystems checks for registered [active users](add-delete-users.md#deactivate) when determining the number of Internal/External Users in an environment.

Note that this classification applies only to Registered Users (or Named Users). Anonymous Users are not taken into account for this classification. Check [End User Management](intro.md) for more information on end user classification.

## Define user classification rules

To define the list of domain names used to identify Internal Users do the following:

1. Open the Service Center management console of your environment.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

1. In "User Classification Rules", select the option "Only users registered with these domains count as Internal" and enter the domain names associated with the email addresses of Internal Users. Separate each domain with a comma.

    E.g., `mycompany.com`

    ![](images/sc-user-classification-rules.png?width=900)

1. Press **Save**.

After saving your changes, OutSystems starts the process of obtaining the current Internal/External User count. This process might take a few minutes. The "Last update on" label displays the finish date/time of the last user count process.

## Check the total number of Internal/External Users

You can check the current usage of Internal and External Users — both the total number of each end user type and their distribution per User Provider — for a given environment in Service Center.

To check the number of Internal/External Users do the following:

1. Open the Service Center management console of the environment.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

![](images/sc-end-users-configuration.png?width=900)

This page displays the total number of Internal and External Users, as well as their distribution per User Provider in the current environment. 

Note: The process of determining the current user count is executed based on a timer, and therefore the displayed user count values might not reflect the exact user count.
