---
summary: The Processes API allows you to get information from the OutSystems data model to customize and extend the design of your Processes.
tags: 
---

# Processes API

The Processes API allows you to get information from the OutSystems data model to customize and extend the design of your Processes. With this API your can, for example, do the following:

* **Build Your Taskbox**: Build your custom Taskbox to display the tasks to end-users. 

* **Extend the Data Model**: Extend the OutSystems data model to better adapt Processes to your needs. 

* **Build Process Reports**: Build reports about your Process and KPIs (Key Performance Indicators) from the extracted information. 

The information about your processes is obtained by querying System entities. As such, you must add references to those entities to your module, using the Manage Dependencies dialog box.

## Entities Storing Definitions

The following entities have the definition of all elements related with Processes:

* `Process_Definition`: the Process definitions
* `Process_Input_Definition`: the definition of all Input Parameters of a Process
* `Process_Output_Definition`: the definition of all Output Parameters of a Process
* `Process_Definition_Lang`: the translations for all translatable properties of a Process
* `Activity_Definition`: the definition of all Activities of a Process
* `Activity_Output_Definition`: the definition of all Output Parameters of an Activity
* `Activity_Def_Link`: the definition of connections between Activities

## Entities Storing Runtime Data

The runtime data of all elements related with Processes is stored in the following entities:

* `Process`: the runtime data of all created Process instances – active and ended ones
* `Process_Input`: the runtime data of all Input Parameters of a Process instance
* `Process_Output`: the runtime data of all Output Parameters of a Process instance
* `Activity`: the runtime data of all created Activity instances of a Process – pending, planned and closed ones. There are no created instances for future activities because activity instances are only created on demand
* `Activity_Output`: the runtime data of all Output Parameters of an Activity.

## Entities Storing Useful Codes

Some useful codes are stored in the following (static) entities:

* `Process_Status`: the possible statuses for a Process
* `Activity_Kind`: the kind of Activities
* `Activity_Status`: the possible statuses for an Activity
