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
|EventDetails|log.body|Text|A JSON object with the details about the event. Each built-in request event has its own details: WebScreenClientExecuted; WebScreenServerExecuted; QueryExecuted; ConsumedIntegrationExecuted; ExtensionExecuted.|
|Instant|@timestamp|Date Time|Date and time when the event occurred in the front-end (server log) or in the mobile device (client log).|
|Module_Name|log.attributes.outsystems.log.message.tag|Text|Unique identifier of the module where the event occurred.|
|ModuleKey|resource.attributes.outsystems.module.key|Text|Name of the module where the event occurred.|
|RequestEventName|log.attributes.outsystems.log.event.type|Text|The name of the event.|
|RequestKey|log.attributes.outsystems.request.key|GUID|Correlation field of the several log types to a single request.|
|N/A|log.attributes.outsystems.log.type|Text|Type of log: RequestEvent. This field can be used to differentiate the different log types. In Elastic Cloud, it is named as  `labels.outsystems_log_type`|

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
