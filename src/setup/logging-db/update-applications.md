---
summary: How to update OutSystems applications that became invalid due to the log model changes in OutSystems 11.
tags: support-Installation_Configuration; version-11
locale: en-us
guid: fb46fada-91f7-45b9-b936-b0310303f4e8
---

# Update applications that access OutSystems log data

To update any applications that became invalid after upgrading them to OutSystems 11 for having joins with log entities, you should basically take the following approach: get old log data, store it locally and perform any necessary joins to fill in missing data.

This approach can be summarized in the following steps:

1. Go through the invalid queries, i.e. queries that are joining application data with log data;

1. Identify the attributes being obtained through the join;

1. Evaluate each identified attribute, checking if it's part of the following list:  
Espace name, application key, application name, username.

    _If it is_ — These attributes were added to log entities and you can now obtain their values from them.

    _If it's not_ — Do the following:
    
    1. Create an entity to hold log information;
    1. Store the log information in the new entity;
    1. Create an aggregate joining the new entity with the entity containing the desired attribute, correlating records accordingly;
    1. Use the returned result set.


## Example use case

To better understand the exact steps that should be taken to change an application making it compatible with the OutSystems 11 log model, let's go through a real world scenario.

Consider AdoptionMonitor, an OutSystems component providing insights into a factory's application adoption statistics — who accessed what screen, when and how often — for a selected period of time, including trends over time. 

To gather this statistical data, a cyclic job periodically performs the following:

1. Read screen log information from a log entity (still residing in the platform database in  OutSystems versions prior to 11);
1. Remove any non-relevant data for statistic purposes (e.g. client IP address);
1. Add data that will make it easier to build the dashboard such as the application the log refers to;
1. Store the transformed data in the application database.

When users access AdoptionMonitor they visualize statistical information about factory applications, created from the transformed log information that is being stored in the application database.

### Issues detected after upgrading the application

After upgrading to OutSystems 11, queries used by the cyclic job became invalid, since they performed a join between the `Log_Screen` entity, now stored in the log database, with the `Application` entity, which is stored in the application database. These entities were being joined so that each log had information about the application identifier they referred to.

After analyzing metrics obtained in several customer factories, it was possible to conclude that the most common use case was "adding information to log data to understand where it was generated (e.g. module, application) and who generated it (e.g. username)".

### Changing the application

In the AdoptionMonitor example, log data was being combined with AdoptionMonitor (application) data to obtain the application identifier (i.e. the `Id` attribute value of the `Application` entity) related to each log entry, storing this information in a local entity. This entity was then used across the application to allow several use cases such as "what were the accesses made to application X?".

To make the application valid again, the developers took the following steps:

1. They removed the join;
1. They added an attribute to the local entity to hold the 'Application_Key';
1. They filled in the new attribute with the value already present in the log record;
1. After the log data was stored in the local entity, the application identifier (i.e. the `Id` attribute value of the `Application` entity) was still missing. They created a server action to perform a join between the local entity and the `Application` entity, by application key. This server action was responsible for updating the application identifier.

Note that, instead of having a server action to obtain the application identifier, the AdoptionMonitor application could have been changed to start using application keys throughout the application, dropping the need for knowning the application identifier value.  

However, along with the database performance issues that we could have for using a GUID value (a string used as the application key) instead of a number (the data type of the application identifier), in this specific case the change would be so significant that it would imply changes all the way up to the application UI. As such, the number of changes was minimized by obtaining the application identifier through a server action.

