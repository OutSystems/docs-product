---
locale: en-us
guid: c62b20a1-5cec-4050-9139-e46b4c55395f
app_type: traditional web apps, mobile apps, reactive web apps
---

# Query log data

This document shows examples on how you can query views associated with the log records. Keep in mind that querying views of a live system negatively affects the runtime performance of the environment, because the logging mechanism is optimized for writing. We recommend that you implement your own mechanism for creating copies of the log data, in models designed for the types of searches you need.

<div class="info" markdown="1">

Also available: [Query log data in OutSystems 10](https://success.outsystems.com/Documentation/10/Managing_the_Applications_Lifecycle/Monitor_and_Troubleshoot/Logging_database_and_architecture/Query_log_data).

</div>

# Examples of queries

These examples are written for the databases running the Oracle SQL database management system.

## Mobile app calls server-side logic to invoke an external integration (REST/SOAP)

This SQL query enables you to list all integrations (SOAP, REST, SAP) called for a specific mobile request (in the example, the request_key is `9c35b89a-2ec3-4716-bb96-4e3ea41b664c`).

```sql
select request_key, 'MOBILE REQUEST' log_type, instant,  
'eSpace ID: '||espace_id||'; Screen: '|| screen || '; Endpoint: '||endpoint||'; User ID: '||user_id information, duration  
from oslog_mobile_request  
where request_key = '9c35b89a-2ec3-4716-bb96-4e3ea41b664c'  
union all  
select request_key, 'INTEGRATION', instant,  
'Type: '||type||'; Endpoint: '||endpoint||'; Action: '||action information, duration  
from oslog_integration  
where request_key = '9c35b89a-2ec3-4716-bb96-4e3ea41b664c';
```

### Sample result

Here is a sample result set of the query.

|REQUEST_KEY|LOG_TYPE|INSTANT|INFORMATION|DURATION|
|--- |--- |--- |--- |--- |
|9c35b89a-2ec3-4716-bb96-4e3ea41b664c|MOBILE REQUEST|01-AUG-18 01.22.01.378236000 PM|eSpace ID: 1234; Screen: Synchronize; Endpoint: LoginData_Sync; User ID: 123456|3015|
|9c35b89a-2ec3-4716-bb96-4e3ea41b664c|INTEGRATION|01-AUG-18 01.22.00.253199000 PM|Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/userData/Get; Action: UserData.GetDate|328|
|9c35b89a-2ec3-4716-bb96-4e3ea41b664c|INTEGRATION|01-AUG-18 01.22.00.628220000 PM|Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/UserDetails/Get; Action: UserData.GetDetails|375|
|9c35b89a-2ec3-4716-bb96-4e3ea41b664c|INTEGRATION|01-AUG-18 01.22.00.940738000 PM|Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/SaveChanges; Action: UserData.SaveUserProfile|296|
|9c35b89a-2ec3-4716-bb96-4e3ea41b664c|INTEGRATION|01-AUG-18 01.22.01.331361000 PM|Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/Refresh; Action: UserData.RefreshInRepository|390|

## Mobile app calls server-side logic to invoke custom code (Extensions)

This SQL query enables you to list all extensions (created with Integration Studio) called for a specific mobile request.

```sql
select request_key, 'MOBILE REQUEST' log_type, instant,  
'eSpace ID: '||espace_id||'; Screen: '|| screen || '; Endpoint: '||endpoint||'; User ID: '||user_id information, duration  
from oslog_mobile_request  
where request_key = 'd6aaad9c-1786-4f65-a5c9-b89b84397fd8'  
union all  
select request_key, 'EXTENSION', instant,  
'Extension ID: '||extension_id||'; eSpace ID: '||espace_id||'; Action: '||action_name information, duration  
from oslog_extension  
where request_key = 'd6aaad9c-1786-4f65-a5c9-b89b84397fd8';  
```

### Sample result

Here is a sample result set of the query.

|REQUEST_KEY|LOG_TYPE|INSTANT|INFORMATION|DURATION|
|--- |--- |--- |--- |--- |
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|MOBILE REQUEST|01-AUG-18 01.24.00.297507000 PM|eSpace ID: 1234; Screen: Load; Endpoint: Login_LoadApp; User ID: 123456|1906|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.23.58.391285000 PM|Extension ID: 31; eSpace ID: 122; Action: CurrTicks|0|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.23.59.281895000 PM|Extension ID: 31; eSpace ID: 122; Action: CurrTicks|0|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.23.59.281895000 PM|Extension ID: 31; eSpace ID: 122; Action: CurrTicks|0|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.23.59.281895000 PM|Extension ID: 37; eSpace ID: 122; Action: GetActionInfo|0|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.23.59.281895000 PM|Extension ID: 44; eSpace ID: 122; Action: HTTPPost|891|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.24.00.031912000 PM|Extension ID: 31; eSpace ID: 122; Action: CurrTicks|0|
|d6aaad9c-1786-4f65-a5c9-b89b84397fd8|EXTENSION|01-AUG-18 01.24.00.031912000 PM|Extension ID: 44; eSpace ID: 122; Action: HTTPPost|750|

## Mobile app calls server-side logic and it fails, logging errors

This SQL query enables you to list all errors related to a specific mobile request.

```sql
select request_key, 'MOBILE REQUEST' log_type, instant,  
'eSpace ID: '||espace_id||'; Screen: '|| screen || '; Endpoint: '||endpoint||'; User ID: '||user_id information, duration  
from oslog_mobile_request  
where request_key = '18f805aa-7510-4dc1-9f5b-c558647ea3dd'  
union all  
select request_key, 'ERROR', instant,  
'Message: '||message , -1  
from oslog_error  
where request_key = '18f805aa-7510-4dc1-9f5b-c558647ea3dd';
```

### Sample result

Here is a sample result set of the query.

|REQUEST_KEY|LOG_TYPE|INSTANT|INFORMATION|DURATION|
|--- |--- |--- |--- |--- |
|18f805aa-7510-4dc1-9f5b-c558647ea3dd|MOBILE REQUEST|01-AUG-18 01.24.55.011380000 PM|eSpace ID: 1234; Screen: Load; Endpoint: Login_LoadApp; User ID: 123456|31|
|18f805aa-7510-4dc1-9f5b-c558647ea3dd|ERROR|01-AUG-18 01.24.55.011380000 PM|Message: The underlying connection was closed: A connection that was expected to be kept alive was closed by the server.|-1|
|18f805aa-7510-4dc1-9f5b-c558647ea3dd|ERROR|01-AUG-18 01.24.55.011380000 PM|Message: The underlying connection was closed: A connection that was expected to be kept alive was closed by the server.|-1|
