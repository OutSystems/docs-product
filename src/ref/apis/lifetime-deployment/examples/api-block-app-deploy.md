---
summary: Learn how to block applications from being deployed to environments using the LifeTime API in OutSystems 11 (O11).
locale: en-us
guid: bcd187f6-c00a-409b-9e57-86c9781fb88a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: api integration, deployment automation, continuous delivery, software lifecycle management, outsystems api
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - tech leads
outsystems-tools:
  - lifetime
coverage-type:
  - remember
topic:
  - deployments-api-automation
---
# Block an app from deployment using the LifeTime API

To block an app from deployment using the APIs, follow these steps:

1. Get the **environment key** of the environment where you want to block the app. _(optional if you already have this information)_;

1. Get the **application key** of the desired application to be blocked._(optional if you already have this information)_;

1. Block the app using the information obtained in the previous steps

Here’s an example of API calls with requests and responses.

### Get environment key

If you do not know the environment key, then call the API method that returns all the environments available on your infrastructure.

Request: `GET /lifetimeapi/rest/v2/environments/`

Response:

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
        "Key": "849515f2-b4ff-4aca-a9d6-9407bea655f4",
        "Name": "Production",
        "OSVersion": "11.0.110.0",
        "Order": 1,
        "HostName": "prd-env-1.company.com",
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
Retrieve the environment key of the environment where you want to block the app from being deployed.

Example:

If you want to block an app from being deployed to production, retrieve the environment key of production:

Production environment key: **849515f2-b4ff-4aca-a9d6-9407bea655f4**

### Get application key

If you do not know the application key, then call the API method that returns all the available applications in the infrastructure to retrieve the app key 

Request: `GET /lifetimeapi/rest/v2/applications/`

Response body:

```javascript
[
     {...},
     {
        "Key": "c9a7a82e-0eee-4a3d-8e22-2a19c69c766f",
        "Name": "EmployeeBackoffice",
        "Kind": "WebResponsive",
        "Team": "",
        "Description": "",
        "URLPath": "/EmployeeBackoffice",
        "IconHash": "IconHash6a79e71e-c8e5-9e18-115c-cab789517672",
        "IconURL": "/LifeTimeSDK/ApplicationIcon.aspx?ApplicationKey=c9a7a82e-0eee-4a3d-8e22-2a19c69c766f",
        "IsSystem": false,
        "AppStatusInEnvs": []
      },
      {...}
]

```
Retrieve the app key of the app you want to block from deployment. 

Example: To block the EmployeeBackoffice app from deployment to production, retrieve 

EmployeeBackoffice application key: **c9a7a82e-0eee-4a3d-8e22-2a19c69c766f**


### Block or unblock the app from deployment

Call the API method that updates the app configurations to block or unblock the desired app in all the environments provided in the request.

API endpoint: `PUT /lifetimeapi/rest/v2/applications/{ApplicationKey}/configurations/`

Where {ApplicationKey} is the application key retrieved in the previous step. 

Configure the following in the PUT request body:

* Enter the **environmentKey** retrieved in the previous step.

* To block the app from deployment to the environment, set `isBlocked` to `true`. To unblock the app and allow deployment, set `isBlocked`  to `false.`

* Enter the reason for blocking or unblocking the app from deployment.

Request body:

```javascript
{
    "configurations": [
        {
          "environmentKey": "e80f23ca-218e-4da1-80db-402ff463da69",
          "isBlocked": true,
          "isBlockedChangeReason": "It's a sandbox app for demo purposes."
        }
      ]
}

```
The request should return a **204 No content** in order to be successful. 
