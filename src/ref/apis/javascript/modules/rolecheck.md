---
tags: runtime-mobileandreactiveweb
summary: Provides methods for doing client side role checks. Used to programmatically show or hide UI elements depending on a given role.
locale: en-us
guid: efe75497-2f0f-4bbe-9f97-e65c2b345210
app_type: mobile apps, reactive web apps
---

# Role Check

<div class="info" markdown="1">

Applies to Mobile Apps and Reactive Web Apps only

</div>

Provides methods for performing client side role checks. Used to programmatically show or hide UI elements depending on a given role.

**Note:** This API is not intended to be used for security checks, but solely as a convenient means of making UI decisions (for example, showing or hiding UI elements) on the client side. As a best practice, OutSystems recommends to always check the user's role on the server side before performing any sensitive operations (for example, saving data) that are restricted based on the user's role.

## Summary

|Functions|Description|
|---|---|
|[checkIfCurrentUserHasRole](rolecheck.md#checkifcurrentuserhasrole)|Checks if the current user has the given role.|

## Functions

### checkIfCurrentUserHasRole

**checkIfCurrentUserHasRole(roleKey: string): boolean**

Checks if the current user has the given role.

Tip: Module roles are available through the `$roles` pre-defined object.

Example:

```javascript
// check if the current user has the 'MyAppManager' role
$parameters.IsManager = $public.Security.checkIfCurrentUserHasRole($roles.MyAppManager);
```

Parameters:

* **roleKey**: string<br/> Object with role information, accessible in JavaScript code using `$roles.<RoleName>`.

Returns: boolean

Returns `true` if the current user has the given role, `false` otherwise.
