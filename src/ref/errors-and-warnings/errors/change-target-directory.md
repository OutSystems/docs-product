---
summary: Fix the target directory of a resource to allow your deployment to complete.
tags:
locale: en-us
guid: 3be20de4-b979-43e3-89a4-c56d7b9ea6f1
app_type: traditional web apps, mobile apps, reactive web apps
---

# Change target directory error

## Error message
You must change the target directory of the *resource_name* before deploying, as it can't be located at the *directory_name* system resource directory.

## Cause
You specified an invalid target directory for a resource in your module. This target isn't valid because it's a system-level resource directory. 

## Recommended action
In Service Studio, change the target directory of the specified resource to a directory that isn't a system resource directory. 

To change the resource target: 
1. Go to the **Data** tab > **Resources**.

1. Select the resource you want to change. 

1. In the **properties pane**, change the target directory to one that isn't a system resource directory.

