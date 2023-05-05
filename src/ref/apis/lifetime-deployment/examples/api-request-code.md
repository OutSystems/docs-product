---
summary: Learn how to get the source code of an application for static code analysis. OutSystems provides an API that lets you download the code. 
locale: en-us
guid: 8DD3FD53-11F9-4CE4-9251-BACDA78F7D1C
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Get the source code of an application

For OutSystems customers security is an important aspect of an application development cycle. A common security best practice recommends that the code should be analyzed statically (SAST).

OutSystems platform provides an API that enables our customers to download the generated code for the current running apps. The source code package returned by the API contains the server-side code and the native code, if it’s a mobile application.

This will leverage the customers' ability to request the source code of an OutSystems application and run-it against one of the SAST tools they might use in-house.

<div class = "info" markdown="1">

The code shared in the API will be as much as possible the same as the one running on the server. For security and licensing reasons, some files with configurations, secrets and proprietary code will not be shared by the API.

</div>


## Prerequisites

To download the source code of an app, ensure that you have the following:

* Environment from where you want to get the source code must comply with the following:
    * Platform Server version 11.19.0 or higher
    * Only available on non-production environments
* LifeTime version 11.16.1 or higher
* [LifeTime Service Account](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/LifeTime_API_v2/REST_API_Authentication)
    * Service Account needs Full Control on the environment

 
## Process Overview 

To request the source code of an application, follow these steps:

1. Get the **environment key** of the environment where you want to request the application source code (move ahead if you already have this information).
1. Get the **application key** of the application you want to request the source code (move ahead if you already have this information).
1. Get the **package key** of the application source code you want to request.
1. Check the **status** of the application source code packaging you want to request.
1. Once done, get the **download link** of the application source code package you want to request.
1. Download the application source code package you want to request.

Read the example API calls (requests and responses) below for each of the presented steps.

### 1 - Get the environment key

We start by calling the API method that returns all the environments available on your infrastructure (only necessary if we don't know the environment key yet):

Request: `GET /lifetimeapi/rest/v2/environments/`

Response body:

```
[
    {...},
    {
        "Key": "849515f2-b4ff-4aca-a9d6-9407bea655f4",
        "Name": "Testing",
        "OSVersion": "11.18.1.0",
        "Order": 2,
        "HostName": "hostname.outsystems.com",
        "UseHTTPS": true,
        "EnvironmentType": "Test",
        "NumberOfFrontEnds": 1,
        "ApplicationServerType": ".NET",
        "ApplicationServer": "IIS",
        "DatabaseProvider": "SQLServer",
        "IsCloudEnvironment": true,
        "IsOffline": false
    },
    {...}
]
```

Since we want to request the source code of an application in our environment of type "NonProduction", we chose the environment "Testing", we take note of its key so that we can use it in the upcoming API calls.

Example of an environment key: **849515f2-b4ff-4aca-a9d6-9407bea655f4**

### 2 - Get the application key

Next, we call the API method that returns all the available applications in the infrastructure to get the application key. You can skip this step if you already have the application key. 

Request: `GET /lifetimeapi/rest/v2/applications/`

Response body:

```
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

We want to request the application source code for the "EmployeeBackoffice" application. We take note of its key so that we can use it in the next API calls:

Example "EmployeeBackoffice" application key: **c9a7a82e-0eee-4a3d-8e22-2a19c69c766f**

### 3 - Get the package key

We start by taking the API method "template" URL used to get the source code package key for an application on a given environment.

`POST/environments/{EnvironmentKey}/applications/{ApplicationKey}/sourcecodeaccess`


We then change the `{EnvironmentKey}` and `{ApplicationKey}` placeholders to the correct values and perform the following request:

`POST /lifetimeapi/rest/v2/environments/849515f2-b4ff-4aca-a9d6-9407bea655f4/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/sourcecodeaccess`


Response body:

```
{
    "PackageKey": "bc354abb-6691-41ee-9ed3-9454747e2d4d",
    "Status": "InProgress",
    "Messages": []
}
```

The request for the platform to package the source code of the application "EmployeeBackoffice". We take note of the package key.

Example package key: **bc354abb-6691-41ee-9ed3-9454747e2d4d**


### 4 - Check status

We start by taking the API method "template" URL used to get the status of the application source code packaging. Perform the following request:

`GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/sourcecodeaccess/{PackageKey}/status`

We then change the `{EnvironmentKey}`, `{ApplicationKey}` and `{PackageKey}` placeholders to the correct values and perform the following request:

`GET /lifetimeapi/rest/v2/environments/849515f2-b4ff-4aca-a9d6-9407bea655f4/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/sourcecodeaccess/bc354abb-6691-41ee-9ed3-9454747e2d4d/status`

Example response body:

```
{
    "PackageKey": "bc354abb-6691-41ee-9ed3-9454747e2d4d",
    "Status": "Done",
    "Messages": [
        {
            "Id": "",
            "Message": "Source Code Access",
            "Detail": "Source code access for application 'TestSourceCode'.",
            "HelpRef": 0,
            "ExtraInfo": "",
            "Type": "Info",
            "Submitable": false
        },
        {
            "Id": "",
            "Message": "Preparing Source Code",
            "Detail": "Preparing module 'TestSourceCode' source code for access.",
            "HelpRef": 0,
            "ExtraInfo": "",
            "Type": "Info",
            "Submitable": false
        },
        {...}
    ]
}
```

### 5 - Get download link

Start by taking the API method "template" URL used to get the download link of the application source code package.

`GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/sourcecodeaccess/{PackageKey}/download`

We then change the `{EnvironmentKey}`, `{ApplicationKey}` and `{PackageKey}` placeholders to the correct values and perform the following request:

`GET /lifetimeapi/rest/v2/environments/849515f2-b4ff-4aca-a9d6-9407bea655f4/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/sourcecodeaccess/bc354abb-6691-41ee-9ed3-9454747e2d4d/download`

Response body:

```
{
    "url": "https://hostname.outsystems.com/lifetimeapi/rest/v2/downloads/f4ee541b-5791-4997-a56d-360d80c24821",
    "expires": "2022-12-21T17:00:00Z"
}
```
The response contains the link to download the source code package of the application.

### 6 - Download package

Use the URL obtained from the previous step and get the source code package of the application requested. The download link is a call to a Lifetime API. The authentication token is mandatory for the request. The API method "template" URL used to download the application source code package is:

`GET /lifetimeapi/rest/v2/downloads/{DownloadKey}`

We then can change the `{DownloadKey}` with the value on the recieved URL or call the full value of the URL received from the previous step, performing the following request:

`GET /lifetimeapi/rest/v2/downloads/f4ee541b-5791-4997-a56d-360d80c24821`

Response body:

```
{
    "fileContents":"UEsDBC0AAAgIAJRNaFaAfAsH//////////8VABQAVGVzdFNvdXJjZUNvZGUud[...]2aNVw2umzbtm3btm3btm3AAAAA=",
    "contentType":"application/zip",
    "fileDownloadName":"",
    "lastModified":null,
    "entityTag":null,
    "enableRangeProcessing":false
}
```
The response contains the source code package of the application in base 64 string form and the property `fileContents`. The string needs to be decoded to binary to be unpacked.

If you are unable to download source code of the application, refer to [this article](https://success.outsystems.com/support/troubleshooting/application_lifecycle/unable_to_download_the_source_code_of_an_application/). 
