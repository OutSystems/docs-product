---
tags: 
summary: 
locale: en-us
guid: b50a081a-6a39-46aa-acc6-23909bcf0247
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---


# Avoid site property updates

Site properties, loaded by the server and then cached for faster access, are used to hold data that has to be available across the module. It's a configuration-related information that should be updated manually in Service Center. It's possible to update them programmatically, but it's not recommended: site properties aren't designed to be a “global variable” and store information that changes frequently. For example, don't hold the timestamp of the last sync or a counter for processed elements in these properties. 

## Impact

Every time you update a site property, the cache of the module and its consumers will be invalidated and reloaded from the database again. This causes unnecessary database overhead for all parts of the application using site properties. 

## Best practices

Place non-configuration information that needs to be changed in a specific database table. This way the data can be updated without invalidating the cache and without degrading the performance of the app.
