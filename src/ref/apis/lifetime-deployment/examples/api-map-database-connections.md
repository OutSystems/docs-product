---
summary: Learn how to map logical databases to database connections using the LifeTime API in OutSystems 11 (O11).
locale: en-us
guid: f4b0e6fd-f612-4773-8e37-d2693ef6a005
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
coverage-type:
  - remember
tags: api usage, database mapping, deployment status, lifetime api, outsystems 11
audience:
  - platform administrators
  - backend developers
  - full stack developers
outsystems-tools:
  - lifetime
---
# Map logical database to database connections using the LifeTime API

In this example, perform the following generic steps using API calls:

1. Get the deployment status.

1. Get the extensions and database connections to map.

1. Map the missing database connections.

<div class="info" markdown="1">

To map database connections using the LifeTime API you need LifeTime version 11.21.1, or higher.

</div>

## 1. Get the deployment status

Start by calling the API method that returns the status for the deployment.

`GET /lifetimeapi/rest/v2/deployments/{DeploymentKey}/status`

You should already have a deployment key. If you need to know how to obtain it, follow the steps in [How to deploy an application](api-deploy-app.md).

In this example, the deployment key is: **dce64ad4-2ddf-4e54-a639-3524bcd5b9a1**

After replacing the `{DeploymentKey}` placeholder with the correct key, you get the following final URL:

Request: `GET /lifetimeapi/rest/v2/deployments/dce64ad4-2ddf-4e54-a639-3524bcd5b9a1/status`

Response body:

```JavaScript
{
    "DeploymentStatus": "needs_user_intervention",
    "Info": "needs_configuration_or_confirmation",
    "DeploymentLog": [
        {
            "Instant": "2023-02-01T15:53:53.637Z",
            "Message": "Uploading modules from DEV to QA"
        },
        {
            "Instant": "2023-02-01T15:53:55.2Z",
            "Message": "Uploading 'ExtensionTest' from DEV to QA"
        },
        {
            "Instant": "2023-02-01T15:53:55.34Z",
            "Message": "Uploading 'ExternalExample' from DEV to QA"
        },
        {
            "Instant": "2023-02-01T15:53:58.217Z",
            "Message": "Applying Deployment Zones configurations in QA Environment"
        },
        {
            "Instant": "2023-02-01T15:54:01.36Z",
            "Message": "Creating solution pack in QA"
        },
        {
            "Instant": "2023-02-01T15:54:01.903Z",
            "Message": "No need to upgrade Solution."
        },
        {
            "Instant": "2023-02-01T15:54:01.907Z",
            "Message": "There is one or more Extensions with missing configuration which may lead to publishing errors. Please configure the Database Connections for the listed Extensions' Logical Databases."
        }
    ]
}
```

The last message returned indicates that there are unmapped database connections.

## 2. Get the extensions and database connections to map

Call the API action that retrieves all the extensions and databases in the deployment that is missing configurations.

`GET /lifetimeapi/rest/v2/deployments/{DeploymentKey}/getmissingdbmappings`

Again, you must replace the `{DeploymentKey}` placeholder with the correct key. This is the final request:

Request: `GET /lifetimeapi/rest/v2/deployments/dce64ad4-2ddf-4e54-a639-3524bcd5b9a1/getmissingdbmappings`

Response body:

```JavaScript
[
  {
    "ExtensionKey": "a6ada142-0cf1-49b6-a743-166dcffcc8f1",
    "ExtensionName": "ExtensionTest",
    "LogicalDatabase": "Ext"
  },
  {
    "ExtensionKey": "a6ada142-0cf1-49b6-a743-166dcffcc8f1",
    "ExtensionName": "ExtensionTest",
    "LogicalDatabase": "Ext2"
  }
]
```

In this example, the deployment has one extension called `ExtensionTest` with its unique identifier (or extension key) `a6ada142-0cf1-49b6-a743-166dcffcc8f1`. It has two logical databases that must be mapped: `Ext` and `Ext2`.

## 3. Map the missing database connections

Call another API action to map the connections.

`POST /lifetimeapi/rest/v2/deployments/{DeploymentKey}/configuration`

Adapting the template above to the example:

Request: `POST /lifetimeapi/rest/v2/deployments/dce64ad4-2ddf-4e54-a639-3524bcd5b9a1/configuration`

Request body:

You must send a payload such as the following one:

```JavaScript
[
    {
        "ExtensionKey": "a6ada142-0cf1-49b6-a743-166dcffcc8f1",
        "DBMapping": [
            {
                "DatabaseName": "DestinationConnectionName",
                // the name of the database connection in the
                // destination environment
                "LogicalDatabaseName": "SourceConnectionName"
                // the name of the database connection in the
                // source environment
            }
        ]
    } // one object per connection
]
```

In the example:

```JavaScript
[
    {
        "ExtensionKey": "a6ada142-0cf1-49b6-a743-166dcffcc8f1",
        "DBMapping": [
            {
                "DatabaseName": "ExtQA",
                "LogicalDatabaseName": "Ext"
            }
        ]
    },
    {
        "ExtensionKey": "a6ada142-0cf1-49b6-a743-166dcffcc8f1",
        "DBMapping": [
            {
                "DatabaseName": "Ext2QA",
                "LogicalDatabaseName": "Ext2"
            }
        ]
    }
]
```

If there are no errors, this action returns the message `Mapping succeeded and deployment triggered`. You can now go back to step one and check the status of the deployment.
