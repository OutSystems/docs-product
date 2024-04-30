---
summary: Learn how to get the source code of an application for static code analysis. OutSystems provides an API that lets you download the code. 
locale: en-us
guid: c0f22c7d-ac63-4704-b50f-97a3c697da44
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Get the source code of an application

<div class="warning" markdown="1">

This feature is currently available for use and packaging and pricing details may be subject to updates in the future.

</div>

Highly regulated industries typically have internal organizational security and compliance policies that they must comply with. Frequently, these procedures include employing specific static code analysis tools to test applications security.

The OutSystems platform provides an API that enables you to download the generated code for the current running apps. The source code package returned by the API contains the server-side code and the native code, if it’s a mobile application.

With this capability, you can extend OutSystems’s built-in security capabilities by integrating your preferred Static Application Security Testing (SAST) tool. This supports your security and compliance needs, facilitating integration into continuous deployment pipelines, where automated application source code security validations occur across multiple CI/CD stages.

<div class = "info" markdown="1">

The code retrieved in the API is almost same as the one running on the server. For security and licensing reasons, some files with configurations, secrets and proprietary code are not shared by the API.

</div>

<div class = "info" markdown="1">

The code in the package does not compile or is an executable.

</div>

<div class = "info" markdown="1">

Extension code is not available through the API.

</div>

## Prerequisites

To download the source code of an app, ensure that the environment from where you want to get the source code has:

* Platform Server version 11.27.0 or higher
* LifeTime version 11.21.1 or higher
* [LifeTime Service Account](https://success.outsystems.com/Documentation/11/Reference/OutSystems_APIs/LifeTime_API_v2/REST_API_Authentication)
    * Service Account needs Open and Debug on the environment

## Process Overview 

To request the source code of an application, follow these steps:

1. [Get the environment key](#step-1-get-the-environment-key) of the environment where you want to request the application source code (skip this step if you already have this information).
1. [Get the application key](#step-2-get-the-application-key) of the application you want to request the source code (skip this step if you already have this information).
1. [Get the package key](#step-3-get-the-package-key) of the application source code you want to request.
1. [Check the status](#step-4-check-status) of the application source code packaging you want to request.
1. [Get the download link](#step-5-get-download-link) of the application source code package.
1. Download the application source code package.

### Step 1: Get the environment key

This step is optional and call the API only if you don't know the environment key. 

This API returns all the environments available on your infrastructure.

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

In this request example, the source code of an application is requested from the **Testing** environment. 

<div class = "info" markdown="1">

Note the environment key to use it in the upcoming API calls.

</div>

Example of an environment key: **849515f2-b4ff-4aca-a9d6-9407bea655f4**

### Step 2: Get the application key

You can skip this step if you already have the application key.

This API returns all the available applications in the infrastructure along with the application key.  

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

In this request, you request the source code for **EmployeeBackoffice** application.  

<div class = "info" markdown="1">

Note the application key to use it in the upcoming API calls.

</div>

Example "EmployeeBackoffice" application key: **c9a7a82e-0eee-4a3d-8e22-2a19c69c766f**

### Step 3: Get the package key

This API returns the package key for an application on a given environment.

`POST /environments/{EnvironmentKey}/applications/{ApplicationKey}/sourcecodeaccess`

Replace the `{EnvironmentKey}` and `{ApplicationKey}` with values retrieved from Step 1 and Step 2 and make a request:

`POST /lifetimeapi/rest/v2/environments/849515f2-b4ff-4aca-a9d6-9407bea655f4/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/sourcecodeaccess`

Response body:

```
{
    "PackageKey": "bc354abb-6691-41ee-9ed3-9454747e2d4d",
    "Status": "InProgress",
    "Messages": []
}
```

In this request, you request the source code for **EmployeeBackoffice** application.  

<div class = "info" markdown="1">

Note the package key to use it in the upcoming API calls.

</div>

Example package key: **bc354abb-6691-41ee-9ed3-9454747e2d4d**

### Step 4: Check status

Get the status of the application source code package.

`GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/sourcecodeaccess/{PackageKey}/status`

Replace the `{EnvironmentKey}`, `{ApplicationKey}`, and `{PackageKey}` with values retrieved from Step 1, Step 2, and Step 3and make a request: 

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

### Step 5: Get download link

Get the download link of the application source code package.

`GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/sourcecodeaccess/{PackageKey}/download`

Replace the  `{EnvironmentKey}`, `{ApplicationKey}`, and `{PackageKey}` with values retrieved from Step 1, Step 2, and Step 3 and make the following request:

`GET /lifetimeapi/rest/v2/environments/849515f2-b4ff-4aca-a9d6-9407bea655f4/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/sourcecodeaccess/bc354abb-6691-41ee-9ed3-9454747e2d4d/download`

Response body:

```
{
    "url": "https://hostname.outsystems.com/lifetimeapi/rest/v2/downloads/f4ee541b-5791-4997-a56d-360d80c24821",
    "expires": "2022-12-21T17:00:00Z"
}
```

The response contains the link to download the source code package of the application.

### Step 6: Download package

Use the URL obtained from [Use download link](#step-5-get-download-link) and get the source code package of the application. The download link is a call to a Lifetime API. The authentication token is mandatory for the request. The API method "template" URL used to download the application source code package is:

`GET /lifetimeapi/rest/v2/downloads/{DownloadKey}`

Replace the `{DownloadKey}` with the value on the download URL or call the full URL received from the step [Use download link](#step-5-get-download-link).

`GET /lifetimeapi/rest/v2/downloads/f4ee541b-5791-4997-a56d-360d80c24821`

If you are unable to download source code of the application, refer to [Unable to download the source code of an application article](api-unable-to-download-code.md). 

## Review results

When reviewing static code analysis results, you must note that each static code analysis tool can report findings without proper context. These findings must be reviewed to detect false positives. You can consult the experts in OutSystems development to help understand these findings with proper context.

For more information on why certain findings should be considered false positives, refer to [Static application security testing](https://success.outsystems.com/support/security/static_application_security_testing/#review-results).
