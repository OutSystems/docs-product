---
summary: API to access logged request events by OutSystems Platform with valuable data for your analytics. You can use it to analyze the user experience of your applications.
tags: support-devOps; support-monitoring
---

# PerformanceMonitoring API

To allow you to analyze the user experience of your applications, OutSystems logs [request events](#requestevent) with valuable data for your analytics. To give you access to request events, the PerformanceMonitoring API provides REST API methods to:

* retrieve a list of request events that occurred in your application
* register your own request related events

The server only stores data for the last two days. Learn [how application performance is measured](../../managing-the-applications-lifecycle/monitor-and-troubleshoot/how-application-performance-is-measured.md).

## Summary

Methods | Description
---|---  
[GET RequestEvents](#get-requestevents) | Returns a list of request events, filtered by the event names and time interval you specify in the parameters.
[POST RequestEvents](#post-requestevents) | Logs a request event. Based on that data you can analyze the user experience of your applications.

Resources | Description
---|---  
[RequestEvent](#requestevent) | Represents an event of a web request, sent to an OutSystems application.

## Methods

### GET RequestEvents

Returns a list of request events, filtered by event names and time interval you specify in the parameters.

This method requires basic authentication. You need to provide the credentials of a LifeTime user. It returns request events only for those applications to which the user has 'Reuse & Monitor' permission in the environment. Learn more about how to [configure security for an infrastructure](../../managing-the-applications-lifecycle/manage-it-teams/intro.md).

To use it in an application, make sure that [monitoring is turned on](../../managing-the-applications-lifecycle/monitor-and-troubleshoot/enable-analytics-for-an-environment.md) for the environment, and for the application module. Otherwise the API responds with a status code of '200 - OK', but doesn't retrieve any events.

#### URL

`http://[server]/PerformanceProbe/rest/PerformanceMonitoringAPI/RequestEvents/?EventNames={EventNames}&StartInstant={StartInstant}&EndInstant={EndInstant}&NumberOfResults={NumberOfResults}`

#### Input

EventNames
:   Type: string, optional, sent in the URL.  
    List of events to filter on. Separate event names with a comma.  
    Example: "WebScreenClientExecuted,WebScreenServerExecuted".

StartInstant
:   Type: date time, mandatory, sent in the URL.  
    The start date and time of the time interval you want to filter on. Format: ISO 8601.  
    Example: "2012-04-23T18:25:43.511Z".

EndInstant
:   Type: date time, mandatory, sent in the URL.  
    The end date and time of the time period you want to filter on. Format: ISO 8601.  
    Example: "2012-04-23T18:25:43.511Z".

NumberOfResults
:   Type: int32, optional, sent in the URL.  
    The maximum number of events to return. Note that the actual upper limit never exceeds the default limit (15000).  
    This limit is set in the 'MaxResponseSize' site property of the PerformanceProbe module of your environment.

#### Output

RequestEventList
:   Type: list of RequestEvent.  
    List of RequestEvent objects filtered on.

ResultsTruncated
:   Type: boolean.  
    Indicates if not all the results were returned, due to the limit of objects in the list.  
    This can occur due to the limit set either in the 'NumberOfResults' parameter, or in the 'MaxResponseSize' site property of the PerformanceProbe module of your environment. Default limit: 15000.  
    To retrieve the next set of results, you can send a new GET request. Set its StartInstant parameter to the Instant of the most recent RequestEvent you got on the previous request.

#### Example request

```
curl --user mike.fitt:123456 
"http://outsystemscloud.com/PerformanceProbe/rest/PerformanceMonitoringAPI/RequestEvents/?StartInstant=2015-09-28T12:45:00.000Z&EndInstant=2015-09-28T12:47:00.025Z"
```

#### Example result

```javascript
{
    "RequestEventList": [
        {
            "Instant": "2015-09-28T12:46:50.713Z",
            "RequestKey": "11bcf87b-35ca-44dc-b4b3-567db2a159cb",
            "RequestEventName": "WebScreenClientExecuted",
            "ModuleKey": "1e758d31-e7de-4641-a731-d3976254108d",
            "ModuleName": "PerformanceSampleDat",
            "ApplicationKey": "d026f21a-cbe8-490e-8fbb-47b7fe0db79e",
            "ApplicationName": "Performance Sample Data",
            "RequestEventDetails": {
                "AK": "7449c66a-9863-4673-91c0-cb0440344497",
                "AN": "StartBootstrap",
                "EPK": "5a0a2e6c-570f-414f-9b19-ee2cafde273d",
                "EPN": "HomePage",
                "TK": "6284e8bf-2aa5-50a4-f1bc-9918c2801df6",
                "TN": "Users",
                "EK": "c5be45ac-ccac-4091-a825-d6a7bb9554a0",
                "EN": "Development",
                "FN": "qaos1296lt5308",
                "VK": "d6aa213f-6b4a-42b6-8e39-6624008a576a",
                "ViK": "82359545-98b8-4010-8c72-cca1a2fe7b3b",
                "SK": "73562726-2f4f-9bc1-9f44-6219febee940",
                "UK": "666d9979-32be-4b2d-5271-d267d996bfca",
                "SR": "1680x1050",
                "D": 314,
                "LT": 2,
                "TTFB": 312,
                "TTLB": 312,
                "UA": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/45.0.2454.93 Safari\/537.36"
            }
        },
        {
            "Instant": "2015-09-28T12:46:51.037Z",
            "RequestKey": "ad133aee-5cc9-4eb9-8faf-016d2b811d0c",
            "RequestEventName": "WebScreenClientExecuted",
            "ModuleKey": "1e758d31-e7de-4641-a731-d3976254108d",
            "ModuleName": "PerformanceSampleDat",
            "ApplicationKey": "d026f21a-cbe8-490e-8fbb-47b7fe0db79e",
            "ApplicationName": "Performance Sample Data",
            "RequestEventDetails": {
                "AK": "f6151d08-6edd-01a7-e402-8f5a6a6fce40",
                "AN": "Feedback_Message.Refresh",
                "EPK": "5a0a2e6c-570f-414f-9b19-ee2cafde273d",
                "EPN": "HomePage",
                "TK": "6284e8bf-2aa5-50a4-f1bc-9918c2801df6",
                "TN": "Users",
                "EK": "c5be45ac-ccac-4091-a825-d6a7bb9554a0",
                "EN": "Development",
                "FN": "qaos1296lt5308",
                "VK": "d6aa213f-6b4a-42b6-8e39-6624008a576a",
                "ViK": "82359545-98b8-4010-8c72-cca1a2fe7b3b",
                "SK": "73562726-2f4f-9bc1-9f44-6219febee940",
                "UK": "666d9979-32be-4b2d-5271-d267d996bfca",
                "SR": "1680x1050",
                "D": 179,
                "LT": 24,
                "TTFB": 155,
                "TTLB": 155,
                "UA": "Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/45.0.2454.93 Safari\/537.36"
            }
        }
    ],
    "ResultsTruncated": false
}
```

### POST RequestEvents

Adds an event to the request event logs, allowing you to collect custom data about web requests. This method uses the [LogRequestEvent](auto/asynchronous-logging-api.final.md) method of the AsynchronousLogging API, which relies on a non-persistent message queue. As a result, request events that are in the message queue waiting to be processed are lost in the case of a system failure.

To use this method in an application, make sure that [monitoring is turned on](../../managing-the-applications-lifecycle/monitor-and-troubleshoot/enable-analytics-for-an-environment.md) for the environment, and for the application module. Otherwise the API responds with a status code of '200 – OK', but doesn't register the event.

#### URL

`http://<server>/PerformanceProbe/rest/PerformanceMonitoringAPI/RequestEvents/`

#### Input

RequestEvent
:   Type: RequestEvent, mandatory, sent in the request body (JSON).  
    The event of a request in an application to be logged.

#### Example request

```
curl -X POST -H "Content-Type: application/json" 
-d {\"Instant\":\"2015-09-28T12:46:50.713Z\",\"RequestKey\":\"67b6ae64-fbf0-4e45-b798-0981749018ba\",   
\"RequestEventName\":\"TelecomServices_ModuleLoaded\",\"ModuleKey\":\"2d206f37-af0b-4b46-b11e-375f50c3c282\",  
\"ModuleName\":\"TelecomServices\",\"ApplicationKey\":\"00000000-0000-0000-0000-006f74686572\",  
\"ApplicationName\":\"Field%20Services\",\"RequestEventDetails\":\"{\\\"Ver\\\":\\\"7.2\\\"}\"} 
http://outsystemscloud.com/PerformanceProbe/rest/PerformanceMonitoringAPI/RequestEvents/
```

## Resources

### RequestEvent

<table markdown="1">
<thead>
<tr>
<th>Property</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>Instant</td>
<td>Date and time when the event occurred.</td>
</tr>
<tr>
<td>Request Key</td>
<td>The GUID that identifies the request.</td>
</tr>
<tr>
<td>Request Event Name</td>
<td>The name of the event.</td>
</tr>
<tr>
<td>Module Key</td>
<td>Unique identifier of the module where the event occurred.</td>
</tr>
<tr>
<td>Module Name</td>
<td>Name of the module where the event occurred.</td>
</tr>
<tr>
<td>Application Key</td>
<td>Unique identifier of the application where the event occurred.</td>
</tr>
<tr>
<td>Application Name</td>
<td>Name of the application where the event occurred.</td>
</tr>
<tr>
<td>Request Event Details</td>
<td>A JSON object with the details about the event. Each built-in request event has its own details:<br/>
&#8226; [WebScreenClientExecuted](#webscreenclientexecuted-details)<br/>
&#8226; [WebScreenServerExecuted](#webscreenserverexecuted-details)<br/>
&#8226; [QueryExecuted](#queryexecuted-details)<br/>
&#8226; [ConsumedIntegrationExecuted](#consumedintegrationexecuted-details)<br/>
&#8226; [ExtensionExecuted](#extensionexecuted-details)<br/>
&#8226; [ScreenServer](#screenserver-details)<br/>
&#8226; [TimerExecuted](#timerexecuted-details)
</td>
</tr>
</tbody>
</table>

#### Request event details for WebScreenClientExecuted event { #webscreenclientexecuted-details }

This event occurs whenever the user’s browser finishes processing a request (initial page load, any form submission, or any AJAX request). The event's properties are the following:

Property | Meaning | Description  
---|---|---  
AK | Action Key | The key of the action that was handling the request on the server.  
AN | Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".  
EK | Environment Key | The unique key identifying the environment the user was accessing.  
EN | Environment Name | The name of the environment the user was accessing.  
EPK | EndPoint Key | The key of the web screen that was handling the request.  
EPN | EndPoint Name | The name of the web screen that was handling the request.  
TK | Tenant Key | A unique key identifying the tenant.  
TN | Tenant Name | The name of the tenant.  
FN | Front-end Name | The name of the front-end server that handled the request.  
VK | Visitor Key | Unique identifier key for the visitor that performed the request.<br/>A visitor is a combination of a device and a browser. The key is created at the first time the visitor accesses the website’s domain using a given device and browser. The same key is used until the browser cookies are cleared.  
ViK | Visit Key | Unique identifier of the visit associated with the current request.<br/>A visit is defined as a series of page requests from the same visitor. A visit is considered finished when no requests have been recorded for 30 minutes.  
SK | Session Key | Unique identifier of the session associated with the request.  
UK | User Key | Unique user identifier associated with the user, if logged in during the request.  
SR | Screen Resolution | The browser window screen resolution. Formatted as "&lt;width&gt;x&lt;height&gt;". Example: "1024x768".  
UA | User Agent | The user agent string as provided by the browser.  
D | Duration | The time, in milliseconds, that passed from the moment the user made the request (for example, by clicking on a link) until the browser finished processing the response.<br/>Note: This attribute is related only to the HTTP request itself. If the HTML contains references to other resources (for example, images or fonts), the time it took to download and process those resources is not included.  
LT | Load Time | The time, in milliseconds, that the browser took to process the response. The load time includes for example the page rendering and the JavaScript execution.  
TTFB | Time To First Byte | The time, in milliseconds, that passed from the moment the user made the request (e.g. user clicked on a link), until the browser received the first byte of the response from the platform server.  
TTLB | Time To Last Byte | The time, in milliseconds, that passed from the moment the user made the request (e.g. user clicked on a link), until the browser received the last byte of the response from the platform server.  
DMan | Device Manufacturer | The name of the device manufacturer. The value is collected only when running the application natively on a mobile device.  
DMod | Device Model | The name of the device model. The value is collected only when running the application natively on a mobile device.  
DPlat | Device Platform | The operating system running on the device. The value is collected only when running the application natively on a mobile device.  
DPlatV | Device Platform Version | The version of the device's operating system. The value is collected only when running the application natively on a mobile device.  
NT | Network Type | The active network type used by the device. This can either be the Carrier Network Type (e.g. 3G) or WiFi. The value is collected only when running the application natively on a mobile device.  
CN | Carrier Name | The name of the communications service provider of the device. The value is collected only when running the application natively on a mobile device, and the device supports a carrier-based network service such as 3G or GPRS.  
CCC | Client Country Code | The ISO-Alpha2 country code associated with the device's carrier. The value is collected only when running the application natively on a mobile device, and the device supports a carrier-based network service such as 3G or GPRS.  
CNT | Carrier Network Type | The active network type provided by the device's carrier, such as 3G or GPRS. The value is collected only when running the application natively on a mobile device, and the device supports a carrier-based network service such as 3G or GPRS.  

#### Request event details for WebScreenServerExecuted event { #webscreenserverexecuted-details }

This event occurs whenever the server finishes handling a request. The event's properties are the following:

Property | Meaning | Description  
---|---|---  
TK | Tenant Key | A unique key identifying the tenant.  
TN | Tenant Name | The name of the tenant.  
EK | Environment Key | The unique key identifying the environment the user was accessing.  
EN | Environment Name | The name of the environment the user was accessing.
FN | Front-end Name | The name of the front-end server that handled the request.  
EPN | EndPoint Name | The name of the web screen that was handling the request.  
EPK | EndPoint Key | The key of the web screen that was handling the request.  
AN | Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen does not have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".  
AK | Action Key | The key of the action that was handling the request.  
D | Duration | The total time, in milliseconds, the server spent serving the request.<br/>Note: If the application server (for example, IIS) queued the request due to server load, the time spent waiting in the queue is not included in this metric.  
TQT | Total Query Time | The total time spent, in milliseconds, executing queries (Aggregates and Advanced Queries).  
TQE | Total Query Executions | The total number of executed queries (Aggregates and Advanced Queries).  
TET | Total Extension Time | The total time spent, in milliseconds, calling actions provided by extensions.  
TEE | Total Extension Executions | The total number of calls to actions provided by extensions.  
TCIT | Total Consumed Integration Time | The total time spent, in milliseconds, calling actions provided by consumed integrations (SOAP, REST, SAP).  
TCIE | Total Consumed Integration Executions | The total number of calls to actions provided by consumed integrations (SOAP, REST, SAP).  
IP | Client IP | The client's public IP address, collected from the [X-FORWARDED-FOR header](http://tools.ietf.org/html/rfc7239#section-5.2), or if that doesn't exist, from the [REMOTE_ADDR header](https://www.ietf.org/rfc/rfc3875).  
SAT | Session Acquisition Time | The time spent, in milliseconds, retrieving the session from the database.  
SS | Session Size | The session size, in bytes  
VSS | View State Size | The view state, in bytes.  
UID | User Id | The unique identifier of the user that made the request. It corresponds to the user's identifier stored in the User system entity.<br/>If the request was made by an anonymous user, the User Id is not included in the event attributes.
EC | Number of errors | The number of errors that occurred during the request.

#### Request event details for QueryExecuted event { #queryexecuted-details }

This event occurs when the platform detects a [slow query](../../managing-the-applications-lifecycle/monitor-and-troubleshoot/how-application-performance-is-measured.md#about-slow-calls). The event's properties are the following:

Property | Meaning | Description  
---|---|---  
TK | Tenant Key | A unique key identifying the tenant.  
TN | Tenant Name | The name of the tenant.  
AK | Action Key | The key of the action that was handling the request.  
AN | Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen does not have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".  
EK | Environment Key | The unique key identifying the environment the user was accessing.  
EN | Environment Name | The name of the environment the user was accessing.  
EPK | EndPoint Key | The key of the web screen that was handling the request.  
EPN | EndPoint Name | The name of the web screen that was handling the request.  
FN | Front-end Name | The name of the front-end server that handled the request.  
D | Duration | The total duration of all the slow query executions.  
OK | Object Key | The key that identifies the slow query.  
ON | Object Name | The name of the slow query.  
NE | Number of Executions | The total number of calls for a given slow query.  
OEK | Object’s eSpace Key | The key of the application module where the slow query was called.  
OEN | Object’s eSpace Name | The name of the application module where the slow query was called.  
EC | Number of errors | The number of errors that occured during the request.

#### Request event details for ConsumedIntegrationExecuted event { #consumedintegrationexecuted-details }

This event occurs when the platform detects a [slow consumed integration](../../managing-the-applications-lifecycle/monitor-and-troubleshoot/how-application-performance-is-measured.md#about-slow-calls). The event's properties are the following:

Property | Meaning | Description  
---|---|---  
TK | Tenant Key | A unique key identifying the tenant.  
TN | Tenant Name | The name of the tenant.  
EK | Environment Key | The unique key identifying the environment the user was accessing.  
EN | Environment Name | The name of the environment the user was accessing. 
FN | Front-end Name | The name of the front-end server that handled the request.  
ON | Object Name | The name of the slow integration method.  
OK | Object Key | The key that identifies the slow integration method.  
OEN | Object's eSpace Name | The name of the application module where the slow integration was called.  
OEK | Object's eSpace key | The key of the application module where the slow integration was called.  
NE | Number of Executions | The total number of calls for a given slow integration.  
D | Duration | The total duration of all the slow integration executions.  
EPN | EndPoint Name | The name of the web screen that was handling the request.  
EPK | EndPoint Key | The key of the web screen that was handling the request.  
AN | Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen does not have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)".  
AK | Action Key | The key of the action that was handling the request.  
IT | Integration Type | The integration type. Current supported integration types: SOAP, REST and SAP.  
IE | Integration Endpoint | The integration's endpoint URL.  
EC | Number of errors | The number of errors that occured during the request.

#### Request event details for ExtensionExecuted event { #extensionexecuted-details }

This event occurs when the platform detects a [slow extension action](../../managing-the-applications-lifecycle/monitor-and-troubleshoot/how-application-performance-is-measured.md#about-slow-calls). The event's properties are the following:

Property | Meaning | Description  
---|---|---  
TK | Tenant Key | A unique key identifying the tenant.  
TN | Tenant Name | The name of the tenant.  
EK | Environment Key | The unique key identifying the environment the user was accessing.  
EN | Environment Name | The name of the environment the user was accessing. 
FN | Front-end Name | The name of the front-end server that handled the request.  
OK | Object key | The key that identifies the slow extension's action.  
ON | Object name | The name of the slow extension's action.  
OEK | Object's eSpace key | The key of the eSpace where the slow extension action was called.  
OEN | Object's eSpace name | The name of the eSpace where the slow extension action was called.  
NE | Number of Executions | The total number of calls for a given slow extension’s action.  
D | Duration | The total duration of all the slow extension executions.  
EPK | EndPoint Key | The key of the web screen that was handling the request.  
EPN | EndPoint Name | The name of the web screen that was handling the request.  
AK | Action Key | The key of the action that was handling the request.  
AN | Action Name | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen does not have a Preparation action, or if a cached version was served, then ActionName is "(PageRender)".  
EC | Number of errors | The number of errors that occurred during the request.

#### Request event details for ScreenServer event { #screenserver-details }

<div class="info" markdown="1">

Applies only to Mobile Apps and Reactive Web Apps.

</div>

This event occurs whenever the server finishes handling a request. This is identical to WebScreenServerExecuted without its client counterpart. The event's properties are the following:

| Property | Meaning                               | Description                                                  |
| -------- | ------------------------------------- | ------------------------------------------------------------ |
| TK       | Tenant Key                            | A unique key identifying the tenant.                         |
| TN       | Tenant Name                           | The name of the tenant.                                      |
| EK       | Environment Key                       | The unique key identifying the environment the user was accessing. |
| EN       | Environment Name                      | The name of the environment the user was accessing.          |
| FN       | Front-end Name                        | The name of the front-end server that handled the request.   |
| EPN      | EndPoint Name                         | The name of the web screen that was handling the request.    |
| EPK      | EndPoint Key                          | The key of the web screen that was handling the request.     |
| AN       | Action Name                           | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen does not have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)". |
| AK       | Action Key                            | The key of the action that was handling the request.         |
| D        | Duration                              | The total time, in milliseconds, the server spent serving the request.<br/>Note: If the application server (for example, IIS) queued the request due to server load, this metric doesn't include the time spent waiting in the queue. |
| TQT      | Total Query Time                      | The total time spent, in milliseconds, executing queries (Aggregates and Advanced Queries). |
| TQE      | Total Query Executions                | The total number of executed queries (Aggregates and Advanced Queries). |
| TET      | Total Extension Time                  | The total time spent, in milliseconds, calling actions provided by extensions. |
| TEE      | Total Extension Executions            | The total number of calls to actions provided by extensions. |
| TCIT     | Total Consumed Integration Time       | The total time spent, in milliseconds, calling actions provided by consumed integrations (SOAP, REST, SAP). |
| TCIE     | Total Consumed Integration Executions | The total number of calls to actions provided by consumed integrations (SOAP, REST, SAP). |
| TSAT     | Total Consumed Service Action Time    | The total time spent, in milliseconds, calling service actions. |
| TSAE     | Total Consumed Service Action Calls   | The total number of calls of service actions.                |
| IP       | Client IP                             | The client's public IP address, collected from the [X-FORWARDED-FOR header](http://tools.ietf.org/html/rfc7239#section-5.2), or if that doesn't exist, from the [REMOTE_ADDR header](https://www.ietf.org/rfc/rfc3875). |
| UID      | User Id                               | The unique identifier of the user that made the request. It corresponds to the user's identifier stored in the User system entity.<br/>If the request was made by an anonymous user,  the event attributes don't include the User Id. |
| EC       | Number of errors                      | The number of errors that occurred during the request.        |

#### Request event details for TimerExecuted event { #timerexecuted-details }

This event occurs whenever the server finishes handling a timer. The event's properties are the following:

| Property | Meaning                               | Description                                                  |
| -------- | ------------------------------------- | ------------------------------------------------------------ |
| TK       | Tenant Key                            | A unique key identifying the tenant.                         |
| TN       | Tenant Name                           | The name of the tenant.                                      |
| EK       | Environment Key                       | The unique key identifying the environment the user was accessing. |
| EN       | Environment Name                      | The name of the environment the user was accessing.          |
| FN       | Front-end Name                        | The name of the front-end server that handled the request.   |
| EPN      | EndPoint Name                         | The name of the web screen that was handling the request.    |
| EPK      | EndPoint Key                          | The key of the web screen that was handling the request.     |
| AN       | Action Name                           | The name of the action that was handling the request. Actions include the Preparation action and Screen Actions.<br/>Note: If the web screen doesn't have a Preparation action, or if a cached version was served, then the ActionName is "(PageRender)". |
| AK       | Action Key                            | The key of the action that was handling the request.         |
| D        | Duration                              | The total time, in milliseconds, the server spent serving the request.<br/>Note: If the application server (for example, IIS) queued the request due to server load, this metric doesn't include the time spent waiting in the queue. |
| TQT      | Total Query Time                      | The total time spent, in milliseconds, executing queries (Aggregates and Advanced Queries). |
| TQE      | Total Query Executions                | The total number of executed queries (Aggregates and Advanced Queries). |
| TET      | Total Extension Time                  | The total time spent, in milliseconds, calling actions provided by extensions. |
| TEE      | Total Extension Executions            | The total number of calls to actions provided by extensions. |
| TCIT     | Total Consumed Integration Time       | The total time spent, in milliseconds, calling actions provided by consumed integrations (SOAP, REST, SAP). |
| TCIE     | Total Consumed Integration Executions | The total number of calls to actions provided by consumed integrations (SOAP, REST, SAP). |
| TSAT     | Total Consumed Service Action Time    | The total time spent, in milliseconds, calling service actions. |
| TSAE     | Total Consumed Service Action Calls   | The total number of calls of service actions.                |
| IP       | Client IP                             | The client's public IP address, collected from the [X-FORWARDED-FOR header](http://tools.ietf.org/html/rfc7239#section-5.2), or if that doesn't exist, from the [REMOTE_ADDR header](https://www.ietf.org/rfc/rfc3875). For TimerExecuted, this reflects the IP address of the Scheduler Service that triggered the timer. |
| UID      | User Id                               | The unique identifier of the user that made the request. It corresponds to the user's identifier stored in the User system entity.<br/>If the request was made by an anonymous user, the User Id is not included in the event attributes. |
| EC       | Number of errors                      | The number of errors that occurred during the request.        |
