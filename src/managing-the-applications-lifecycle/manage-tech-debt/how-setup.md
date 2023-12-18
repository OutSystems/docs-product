---
tags: 
summary: Learn about pre-requirements and how to setup AI Mentor Studio.
locale: en-us
guid: c9fd26ba-85ea-406d-834a-df6c0399d11a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/rEgQrcpdEWiKIORddoVydX/Managing%20the%20Applications%20Lifecycle?node-id=928:604
---

# How to set up AI Mentor Studio

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>
 
This topic shows you how to add an infrastructure to AI Mentor Studio and how to associate your IT user with AI Mentor Studio. 

<div class="info" markdown="1">

To change the language of AI Mentor Studio, select your user name, then select a language under **Language**.

![Screenshot showing how to change language settings in AI Mentor Studio by selecting the user name](images/select-language-ams.png "Selecting Language in AI Mentor Studio")

</div>

## Log in for the first time {#first-login}

You can log into [AI Mentor Studio](https://aimentorstudio.outsystems.com/) with your **OutSystems account** or with your **IT user account**. 

<div class="info" markdown="1">

IT administrators can enforce IT User authentication in a specific environment. If you’re logging into an environment with IT User authentication activated, you can only log in with your IT user account.

</div>

### Log in with OutSystems account {#os-login}

If you log in with your **OutSystems account**, AI Mentor Studio shows you the following welcome screen:

![Welcome screen in AI Mentor Studio for users logging in with an OutSystems account](images/welcome-os-ams.png "Welcome Screen for OutSystems Account in AI Mentor Studio")

Select one of the options shown on the welcome screen:

[Register and set up my infrastructure](#register)
:   Choose this option if your infrastructure isn't registered in AI Mentor Studio. You must have a LifeTime administrator role. If you don't have a LifeTime administrator role, you won't have this option available and you must ask your administrator to complete the setup.    

[Associate my IT user](#associate-os-login)
:   Choose this option if your infrastructure is already registered in AI Mentor Studio.  

[Use your IT user account](#it-user-login)
:   Choose this option if your administrator activated IT user authentication for your infrastructure.  

### Log in with IT user account {#it-user-login}

If you log in with your **IT user account** and your infrastructure isn’t registered yet, AI Mentor Studio shows you the following welcome screen:

![Welcome screen in AI Mentor Studio for users logging in with an IT user account](images/welcome-it-user-ams.png "Welcome Screen for IT User Account in AI Mentor Studio")

AI Mentor Studio shows you the option:

[Register and set up my infrastructure](#register)
:   Choose this option if your infrastructure isn't registered in AI Mentor Studio. You must have a LifeTime administrator role. If you don't have a LifeTime administrator role, you won't have this option available and you must ask your administrator to complete the setup.  

If you log in with your **IT user account** and your infrastructure is already registered, you’ll have to [associate your IT user](#associate-it-user-login).

## Register and set up your infrastructure in AI Mentor Studio {#register}

### Prerequisites

Before registering and setting up your infrastructure in AI Mentor Studio, make sure that the following requirements are met:

* Your infrastructure is associated with an [OutSystems Edition](https://www.outsystems.com/pricing-and-editions/) that isn't the Free Edition. **You can't use a Personal Environment with AI Mentor Studio**.

* **LifeTime** is deployed in a **dedicated environment**.

* Your code analisys environment uses **Platform Server 11.18.1** or later.

* Your LifeTime environment uses **LifeTime Management Console 11.16.1** or later.

* You have the **Administrator** role in your infrastructure.

* AI Mentor Studio will use the environment's public DNS hostname to communicate. Check [AI Mentor Studio network requirements](../../setup-maintain/setup/network-requirements.md#ai-mentor-studio) for detailed information.

<div class="info" markdown="1">

AI Mentor Studio probes prior to 5.0 require as minimum versions: Platform Server 11.7.2 and LifeTime Management Console Release Jul.2019.

</div>

### Register and set up your infrastructure

To set up your infrastructure in AI Mentor Studio, follow these steps:

<div class="info" markdown="1">

Depending on your authentication method, the interface might differ slightly from what you see in these screenshots.  

</div>

1. After logging into [AI Mentor Studio](https://aimentorstudio.outsystems.com/), select **Register and set up my infrastructure**.

1. Fill in your infrastructure information, or confirm it is correct in case it's already pre-filled. Then, click **Register**.

    ![Form for registering and setting up infrastructure information in AI Mentor Studio](images/infra-setup-ams.png "Infrastructure Setup in AI Mentor Studio")

1. Read the **AI Mentor Studio disclaimer** with the terms and conditions. If you agree, select **Accept and continue**.

1. Fill in your code analysis environment address, or confirm it is correct in case it's already pre-filled. Follow the procedure shown in AI Mentor Studio to install the code analysis probe:

    <div class="info" markdown="1">

    The code analysis environment is the environment in which AI Mentor Studio performs the code analysis.

    </div>

    ![Instructions for downloading and installing the code analysis probe in AI Mentor Studio](images/install-code-analysis-probe-ams.png "Installing Code Analysis Probe in AI Mentor Studio")

    1. Select **Download code analysis probe** to download the probe.

    1. In the Service Center of the **code analysis environment** (`https://<code_analysis_environment>/ServiceCenter`), go to **Factory**>**Solutions** and install the **code analysis probe**.

1. After completing the previous steps, select the **I confirm I completed all the steps above.** checkbox and select **Next**.

1. Fill in your LifeTime environment address, or confirm it is correct in case it's already pre-filled. Follow the procedure shown in AI Mentor Studio to install the LifeTime probe:

    ![Instructions for downloading and installing the LifeTime probe in AI Mentor Studio](images/install-lifetime-probe-ams.png "Installing LifeTime Probe in AI Mentor Studio")

    1. Select **Download LifeTime probe** to download the probe.

    1. In the Service Center of the **LifeTime environment** (`https://<lifetime_environment>/ServiceCenter`), go to **Factory**>**Solutions** and install the **LifeTime probe**.

1. After completing the previous steps, select the **I confirm I completed all the steps above.** checkbox and select **Next**.

1. After being redirected to LifeTime, log in with your IT user.

1. Configure the **code analysis probe** by selecting the development environment as the **Target environment**. 

    ![Configuring the target environment for the code analysis probe in LifeTime](images/setup-probe-environment-lt.png "Setting Up Probe Environment in LifeTime")

    <div class="info" markdown="1">

    To change the target environment of a code analysis probe, contact [technical support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support) to delete existing data from AI Mentor Studio. Do this before installing probes in a new environment or deleting probes from an existing environment to avoid data inconsistencies. Once existing data is deleted from AI Mentor Studio, follow the setup procedure in this article to configure a new target environment.
    
    </div>

1. Optional: If you want the AI Mentor Studio plugin to use a forward proxy while connecting to the AI Mentor Studio SaaS, in the **Proxy configuration** section, select **show request information**, and enter the proxy URL and the credentials.

1. Select **Save and activate**.

1. After being redirected to AI Mentor Studio:

    1. Check the **Installation details** and read the **privacy policy** carefully.

    1. If you agree with the privacy policy, select the checkbox and then select **Agree and continue**.

    ![Privacy policy agreement screen in AI Mentor Studio](images/privacy-policy-ams.png "AI Mentor Studio Privacy Policy")

After completing these steps, you can see your infrastructure listed, but it may take up to 12 hours for your apps to appear in AI Mentor Studio.

## Associate your IT user with AI Mentor Studio {#associate}

The steps to associate your IT user with AI Mentor Studio are different depending on the authentication mode you use. This section explains how to associate your IT user for **OutSystems account** authentication and **IT user account** authentication.

### Log in with OutSystems account {#associate-os-login}

If you log in with your **OutSystems account**, follow these steps to associate your IT user with AI Mentor Studio:

1. After logging into [AI Mentor Studio](https://aimentorstudio.outsystems.com/), select **Associate my IT user** and select **Start**.

1. Go to **LifeTime** (`https://<lifetime_environment>/lifetime`) and log in using your IT user credentials.

    `<lifetime_environment>` is the address of the LifeTime Environment for the infrastructure that you are associating with your account.

1. Select **Plugins** \> **AI Mentor Studio**.

    ![Navigating to the AI Mentor Studio plugin in the LifeTime application](images/select-plugin-lt.png "Selecting AI Mentor Studio Plugin in LifeTime")

    <div class="info" markdown="1">

    If your LifeTime doesn't have a **Plugins** menu, select **More** \> **AI Mentor Studio**.

    </div>

1. Select **Go to AI Mentor Studio**.

    ![Button to go to AI Mentor Studio from the LifeTime application](images/go-to-ai-mentor-studio-lt.png "Accessing AI Mentor Studio from LifeTime")

1. After being redirected to AI Mentor Studio:

    1. Check the **Installation details** and read the **privacy policy** carefully.

    1. If you agree with the privacy policy, select the check box and then select **Agree and continue**.

### Log in with IT user account {#associate-it-user-login}

If you log in with your **IT user account**, follow these steps to associate your IT user with AI Mentor Studio:

1. After logging into AI Mentor Studio:

    ![Privacy policy agreement screen in AI Mentor Studio](images/privacy-policy-ams.png "AI Mentor Studio Privacy Policy")

    1. Check the **Installation details** and read the **privacy policy** carefully.

    1. If you agree with the privacy policy, select the check box and then select **Agree and continue**.
