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
  
<table>  
<tr>  
<th>
REQUEST_KEY
</th>  
<th>
LOG_TYPE
</th>  
<th>
INSTANT
</th>  
<th>
INFORMATION
</th>  
<th>
DURATION
</th></tr>  
<tr>  
<td>
9c35b89a-2ec3-4716-bb96-4e3ea41b664c
</td>  
<td>
MOBILE REQUEST
</td>  
<td>
01-AUG-18 01.22.01.378236000 PM
</td>  
<td>
eSpace ID: 1234; Screen: Synchronize; Endpoint: LoginData_Sync; User ID: 123456
</td>  
<td>
3015
</td></tr>  
<tr>  
<td>
9c35b89a-2ec3-4716-bb96-4e3ea41b664c
</td>  
<td>
INTEGRATION
</td>  
<td>
01-AUG-18 01.22.00.253199000 PM
</td>  
<td>
Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/userData/Get; Action: UserData.GetDate
</td>  
<td>
328
</td></tr>  
<tr>  
<td>
9c35b89a-2ec3-4716-bb96-4e3ea41b664c
</td>  
<td>
INTEGRATION
</td>  
<td>
01-AUG-18 01.22.00.628220000 PM
</td>  
<td>
Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/UserDetails/Get; Action: UserData.GetDetails
</td>  
<td>
375
</td></tr>  
<tr>  
<td>
9c35b89a-2ec3-4716-bb96-4e3ea41b664c
</td>  
<td>
INTEGRATION
</td>  
<td>
01-AUG-18 01.22.00.940738000 PM
</td>  
<td>
Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/SaveChanges; Action: UserData.SaveUserProfile
</td>  
<td>
296
</td></tr>  
<tr>  
<td>
9c35b89a-2ec3-4716-bb96-4e3ea41b664c
</td>  
<td>
INTEGRATION
</td>  
<td>
01-AUG-18 01.22.01.331361000 PM
</td>  
<td>
Type: REST (Consume); Endpoint: https://internalapi.example.com/v1/Refresh; Action: UserData.RefreshInRepository
</td>  
<td>
390
</td></tr></table>

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
  
<table>  
<tr>  
<th>
REQUEST_KEY
</th>  
<th>
LOG_TYPE
</th>  
<th>
INSTANT
</th>  
<th>
INFORMATION
</th>  
<th>
DURATION
</th></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
MOBILE REQUEST
</td>  
<td>
01-AUG-18 01.24.00.297507000 PM
</td>  
<td>
eSpace ID: 1234; Screen: Load; Endpoint: Login_LoadApp; User ID: 123456
</td>  
<td>
1906
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.23.58.391285000 PM
</td>  
<td>
Extension ID: 31; eSpace ID: 122; Action: CurrTicks
</td>  
<td>
0
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.23.59.281895000 PM
</td>  
<td>
Extension ID: 31; eSpace ID: 122; Action: CurrTicks
</td>  
<td>
0
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.23.59.281895000 PM
</td>  
<td>
Extension ID: 31; eSpace ID: 122; Action: CurrTicks
</td>  
<td>
0
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.23.59.281895000 PM
</td>  
<td>
Extension ID: 37; eSpace ID: 122; Action: GetActionInfo
</td>  
<td>
0
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.23.59.281895000 PM
</td>  
<td>
Extension ID: 44; eSpace ID: 122; Action: HTTPPost
</td>  
<td>
891
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.24.00.031912000 PM
</td>  
<td>
Extension ID: 31; eSpace ID: 122; Action: CurrTicks
</td>  
<td>
0
</td></tr>  
<tr>  
<td>
d6aaad9c-1786-4f65-a5c9-b89b84397fd8
</td>  
<td>
EXTENSION
</td>  
<td>
01-AUG-18 01.24.00.031912000 PM
</td>  
<td>
Extension ID: 44; eSpace ID: 122; Action: HTTPPost
</td>  
<td>
750
</td></tr></table>

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
  
<table>  
<tr>  
<th>
REQUEST_KEY
</th>  
<th>
LOG_TYPE
</th>  
<th>
INSTANT
</th>  
<th>
INFORMATION
</th>  
<th>
DURATION
</th></tr>  
<tr>  
<td>
18f805aa-7510-4dc1-9f5b-c558647ea3dd
</td>  
<td>
MOBILE REQUEST
</td>  
<td>
01-AUG-18 01.24.55.011380000 PM
</td>  
<td>
eSpace ID: 1234; Screen: Load; Endpoint: Login_LoadApp; User ID: 123456
</td>  
<td>
31
</td></tr>  
<tr>  
<td>
18f805aa-7510-4dc1-9f5b-c558647ea3dd
</td>  
<td>
ERROR
</td>  
<td>
01-AUG-18 01.24.55.011380000 PM
</td>  
<td>
Message: The underlying connection was closed: A connection that was expected to be kept alive was closed by the server.
</td>  
<td>
-1
</td></tr>  
<tr>  
<td>
18f805aa-7510-4dc1-9f5b-c558647ea3dd
</td>  
<td>
ERROR
</td>  
<td>
01-AUG-18 01.24.55.011380000 PM
</td>  
<td>
Message: The underlying connection was closed: A connection that was expected to be kept alive was closed by the server.
</td>  
<td>
-1
</td></tr></table>
