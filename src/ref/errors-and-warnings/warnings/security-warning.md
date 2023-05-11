---
locale: en-us
guid: 2dd8aae1-92e8-4901-a1d4-95e98c968ae7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Security Warning

Message
:   `You're exposing a database operation in the client side. Validate the data in a Server Action before changing the database.`

Cause
:   There's client-side logic in your app that can access and write changes to the server database. 

Recommendation
:   You must validate the data on the server before you perform a database operation that can modify data or change the permissions. From the security and data integrity point of view, you must implement this validation on the server. A client-side validation isn't enough, as its purpose is to provide fast feedback to the users.

:   To resolve the warning, create a Server Action that calls the Entity Action, and then use this Server Action on the Client Actions. Keep in mind that you still need to create the server logic to ensure that your data is valid before saving. Here's an example of a Server Action calling the Entity Action:

: ![Create a server action](images/security-warning-1-ss.png)

---

Message
:   `You're exposing a generic Server Action for public access and without authentication. Consider removing the Anonymous Role from this Screen.`

Cause
:    Reserve calling Server Actions without first authenticating the request for special use cases only, such as authentication operations, where a request can't initially have the authentication information.

:    An **Anonymous** screen generates public endpoints, that is, a public IP address that can be accessed and manipulated by anyone that has access to that screen. Exposing public endpoints is a security risk as it can lead to **cross-site request forgery attacks**. Server actions inside Anonymous screens expose public endpoints. If an anonymous screen uses a block, it generates a public endpoint. If an anonymous screen uses a client action that calls the global client action, it generates a public endpoint.

Recommendation
:   Review how and where you use Server Action and ensure the logic isn't compromising security. For example, you may be allowing all visitors that aren't signed in to change the employee information. To fix such an issue, you must limit the access to the screen, and later validate the data on the server side.

:   To resolve the warning, you have the following options:

:    * Remove the Anonymous role by unchecking the **Anonymous** checkbox in the screen properties area. This means the screen is now a **Registered** screen and all users must be logged in to access the page.

:    * Ensure that all data sent from the app to the server is re-validated in the server action in a way that prevents unauthorized access to read or edit data.

:    * Redesign your logic so that the screen doesn’t fetch data from sources with sensitive data. 

:    ![Uncheck Anonymous checkbox](images/security-warning-2-ss.png)

