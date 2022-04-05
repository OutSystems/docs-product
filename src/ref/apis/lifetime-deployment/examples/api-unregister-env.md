---
summary: Learn how to unregister an environment using the LifeTime API.
tags:
---

# Unregister an Environment using the LifeTime API

In this example we will perform the following generic steps using API calls:

1. Get the **environment key** of the environment to unregister from LifeTime _(optional if you already have this information)_;

1. Unregister the **environment** from LifeTime.

Check below for example API calls (requests and responses) for each of the presented steps.

## 1. Get environment key

We start by calling the API method that returns all the environments available in the infrastructure (only necessary when we don't have this information yet):

Request: `GET /lifetimeapi/rest/v2/environments/`

Response body:

```javascript
[
  {
    "Key": "f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e",
    "Name": "Development",
    "OSVersion": "11.0.110.0",
    "Order": 0,
    "HostName": "dev-env.company.com",
    "UseHTTPS": true,
    "EnvironmentType": "Development",
    "NumberOfFrontEnds": 1,
    "ApplicationServerType": ".NET",
    "ApplicationServer": "IIS",
    "DatabaseProvider": "SQLServer",
    "IsCloudEnvironment": false
  },
  {
    "Key": "c7155bc0-2154-4b8e-9570-df86cad30b40",
    "Name": "Test",
    "OSVersion": "11.0.110.0",
    "Order": 1,
    "HostName": "tst-env.company.com",
    "UseHTTPS": true,
    "EnvironmentType": "Development",
    "NumberOfFrontEnds": 1,
    "ApplicationServerType": ".NET",
    "ApplicationServer": "IIS",
    "DatabaseProvider": "SQLServer",
    "IsCloudEnvironment": false
  },
  {
    "Key": "1ee9297b-edfc-4826-ad95-2a8a6e40957f",
    "Name": "Production",
    "OSVersion": "11.0.110.0",
    "Order": 2,
    "HostName": "prd-env.company.com",
    "UseHTTPS": true,
    "EnvironmentType": "Production",
    "NumberOfFrontEnds": 1,
    "ApplicationServerType": ".NET",
    "ApplicationServer": "IIS",
    "DatabaseProvider": "SQLServer",
    "IsCloudEnvironment": false
  }
]
```
As we want to unregister the "Production" environment, we take note of its key so that we can use it in the next API call:

"Production" environment key: **1ee9297b-edfc-4826-ad95-2a8a6e40957f**

## 2. Unregister environment

Next, we call the API method to unregister the environment from LifeTime. We start by taking the API method "template" URL used to unregister an environment:

`DELETE /lifetimeapi/rest/v2/environments/{EnvironmentKey}`

We then change the {EnvironmentKey} placeholder to the correct value and perform the following request:

Request: `DELETE /lifetimeapi/rest/v2/environments/{1ee9297b-edfc-4826-ad95-2a8a6e40957f}`
