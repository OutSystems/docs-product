---
summary: OutSystems allows your IT users to authenticate an external IdP via OpenID Connect.
tags:
locale: en-us
guid: 722169AB-BF65-4357-89F3-0AF7D7D49264
app_type: traditional web apps, mobile apps, reactive web apps
---

# Authentication using an external identity provider

## Logging into OutSystems management consoles

When accessing any OutSystems management console (Service Center and LifeTime) without a valid session, the login screen displays  two options to login, **Login with SSO** or **Login with Username and Password**.

![Options to login to LifeTime](images/login-lt.png)

To login using SSO, follow these steps:

1. Click **Login with SSO**.

    The **Login** screen redirects the user to the IdP authentication flow.

    When the authentication flow finishes on the IdP, it redirects back to the platform, and performs a successful login (if the user exists in the platform).

### Logging out from OutSystems management consoles

When a user, authenticated using the IdP, attempts to log out, the platform logs the user out and redirects to the logout flow in the IdP.

## Logging into Service Studio

When a user logs into a Service Studio environment, they are redirected to a browser to complete the login instead of entering  a username and password.

To log into Service Studio using an IdP,  follow these steps:

1. Open **Service Studio**.

1. Click **Connect to Environment**.

    ![Click Connect to Environment](images/connect-ss.png)

1. Enter the environment URL and click **Next**.

    ![Enter environment and click Next](images/environment-ss.png)

    If the environment configuration to use an external IdP is correct, then the button changes to **Waiting to log in from your browser**.

    ![Waiting to log into browser](images/waiting-ss.png)

    At the same time, a new browser window opens to perform the IdP authentication flow. When the flow finishes, the browser displays a popup asking the user to **Open Service Studio**.

    ![Open Service Studio](images/open-ss.png)

1. Click the **Open Service Studio** button and complete the login process.

## Logging into Integration Studio

The flow to login into an environment is similar to the old one, with the developer being redirected to a browser to complete the login instead of typing the username and password.

To log into Integration Studio using an IdP,  follow these steps:

1. Access Integration Studio.

1. Click **Connect to Environment**.

    ![Click Connect to Environment](images/connect-is.png)

1. Enter the environment URL and click **Next**.

    ![Enter environment and click Next](images/environment-is.png)

    A message informing you to **Use the Identity Service website to complete the login process** is displayed.

    ![Use identity service website](images/identity-service-is.png)

   At the same time, a new browser window opens to perform the IdP authentication flow. When the flow finishes, the browser displays a popup asking the user to **Open Integration Studio**.

1. Click **Open Integration Studio** and complete the login process.

