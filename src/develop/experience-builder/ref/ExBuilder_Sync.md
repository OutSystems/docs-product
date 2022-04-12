---
locale: en-us
guid: 8b8cb064-12a6-44aa-b765-3b44f070b8ea
---

# ExBuilder_Sync

Module to implement the sync mechanism for the generated mobile applications.

## Summary

Client Action | Description
---|---
[OfflineDataSync_Wrapper](<#Client_OfflineDataSync_Wrapper>) | Client action that executes the offline data synchronization.

## Client Actions

### OfflineDataSync_Wrapper { #Client_OfflineDataSync_Wrapper }

Client action that executes the offline data synchronization.

*Inputs*

SyncUnit
:   Type: mandatory, Text.  
    Input variable with the unit to sync. This parameter allows comma separated lists of sync units to execute several syncs.  
    This parameter is set in explict synchronizations executed from the 'TriggerOfflineDataSync' client action.

