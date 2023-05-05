---
tags: 
summary: Learn about pre-requirements and how to setup AI Mentor Studio.
locale: en-us
guid: c9fd26ba-85ea-406d-834a-df6c0399d11a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# How to set up AI Mentor Studio

<div class="info" markdown="1">

Architecture Dashboard is now AI Mentor Studio.

</div>
 
This topic shows you how to add an infrastructure to AI Mentor Studio and how to associate your IT user with AI Mentor Studio. 

<div class="info" markdown="1">

To change the language of AI Mentor Studio, select your user name, then select a language under **Language**.

![Change language](images/select-language-ams.png)

</div>

## Log in for the first time {#first-login}

You can log into [AI Mentor Studio](https://aimentorstudio.outsystems.com/) with your **OutSystems account** or with your **IT user account**. 

<div class="info" markdown="1">

IT administrators can enforce IT User authentication in a specific environment. If you’re logging into an environment with IT User authentication activated, you can only log in with your IT user account.

</div>

### Log in with OutSystems account {#os-login}

If you log in with your **OutSystems account**, AI Mentor Studio shows you the following welcome screen:

![Welcome screen for OutSystems login](images/welcome-os-login-ams.png)

Select one of the options shown on the welcome screen:

[Log in with IT user account](#it-user-login)
:   Choose this option if you want to access an infrastructure that uses IT user authentication or if your infrastructure isn't registered in AI Mentor Studio yet. You can only register a new infrastructure if you log in with your IT user account. When selecting this option, you’re redirected to the login page again to log in with your IT user account.

[Associate my IT user](#associate-os-login)
:   Choose this option if your infrastructure is already registered in AI Mentor Studio.

### Log in with IT user account {#it-user-login}

If you log in with your **IT user account** and your infrastructure isn’t registered yet, AI Mentor Studio shows you the following welcome screen:

![Welcome screen for IT user login](images/welcome-it-login-ams.png)

AI Mentor Studio shows you the option:

[Set up AI Mentor Studio](#register)
:   Choose this option if your infrastructure isn't registered in AI Mentor Studio. You must have a LifeTime administrator role. If you don't have a LifeTime administrator role, you won't have this option available and you must ask your administrator to complete the setup.

If you log in with your **IT user account** and your infrastructure is already registered, you’ll have to [associate your IT user](#associate-it-user-login).

## Register and set up your infrastructure in AI Mentor Studio {#register}

### Prerequisites

Before registering and setting up your infrastructure in AI Mentor Studio, make sure that the following requirements are met:

* Your infrastructure is associated with an [OutSystems Edition](https://www.outsystems.com/pricing-and-editions/) that isn't the Free Edition. **You can't use a Personal Environment with AI Mentor Studio**.

* **LifeTime** is deployed in a **dedicated environment**.

* Your infrastructure uses **OutSystems 11**.

* Your development environment uses **Platform Server 11.7.2** or later.

* Your LifeTime environment uses **LifeTime Management Console Release Jul.2019** or later.	

* Allow inbound and outbound HTTPS communication (port 443) with `https://aimentorstudio.outsystems.com`. The AI Mentor Studio will use the environment's public DNS hostname to communicate. Check [AI Mentor Studio network requirements for detailed information](../../setup-maintain/setup/network-requirements.md#ai-mentor-studio).

* You have the **Administrator** role in your infrastructure.

### Register and set up your infrastructure

To set up your infrastructure in AI Mentor Studio, follow these steps:

1. After logging into [AI Mentor Studio](https://aimentorstudio.outsystems.com/) with your IT user account, select **Set up AI Mentor Studio**.

1. Your infrastructure information is already pre-filled. Confirm your infrastructure name and your time zone, and then click **Register**.

    ![Register infrastructure step](images/infra-setup-ams.png)

1. Read the **AI Mentor Studio disclaimer** with the terms and conditions. If you agree, select **Accept and continue**.

1. Your code analysis environment address is already pre-filled. Follow the procedure shown in AI Mentor Studio to install the code analysis probe:

    <div class="info" markdown="1">

    The code analysis environment is the environment in which AI Mentor Studio performs the code analysis.

    </div>

    ![Install code analysis probe](images/code-analysis-probe-ams.png)

    1. Select **Download code analysis probe** to download the probe.

    1. In the Service Center of the **code analysis environment** (`https://<development_environment>/ServiceCenter`), go to **Factory**>**Solutions** and install the **code analysis probe**.

1. After completing the previous steps, select the **I confirm I completed all the steps above.** checkbox and select **Next**.

1. Your LifeTime environment address is already pre-filled. Follow the procedure shown in AI Mentor Studio to install the LifeTime probe:

    ![Install the LifeTime probe](images/lifetime-probe-ams.png)

    1. Select **Download LifeTime probe** to download the probe.

    1. In the Service Center of the **LifeTime environment** (`https://<lifetime_environment>/ServiceCenter`), go to **Factory**>**Solutions** and install the **LifeTime probe**.

1. After completing the previous steps, select the **I confirm I completed all the steps above.** checkbox and select **Next**.

1. After being redirected to LifeTime, log in with your IT user.

1. Configure the **code analysis probe** by selecting the development environment as the **Target environment**. 

    ![Configure the Code analysis](images/setup-probe-environment-lt.png)

    <div class="info" markdown="1">

    To change the target environment of a code analysis probe, contact [technical support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support) to delete existing data from AI Mentor Studio. Do this before installing probes in a new environment or deleting probes from an existing environment to avoid data inconsistencies. Once existing data is deleted from AI Mentor Studio, follow the setup procedure in this article to configure a new target environment.
    
    </div>

1. Optional: If you want the AI Mentor Studio plugin to use a forward proxy while connecting to the AI Mentor Studio SaaS, in the **Proxy configuration** section, select **show request information**, and enter the proxy URL and the credentials.

1. Select **Save and activate probes**.

1. After being redirected to AI Mentor Studio:

    1. Check the **Installation details** and read the **privacy policy** carefully.

    1. If you agree with the privacy policy, select the checkbox and then select **Agree and continue**.

    ![Accept privacy policy](images/privacy-policy-ams.png)

After completing these steps, you can see your infrastructure listed, but it may take up to 12 hours for your apps to appear in AI Mentor Studio.

## Associate your IT user with AI Mentor Studio {#associate}

The steps to associate your IT user with AI Mentor Studio are different depending on the authentication mode you use. This section explains how to associate your IT user for **OutSystems account** authentication and **IT user account** authentication.

### Log in with OutSystems account {#associate-os-login}

If you log in with your **OutSystems account**, follow these steps to associate your IT user with AI Mentor Studio:

1. After logging into [AI Mentor Studio](https://aimentorstudio.outsystems.com/), select **Associate my IT user** and select **Start**.

1. Go to **LifeTime** (`https://<lifetime_environment>/lifetime`) and log in using your IT user credentials.

    `<lifetime_environment>` is the address of the LifeTime Environment for the infrastructure that you are associating with your account.

1. Select **Plugins** \> **AI Mentor Studio**.

    ![Select AI Mentor Studio plugin](images/select-plugin-lt.png)

    <div class="info" markdown="1">

    If your LifeTime doesn't have a **Plugins** menu, select **More** \> **AI Mentor Studio**.

    </div>

1. Select **Go to AI Mentor Studio**.

    ![Setup AI Mentor Studio plugin](images/go-to-ai-mentor-studio-lt.png)

1. After being redirected to AI Mentor Studio:

    1. Check the **Installation details** and read the **privacy policy** carefully.

    1. If you agree with the privacy policy, select the check box and then select **Agree and continue**.

### Log in with IT user account {#associate-it-user-login}

If you log in with your **IT user account**, follow these steps to associate your IT user with AI Mentor Studio:

1. After logging into AI Mentor Studio:

    ![Accept privacy policy](images/privacy-policy-ams.png)

    1. Check the **Installation details** and read the **privacy policy** carefully.

    1. If you agree with the privacy policy, select the check box and then select **Agree and continue**.
