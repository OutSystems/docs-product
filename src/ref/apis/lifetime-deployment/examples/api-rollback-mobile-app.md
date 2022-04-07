---
summary: Learn how to rollback a mobile app using the LifeTime API.
locale: en-us
guid: 9e68edab-dc6e-4606-b3b8-ceb4f1c2d406
---

# Rollback a Mobile App using the LifeTime API

In this example we will rollback a mobile application deployed between the **Quality Assurance** environment and the **Production** environment to a previous version. For that, we will perform the following generic steps using API calls:

1. Get the **environment keys** of the source (Quality) and target (Production) environments _(optional if you already have this information)_.

1. Get the **application key** of the application to rollback _(optional if you already have this information)_.

1. Get the **application version key** of the application version to deploy, which is the mobile application previous version.

1. Create a new **deployment** for that previous version of the mobile application.

1. **Start** the created deployment.

1. Get the deployment **execution status** until the execution has finished and check if the deployment status is a terminal one (one of "needs_user_intervention", "aborted", "finished_successful", "finished_with_warnings", "finished_with_errors").

<div class="info" markdown="1">

By performing the rollback of a mobile app to a previous version, the application version is rolled back. However, the tag for the mobile app version remains the same, as LifeTime doesn't support creating a tag based on a previous mobile app version

</div>

Check below for example API calls (requests and responses) for each of the presented steps.

## 1. Get the source and target environments keys

We start by calling the API method that returns all the environments available on the infrastructure to determine the source and target environment keys (only necessary when we don't have this information yet):

Request: `GET /lifetime/rest/v2/environments/`

Response body:

```javascript
[
    {
        "Key": "b86339de-38af-4a8e-bfe6-25a444c78bc2",
        "Name": "Development",
        "OSVersion": "11.13.2.32392",
        "Order": 0,
        "HostName": "dev-env.company.com",
        "UseHTTPS": true,
        "EnvironmentType": "Development",
        "NumberOfFrontEnds": 1,
        "ApplicationServerType": ".NET",
        "ApplicationServer": "IIS",
        "DatabaseProvider": "SQLServer",
        "IsCloudEnvironment": false,
        "IsOffline": false
    },
    {
        "Key": "f5d16abb-612d-4fa5-a34e-4695e49678b2",
        "Name": "Quality Assurance",
        "OSVersion": "11.13.2.32392",
        "Order": 1,
        "HostName": "qa-env.company.com",
        "UseHTTPS": true,
        "EnvironmentType": "",
        "NumberOfFrontEnds": 1,
        "ApplicationServerType": ".NET",
        "ApplicationServer": "IIS",
        "DatabaseProvider": "SQLServer",
        "IsCloudEnvironment": false,
        "IsOffline": false
    },
    {
        "Key": "f78966c5-4c1f-4c35-9b3d-502b66943964",
        "Name": "Production",
        "OSVersion": "11.13.2.32392",
        "Order": 2,
        "HostName": "prd-env.company.com",
        "UseHTTPS": true,
        "EnvironmentType": "Production",
        "NumberOfFrontEnds": 1,
        "ApplicationServerType": ".NET",
        "ApplicationServer": "IIS",
        "DatabaseProvider": "SQLServer",
        "IsCloudEnvironment": false,
        "IsOffline": false
    }
]
```

We take note of the environment keys of the Quality Assurance and Production environments so that we can use them in the next API calls:

Quality Assurance environment key: **f5d16abb-612d-4fa5-a34e-4695e49678b2**  
Production environment key: **f78966c5-4c1f-4c35-9b3d-502b66943964**

## 2. Get the application key

Next, we call the API method that returns all the available applications in the infrastructure to find the application key of the mobile application we want to rollback:

Request: `GET /lifetimeapi/rest/v2/applications/`

Response body:

```javascript
[
    {...},
    {
        "Key": "0f47c804-bce5-46e8-9706-585a044d17e6",
        "Name": "Directory Mobile",
        "Kind": "Mobile",
        "Team": "",
        "Description": "Mobile application to display your organization employees' contacts, departments, and office information. Specially designed for smartphone use, with offline capabilities, the app can be installed as a Progressive Web App.",
        "URLPath": "/DirectoryMobile",
        "IconHash": "IconHash57f340fb-050c-fce7-3402-1dbb56822b7f",
        "IconURL": "/LifeTimeSDK/ApplicationIcon.aspx?ApplicationKey=0f47c804-bce5-46e8-9706-585a044d17e6",
        "IsSystem": false,
        "AppStatusInEnvs": []
    },
    {...}
]
```

We take note of the application key of the "Directory Mobile" app so that we can use it in the next API calls:

Application key: **0f47c804-bce5-46e8-9706-585a044d17e6**

## 3. Get the application version key

The following API method retrieves all the versions of an application in the infrastructure:

`GET /lifetimeapi/rest/v2/applications/{ApplicationKey}/versions/`

With the application key retrieved from the previous method, we do the following request:

Request: `GET /lifetimeapi/rest/v2/applications/0f47c804-bce5-46e8-9706-585a044d17e6/versions/`

Response body:

```javascript
[
    {...},
    {
        "Key": "fa5936cd-2625-43c6-bec7-de8ee90a4c71",
        "ApplicationKey": "0f47c804-bce5-46e8-9706-585a044d17e6",
        "Version": "0.3",
        "ChangeLog": "",
        "CreatedOn": "2021-10-27T17:22:21.45Z",
        "InUse": false,
        "MobileVersions": [
            {
                "NativePlatform": "Android",
                "VersionNumber": "0.3",
                "VersionDescription": ""
            }
        ],
        "PrimaryColor": "",
        "NativeHash": "ab73331b-1891-2cd1-ac84-c5cf94f1a5b5",
        "ModuleVersions": [
            {
                "Key": "75b5d7a2-4336-4a1d-99ab-53ba73cc8172",
                "ModuleKey": "0a958fc2-4b03-6eba-4348-d9c3627d8af5",
                "CreatedOn": "2021-10-27T17:20:44Z",
                "CreatedBy": "Administrator",
                "CreatedByUsername": "admin",
                "GeneralHash": "sSVqtD4lnMd73JrRyOl6RA",
                "DirectUpgradeFromHash": ""
            },
            {
                "Key": "619b072c-cc34-49a2-8304-05d184d47021",
                "ModuleKey": "0c6a024a-cfb6-2ba6-d848-dec31017f9a4",
                "CreatedOn": "2021-10-27T16:51:34Z",
                "CreatedBy": "Administrator",
                "CreatedByUsername": "admin",
                "GeneralHash": "4qms8nZVXhNI0yQb8tysWg",
                "DirectUpgradeFromHash": ""
            },
            {
                "Key": "78a4f4de-49a4-4b0b-9ca1-7cffc24de6f3",
                "ModuleKey": "25dca7c7-5e39-99b5-9400-195eeaf7647c",
                "CreatedOn": "2021-10-27T16:51:37Z",
                "CreatedBy": "Administrator",
                "CreatedByUsername": "admin",
                "GeneralHash": "Wnk+4qeG2MOPAqmDtgp37A",
                "DirectUpgradeFromHash": ""
            }
        ]
    },
    {...}
]
```

In this case, we want to downgrade the current version of the application in the Production environment to a previous version (for example, 0.4 -> 0.3). So we take note of the key for the 0.3 version:

Application version key (0.3): **fa5936cd-2625-43c6-bec7-de8ee90a4c71**

## 4. Create the deployment

Now we have the necessary information to create a new deployment. We need to provide the source and target environment keys and the application version key. In this case, the **SourceEnvironmentKey** value will be the key of the **Quality Assurance** environment and the **TargetEnvironmentKey** value will be the key for the **Production** environment.

Request: `POST /lifetimeapi/rest/v2/deployments`

Request body:

```javascript
{
    "ApplicationOperations":[
        {
            "ApplicationVersionKey": "fa5936cd-2625-43c6-bec7-de8ee90a4c71",
            "DeploymentZoneKey": ""
        }
    ],
    "Notes": "",
    "SourceEnvironmentKey": "f5d16abb-612d-4fa5-a34e-4695e49678b2",
    "TargetEnvironmentKey": "f78966c5-4c1f-4c35-9b3d-502b66943964"
}
```

If the operation is successful, the response body will contain the deployment key of the new deployment.

Response body:

```
1381f766-81b5-4570-a37c-5729c7a305e2
```

## 5. Start deployment execution

We can now start the deployment execution by calling the following API method:

`POST /lifetimeapi/rest/v2/deployments/{DeploymentKey}/{Command}/`

The possible commands are: "start", "continue", or "abort".

In this case, we’ll use the deployment key obtained in the previous step and the "start" command to start the deployment execution:

Request: `POST /lifetimeapi/rest/v2/deployments/1381f766-81b5-4570-a37c-5729c7a305e2/start/`

If the "start" command is successful, OutSystems will return a `202 Accepted` HTTP status code, with an empty response body.

## 6. Check deployment status

At this point, we use the following API method to determine the execution status of the previously issued "start" command:

`GET /lifetimeapi/rest/v2/deployments/{DeploymentKey}/status/`

Using our deployment key, we'll get the following:

`GET /lifetimeapi/rest/v2/deployments/1381f766-81b5-4570-a37c-5729c7a305e2/status/`

Response body:

```javascript
{
    "DeploymentStatus": "finished_successful",
    "Info": "",
    "DeploymentLog": [
        {
            "Instant": "2021-11-03T14:35:42.173Z",
            "Message": "Uploading modules from Quality Assurance to Production"
        },
        {
            "Instant": "2021-11-03T14:35:45.247Z",
            "Message": "Applying Deployment Zones configurations in Production Environment"
        },
        {
            "Instant": "2021-11-03T14:35:48.407Z",
            "Message": "Creating solution pack in Production"
        },
        {
            "Instant": "2021-11-03T14:36:01.673Z",
            "Message": "No need to upgrade Solution."
        },
        {
            "Instant": "2021-11-03T14:36:01.677Z",
            "Message": "Uploading Solution."
        },
        {
            "Instant": "2021-11-03T14:36:01.677Z",
            "Message": "Creating Solution 'Quality Assurance to Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.68Z",
            "Message": "Creating Solution version."
        },
        {
            "Instant": "2021-11-03T14:36:01.68Z",
            "Message": "Verifying the Solution consistency and permission settings."
        },
        {
            "Instant": "2021-11-03T14:36:01.683Z",
            "Message": "Upgrading and refreshing modules of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.683Z",
            "Message": "Performing Impact Analysis of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.687Z",
            "Message": "Preparing extensions of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.687Z",
            "Message": "Preparing database of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.687Z",
            "Message": "Preparing database of module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.69Z",
            "Message": "Associating dependencies of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.69Z",
            "Message": "Associating dependencies of module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.69Z",
            "Message": "Compiling modules of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.69Z",
            "Message": "Compiling module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.693Z",
            "Message": "Compiling dependencies of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.693Z",
            "Message": "Compiling dependencies of module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.693Z",
            "Message": "Gathering dependencies of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.693Z",
            "Message": "Gathering dependencies of module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.7Z",
            "Message": "Preparing deploy of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.7Z",
            "Message": "Preparing deploy of module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.7Z",
            "Message": "Deploying modules of 'Quality_Assurance_to_Production'."
        },
        {
            "Instant": "2021-11-03T14:36:01.703Z",
            "Message": "Updating static entity records of module 'DirectoryMobile'"
        },
        {
            "Instant": "2021-11-03T14:36:01.703Z",
            "Message": "Updating site properties of module 'DirectoryMobile'"
        },
        {
            "Instant": "2021-11-03T14:36:01.707Z",
            "Message": "Updating roles of module 'DirectoryMobile'"
        },
        {
            "Instant": "2021-11-03T14:36:01.707Z",
            "Message": "Updating timers of module 'DirectoryMobile'"
        },
        {
            "Instant": "2021-11-03T14:36:01.707Z",
            "Message": "Updating system entities of module 'DirectoryMobile'"
        },
        {
            "Instant": "2021-11-03T14:36:01.71Z",
            "Message": "Deploying module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:01.71Z",
            "Message": "Updating status of module 'DirectoryMobile'."
        },
        {
            "Instant": "2021-11-03T14:36:05.323Z",
            "Message": "Creating application versions in Production"
        },
        {
            "Instant": "2021-11-03T14:36:08.037Z",
            "Message": "Applying extension entities configurations in Production Environment"
        },
        {
            "Instant": "2021-11-03T14:36:08.05Z",
            "Message": "Applying Progressive Web App configuration in Production Environment"
        },
        {
            "Instant": "2021-11-03T14:36:10.993Z",
            "Message": "Synchronizing data with 'Production' environment."
        },
        {
            "Instant": "2021-11-03T14:36:58.34Z",
            "Message": "Updating application versions for 'Production' environment."
        },
        {
            "Instant": "2021-11-03T14:37:01.387Z",
            "Message": "Deploy completed"
        }
    ]
}
```

In the response body, we see the different steps taken during the deployment process. They are shown as they happen, similar to the LifeTime UI.

As we did the status request when the operation was already finished with success, we got the deployment status "finished_successful".

If we get an intermediate deployment status like "running" in the response, we would need to keep polling the status of the deployment execution (by repeating the API method call) until the execution reached a terminal deployment status, either a successful or an unsuccessful one.

The possible values for the deployment status are: "saved", "running", "needs_user_intervention", "aborted", "aborting", "finished_successful", "finished_with_warnings", "finished_with_errors".
