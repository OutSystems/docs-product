---
summary: How to define user classification rules for identifying Internal Users.
---

# Classify Users as Internal Users

<div class="info" markdown="1">

Applies to OutSystems licenses purchased after January 2020.

</div>

OutSystems identifies two different types of registered end users for licensing purposes: [**Internal Users** and **External Users**](intro.md#internal-external).

OutSystems classifies registered users according to the following rules:

![](images/classify_internal_users.png?width=750)

*When adding a new environment, all your users are internal by default. [Check here how to configure external users](https://success.outsystems.com/Documentation/11/Developing_an_Application/Secure_the_Application/End_User_Management/Classify_Users_as_Internal_Users#Configuring_the_users_to_be_internal_or_external
).

## Defining user classification rules

Classification rules are configured per environment using Service Center, and you can have different classification rules in different environments. 

<div class="info" markdown="1">
Note that when adding a new environment, all your users are internal by default.
</div>

OutSystems checks for registered [active users](add-delete-users.md#activate-deactivate) when determining the number of Internal/External Users in an environment. Also, user classification in Internal Users or External Users applies only to **Registered Users** (or Named Users). 

Anonymous Users aren't taken into account for this classification. Check [End User Management](intro.md) for more information on end user classification.

So, let’s look at these rules in detail.

### Ensuring that users are ready to be classified as Internal and External

To be able to configure your users as internal or external make sure that:

1. Your users have a valid email address. This email address **can exist** in the **Username** field or **Email** field of [your user](add-delete-users.md).

1. You keep in mind that **users without a valid email address will always be classified as Internal Users**.

### Configuring the users to be internal or external 

You can configure your users to be internal or external by using Internal User domains. The **User Classification rules** field can contain one or more domains separated by commas.

OutSystems considers that a subdomain is a different value from its domain. To classify users based on a subdomain, add a value to the **User Classification rules*** field for the subdomain.

For example, to classify a user with the email address `scott.green@sales.mycompany.com` as an Internal User, the **User Classification rules** field value must contain the `sales.mycompany.com` subdomain.

**To configure your internal user domains, do the following:**

1. Open the Service Center management console of your environment.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

1. In **User Classification Rules**, select the option **Only users registered with these domains count as Internal** and enter the domain names associated with the email addresses of Internal Users. 

    Separate multiple domains using a `,` (comma) character.

    For example, `mycompany.com` and `sales.mycompany.com`:

    ![](images/sc-user-classification-rules.png?width=900)

1. Click **Save**.

After saving your changes, OutSystems starts the process of obtaining the current Internal/External User count. This process might take a few minutes. The **Last update on** label displays the finish date/time of the last user count process.

## User classification examples

Let’s look to some examples on how to classify users.

In this example, consider that the following user domains were added in the User Classification rules field:

`mycompany.com,sales.mycompany.com`

By adding these two domains, the following examples detail the classification of each user according to their Email and Username attribute values:

|Username|Email|User Classification|
|---|---|---|
|sgreen|scott.green@mycompany.com|Considered an **Internal User**|
|sgreen|scott.green@sales.mycompany.com|Considered an **Internal User**|
|jane.green@mycompany.com|`<empty>`|Considered an **Internal User**|
|sjones|scarlett.jones@outsourcing.com|Considered an **External User**|
|sdavidson|samantha.davidson@finance.mycompany.com|Considered an **External User**, because classification rules consider subdomains different from domains (`sales.mycompany.com <> mycompany.com`)|
|mjohnson|`<empty>`|Considered an **Internal User**|

## Check the total number of Internal/External users

You can check the current usage of Internal and External Users — both the total number of each end user type and their distribution per User Provider — for a given environment in Service Center.

To check the number of Internal/External Users do the following:

1. Open the Service Center management console of the environment.

1. Navigate to **Administration** > **Licensing** and click the "End-Users Configuration" link.

![](images/sc-end-users-configuration.png?width=900)

This page displays the total number of Internal and External Users, as well as their distribution per User Provider in the current environment. 

**Note:** A timer executes the process of determining the current user count, and therefore the displayed user count values might not reflect the exact user count.
