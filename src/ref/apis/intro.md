---
summary: APIs provided by OutSystems that you can use to extend the capabilities of your applications.
tags: support-application_development; support-Integrations_Extensions
---

# OutSystems APIs

OutSystems provides APIs that allow you to extend the capabilities of your applications. With these APIs you can integrate your applications with external systems, and programmatically access OutSystems features.

Check here the available APIs:

## Business Processes

API Name | Available As | Description
---|---|---
[BPT API](auto/bpt-api.final.md) | Referenced extension | Provides functionality to manage processes and activities.
[Processes API](processes-api.md) | Referenced system module | Allows you to get information from the OutSystems data model to customize and extend the design of your processes.
[EPA TaskBox API](auto/epa-taskbox-api.final.md) | Referenced module | Provides access to the BPT taskbox, allowing you to extend its functionality according to your specifications.

## Charts

API Name | Available As | Description
---|---|---
[Charts API](auto/charts-api.final.md) | Referenced module | Allows you to plot charts for the web and mobile devices.

## Client-side Behavior

API Name | Available As | Description
---|---|---
[outsystems.api.preloader API](outsystems-api-preloader-api.md) | Referenced extension and JavaScript file | A JavaScript API that allows you to prefetch static resources (css, js, png, gif. jpg, jpeg, woff) for a list of modules.
[outsystems.api.requestInfo API](outsystems-api-requestinfo-api.md) | Predefined JavaScript object | A JavaScript API that provides methods to get information about the current request and session.

## Database

API Name | Available As | Description
---|---|---
[DbCleaner API](auto/dbcleaner-api.final.md) | Referenced module | Provides you the actions to drop tables and columns in the database related with entities, attributes, or module versions.
[PlatformRuntime API](auto/platformruntime-api.final.md) | Referenced extension | Allows your applications to switch the database connection in runtime.
[RuntimePublic.Db API](runtimepublic-db/intro.md) | .NET classes | Allows your extensions modules to call the databases configured in the environment console.

## Emails

API Name | Available As | Description
---|---|---
[Emails API](emails-api.md) | Referenced system module | Allows you to access data about your Emails.

## End User Management

API Name | Available As | Description
---|---|---
[Users API](auto/users-api.final.md) | Referenced module | Allows you to programmatically manage OutSystems Users and Roles.

## Infrastructure and IT Users management

API Name | Available As | Description
---|---|---
[LifeTime API](auto/lifetime-deployment-api-v2.final.md) | REST API | Allows you to manage applications, modules, environments and deployments of your OutSystems infrastructure.  
[LifeTime Services API](auto/lifetime-services-api.final.md) | SOAP web services | Provides you functionality to manage the infrastructure made available by OutSystems.
[LifeTime SDK](auto/lifetime-sdk.final.md) | Referenced module | API for extending the LifeTime functionality including developing your own plug-ins.

## Integration

API Name | Available As | Description
---|---|---
[BinaryData API](auto/binarydata-api.final.md) | Referenced extension | API to manipulate binary content such as conversions from and to Text or Base64 Text, encoding conversion, binary content length, and binary data comparison.
[EnhancedWebReferences API](auto/enhancedwebreferences-api.final.md) | Referenced extension | API to dynamically change Web Service and Web Reference URLs, SOAP headers, credentials, and proxies.<br/>Applicable to exposed SOAP Web Services and consumed SOAP Web Services that were upgraded to OutSystems 11.
[HTTPRequestHandler API](auto/httprequesthandler-api.final.md) | Referenced extension | API with functionality to allow you to manipulate HTTP Requests and Responses.
[REST Extensibility API](rest-extensibility-api.md) | .NET classes | API that enables you to access the content of requests and responses used by methods consumed from other REST APIs.
[SAP Extensibility API](sap-extensibility-api.md) | .NET libraries | API that enables you to customize your connection and calls to SAP remote functions through an extension.
[SOAP Extensibility API](soap-extensibility-api.md) | .NET classes | API that enables you to modify the SOAP connection, request and/or response message using .NET code.<br/>Applicable to consumed SOAP Web Services created in OutSystems 11.

## Monitoring and Traceability

API Name | Available As | Description
---|---|---
[Asynchronous Logging API](auto/asynchronous-logging-api.final.md) | Referenced extension | Provides a highly scalable mechanism to perform logging.
[PerformanceMonitoring API](performancemonitoring-api.md) | REST API | Provides you REST API methods to retrieve or register request events of your applications. Request events contain metrics about the user experience of your applications.

## Scripting

API Name | Available As | Description
---|---|---
[IncludeJavaScript API](auto/includejavascript-api.final.md) | Referenced extension | Allows you to programmatically include JavaScript snippets in all Web Screens.
[JavaScript API](javascript/README.md) | Predefined JavaScript objects | Allows you to call OutSystems specific actions and act upon mobile app events in your JavaScript code, to tweak and customize the mobile app experience of the final user.

## System Actions

API Name | Available As | Description
---|---|---
[System Actions](auto/system-actions.final.md) | Referenced system module | Contains client and server actions that allow you to operate on system elements like lists and activities.

## Security and Cryptography

API Name | Available As | Description
---|---|---
[PlatformPasswordUtils API](auto/platformpasswordutils-api.final.md) | Referenced extension | Provides you actions for validating and securely storing passwords in the database, compliant with established cryptographic practices.
[Sanitization API](auto/sanitization-api.final.md) | Referenced extension | Provides methods to avoid code injection in HTML, JavaScript and SQL snippets that need to include untrusted content, i.e., content gathered from end users.

## Text

API Name | Available As | Description
---|---|---
[Text API](auto/text-api.final.md) | Referenced extension | Provides functionality to manipulate texts as, for example: search and replace using a regular expression, split, join, or format DateTimes.
