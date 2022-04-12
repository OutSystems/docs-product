---
locale: en-us
guid: 83ba44be-1320-4def-9741-0cf7e7842b05
---

# Environment

|Name|Description|
|--- |--- |
|[GetApplicationServerType](#getapplicationservertype--getapplicationservertype)()|Returns ".Net".|
|[GetCurrentLocale](#getcurrentlocale--getcurrentlocale)()|Returns the name of the current language locale of the user session. The name of the language locale is used for presentation purposes and follows the RFC 1766 standard format.|
|[GetDatabaseProvider](#getdatabaseprovider--getdatabaseprovider)()|Returns the type of the Platform Database (SqlServer or Oracle) where the module is running.|
|[GetUserAgent](#getuseragent--getuseragent)()|Returns the user agent, as indicated by the header of the HTTP message.|
|[GetOwnerEspaceIdentifier](#getownerespaceidentifier--getownerespaceidentifier)()|Returns the identifier of the module that owns the element that is being processed.|
|[GetEntryEspaceName](#getentryespacename--getentryespacename)()|Returns the name of the module that is processing the web request.|
|[GetEntryEspaceId](#getentryespaceid--getentryespaceid)()|Returns the identifier of the module that is processing the web request.|
|[GetObsoleteTenantId](#getobsoletetenantid--getobsoletetenantid)()|Method to return a fake tenant identifier for single-tenant modules in order to mimic Site.TenantId semantic from the 6.0 version|

## GetApplicationServerType { #GetApplicationServerType }

Returns ".Net".  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetApplicationServerType() = ".Net"
```

## GetCurrentLocale { #GetCurrentLocale }

Returns the name of the current language locale of the user session. The name of the language locale is used for presentation purposes and follows the RFC 1766 standard format.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetCurrentLocale() = "en-US"
```

## GetDatabaseProvider { #GetDatabaseProvider }

Returns the type of the Platform Database (SqlServer or Oracle) where the module is running.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetDatabaseProvider() = "SqlServer"
GetDatabaseProvider() = "Oracle"

```

## GetUserAgent { #GetUserAgent }

Returns the user agent, as indicated by the header of the HTTP message.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetUserAgent() = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
GetUserAgent() = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"
```

## GetOwnerEspaceIdentifier { #GetOwnerEspaceIdentifier }

Returns the identifier of the module that owns the element that is being processed.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: EspaceId  

### Examples

```
GetOwnerEspaceIdentifier() = 141
```

## GetEntryEspaceName { #GetEntryEspaceName }

Returns the name of the module that is processing the web request.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: Text  

### Examples

```
GetEntryEspaceName() = "MyModule"
```

## GetEntryEspaceId { #GetEntryEspaceId }

Returns the identifier of the module that is processing the web request.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: EspaceId  

### Examples

```
GetEntryEspaceId() = 70
```

## GetObsoleteTenantId { #GetObsoleteTenantId }

Method to return a fake tenant identifier for single-tenant modules in order to mimic Site.TenantId semantic from the 6.0 version  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Output

Type: TenantId  

### Examples

```
GetObsoleteTenantId() = 30
```

