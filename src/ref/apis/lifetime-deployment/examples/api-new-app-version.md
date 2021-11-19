---
summary: Learn how to create a new application version using the LifeTime API.
---

# Create a new Application Version using the LifeTime API

In this example we will perform the following generic steps using API calls:

1. Get the **environment key** of the environment where you want to create the application version _(optional if you already have this information)_;

1. Get the **application key** of the desired application _(optional if you already have this information)_;

1. Get the **module version key** of each application module;

1. Create a new **application version** using the module(s) version information obtained in the previous step.

Check below for example API calls (requests and responses) for each of the presented steps.

## 1. Get environment key

We start by calling the API method that returns all the environments available on your infrastructure (only necessary if we don't know the environment key yet):

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

Since we want to create an application version in our environment of type "Development" — coincidentally, the environment is also called "Development" —, we take note of its key so that we can use it in the upcoming API calls: 

Environment key: **f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e**

## 2. Get application key

Next, we call the API method that returns all the available applications in the infrastructure to get the application key (only necessary if we don't know the application key yet):

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

We want to create an application version for the "EmployeeBackoffice" application. We take note of its key so that we can use it in the next API calls: 

"EmployeeBackoffice" application key: **c9a7a82e-0eee-4a3d-8e22-2a19c69c766f**

### 3. Get module version key of each application module

We start by taking the API method "template" URL used to get the details of an application on a given environment:

`GET /lifetimeapi/rest/v2/environments/{EnvironmentKey}/applications/{ApplicationKey}/`

We then change the `{EnvironmentKey}` and `{ApplicationKey}` placeholders to the correct values and perform the following request:

Request: `GET /lifetimeapi/rest/v2/environments/f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/?IncludeEnvStatus=true&IncludeModules=true`

Note: We need the extra flags (`IncludeEnvStatus` and `IncludeModules`) to obtain the necessary module version key information.

Response body:

```javascript
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
  "AppStatusInEnvs": [
    {
      "EnvironmentKey": "f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e",
      "BaseApplicationVersionKey": "e9eedcbd-fe87-4ccf-a9c3-f7225ddcb8ff",
      "IsModified": true,
      "IsModifiedReason": "Module_Modified",
      "IsModifiedMessage": "At least one module was modified since the version 0.1",
      "ConsistencyStatus": "",
      "ConsistencyStatusMessages": "",
      "MobileAppsStatus": [],
      "ModuleStatusInEnvs": [
        {
          "ApplicationKey": "c9a7a82e-0eee-4a3d-8e22-2a19c69c766f",
          "EnvironmentKey": "f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e",
          "ModuleVersionKey": "bc354abb-6691-41ee-9ed3-9454747e2d4d",
          "ConsistencyStatus": "",
          "ConsistencyStatusMessages": ""
        }
      ],
      "DeploymentZoneKey": ""
    }
  ]
}
```

The "EmployeeBackoffice" application has only one module. We take note of its version key, included in the "ModuleStatusInEnvs" list:

Module version key: **bc354abb-6691-41ee-9ed3-9454747e2d4d**

Note: If the application had several modules, we would need to take note of all their version keys.

## 4. Create a new application version

Starting from the "template" URL of the API method for creating a new application version:

`POST /lifetimeapi/rest/v2/environments/{EnvironmentKey}/applications/{ApplicationKey}/versions/`

We change the `{EnvironmentKey}` and `{ApplicationKey}` placeholders to the correct values, defining the full URL for the request:

Request: `POST lifetimeapi/rest/v2/environments/f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e/applications/c9a7a82e-0eee-4a3d-8e22-2a19c69c766f/versions/`

We insert the following text in the `POST` request body (using the module version key retrieved in step 3):

```javascript
{
  "ChangeLog": "Go live 1.0",
  "Version": "1.0",
  "MobileVersions": [],
  "ModuleVersionKeys": [
    "bc354abb-6691-41ee-9ed3-9454747e2d4d"
  ]
}
```

The response contains the key of the created application version in the "ApplicationVersionKey" element when the operation is successful.

Response body:

```javascript
{
  "ApplicationVersionKey": "b3d2ef6b-e5c5-4c7e-851e-0547f7bd634c"
}
```
