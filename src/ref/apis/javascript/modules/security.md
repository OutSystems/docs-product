---
tags: runtime-mobileandreactiveweb
summary: Provides methods for doing client side role checks. Used to programmatically show or hide UI elements depending on a given role.
---

# Security

Provides methods for doing client side role checks. Used to programmatically show or hide UI elements depending on a given role.

## Summary

<table markdown="1">
<thead>
<tr>
<th colspan="2">Functions</th>
</tr>
</thead>
<tbody>
<tr>
<td>[checkIfCurrentUserHasRole](security.md#checkifcurrentuserhasrole)</td>
<td>
Checks if the current user has the given role.
</td>
</tr>
</tbody>
</table>

## Functions

### checkIfCurrentUserHasRole

**checkIfCurrentUserHasRole(roleKey: string): boolean**

Checks if the current user has the given role.

Tip: module roles are available through the `$roles` pre-defined object.

Example:

```javascript
// check if the current user has the 'MyAppManager' role
$parameters.IsManager = $public.Security.checkIfCurrentUserHasRole($roles.MyAppManager);
```

Parameters:

* **roleKey**: string<br/> Object with role information, accessible in JavaScript code using `$roles.<RoleName>`.

Returns: boolean

Returns `true` if the current user has the given role, `false` otherwise.

