---
summary: Understand the difference between two types of end-users (internal users and external users) and how you can define the end-user classification rules.
---

# Internal Users vs External Users

<div class="info" markdown="1">

Applies to OutSystems licenses purchased after January 2020.

</div>

OutSystems identifies two different types of end-users for licensing purposes:

* **Internal users** – individuals employed by your organization that are registered end-users of your OutSystems applications.

* **External users** – individuals not employed by your organization that are registered end-users of your OutSystems applications.

By default, all end-users are considered **internal users**.

However, you can classify all users whose email address contains a specific domain (e.g. `mycompany.com`) as internal users, while all other end-users should be considered external users.

The list of one or more domains used to identify internal users is defined in **classification rules**. Any end-users whose email address contains one of the domains contained in the classification rules are considered **internal users**. Every other user is considered an **external user**.

For example, if you set the classification rules to "mycompany.com":

* An end-user registered with the "scott.green@mycompany.com" email address is considered an internal user.
* An end-user registered with the "scarlett.doe@outsourcing.com" email address is considered an external user.

The user classification rules are checked against the user's email address field, if it contains a value, or to the username, if the field value contains an email address. Any end-users that do not have a valid email address in one of these fields will be classified as internal users.

The configuration of classification rules is done per environment in Service Center, and you can configure different classification rules in different environments. OutSystems checks for [active users](add-delete-users.md#deactivate) when determining the number of internal/external users in an environment.

<div class="info" markdown="1">

The distinction between internal users and external users is only applicable to the **end-users** of your OutSystems applications. [IT users](../../../managing-the-applications-lifecycle/manage-it-teams/intro.md) (e.g. OutSystems developers or Administrators) are a separate set of users that don't have this distinction.

</div>


## Define end-user classification rules

To define the list of domain names that will define what end-users are internal users do the following:

1. Open the Service Center management console of your environment.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

1. In "User Classification Rules", select the option "Only users registered with these domains count as Internal" and enter the domain names associated with the internal users' email addresses. Separate each domain with a comma.

    E.g. `mycompany.com`

    ![](images/sc-user-classification-rules.png?width=900)

1. Press **Save**.

After saving your changes, OutSystems starts the process of obtaining the current internal/external user count. This process might take a few minutes. The "Last update on" label displays the finish date/time of the last user count process.


## Check the total number of internal/external users

You can check the current usage of internal and external users — both the total number of each end-user type and their distribution per user provider — for a given environment in Service Center.

To check the number of internal/external users do the following:

1. Open the Service Center management console of the environment.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

![](images/sc-end-users-configuration.png?width=900)

This page displays the total number of internal and external users, as well as their distribution per user provider in the current environment. 

Note: The process of determining the current user count is executed based on a timer, and the displayed user count values might not reflect the exact user count.
