---
summary: Learn how to register an environment using the LifeTime API.
tags:
locale: en-us
guid: fa3c3a72-304f-4171-b85a-77e614a20326
---

# Register an Environment using the LifeTime API

In this example we will perform the following generic steps using API calls:

1. Get the **roles** defined in LifeTime _(optional if you already have this information)_;

1. Register a new **environment** in LifeTime, defining the permission levels that each role will have over that environment.

Check below for example API calls (requests and responses) for each of the presented steps.

## 1. Get LifeTime's roles

We start by calling the API method that returns all the roles defined in LifeTime (only necessary when we don't have this information yet):

Request: `GET /lifetimeapi/rest/v2/roles?IncludeEnvPermissions=true`

Note: Adding the optional parameter `IncludeEnvPermissions`, we obtain the permission levels that each role has over the environments of the infrastructure.

Response body:

```javascript
[
    {
        "Key": "c4c49f62-ff68-42bf-9dc9-a023182f7ec9",
        "name": "Administrator",
        "description": "Built-in administrator role of the platform",
        "manageInfrastructure": true,
        "manageTeams": true,
        "environmentPermissions": [
            {
                "environmentKey": "f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e",
                "environmentName": "Development",
                "level": 6,
                "levelLabel": "Full Control",
                "createApplications": true,
                "addDependenciesToSystem": true
            },
            {
                "environmentKey": "c7155bc0-2154-4b8e-9570-df86cad30b40",
                "environmentName": "Test",
                "level": 6,
                "levelLabel": "Full Control",
                "createApplications": true,
                "addDependenciesToSystem": true
            }
        ]
    },
    {
		(...)
	},
	{
        "Key": "001c45e7-0cb6-41d1-85ba-8f0377453200",
        "name": "ExternalDev",
        "description": "External developer",
        "manageInfrastructure": false,
        "manageTeams": false,
        "environmentPermissions": [
            {
                "environmentKey": "f3582e43-43c7-4bb4-8cbb-d9f6cbcbd35e",
                "environmentName": "Development",
                "level": 5,
                "levelLabel": "Change and Deploy Applications",
                "createApplications": true,
                "addDependenciesToSystem": true
            },
            {
                "environmentKey": "c7155bc0-2154-4b8e-9570-df86cad30b40",
                "environmentName": "Test",
                "level": 2,
                "levelLabel": "Open and Debug Applications",
                "createApplications": false,
                "addDependenciesToSystem": false
            }
        ]
    }
]
```
We take note of all the role keys so that we can use them in the next API call:

"Administrator" role key: **c4c49f62-ff68-42bf-9dc9-a023182f7ec9**  
(...)  
"ExternalDev" role key: **001c45e7-0cb6-41d1-85ba-8f0377453200**

## 2. Register environment

Next, we call the API method to register the environment in LifeTime. We need to provide:

* The environment name and address
* The Service Center credentials of an administrator user
* The LifeTime address
* The environment position in the infrastructure

In this case, we will also define the permission levels that each LifeTime role has over the new environment, using the role keys obtained in the previous step.

The mapping for permission levels is the following:

* No Access - 0
* Access - 1
* List Applications - 2
* Monitor and Add Dependencies - 3
* Open and Debug Applications - 4
* Change and Deploy Applications - 5
* Full Control - 6

If the role permissions for the environment are not provided at this point (`EnvironmentRolePermissions` parameter in the request body), the registered environment will have the default permission level for the existing roles - "Full Control" for the Administrator role, and "List Applications" for all the remaining roles.

Request: `POST /lifetimeapi/rest/v2/environments/`

Request body:

```javascript
{
  "EnvironmentName": "Production",
  "EnvironmentAddress": "prd-env.company.com",
  "ServiceCenterUsername": "admin",
  "ServiceCenterPassword": "<password>",
  "LifeTimeAddress": "lt-env.company.com",
  "EnvironmentPosition": 2,
  "OverridePreviousLifetime": false,
  "EnvironmentRolePermissions": [
    {
      "RoleKey": "c4c49f62-ff68-42bf-9dc9-a023182f7ec9",
      "PermissionLevel": 6,
      "CanCreateApplications": true,
      "CanAddDependenciesToSystem": true
    }
    (...)
    {
      "RoleKey": "001c45e7-0cb6-41d1-85ba-8f0377453200",
      "PermissionLevel": 0,
      "CanCreateApplications": false,
      "CanAddDependenciesToSystem": false
    }
  ]
}

```
If the operation is successful, the response body will contain the key of the registered environment and the users imported from that environment.

Response body:

```javascript
{
    "EnvironmentKey": "1ee9297b-edfc-4826-ad95-2a8a6e40957f",
    "ImportedUsers": []
}
```
