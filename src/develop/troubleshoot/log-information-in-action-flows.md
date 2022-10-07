---
summary: Use the LogMessage System Action when debugging action flows or to register some kind of information that you wish to examine at runtime.
tags: support-application_development; support-Application_Troubleshooting
locale: en-us
guid: 2ebf3be6-b46a-4276-94f6-af76e4b07ff0
app_type: traditional web apps, mobile apps, reactive web apps
---

# Log Information in Action Flows

When designing your actions you may need to debug the action flow or to register some information that you can examine afterwards, at runtime. You can do this using the [LogMessage](<../../ref/apis/auto/system-actions.final.md#LogMessage>) System Action. The information that you log, along with the exact time of log, will be available in the environment management console.

## How to Log Information in your Action Flow

1. Open your action flow. 

2. Drag the  LogMessage action from the System Objects tree to the exact place of the action flow that you want to audit. You might need to add the LogMessage System Action in the Manage Dependencies window, if it hasn’t been added before. 

3. Fill-in the Message and ModuleName properties with the information you want to log. 

If you are developing a Reactive Web or a Mobile app, you have a LogMessage Client Action to use in your client side action flows, and a LogMessage Server Action to use in your server side action flows.

You can have multiple LogMessage actions in your action flow. However, the logging is asynchronous and the order of the logs in the environment management console may not be the same as the order of the LogMessage actions in the flow. Therefore, you should not examine the log information in a sequential way.

## How to Access to the Logged Information

To access the information you have logged in your action flow, do the
following:

1. Go to the management console of your OutSystems environment. 
2. Go to the Monitoring section and select General. 
3. Select your application. You can also add to the filter the ModuleName that you used in the LogMessage property. 
4. Click Filter. 

You can view only the logged information of the modules for which you have permissions.

## Switch Off the Logging

The logging performed in the LogMessage System Action may be switched off when debugging is no longer a priority. To switch off the logging, do the following:

1. Go to the management console of your OutSystems environment. 
2. Go to the Factory section and open your application. 
3. Open the module where you added the logging. 
4. Select the Operations tab and uncheck the Auditing option. 
5. Click Apply. 

This change takes immediate effect, you don't have to publish your application again.
