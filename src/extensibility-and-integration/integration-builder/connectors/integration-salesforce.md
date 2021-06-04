# Salesforce integration

## Prerequisites

* Make sure you meet the general [Integration Builder prerequisites](../set-up.md#prerequisites).
* Your OutSystems development environment can make HTTPS outbound requests to your Salesforce instance, available at `*.my.salesforce.com`.
* You have a Salesforce user with an Administrator role.

## Authorizing Integration Builder in Salesforce

Follow the instructions provided in [Creating and using an integration](../use.md#create-use). You must authorize Integration Builder to access your data (list of objects) through your Salesforce account.

![Authorizing Integration Builder in Salesforce](images/salesforce-authorize.png)

Integration Builder uses this authorization to obtain the available objects for building a Salesforce integration.

Additionally, when you're creating a connection, Integration Manager connects to Integration Builder, requesting the creation of a Salesforce connected app. This operation uses the same authorization, since only Integration Builder has the access tokens for this authorization.

## Authorizing a Salesforce connection

Salesforce integrations generated with Integration Builder use an access token to authenticate requests.

Integration Builder creates a connected app in Salesforce at the request of Integration Manager. Then, Integration Builder returns the obtained access token for this specific app to Integration Manager. Integration Manager saves this access token in an encrypted way as part of the connection information.

Request authentication is handled transparently when you call Server Actions exposed by the service module (the module with a "_IS" suffix, by default). The Server Actions obtain the token from the connection that you previously associated with the integration in Integration Manager. Therefore, you don't need to provide a token as an input parameter.

## Connection fields

* **Email address of the app administrator** — The email address that Salesforce uses to contact you or your support team.

* **Salesforce username** — The username of the Salesforce account that you want to associate with all requests that Integration Builder sends to the Salesforce API. Salesforce usernames look like email addresses (for example, john@example.com) but don't have to be an actual email address.  
    If you're not sure, search your inbox for the following emails that include your username: "Subject: Welcome to Salesforce: Verify your account", or "Subject: Finish resetting your Salesforce".

### Use the integration in Service Studio

Check [how to use the integration in Service Studio](../use.md#use).
