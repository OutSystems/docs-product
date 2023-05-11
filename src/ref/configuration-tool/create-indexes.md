---
summary: Improve platform performance by creating indexes for a specific set of platform tables.
locale: en-us
guid: d70c93e7-404e-468d-b405-3711108e5311
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Creating indexes for platform database tables

_Available since Platform Server 11.10._

Configuration Tool can create indexes for a specific set of tables used by OutSystems. These indexes, though not mandatory, can improve the performance of the platform.

The index creation operation has a defined timeout of **10 minutes**. You can customize this timeout value when running Configuration Tool in command-line mode.

The creation of indexes is **cumulative**. Any indexes already created by Configuration Tool during the execution window (10 minutes, by default) are kept, even if Configuration Tool wasn't able to create all the database indexes.

You can execute the index creation operation using Configuration Tool several times in a row until all indexes are created, since this operation is idempotent.

## Creating indexes when applying database model changes

The **Create/Upgrade Database** operation, available on the **Platform** tab, creates these indexes after applying any required model changes in the database.

The index creation operation has a defined timeout of **10 minutes**. Index creation can take a long time in some databases, due to the nature of the tables where OutSystems is creating the indexes. If the platform can't create the indexes in this timeframe, you get a pop-up message when the create/upgrade database action finishes, stating that it couldn't create some of the indexes.

## Creating indexes at a later time

If the provided 10-minute window isn't enough for creating the indexes, your operations team should provide your DBA with the index creation SQL script that Configuration Tool uses. After their approval, run Configuration Tool in command-line mode to create the indexes with an increased timeout.

Do the following:

1. In a machine where you installed Platform Server, open the folder `<platform_install_folder>\db`.

1. Provide the file `platform_asyncindex_<database_engine>.sql` (according to your database engine) to your DBA for validation.

1. If the DBA approves the content of the SQL script, open a command-line console and run the following Configuration Tool command:

    `ConfigurationTool.com /createAsyncIndexes /maxAsyncIndexesCreateTimeInMin <index_creation_timeout>`

    The timeout value is in **minutes**.

    For example, to create the indexes on your platform using a timeout of 15 minutes, run the following command:

    `ConfigurationTool.com /createAsyncIndexes /maxAsyncIndexesCreateTimeInMin 15`

1. Check the output of the Configuration Tool command to understand if there are still some indexes missing. In this case, you get a message similar to the following:

    `Some performance indexes were not created, these are not mandatory.`

    Run the command again to create the missing indexes, adjusting the timeout value, if necessary.

**Notes:**

* If you don't provide a value for `/maxAsyncIndexesCreateTimeInMin`, Configuration Tool uses the default timeout of 10 minutes.

* The `/maxAsyncIndexesCreateTimeInMin` argument defines the total amount of time (also called the execution window) that Configuration Tool has to create all the missing indexes to improve platform performance. For example, with a total time of 10 minutes, if creating the first index takes 4 minutes, there's only 6 minutes left to create the other indexes.

## Checking for new available indexes in a platform release

Every time OutSystems adds a new index in a Platform Server release, you can find a release note in the [Release Notes](https://success.outsystems.com/Support/Release_Notes/11/Platform_Server) page similar to the following:

* Added the OSAIX_\* index on the table OSSYS_\* to the platform. This index is created outside the main database create or upgrade process due to its creation impact.
