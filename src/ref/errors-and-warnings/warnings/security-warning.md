# Security Warning

Message
:   `You're exposing a database operation in the client side. Validate the data in a Server Action before changing the database.`

Cause
:   There's client-side logic in your app that can access and write changes to the server database. 

Recommendation
:   You need to validate the data on the server before you perform a database operation that can modify data or change the permissions. From the security and data integrity point of view, such validation must be implemented on the server. A client-side validation is not enough, as its purpose is to provide fast feedback to the users.

---

Message
:   `You're exposing a generic Server Action for public access and without authentication. Consider removing the Anonymous Role from this Screen.`

Cause
:    Calling Server Actions without first authenticating the request is reserved for special use cases, such as authentication operations, where a request cannot initially have the authentication info.

Recommendation
:   Review how and where you use Server Action and ensure the logic is not compromising security. For example, you may be allowing all visitors that are not signed in to change the employee information. To fix such an issue, you'd need to limit the access to the screen, and later validate the data on the server side.