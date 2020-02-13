---
summary: Check how you can troubleshoot REST APIs by temporarily setting higher logging levels.
tags: 
---

# Troubleshoot a REST API

OutSystems keeps track of all requests and responses of your REST API, namely, a time log of all request/response activity and content.

To access the logs of your REST API, do the following:

1. Go to the Service Center management console of your OutSystems environment. 
1. Go to the **Monitoring** section and select **Integrations**. 
1. In "Type", filter the logging you want to see: `REST (Consume)` or `REST (Expose)`. 
1. Click **Filter**. 

## Set Logging Level

Use the logging level of a module to store detailed information about requests and responses.

To configure the logging level of your REST API, do the following:

1. Go to the Service Center management console of your OutSystems environment. 
1. Go to the **Factory** section and open your application. 
1. Open the module containing your REST API. 
1. Select the **Integrations** tab and click on the REST API name to edit it. 
1. Set the "Logging Level" to the value you want. 
1. Click **Apply**. 

Because logs are stored within the environment, increasing the logging level implies:

* More information is logged, therefore, more information is stored in the database.
* Input and output parameters values are logged with the request, thus making any sensitive information passing through these parameters available in the environment console.
