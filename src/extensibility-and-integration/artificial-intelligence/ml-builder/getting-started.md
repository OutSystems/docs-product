---
summary: How to get started with ML Builder and creating your model. 
tags:
---

# Getting started

<div class="info" markdown="1">

ML Builder is currently in a public **early access program (EAP)** and you need to register at the [ML Builder registration page](https://www.outsystems.com/eap-ml-builder/) to try it out.

</div>

To get started with ML Builder, do the following:

1. Sign in to the [ML Builder portal](https://mlbuilder.outsystems.com/) and register your non-production environment. When signing in, enter the name of your environment in **Environment**. For example, if the URL of the environment is **https://pp.example.com** enter **pp.example.com**. This is the **source environment** ML Builder connects to get data for training models.
    
    ![Sign into ML Builder](images/sign-in.png?width=280)

    <div class="info" markdown="1">

    Click on **How to select the best environment?** to read more about which environment to use.

    </div>

1. [Configure ML Builder](#configuration) to work with your Microsoft Azure subscription and set up your training machines and workspaces.

1. Install the ML Builder plugin in your development environment. In one of the setup steps click **Download the ML Builder plugin** to download the plugin and install it in the **development environment** where you develop apps and try out your models.

    ![ML Builder plugin](images/download-plugin.png?width=650)

1. [Create a model](creating-model.md) in the ML Builder app. Select your use case depending on what you want to predict, choose data, and let ML Builder create a model. Validate the performance in the model details page.

1. Implement the model in your app.

## Configuration { #configuration }

ML Builder requires Azure to create a model. The first time you log in, ML Builder asks you to set up your environment to work with Azure.

Follow the instructions in the wizard. You need the following configuration information:

* Subscription ID
* Application / Client ID
* Directory / Tenant ID
* Client secret
* Machine learning workspace and a training cluster
* Storage container and the connection string for storing data

For detailed instructions about the configuration of Microsoft Azure, check out [Setting up an AI provider](https://docs.google.com/document/d/167TZlQ4RIx1-Dm_3GEY9oO_sFQYsSuhHVTQXav73Bko/edit#heading=h.gjdgxs).