# Platform Safe Indexes Creation

In version 11.10.0 of OutSystems platform it was introduced a new performance feature that enables the platform to create indexes to a specific set of tables increasing the performance of some parts of the platform.

These indexes are not obligatory for the platform to run, however their presence can lead to performance improvements.

From version 11.10.0 the action of “Create/Upgrade Database” on the platform tab in the configuration tool will create these indexes at the end of doing the model changes to the database.

## What to do if the indexes are not being created

Due to the nature of the tables where we are creating the indexes in some databases the creation of these indexes can take a long time. Because of this the indexes are created with a timeout of 10 minutes. If the index fails to create in this timeframe a message saying “Some performance indexes were not created, these are not mandatory.” will popup in the configuration tool at the end of the platform's create or update action with the option to open this document.

If the 10 minutes windows we provide for this operation proves to not be enough for the creation of the indexes the operations team should do the following:
1. Provide to their DBA the script of the indexes the platform is trying to create. This script file can be found under the platform installation folder inside the db folder. Inside it pick the file platform_asyncindex_\<database stack\>.sql
2. After the analysis of the DBA the configuration tool should be execute in command line mode with the arguments **/createAsyncIndexes /maxAsyncIndexesCreateTimeInMin \<timeout in minutes to create the indexes\>**

For example, to execute the creation of this set of indexes in your platform with a timeout of 15 minutes run in the command line
```ConfigurationTool.com /createAsyncIndexes /maxAsyncIndexesCreateTimeInMin 15``` 

**Note:** not passing a value to the argument _/maxAsyncIndexesCreateTimeInMin_ will always run the creation of the indexes with a timeout of 10 minutes.

The creation of indexes is cumulative, meaning that if an execution of the above command is not successful in creating all the indexes it will keep the successful ones in the database. This command can be executed multiple times since it is idempotent.

Regarding the timeout argument it defines the maximum amount of time the configuration tool will have to create all the missing indexes. For example, in a timeout value of 10 minutes, if the first index takes 4 minutes to create the subsequent ones will only have a window of 6 minutes to execute.

## How to understand if a new index was added to to platform

Every time a new index is added to the platform in the release notes there will be a release note with the text  “Added the OSAIX_* index on the table OSSYS_* to the platform. This index is created outside the main database create or upgrade process due to its creation impact.”
