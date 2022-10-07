---
locale: en-us
guid: a3d00b4b-8f79-4136-9b52-bc9052faaa8d
app_type: traditional web apps, mobile apps, reactive web apps
---

# Roles

Besides the functions listed below, you also have another built-in function available for each existing role. This function, which is automatically defined by the platform, is the following:

* `Check<role_name>Role`

Check [Role Functions](../../../develop/security/user-roles/create-a-custom-role.md#role-functions) for more information.




<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#CheckRole">CheckRole</a>(&#8203;RoleId, UserId)</td>
<td>Returns true when the given user has the specific role.</td>
</tr>
<tr>
<td><a href="#GetUserId">GetUserId</a>()</td>
<td>Returns the identifier of the user that is currently authenticated with the server or 'NullIdentifier()' if the user is not authenticated.</td>
</tr>
</tbody>
</table>

## CheckRole { #CheckRole }

Returns true when the given user has the specific role.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: No
  * Database: Can be used with attributes in aggregates.
  * Local Storage: Can be used with attributes in aggregates.

### Parameters

RoleId
:    Type: RoleId. Mandatory.  
The identifier of the role to be validated.

UserId
:    Type: UserId. Mandatory.  
The identifier of the user for which to validate if role is granted.

### Output

Type: Boolean  

## GetUserId { #GetUserId }

Returns the identifier of the user that is currently authenticated with the server or 'NullIdentifier()' if the user is not authenticated.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

<div class="info" markdown="1">
Don't use the GetUserId() function in the On After Fetch event of Data Actions or client-side Agreggates. The parallel execution of Data Actions and client-side Agreggates in a Screen overrides the session authentication cookie. Therefore, using the GetUserId() function in the On After Fetch event might return an empty value.
</div>

### Output

Type: UserId  

