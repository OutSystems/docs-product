---
summary: How to override the Base URL and the Basic Authentication credentials of a consumed REST API for a given environment.
tags: 
---

# Configure a Consumed REST API at Runtime

When you [consume a REST API](<consume-a-rest-api.md>) in your module, you must set the following information:

* Base URL
* Basic Authentication

The values you set in your module for these properties are the default settings. However, you can customize these settings for different environments, which override the default values.

This allows your application to consume a REST API with different configurations in different environments, without having to change or republish the module. For example, you may have a REST API URL for development and test purposes and a different one for production.

To configure the runtime settings of a REST API you are consuming, do the following:

1. Go to the Service Center management console of your OutSystems environment. 
1. Go to Factory section and open your application. 
1. Open the module where you are consuming the REST API. 
1. Select the Integrations tab and click on the consumed REST API name to edit it. 
1. Set the **effective URL** and/or **effective authentication credentials** for the current environment and click apply.   
  
![REST runtime configuration](images/rest-runtime-configuration-sc.png)
