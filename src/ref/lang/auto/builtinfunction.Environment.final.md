# Environment


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#GetApplicationServerType">GetApplicationServerType</a>()</td>
<td>Returns ".Net".</td>
</tr>
<tr>
<td><a href="#GetCurrentLocale">GetCurrentLocale</a>()</td>
<td>Returns the name of the current language locale of the user session. The name of the language locale is used for presentation purposes and follows the RFC 1766 standard format.</td>
</tr>
<tr>
<td><a href="#GetDatabaseProvider">GetDatabaseProvider</a>()</td>
<td>Returns the type of the Platform Database (SqlServer or Oracle) where the module is running.</td>
</tr>
<tr>
<td><a href="#GetUserAgent">GetUserAgent</a>()</td>
<td>Returns the user agent, as indicated by the header of the HTTP message.</td>
</tr>
<tr>
<td><a href="#GetOwnerEspaceIdentifier">GetOwnerEspaceIdentifier</a>()</td>
<td>Returns the identifier of the module that owns the element that is being processed.</td>
</tr>
<tr>
<td><a href="#GetEntryEspaceName">GetEntryEspaceName</a>()</td>
<td>Returns the name of the module that is processing the web request.</td>
</tr>
<tr>
<td><a href="#GetEntryEspaceId">GetEntryEspaceId</a>()</td>
<td>Returns the identifier of the module that is processing the web request.</td>
</tr>
<tr>
<td><a href="#GetObsoleteTenantId">GetObsoleteTenantId</a>()</td>
<td>Method to return a fake tenant identifier for single-tenant modules in order to mimic Site.TenantId semantic from the 6.0 version</td>
</tr>
</tbody>
</table>

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

