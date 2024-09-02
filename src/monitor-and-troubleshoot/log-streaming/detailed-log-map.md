---
summary: Explore the integration of OpenTelemetry standards in OutSystems 11 (O11) for enhanced log data management across various modules and applications.
tags: article-page; support-Installation_Configuration; version-11; cloud_configuration; conceptual
locale: en-us
guid: 83602415-028e-4bd2-937f-99ff473939c0
app_type: traditional web apps, mobile apps, reactive web apps
figma: 
platform-version: o11
---

# Logged data fields

The underlying data schema for Log separation is based on the [OpenTelemetry](https://opentelemetry.io/) specification, an open standard to ensure vendor-agnostic data. The following tables describe the mapping between the existing data fields and the new OpenTelemetry fields. For more information about the existing data fields, see [Log data reference](../logging/reference.md)

<div class="info" markdown="1">

The field names shown in the APM tool can differ from the OpenTelemetry field names listed in the tables, as seen in the Elastic Cloud APM tool.

The field `log.attributes.outsystems.log.type` can be used to differentiate the different log types. In Elastic Cloud, this field is named as `labels.outsystems_log_type`

</div>

## General logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Action_Name|log.attributes.code.function|Text|Name of the action being called.|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Client_IP|log.attributes.http.client_ip|Text|Client IP address.|
|Entrypoint_Name|log.attributes.outsystems.log.entrypoint_name|Text|Name of the entry point being called.|
|Error_Id|log.attributes.outsystems.log.error.uid|GUID|Identifier of the related error log. Correlation with the Error Log table.|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Message|log.body|Text|Log message|
|Message_type|log.attributes.outsystems.log.message.type|Text|Message type|
|Module_Name|log.attributes.outsystems.log.message.tag|Text|Name of the originating module. Correlation with the Error Log table. Information regarding Slow calls (SLOWSQL, SLOWEXTENSION).|
|Request_Key|log.attributes.outsystems.request.key|GUID|Key of the request that originated the log. Correlation field of the several log types to a single request.|
|Session_Id|log.attributes.outsystems.user.session.id|Text|User Session Identifier|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|User_Id|log.attributes.enduser.id|Int|User identifier. 0 if no user logged in (anonymous navigation).|
|Username|log.attributes.outsystems.user.name|Text|Username relative to the authenticated session|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: General. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Error logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Action_Name|log.attributes.code.function|Text|The name of the action that was handling the request. Actions include the Preparation action and Screen Actions. Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Entrypoint_Name|log.attributes.outsystems.log.entrypoint_name|Text|The name of the web screen that was handling the request.|
|EnvironmentInformation|log.attributes.outsystems.log.environment_information|Text|Detailed low-level information on environmental context of the application (eSpaceVer, RequestUrl, AppDomain, Path, Locale, DateFormat, PID, TID, Thread Name and .NET version).|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Id|log.attributes.outsystems.log.error.uid|GUID|Unique identifier of the error message.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Message|log.body|Text|Error message logged by the application / OutSystems services.|
|Module_Name|log.attributes.outsystems.log.message.tag|Text|Label used to identify specific types of error messages.|
|Request_Key|log.attributes.outsystems.request.key|GUID|Key of the request that originated the log. Correlation field of several log types to a single request.|
|Server|resource.attributes.host.name|Text|Front-end server that originated the error (server log) or empty (client log).|
|Session_Id|log.attributes.outsystems.user.session.id|Text|User session identifier|
|Stack|log.attributes.exception.stacktrace|Text|Error stack logged by the application / OutSystems service|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|User_Id|log.attributes.enduser.id|Int|User identifier. 0 if no user logged in (anonymous navigation).|
|Username|log.attributes.outsystems.user.name|Text|Username relative to the authenticated session|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: Error. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## RequestEvent logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier of the application where the event occurred.|
|Application_Name|resource.attributes.outsystems.app.name|Text|Name of the application where the event occurred.|
|EventDetails|log.body|Text|A JSON object with the details about the event. Each built-in request event has its own details:<br/>• [WebScreenClientExecuted](#webscreenclientexecuted-details)<br/>• [WebScreenServerExecuted](#webscreenserverexecuted-details)<br/>• [QueryExecuted](#queryexecuted-details)<br/>• [ConsumedIntegrationExecuted](#consumedintegrationexecuted-details)<br/>• [ExtensionExecuted](#extensionexecuted-details).|
|Instant|@timestamp|Date Time|Date and time when the event occurred in the front-end (server log) or in the mobile device (client log).|
|Module_Name|log.attributes.outsystems.log.message.tag|Text|Unique identifier of the module where the event occurred.|
|ModuleKey|resource.attributes.outsystems.module.key|Text|Name of the module where the event occurred.|
|RequestEventName|log.attributes.outsystems.log.event.type|Text|The name of the event.|
|RequestKey|log.attributes.outsystems.request.key|GUID|Correlation field of the several log types to a single request.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: RequestEvent. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

#### Request event details for WebScreenClientExecuted event { #webscreenclientexecuted-details }

| Existing data field | OpenTelemetry field | Meaning | Description|
|:-|:-|:-:|-|  
|AK |outsystems.request.event.details.ak| Action Key | The key of the action that was handling the request on the server.|
|AN |outsystems.request.event.details.an| Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".|
|EK |outsystems.request.event.details.ek| Environment Key | The unique key identifying the environment the user was accessing.|
|EN |outsystems.request.event.details.en| Environment Name | The name of the environment the user was accessing.|
|EPK |outsystems.request.event.details.epk| EndPoint Key | The key of the web screen that was handling the request.|
|EPN |outsystems.request.event.details.epn| EndPoint Name | The name of the web screen that was handling the request.|
|TK |outsystems.request.event.details.tk| Tenant Key | A unique key identifying the tenant.|
|TN |outsystems.request.event.details.tn| Tenant Name | The name of the tenant.|
|FN |outsystems.request.event.details.fn| Front-end Name | The name of the front-end server that handled the request.|
|VK |outsystems.request.event.details.vk| Visitor Key | Unique identifier key for the visitor that performed the request.<br/>A visitor is a combination of a device and a browser. The key is created at the first time the visitor accesses the website's domain using a given device and browser. The same key is used until the browser cookies are cleared.|
|ViK |outsystems.request.event.details.vik| Visit Key | Unique identifier of the visit associated with the current request.<br/>A visit is defined as a series of page requests from the same visitor. A visit is considered finished when no requests have been recorded for 30 minutes.|
|SK |outsystems.request.event.details.sk| Session Key | Unique identifier of the session associated with the request.|
|UK |outsystems.request.event.details.uk| User Key | Unique user identifier associated with the user, if logged in during the request.|
|SR |outsystems.request.event.details.sr| Screen Resolution | The browser window screen resolution. Formatted as "&lt;width&gt;x&lt;height&gt;". Example: "1024x768".|
|UA |outsystems.request.event.details.ua| User Agent | The user agent string as provided by the browser.|
|D |outsystems.request.event.details.d| Duration | The time, in milliseconds, that passed from the moment the user made the request (for example, by clicking on a link) until the browser finished processing the response.<br/>Note: This attribute is related only to the HTTP request itself. If the HTML contains references to other resources (for example, images or fonts), the time it took to download and process those resources is not included.|
|LT |outsystems.request.event.details.lt| Load Time | The time, in milliseconds, that the browser took to process the response. The load time includes for example the page rendering and the JavaScript execution.|
|TTFB |outsystems.request.event.details.ttfb| Time To First Byte | The time, in milliseconds, that passed from the moment the user made the request (for example, user clicked on a link), until the browser received the first byte of the response from the Platform Server.|
|TTLB |outsystems.request.event.details.ttlb| Time To Last Byte | The time, in milliseconds, that passed from the moment the user made the request (for example, user clicked on a link), until the browser received the last byte of the response from the Platform Server.|

#### Request event details for WebScreenServerExecuted event { #webscreenserverexecuted-details }

| Existing data field | OpenTelemetry field | Meaning | Description|
|:-|:-|:-:|-|  
|TK |outsystems.request.event.details.tk| Tenant Key | A unique key identifying the tenant.|
|TN |outsystems.request.event.details.tn| Tenant Name | The name of the tenant.|
|EK |outsystems.request.event.details.ek| Environment Key | The unique key identifying the environment the user was accessing.|
|EN |outsystems.request.event.details.en| Environment Name | The name of the environment the user was accessing.|
|FN |outsystems.request.event.details.fn| Front-end Name | The name of the front-end server that handled the request.|
|EPK |outsystems.request.event.details.epk| EndPoint Key | The key of the web screen that was handling the request.|
|EPN |outsystems.request.event.details.epn| EndPoint Name | The name of the web screen that was handling the request.|
|AK |outsystems.request.event.details.ak| Action Key | The key of the action that was handling the request on the server.|
|AN |outsystems.request.event.details.an| Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".|
|D |outsystems.request.event.details.d| Duration | The time, in milliseconds, that passed from the moment the user made the request (for example, by clicking on a link) until the browser finished processing the response.<br/>Note: This attribute is related only to the HTTP request itself. If the HTML contains references to other resources (for example, images or fonts), the time it took to download and process those resources is not included.|
|TQT |outsystems.request.event.details.tqt| Total Query Time | The total time spent, in milliseconds, executing queries (Aggregates and Advanced Queries).|
|TQE |outsystems.request.event.details.tqe| Total Query Executions | The total number of executed queries (Aggregates and Advanced Queries).|
|TET |outsystems.request.event.details.tet| Total Extension Time | The total time spent, in milliseconds, calling actions provided by extensions.|
|TEE |outsystems.request.event.details.tee| Total Extension Executions | The total number of calls to actions provided by extensions.|
|TCIT |outsystems.request.event.details.tcit| Total Consumed Integration Time | The total time spent, in milliseconds, calling actions provided by consumed integrations (SOAP, REST, SAP).|
|TCIE |outsystems.request.event.details.tcie| Total Consumed Integration Executions | The total number of calls to actions provided by consumed integrations (SOAP, REST, SAP).|
|TSAT |outsystems.request.event.details.tsat| Total Consumed Service Action Time | The total time spent, in milliseconds, calling service actions.|
|TSAE |outsystems.request.event.details.tsae| Total Consumed Service Action Calls | The total number of calls of service actions.|
|IP |outsystems.request.event.details.ip| Client IP | The client's public IP address, collected from the [X-FORWARDED-FOR header](http://tools.ietf.org/html/rfc7239#section-5.2), or if that doesn't exist, from the [REMOTE_ADDR header](https://www.ietf.org/rfc/rfc3875).|
|SAT |outsystems.request.event.details.sat| Session Acquisition Time | The time spent, in milliseconds, retrieving the session from the database.|
|SS |outsystems.request.event.details.ss| Session Size | The session size, in bytes.|
|VSS |outsystems.request.event.details.vss| View State Size | The view state, in bytes.|
|UID |outsystems.request.event.details.uid| User Id | The unique identifier of the user that made the request. It corresponds to the user's identifier stored in the User system entity.<br/>If the request was made by an anonymous user, the User Id isn't included in the event attributes.|
|EC |outsystems.request.event.details.ec| Number of errors | The number of errors that occurred during the request.|

#### Request event details for QueryExecuted event { #queryexecuted-details }

| Existing data field | OpenTelemetry field | Meaning | Description|
|:-|:-|:-:|-|  
|TK |outsystems.request.event.details.tk| Tenant Key | A unique key identifying the tenant.|
|TN |outsystems.request.event.details.tn| Tenant Name | The name of the tenant.|
|AK |outsystems.request.event.details.ak| Action Key | The key of the action that was handling the request.|
|AN |outsystems.request.event.details.an| Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".|
|EK |outsystems.request.event.details.ek| Environment Key | The unique key identifying the environment the user was accessing.|
|EN |outsystems.request.event.details.en| Environment Name | The name of the environment the user was accessing.|
|EPK |outsystems.request.event.details.epk| EndPoint Key | The key of the web screen that was handling the request.|
|EPN |outsystems.request.event.details.epn| EndPoint Name | The name of the web screen that was handling the request.|
|FN |outsystems.request.event.details.fn| Front-end Name | The name of the front-end server that handled the request.|
|D |outsystems.request.event.details.d| Duration | The total duration of all the slow query executions.|
|OK |outsystems.request.event.details.ok| Object Key | The key that identifies the slow query.|
|ON |outsystems.request.event.details.on| Object Name | The name of the slow query.|
|NE |outsystems.request.event.details.ne| Number of Executions | The total number of calls for a given slow query.|
|OEK |outsystems.request.event.details.oek| Object's eSpace Key | The key of the application module where the slow query was called.| 
|OEN |outsystems.request.event.details.oen| Object's eSpace Name | The name of the application module where the slow query was called.|
|EC |outsystems.request.event.details.ec| Number of errors | The number of errors that occurred during the request.|

#### Request event details for ConsumedIntegrationExecuted event { #consumedintegrationexecuted-details }

| Existing data field | OpenTelemetry field | Meaning | Description|
|:-|:-|:-:|-|  
|TK |outsystems.request.event.details.tk| Tenant Key | A unique key identifying the tenant.|
|TN |outsystems.request.event.details.tn| Tenant Name | The name of the tenant.|
|EK |outsystems.request.event.details.ek| Environment Key | The unique key identifying the environment the user was accessing.|
|EN |outsystems.request.event.details.en| Environment Name | The name of the environment the user was accessing.|
|FN |outsystems.request.event.details.fn| Front-end Name | The name of the front-end server that handled the request.|
|ON |outsystems.request.event.details.on| Object Name | The name of the slow integration method.|
|OK |outsystems.request.event.details.ok| Object Key | The key that identifies the slow integration method.|
|OEN |outsystems.request.event.details.oen| Object's eSpace Name | The name of the application module where the slow integration was called.| 
|OEK |outsystems.request.event.details.oek| Object's eSpace key | The key of the application module where the slow integration was called.|
|NE |outsystems.request.event.details.ne| Number of Executions | The total number of calls for a given slow integration.|
|D |outsystems.request.event.details.d| Duration | The total duration of all the slow integration executions.|
|EPK |outsystems.request.event.details.epk| EndPoint Key | The key of the web screen that was handling the request.|
|EPN |outsystems.request.event.details.epn| EndPoint Name | The name of the web screen that was handling the request.|
|AK |outsystems.request.event.details.ak| Action Key | The key of the action that was handling the request.|
|AN |outsystems.request.event.details.an| Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".|
|IT |outsystems.request.event.details.it| Integration Type | The integration type. Current supported integration types: SOAP, REST and SAP.|
|IE |outsystems.request.event.details.ie| Integration Endpoint | The integration's endpoint URL.|
|EC |outsystems.request.event.details.ec| Number of errors | The number of errors that occurred during the request.|

#### Request event details for ExtensionExecuted event { #extensionexecuted-details }

| Existing data field | OpenTelemetry field | Meaning | Description|
|:-|:-|:-:|-|  
|TK |outsystems.request.event.details.tk| Tenant Key | A unique key identifying the tenant.|
|TN |outsystems.request.event.details.tn| Tenant Name | The name of the tenant.|
|EK |outsystems.request.event.details.ek| Environment Key | The unique key identifying the environment the user was accessing.|
|EN |outsystems.request.event.details.en| Environment Name | The name of the environment the user was accessing.|
|FN |outsystems.request.event.details.fn| Front-end Name | The name of the front-end server that handled the request.|
|OK |outsystems.request.event.details.ok| Object key | The key that identifies the slow extension's action.|
|ON |outsystems.request.event.details.on| Object name | The name of the slow extension's action.|
|OEK |outsystems.request.event.details.oek| Object's eSpace key | The key of the eSpace where the slow extension action was called.|
|OEN |outsystems.request.event.details.oen| Object's eSpace name | The name of the eSpace where the slow extension action was called.|
|NE |outsystems.request.event.details.ne| Number of Executions | The total number of calls for a given slow extension's action.|
|D |outsystems.request.event.details.d| Duration | The total duration of all the slow extension executions.|  
|EPK |outsystems.request.event.details.epk| EndPoint Key | The key of the web screen that was handling the request.|
|EPN |outsystems.request.event.details.epn| EndPoint Name | The name of the web screen that was handling the request.|
|AK |outsystems.request.event.details.ak| Action Key | The key of the action that was handling the request.|
|AN |outsystems.request.event.details.an| Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".|
|EC |outsystems.request.event.details.ec| Number of errors | The number of errors that occurred during the request.|

## CyclicJob logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Cyclic_Job_Key|log.attributes.outsystems.code.function.key|GUID|Unique identifier of the cyclic job that was executed.|
|Cyclic_Job_Name|log.attributes.code.function|Text|The name of the cyclic job that was executed.|
|Duration|log.attributes.outsystems.request.duration|Int|Duration, in seconds, of the execution of the job.|
|Error_Id|log.attributes.outsystems.log.error.uid|GUID|Correlation with the Error Log table|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Executed_By|resource.attributes.host.name|Text|Front-end server that originated the log.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Next_Run|log.attributes.outsystems.timer.nextrun|Date Time|Schedule for next run|
|Request_Key|log.attributes.outsystems.request.key|GUID|Correlation field of the several log types to a single request.|
|Should_Have_Run_At|log.attributes.outsystems.timer.shouldhaverunat|Date Time|Scheduled time for execution of this  cyclic job. Instant of execution is expected to be equal or larger than this field.|
|Tenant_Id|log.attributes.outsystems.tenant_id|Int|ID of the tenant where the message  was logged. 0 if message originates  from an OutSystems service.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: CyclicJob. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Extension logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Action_Name|log.attributes.code.function|Text|Name of the action being called.|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Duration|log.attributes.outsystems.request.duration|Int|Time in seconds the extension call took.|
|Error_Id|log.attributes.outsystems.log.error.uid|GUID|Identifier of the related error log.|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Executed_By|resource.attributes.host.name|Text|Front-end server that originated the log.|
|Extension_Id|log.attributes.outsystems.code.owner.function.id|Int|Extension from where the log was originated.|
|Extension_Name|log.attributes.outsystems.code.function.owner|Text|The name of the extension.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Request_Key|log.attributes.outsystems.request.key|GUID|Correlation field of the several log types to a single request.|
|Session_Id|log.attributes.outsystems.user.session.id|Text|User Session Identifier.|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|User_Id|log.attributes.enduser.id|Int|User identifier. 0 if no user logged in (anonymous navigation).|
|Username|log.attributes.outsystems.user.name|Text|Username relative to the authenticated session|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: Extension. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Integration logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Action|log.attributes.code.function|Text|Name of the service and action being consumed / exposed. For SOAP (CONSUME), in the form of &lt;service&gt; (&lt;method&gt; For all other types, in the form of &lt;service&gt;. &lt;method&gt;.|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Duration|log.attributes.outsystems.request.duration|Int|Duration of the execution of the integration, in milliseconds. For CONSUME type, this is the time from the beginning of the request to the external system until the response finished transmission to the platform, including the time it takes to create the connection /request and the time spent executing any OnBeforeRequest callback. For EXPOSE type, this is the time from the beginning of execution on the platform until the end of transmission to the external system.|
|Endpoint|log.attributes.outsystems.log.endpoint|Text|For CONSUME type this is the URL of the external system; empty / meaningless for EXPOSE type.|
|Error_Id|log.attributes.outsystems.log.error.uid|GUID|Correlation with the Error Log table.|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Executed_By|resource.attributes.host.name|Text|Front-end server that served the service (EXPOSE) or that called the external system (CONSUME).|
|Id|log.attributes.outsystems.log.uid|Text|Unique identifier.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Is_Expose|log.attributes.outsystems.integration.type|Bool|True if log refers to an integration being exposed. False if calling an integration.|
|Request_Key|log.attributes.outsystems.request.key|Text|Key of the request that originated the log. Correlation field of the several log types to a single request.|
|Source|log.attributes.net.host.ip|Text|Empty / meaningless for CONSUME type; for EXPOSE type this is the source IP of the external system.|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|Type|log.attributes.http.method|Text|One of: SOAP (Consume); SOAP (Expose); REST (Consume); REST (Expose).|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: Integration. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Integration detail 

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Detail|log.attributes.outsystems.log.detail|Text|Detailed log information.|
|DetailLabel|log.attributes.outsystems.log.detail_label|Text|Informative label about what is being logged.|
|Id|log.attributes.outsystems.log.uid|text|Unique identifier.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Message|log.attributes.outsystems.log.detail_message|Text|Short log information.|
|TenantId|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: IntDetailLog. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## MobileRequest logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Duration|log.attributes.outsystems.request.duration|Int|Time in seconds that the request took.|
|Endpoint|log.attributes.code.function|Text|Endpoint being called|
|Error_Id|log.attributes.outsystems.log.error.uid|GUID|Correlation with the Error Log table.|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Executed_By|resource.attributes.host.name|Text|Front-end server that originated the log.|
|Id|log.attributes.outsystems.log.uid|GUID|Unique identifier of the log entry.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Login_Id|log.attributes.outsystems.user.login_id|Text|Authenticated session identifier.|
|Request_Key|log.attributes.outsystems.request.key|GUID|Correlation field of the several log types to a single request.|
|Screen|log.attributes.outsystems.log.screen.name|Text|Application screen mobile request took place.|
|Source|log.attributes.net.host.ip|Text|Source IP address|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|User_Id|log.attributes.enduser.id|Int|User identifier. 0 if no user logged in (anonymous navigation).|
|Username|log.attributes.outsystems.user.name|Text|Username relative to the authenticated session|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: MobileRequest. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Mobile request detail logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Detail|log.attributes.outsystems.log.detail|Text|Log detailed information.|
|DetailLabel|log.attributes.outsystems.log.detail_label|Text|Type of detail|
|Id|log.attributes.outsystems.log.uid|GUID|Unique identifier of the log entry.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Message|log.attributes.outsystems.log.detail_message|Text|Log message|
|TenantId|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: MRDetailLog. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Screen logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Access_mode|log.attributes.outsystems.log.screen.access_mode|Text|Type of web request access (AJAX, SCREEN).|
|Action_name|log.attributes.code.function|Text|Name of the action being called|
|Application_key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Client_ip|log.attributes.http.client_ip|Text|IP of the end user as identified by the platform. This the client IP, if there is an X-FORWARD it appears with the first (Client) and last IP (last proxy IP).|
|Duration|log.attributes.outsystems.request.duration|Int|Duration of the request, as measured on the server side, in milliseconds.|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the modulee.|
|Executed_by|resource.attributes.host.name|Text|Front-end server that originated the log.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Msisdn|Msisdn||Text|Cell phone number if screen belongs to a SMS flow.|
|Request_key|log.attributes.outsystems.request.key|GUID|Key of the request that originated the log. Correlation field of the several log types to a single request.|
|Screen|log.attributes.outsystems.log.screen.name|Text|Name of the screen as declared in the eSpace where it's present. For SMS Flows, name of the SMS Node.|
|Screen_Type|log.attributes.outsystems.log.screen.type|Text|Type of screen (WEB, MOBILE).|
|Session_bytes|log.attributes.outsystems.traditional.ss|Int|Size of the session associated with this request, in bytes, at the beginning of the request.|
|Session_Id|log.attributes.outsystems.user.session.id|Text|User Session Identifier|
|Session_requests|log.attributes.outsystems.user.session_calls|Int|Number of requests to user session.|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|User_Id|log.attributes.enduser.id|Int|User identifier. 0 if no user logged in (anonymous navigation).|
|Username|log.attributes.outsystems.user.name|Text|Username relative to the authenticated session|
|Viewstate_bytes|log.attributes.outsystems.log.viewstate_bytes|Int|Size of the viewstate associated with this request. 0 if the request has no viewstate (GET); greater than 0 if the request is a POST or AJAX request.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: Screen. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Service Action logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Action_Name|log.attributes.code.function|Text|Name of the action being called|
|Application_Key|resource.attributes.outsystems.app.key|Text|Unique identifier for the application.|
|Application_Name|resource.attributes.outsystems.app.name|Text|The name of the app.|
|Duration|log.attributes.outsystems.request.duration|Int|Time in seconds that the service API call took|
|Endpoint|log.attributes.outsystems.log.endpoint|Text|Duration of the request, as measured on the server side, in milliseconds.|
|Entrypoint_Name|log.attributes.outsystems.log.entrypoint_name|Text|The name of the web screen that was handling the request.|
|Error_Id|log.attributes.outsystems.log.error.uid|GUID|Correlation with the Error Log table.|
|Espace_Id|resource.attributes.outsystems.module.id|Int|Module from where the log was originated. 0 if the message originates from an OutSystems service.|
|Espace_Name|resource.attributes.service.name|Text|The name of the module.|
|Executed_by|resource.attributes.host.name|Text|Front-end server that originated the log.|
|Id|log.attributes.outsystems.log.uid|Text|Unique identifier of the log entry.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Login_Id|log.attributes.outsystems.user.login_id|Text|Authenticated session identifier.|
|Original_Request_Key|log.attributes.outsystems.request.original_key|GUID|Key of the request of the original caller (module) that triggered the Service API call|
|Request_Key|log.attributes.outsystems.request.key|GUID|Key of the request that originated the log. Correlation field of the several log types to a single request.|
|Session_Id|log.attributes.outsystems.user.session.id|Text|User Session Identifier|
|Source|log.attributes.net.host.ip|Text|Source IP address|
|Tenant_Id|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|User_Id|log.attributes.enduser.id|Int|User identifier. 0 if no user logged in (anonymous navigation).|
|Username|log.attributes.outsystems.user.name|Text|Username relative to the authenticated session|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: ServiceAPI. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

## Service API detail logs

|Existing data field|OpenTelemetry field|Data type|Description|
|:-|:-|:-:|-|
|Detail|log.attributes.outsystems.log.detail|Text|Detailed log information.|
|DetailLabel|log.attributes.outsystems.log.detail_label|Text|Informative label about what is being logged.|
|Id|log.attributes.outsystems.log.uid|text|Unique identifier.|
|Instant|@timestamp|Date Time|Time of log generation in the front end (server log) or time of log generation in the mobile device (client log).|
|Message|log.attributes.outsystems.log.detail_message|Text|Short log information.|
|TenantId|log.attributes.outsystems.tenant.id|Int|ID of the tenant where the message was logged. 0 if message originates from an OutSystems service.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: ServiceAPIDetailLog. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|
