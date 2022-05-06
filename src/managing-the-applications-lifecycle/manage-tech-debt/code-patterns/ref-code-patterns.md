---
tags: article-page
summary: Up to date list of code patterns analyzed by the current version of Architecture Dashboard.
en_title: Code Patterns
locale: en-us
guid: a7187cf7-6f1d-4f7c-8141-03f856639f08
app_type: traditional web apps, mobile apps, reactive web apps
---


# Code Analysis Patterns

This topic includes the list of code patterns analyzed by the current version of Architecture Dashboard.
The patterns that only apply to a subset of the type of apps, include that information. 

## Architecture

### Lack of module classification

Module not placed in one of the Canvas layers in Discovery.

Impact
:   Since a Module isn't classified (undefined) in Discovery, it doesn't allow proper validation of the architecture and the detection of Canvas violation patterns.

How to fix
:   On the Discovery application, check the unclassified module. Classify its layer based on its nature and architecture best practices (Orchestration, End-user, Core, or Foundation). In case a module falls on more than one layer, classify it as the top one. For example, if a module has concepts of End-user layer (screens) and the Core layer (entities), it should be set as End-user.

### Orchestration module providing services

Orchestration module providing services.

Impact
:   An Orchestration module is not intended to provide services - usually, any reference to it reveals the existence of misplaced reusable code. And, being in the top layer, any reference to an Orchestration module will inherit the entire hierarchy of modules beneath it.

How to fix
:   Check Discovery for which elements are being consumed. Extract those elements and move them to Core/Foundation modules, according to the concepts. Check the Forge component Refactor for more support on this operation.

### End-User module providing services

End-User module providing services to non-Orchestration modules.

Impact
:   An End-user module is not intended to provide services - usually, any reference to it reveals the existence of misplaced reusable code. References to an End-user compromise life cycle independence between applications and typically pull a lot of indirect unwanted references.

How to fix
:   To get more details on each finding, select "Consumed elements". Move each consumed element to a Foundation module or to a Core module.

### Core module consumed by Foundation

Core module providing services to Foundation modules.
    
Impact
:   Foundation modules are not supposed to consume services from a core module. They need to be fully isolated with no business logic or reference to a business module, otherwise consuming a foundation might bring unexpected impacts.
    
How to fix
:   To get more details on each finding, select "Consumed elements". If a consumed element isn't business logic, move the element to a Foundation module. If a consumed element is business logic, reevaluate if you should move the logic in the Foundation module that is consuming the element to another module.

### Cyclic references between modules

Cyclic references between two Foundation or two Core modules.

Impact
:   Cycles between modules usually means an error in service abstraction and brings unwanted impacts in both development and runtime.

How to fix
:   To get more details on each finding, select "Consumed elements". Understand the conceptual relation between modules involved in a cycle, to decide which module isn't supposed to consume the other. Decide whether moving the consumed elements to the module that consumes them makes sense in terms of conceptual abstraction, or if you should move all the consumed elements to a new module.

### Orchestration application providing services

Orchestration application providing services.

Impact
:   An Orchestration application must be fully isolated, not providing services - any reference to it usually reveals the existence of misplaced reusable code. Furthermore, being in the top layer, any reference to an Orchestration application may inherit the entire hierarchy of modules beneath it.

How to fix
:   Check Discovery for which modules are being consumed and move them to Core/Foundation applications, according to the concepts.

### End-User application providing services

End-User application providing services to non-Orchestration applications.

Impact
:   An End-user application is not supposed to provide reusable modules for other applications. References to an End-user compromise life cycle independence between applications and typically pull a lot of unwanted indirect references.

How to fix
:   To get more details on each finding, select "Consumed modules". If a consumed module is a Foundation module, move the module to a Foundation app. If a consumed module is a Core module, move the module to a Core app.

### Core application consumed by Foundations

Core application with modules consumed by Foundation applications.

Impact
:   Foundation applications are not expected to consume modules from a Core application, since they should not rely on business related services.

How to fix
:   To get more details on each finding, select "Consumed modules". If a consumed module is a Foundation module, move the module to a Foundation app. If a consumed module is a Core module, reevaluate if you should move the logic in the Foundation module that is consuming those modules to another app.

### Cyclic references between applications

Cyclic references between two Foundation or two Core applications.

Impact
:   Cycles between Core or Foundation applications usually mean a wrong isolation of reusable modules that leads to consumers being unnecessarily impacted when requiring only one of the applications.

How to fix
:   To get more details on each finding, select "Consumed modules". Understand the conceptual relation between apps involved in a cycle, to decide which app isn't supposed to consume the other. Decide whether moving the consumed modules to the app that is consuming them makes sense in terms of conceptual abstraction.

### Client and server side Entities and logic aren't isolated

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Both client and server side Entities and logic are implemented in the same module.

Impact
:   Supplying client-side logic and entities together with reusable server-side definitions does not optimize mobile functionality. While server-side logic can be extended to support several applications, generalizing client-side logic for the same purpose tends to generate redundant information and useless sync logic for each specific mobile app.

How to fix
:   Client-side logic should be catered to the use cases of each mobile application. The typical pattern is to have a generic server-side module around a concept, e.g., Accounts, and specialization for each mobile app that handles Accounts. For instance, if you have a Mobile Banking (MB) application for end-users and a Mobile Agent (MA) application for agents, on top of the server-side core service Account\_CS module, you should create the MB\_Account\_CS and the MA\_Account\_CS modules each with specialized client-side databases and logic.

### Monolithic mobile UI module

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

All mobile UI content is being kept in the same module.

Impact
:   Due to technical requirements for Native Build generation, all screens of a mobile application, including the exception flow and the menu, must be placed in the same Module. This means the UI screens module can become a monolithic Module that keeps growing, making different life cycles for different processes hard to maintain.

How to fix
:   Keep all the Screen Flows in a single Module but keep Screens only as layout containers. Supply UI content in blocks from different Core widgets modules, organized per functional area to allow different life cycles per such functional area.

### Public Entities aren't read-only

Public Entities should be exposed as read-only.

Impact
:   When public Entities are not exposed as read-only, their entity actions for creating, updating and deleting records are available to be referenced by any consumer. These entity actions directly affect records in the entity, allowing any consumer to perform inconsistent and potentially destructive changes without considering the complete semantic and validation of the operation.

How to fix
:   Enable Expose Read-Only in public Entities and create your own public actions for creating, updating and deleting records of those entities, abstracting all validations, business rules or other side-effects such as audit trailing or notifying changes to another system.

### Foundation or Core module with screens

Misplaced End-user screens.

Impact
:   End-user screens that support business processes should only be provided at Orchestration or End-user modules. The only exceptions are exception handling screens or reusable pop-up screens.

How to fix
:   Move end-user screens supporting business processes to end-user modules. If you are building test screens to validate your logic, remember to delete them when obsolete. If you want to keep the test for future reference, then move the screen to a test end-user module. This way, you can temporarily perform quick tests directly on the Module that you are developing. If you are building reusable popup screens, suffix them with 'popup' and they will be ignored.

### Monolithic Service Module

Module providing services with too many public elements.

Impact
:   A monolithic module with too many public elements probably contains too many concepts inside. The module becomes very heavy and hard to maintain, and the lack of granularity causes unwanted impacts for consumers that only require a subset of services.

How to fix
:   Identify the granular concepts inside the monolithic module and design a conceptual relation among those concepts, making sure that you get a graph with no cycles. Then refactor your monolithic module to split it into the identified concepts, respecting their conceptual relation.

### Monolithic web UI module

<div class="info" markdown="1">

Applies to **Traditional Web** apps only.

</div>

Module has too many end user interfaces.

Impact
:   A monolithic End-user or Orchestration module with too many Screens probably contains too many business processes inside with independent lifecycles. The module becomes very large and causes unwanted impacts on maintainability and release management.

How to fix
:   Identify the independent UI flows, with no destinations among themselves, and separate them in multiple Modules.

### Core module providing services to sublayers

Core module in a higher sublayer is providing services to core modules in lower sublayers.

Impact
:   Within the core sublayer of modules there are upper layer modules (like BL, API, or Sync modules) that are consumed by lower layered ones (like CS). This can indicate a wrong abstraction of concepts, where some core concept is becoming dependent on a particular business concept composition. These types of dependencies inside core modules should usually be done from top to bottom also.

How to fix
:   Check Discovery. Move the upper core module to a lower sublayer (because it is supposed to provide services to other consumers below) alternatively, check if any of the consumed object/logic from the upper module is misplaced, requiring it to be refactored to the lower sublayer module.

### Foundation module providing services to sublayers

Foundation module in a higher sublayer is providing services to Foundation modules in lower sublayers.

Impact
:   An incorrect abstraction of concepts may lead to unmanageable dependencies. The module in the higher layer should be a composition of lower modules and not the other way around.

How to fix
:   Check Discovery for the producer module. If the producer is supposed to provide services to its current consumers move it to a lower sublayer. If not, reevaluate the inclusion of the consumed elements in the producer module, and move the consumed elements to a lower sublayer module.

## Performance

### Unlimited records in Aggregate

Number of records fetched from database is not set in Aggregate.

Impact
:   More records are fetched from the database than are used by the application, resulting in useless I/O and memory consumption.

How to fix
:   Set the Max. Records parameter of the Aggregate to the required amount of records.

### Unlimited records in SQL query

Number of records fetched from database is not set in SQL query.

Impact
:   More records are fetched from the database than are used by the application, resulting in useless I/O and memory consumption.

How to fix
:   Use `ROWNUM` (for Oracle) or `TOP` (for MS SQL Server) in the SQL query to limit the number of records to the required amount. Note that in SQL queries the Max. Records parameter only limits the number of records displayed, and not the number of records fetched.

### Aggregate or SQL query inside a cycle

<div class="info" markdown="1">

Available with **Architecture Dashboard probes 4.0 onwards**.

</div>

An Aggregate or SQL query is being executed inside a For Each cycle.

Impact
:   Executing Aggregates and SQL queries inside a cycle can have severe performance impact due to database communication overhead repeated at each iteration. The impact can be greatly worsened when iterating through a list with a high number of elements or when having nested cycles.

How to fix
:   Avoid executing Aggregates or SQL queries inside a For Each cycle. Instead, replace that Aggregate or SQL query by a more complex one that gets all the related information and execute it before the cycle.

    In case you have an Aggregate to fetch the master entity before the cycle followed by another Aggregate inside the cycle to fetch the details, consider eliminating the inner Aggregate by [adding a join](../../../ref/data/handling-data/queries/supported-join-types.md) to the outer Aggregate.

### Sequence of connected Aggregates

<div class="info" markdown="1">

Available with **Architecture Dashboard probes 4.0 onwards**.

</div>

Sequence of Aggregates that reference one another.

Impact
:   A sequence of Aggregates that reference one another usually leads to unnecessary data fetching. Considering that each Aggregate executes a request to the database, this results in unnecessary database communication overhead.

How to fix
:   Merge the sequence of Aggregates into a single Aggregate [using a join](../../../ref/data/handling-data/queries/supported-join-types.md) to retrieve all the needed data.

### Query data in ViewState

<div class="info" markdown="1">

Applies to **Traditional Web** apps only.

</div>

Screen Actions are using query data obtained in Preparation.

Impact
:   If you use Preparation data on a Screen Action, that data will be saved in the screen's ViewState. Adding more data to the ViewState increases response size and loading time in the browser since it's sent to the user at every page request, and is also sent back to the server on every POST, postback, or AJAX request.

How to fix
:   Avoid using data from Preparation in Screen Actions. For example, instead of using the TableRecords record data in a Screen Action, send the Record's identifier as an Input Parameter of the Screen Action, only fetching the data from the database when needed. If you need the full list of records, refresh the query. It is better to rerun the query server-side than to send the data back and forth through the ViewState.

### Large Input Parameter or Local Variable in ViewState

<div class="info" markdown="1">

Applies to **Traditional Web** apps only.

</div>

A large screen or block Input Parameter or Local Variable is being used in a Screen Action.

Impact
:   When a screen's or block's Input Parameter or Local Variable is used in a Screen Action, the corresponding data is saved in the ViewState of that Screen. To be considered large, the Input Parameters or Local Variables must have data types of type Compound or Collection. Additional data to the ViewState increases response size and loading time in the browser since it's sent to the user at every page request and is also sent back at every POST, postback, or AJAX request.

How to fix
:   Avoid using screen or web block input parameters or local variables with large data in screen actions.

### Long Server Requests Timeout

<div class="info" markdown="1">

Applies to **Reactive Web** and **Mobile** apps only.

</div>

Long Server Request timeout.

Impact
:   The default timeout for server action requests is too long or an explicit timeout in a server call is too long (more than 10 seconds). In a mobile application, a server request should be efficient. 10 seconds is all it takes for a device to go to sleep mode or lose network connectivity.

How to fix
:   Prepare and cache data in advance on the server-side to be promptly available when required. The Server Request timeout should also be reduced to fail quickly (with a "retry later" message), except on explicit operations, because it's acceptable for those to take a little bit longer.

### Inline JavaScript

Inline JavaScript defined in an unescaped Expression.

Impact
:   JavaScript defined at the screen/web block level is optimized by OutSystems. For example, if you have the same web block twice on your screen, it's only included once. It also improves maintenance.

How to fix
:   Define JavaScript at the screen/web block level instead of in inline expressions.

### Inline CSS style

CSS style being defined as an extended property of a screen element.

Impact
:   CSS and HTML should be kept separate. Inline styles are inefficient, harder to maintain, and make your HTML larger.

How to fix
:   CSS should be centrally managed in the application style guide to avoid loading a large number of CSS files. If the CSS is specific to one screen or web block, define your CSS at the screen/web block level instead of in extended properties.

### Dynamic inline parameter

Dynamic expression used in an inline expanded Query Parameter of a SQL Query.

Impact
:   Query Parameters that are expanded inline and change too often don't allow the database to optimize execution plans since it keeps generating new queries

How to fix
:   Change query to remove the frequently changing inline parameters. Consider selecting specialized queries depending on the parameter or using sub-queries or temporary tables.

### Site Property update

Site Property is being updated using Application logic.

Impact
:   When a Site Property is updated it invalidates the Module's cache. Therefore subsequent accesses to cached data have to be fetched from database or recalculated in the application logic, which may result in a performance hit.

How to fix
:   Avoid changing Site Property values programmatically. Use alternatives such as storing the value in the database, accessing it when needed.

### Inefficient empty list test

Using the Count property of an Aggregate or SQL query to check if results were returned.

Impact
:   For performance, OutSystems query optimizer makes sure the output of Aggregates and advanced queries only the essential data to feed a screen. This means, the Count property needs to execute an additional query to get the total number of registries.

How to fix
:   Use **List.Empty** property to test for lack of results instead of **List.Count**

### Inefficient query count

Counting query results using an inefficient query.

Impact
:   SQL queries are usually designed for retrieving data and may perform joins and fetch extra data, needed for processing but that are not required to count the query results. When using the Count property of a query, the same query is executed to count the results, which is inefficient since it will use the same query definition.

How to fix
:   Use a simplified SQL query to efficiently count the results, removing unneeded extra data and joins.

### Inadequate data preparation

Query is being executed inside a loop.

Impact
:   Each run of the query may be fast enough, but when inside a loop, the total amount of database effort may be considerable.

How to fix
:   Often, executing only one complex SQL query to obtain the required information is better than executing a simple Aggregate in a For Each loop. Also, check if the Entity model copes with your needs - when the database model is inadequate, getting the required information proves overly complex to be fetched by a single query.

### Large Session Variable

Large Session Variable is being used.

Impact
:   On all Screen requests, the current session's data is loaded from the database. This data is binary and includes all Session Variables. Session Variables with data type Compound or Collection are considered large. If large Session Variables are used, each request will take longer to process the session data (include serializing and deserializing it), increasing response times and causing contention in all concurrent requests.

How to fix
:   Store this data in your a Entity using the session identifier as primary key and fetch it only when needed. Keep the session limited to context information that is useful in every request.

### Large image

Large images included in the Module.

Impact
:   Large images have different kinds of impact on an application. When large images are being used in a screen to be displayed, they will need to be fetched from the server, increasing bandwidth usage and request processing time in the browser. Even setting their width/height to lower values, will not reduce the bandwidth fetch of the image from the server. On the development side, a Module with large images takes longer to be saved and published, consuming additional bandwidth when uploaded or downloaded from the server.

How to fix
:   Reduce the size of images to the minimum needed to be correctly displayed to the user (below 150KB/500KB for Mobile/Web Applications). Reduce the image's resolution to a maximum of 1024px. Consider the possibility of having big images as external resources not contained inside the module itself.

### Large resource

Large resources included in module.

Impact
:   When publishing to the environment, large resources in the module can slow down publishing and downloading, impacting the development team.

How to fix
:   Reduce the size of the resources to the minimum needed for its usage (below 150KB/500KB for Mobile/Web Applications). Consider the possibility of having the resources served externally to the application, and for example, having a screen to upload the resource, then having it stored in the file system or a Binary database table.

### Server requests in client events

<div class="info" markdown="1">

Applies to **Reactive Web** and **Mobile** apps only.

</div>

Server actions being called in client events.

Impact
:   Server calls should be avoided on client events (On Initialize, On Ready, On Render, On After Fetch). These events are serialized in the request and server calls may tremendously impact the wait time to render the screen.

How to fix
:   A mobile app should rely on local storage for performance and offline. Server-side requests should be limited to synchronization requests (typically performed on business events fired in screen actions, session start or online events) and online transactions (typically performed in screen actions).

### Non-optimized local data fetch 

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Local data fetch performed in client events.

Impact
:   Local data fetch should be avoided on client events (On Initialize, On Ready, On Render). These events are fully serialized, not taking advantage of the parallel fetch of data while the screen is being already rendered.

How to fix
:   Retrieving data should occur inside data fetch calls to enable the parallelization of several data fetches and the screen render. If a data fetch depends on a previous fetch, use the On After Fetch event.

### Non-optimized Local Storage

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Local Storage model is not optimized.

Impact
:   Local Storage is being either copied exactly from server Entities or is using a complex model (including too many fields, Foreign Keys, or Complex data types). This forces the use of multiples joins in Client Aggregates, hindering the performance of the application on mobile devices.

How to fix
:   Simplify local entities to the minimum number of attributes and de-normalize them as much as possible, still keeping them simple; review client Aggregates for unnecessary joins.

### Not taking advantage of Local Storage

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Using too many server requests (screen data action) instead of using Local Storage.

Impact
:   Using too many screen data actions which gather data from server is an indication that local storage is not properly defined or being used, as all data is being retrieved from the server. This hinders performance and offline requirements in mobile applications.

How to fix
:   Implement proper synchronization mechanisms and Local Storage to make sure that most data is available in the local storage, also facilitating offline scenarios.

### Multiple server requests (Aggregates or actions) inside Client Actions

<div class="info" markdown="1">

Applies to **Reactive Web** and **Mobile** apps only.

</div>

Multiple server Aggregates or multiple Server Action requests inside Client Actions.

Impact
:   Each server request or server Aggregate is a different request, generating its overhead on establishing the connection and launching a server-side process. Multiple processes also generate different database transactions.

How to fix
:   Instead of sequencing a set of server requests or server Aggregates on your client-side code, compose all required server logic in a single Server Action to reduce the number of server requests.

### Incorrect offline sync method

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Offline sync patterns are not implemented correctly.

Impact
:   No offline synchronization is being made or is being executed with poor performance

How to fix
:   Place the local entity synchronization actions inside the OfflineDataSync action, configure the manual and automatic start of sync and use TrigerOfflineDataSync for background synchronizations. SyncUnit parameter should be used to prevent updating unnecessary entities.

### No asynchronous Offline sync

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Server data is not being stored in the local database asynchronously.

Impact
:   Synchronously storing server data will result in blocking screens and, or actions that may impact the overall user experience.

How to fix
:   Use TriggerOfflineDataSync to execute OfflineDataSync asynchronously and react to the OnSyncComplete event to update UI modules.

### Not addressing bad network and server connection

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Not addressing a bad network and server connection.

Impact
:   The logic must be designed to deal with different network conditions, not just setting as ON and OFF.

How to fix
:   Use GetNetworkStatus to detect the network conditions and ensure that the logic and UI take the conditions into consideration and reacts appropriately.

### CSS in the screen's style sheet

<div class="info" markdown="1">

Applies to **Reactive Web** and **Mobile** apps only.

</div>

CSS in the screen's style sheet.

Impact
:   Having CSS spread through different screens may create maintenance issues. Centralizing CSS in the app's Theme helps to reduce the maintenance cost. Also, defining CSS in mobile Screens will create flicker when navigating through different pages.

How to fix
:   Define the class inside the theme of the application. Even if it's only a small change it is better to define a specific class (that can then be reused) for it than add to a specific page and then copy the same class over and over.

### Complex splash screen

<div class="info" markdown="1">

Applies to **Mobile** apps only.

</div>

Keep the splash screen simple and fast.

Impact
:   Adding heavy or lengthy operations to the splash screen will increase the time until the app can be used. Additionally, if the splash screen has a complex UI, the users may see a blank screen before the splash screen renders.

How to fix
:   To keep the splash screen simple and fast to load, you should avoid: - Requests to the server. - Heavy logic. - Complex UI, namely too many Blocks.

### Avoid long-running Timers

Avoid running Timers for longer than 30 minutes.

Impact
:   A timer that exceeds its Timeout in the Minutes property may result in the code and data being reprocessed reprocessing because the automatic retry mechanism for timers reruns the code when errors occur. Following the wake timer pattern will decrease the probability of the timer being interrupted by the Scheduler process due to reaching the Timeout in Minutes threshold. Using the wake timer pattern can: - Reduce the probability of a timer being interrupted. - Avoid cases of data inconsistency. - Avoid endless reprocessing of the same data.

How to fix
:   Long execution Timers should follow the wake timer pattern to reschedule themselves to restart and continue the current task at hand. To implement the wake timer pattern start by adding an explicit logical timeout inside the Timer logic that when reached takes the necessary actions to properly terminate the current execution, store the current progress of the process in such a way that when its execution restarts it can easily pick up the execution from this stored last point. This pattern ends with a wake timer action for itself at the end of the timer flow. Another good practice for long Timers is to define them with checkpoints so that the Timer can be killed and restarted with no impact on the data. At these checkpoints, consider executing partial commits to ensure that if some error occurs the processed data is only rolled back until the last commit (and avoid processing the same data all over again on next execution).

## Security

### Automatically generated publicly exposed REST endpoint

<div class="info" markdown="1">

Applies to **Reactive Web** and **Mobile** apps only.

</div>

An automatically generated REST endpoint for a Server Action is being exposed in a screen using the Anonymous Role.

Impact
:   In Reactive Web apps and Mobile apps, Server Actions used in the logic of a screen are automatically exposed as REST endpoints to enable client side consumption.

    If the screen that calls a server action allows anonymous access, the REST endpoint for that server action also allows anonymous access. This means that the REST endpoint can be used without authentication.

    A malicious actor might modify client-side logic (JavaScript), check the server requests, and manipulate input parameters to try to access your data or perform unauthorized actions.


How to fix
:   If you don't need the screen to be publicly accessible, disable the Anonymous Role for that screen.<br/>
Otherwise, ensure that all data sent from the app to the server is re-validated in the server action in a way that prevents unauthorized access to read or edit data.


### SQL injection

Avoid enabling the Expand Inline property of a SQL Query Parameter since it could make your application vulnerable to SQL injection.

Impact
:   OutSystems uses prepared statements by default to execute the SQL queries that you define in SQL elements. These prepared statements contain SQL parameters or placeholders, for which you define values before executing the SQL statement. These parameters can only store a value of a given type and not arbitrary SQL fragments.

    If you enable the Expand Inline property for a Query Parameter, its value will no longer be handled as a SQL parameter value. Instead, the Query Parameter value will be included in the SQL statement without first being evaluated and turned into a literal by the SQL engine. This means that you can use the Query Parameter to insert SQL fragments in the full SQL statement dynamically, but it also means that your end-users may be able to exploit this fact if you do not take the necessary precautions.

    OutSystems will use an SQL parameter for every Query Parameter that has the Expand Inline property disabled. This property is disabled by default, providing you default protection against SQL injection attacks.

    It's difficult to use properly expanded parameters inline since you need to make sure that any user input is properly escaped before using it in an SQL statement. If you can, avoid enabling this property altogether.

How to fix
:   OutSystems provides ways of implementing common use cases without enabling the Expand Inline property and provides recommendations when using the Expand Inline. For more information, see [SQL Injection Warning ](../../../ref/errors-and-warnings/warnings/sql-injection-warning.md).

    If you must enable Expand Inline, take the following recommendations into account:

    * Do not perform manual string encoding using the **Replace** function.String literals should only be encoded using the **EncodeSql** function. Doing it manually using the **Replace** function is prone to errors and can introduce bugs into your application that can later be exploited by end-users.

    * Use **EncodeSql()** to encode string literals. The **EncodeSql** function encodes string literals to be used in SQL statements when the **Expand Inline** property is enabled. Make sure you avoid the following bad practices when using **EncodeSql()**:

        * Do not use **EncodeSql()** to encode the full contents of an SQL parameter. For example:
        ``myparameter = EncodeSql(""WHERE surname = "" + @myVariable1 + "" OR name = "" + @myVariable2).``      
        This pattern is wrong on most occasions, so you will get a warning if you use it.
        
        * Use **EncodeSql** only to encode string literals, not complete fragments of an SQL statement.

    * Do not build ``""WHERE column IN (@values)""`` clauses by wrapping all the values in a EncodeSql call:
    ``values = EncodeSql(name1 + "","" + name2 + "","" + name).``
    
        This approach will not protect you from SQL injection. Instead, use the ``BuildSafe_InClauseIntegerList() and BuildSafe_InClauseTextList()`` functions to build ``""WHERE column IN (@values)""`` clauses.

### Visible disabled Button

Disabled button that is still visible.

Impact
:   A button that is disabled doesn't prevent an experienced person from re-enabling the button at runtime by using, for example, the development tools on a browser. This will lead to the ability to enable the functionality and allow the user to press the button even if the user didn't have permission or was originally unable to press it.

How to fix
:   In the button, instead of having the Enable property set to false, set the Visible property as false instead (or in conjunction with the other one). This will prevent the rendering of the button completely on the client browser and will prevent the possibility of an experienced user to hack the button and enable the functionality.

### Avoid Anonymous and/or Registered access Screens

Screens should have custom Roles set instead of using System Roles (Anonymous and Registered).

Impact
:   OutSystems provides you with a default set of System Roles (Anonymous and Registered) but you should define your own custom Roles that are specific to your app. Giving access to the Registered role, a Screen can be accessed by any end-user with a valid OutSystems session, namely any user that has logged into an app running in the same Platform Server. Giving access to the Anonymous role, a Screen can be accessed by any end-user, including users that are not logged in.

How to fix
:   Disable the Registered Role access on all Screens (that don't have the Anonymous Role) and explicitly grant access for custom Roles that are specific to your app. Disable the Anonymous Role access unless you want to make a Screen public and accessible by everyone that can reach your app.

### Exposed REST services are not secured

Exposed REST services should enforce SSL/TLS, and authentication.

Impact
:   Unsecured connections may be read by unauthorized third-party and be target of man-in-the-middle attacks.

How to fix
:   Secure application end-points by configuring SSL/TLS, which ensures the data sent to the exposed service can't be eavesdropped or tampered with. OutSystems provides controls to exposed REST APIs with login/password protection, except when its configured for internal access only.

### JavaScript or HTML injection

<div class="info" markdown="1">

Applies to **Traditional Web** apps only.

</div>

Unescaped/unencoded user inputs or screen variables.

Impact
:   Screen user inputs and variables may be used for HTML or JavaScript injection. This vulnerability may also be exploited in Cross-Site Scripting (XSS) attacks.

How to fix
:   Do one of the following:

    * Enable the Escape Content property of the expression.
    * Use the EncodeHtml() built-in function to replace all HTML reserved characters by their escaped counterpart.
    * Use the EncodeJavascript() built-in function to replace all JavaScript reserved characters by their escaped counterpart so they can be included in a JavaScript string.
    * Use the SanitizeHtml() function from the Sanitization extension module to ensure that the value entered by the end-user does not contain any malicious content.
    * Use the EncodeUrl() built-in function to replace all URL invalid characters by their percent-encoded counterpart."

### Insecure usage of GetUserId function on client context

<div class="info" markdown="1">

Applies to **Reactive Web** and **Mobile** apps only.

Available with **Architecture Dashboard probes 4.0 onwards**.

</div>

Avoid passing identity information from the client side to the server side as an action parameter.

Impact
:   Passing identity information as a server action parameter is extremely insecure. Identity is obtained in the client context and passed to server functions (exposed as REST APIs) as a parameter. Since execution of GetUserId on reactive client components depends on client cookies, parameters can be easily changed by any user, either by manipulating server calls or changing client session ID identifiers. Malicious users can exploit the ability to change identity-related parameters and impersonate other users, access sensitive data, and even bypass role checks which, though done on the server, become vulnerable due to insecure parameters received from the client.

How to fix
:   Identity information should be obtained on server calls, using functions like GetUserId, executed on the server, and never sent as a regular action parameter. GetUserId executed on the server ensures proper identity flow, is secure and cannot be manipulated. 

    Remove any usages of GetUserId on the client side, and replace them with the same function on the server side. In this way, you’ll avoid passing identity information from the client side to the server side as an action parameter.

For more information refer to [Reactive web security best practices: Securing server calls](https://success.outsystems.com/Documentation/Best_Practices/Security/Reactive_web_security_best_practices#Securing_server_calls). 

## Maintainability

### Duplicated Code

The same logic is duplicated in different action flows.

Impact
:   Repeating the same logic in different action flows makes it more difficult to maintain your code. This means that to change the duplicated logic, you'll need to find that logic and then change it in all the different action flows.

How to fix
:   For each pattern found, select the magnifying glass to get more details.

    In the details' dialog, check the list of actions that include duplicated logic on the left side, and check the representation of the duplicated logic on the right side. The duplicated logic is highlighted and shown in the context of each action flow.
    
    If possible, refactor the actions where the duplicated logic exists by extracting the duplicated logic into a single action that can be reused.

### Missing description on public element

Required description on public elements.

Impact
:   Meaningful descriptions in modules, public elements, entities, and input/output parameters clarify their purpose and expected behavior. It's crucial when consuming closed modules, because the implemented logic isn't visible.

How to fix
:   Add a description to the module that explains the purpose and identifies the concepts it contains. Add meaningful descriptions to all module's public elements, and their related parameters. The only exceptions are Entities and Structures attributes which descriptions are optional. A parameter name that already follows well-established naming conventions doesn't require a description (e.g. Id, Name, Label, Description, CreatedBy, UpdatedBy, CreatedOn, UpdatedOn).

### Unidentified public action managing transaction

Description of a public action doesn't mention that it manages a database transaction.

Impact
:   Explicit CommitTransaction or AbortTransaction operations may commit/rollback data in unexpected places, affecting your app. Since the content of public reusable actions may not be accessible, it is extremely important to explicitly describe when the transaction is being handled inside it, to avoid unwanted runtime behaviors.

How to fix
:   Clearly identify in the description of the public action that the transaction is being managed and in which cases is being committed or aborted by adding, for example, "\[commit transaction\]" or "\[abort transaction\]" at the end of the description.

### Long undocumented flow

Action with a long and undocumented flow.

Impact
:   A Preparation or screen action with more than 20 nodes or an action with more than 40 nodes is hard to maintain, especially if it has no comments to explain the logic.

How to fix
:   Break flow logic into smaller and potentially reusable actions and/or place comments to explain portions of your flow. Note: explore the 'Extract to Action' feature, available in the right-click menu when you select a portion of a flow.

### Too much disabled code

Module containing too much disabled code.

Impact
:   Keeping a large amount of disabled code leaves clutter and makes it difficult to read. It increases maintenance costs and wastes time, as people tend to interpret disabled code to understand its relevance better.

How to fix
:   Remove the code if it has been disabled for a while or the app is in production, and behaving correctly.

