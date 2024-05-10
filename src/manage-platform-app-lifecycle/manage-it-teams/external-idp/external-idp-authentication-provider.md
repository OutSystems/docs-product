---
summary: OutSystems 11 (O11) supports authentication using an external identity provider for management consoles, Service Studio, and Integration Studio.
tags:
locale: en-us
guid: 722169AB-BF65-4357-89F3-0AF7D7D49264
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing-the-Applications-Lifecycle?type=design&node-id=1917%3A8229&mode=design&t=qy82U3bMoQChCp6y-1
---

# Authentication using an external identity provider

## Logging into OutSystems management consoles

When accessing any Outsystems management console (Service Center and Lifetime) without a valid session, the user is redirected to the external IdP login screen. When the authentication flow finishes on the IdP, it redirects back to the platform and performs a successful login (if the user exists in the platform).

![Screenshot of the external identity provider login screen for OutSystems management consoles](images/login.png "External IdP Login Screen")

## Logging out from OutSystems management consoles

When a user, authenticated using the IdP, attempts to log out, the platform logs the user out and redirects to the logout flow in the IdP.

## Logging into Service Studio

When a user logs into a Service Studio environment, they are redirected to a browser to complete the login instead of entering a username and password.

To log into Service Studio using an IdP,  follow these steps:

1. Open **Service Studio**.

1. Click **Connect to Environment**.

    ![Service Studio interface showing the 'Connect to Environment' button](images/connect-ss.png "Connect to Environment in Service Studio")

1. Enter the environment URL and click **Next**.

    ![Entering the environment URL in Service Studio for IdP authentication](images/environment-ss.png "Enter Environment URL in Service Studio")

    If the environment configuration to use an external IdP is correct, then the button changes to **Waiting to log in from your browser**.

    ![Service Studio screen displaying 'Waiting to log in from your browser' message during IdP authentication](images/waiting-ss.png "Waiting to Log in from Browser")

    A new browser window opens to perform the IdP authentication flow. When the flow finishes, the browser displays a pop-up asking the user to **Open Service Studio**.

    ![Browser pop-up asking to open Service Studio after IdP authentication](images/open-ss.png "Open Service Studio Prompt")

1. Click the **Open Service Studio** button and complete the login process.

## Logging into Integration Studio

The flow to login into an environment is similar to the old one, with the developer being redirected to a browser to complete the login instead of typing the username and password.

To log into Integration Studio using an IdP,  follow these steps:

1. Access Integration Studio.

1. Click **Connect to Environment**.

    ![Integration Studio interface showing the 'Connect to Environment' button](images/connect-is.png "Connect to Environment in Integration Studio")

1. Enter the environment URL and click **Next**.

    ![Entering the environment URL in Integration Studio for IdP authentication](images/environment-is.png "Enter Environment URL in Integration Studio")

    A message displays informing you to **Use the Identity Service website to complete the login process**.

    ![Message instructing to use the Identity Service website to complete the login process in Integration Studio](images/identity-service-is.png "Identity Service Login Prompt")

   A new browser window opens to perform the IdP authentication flow. When the flow finishes, the browser displays a pop-up asking the user to **Open Integration Studio**.

1. Click **Open Integration Studio** and complete the login process.

