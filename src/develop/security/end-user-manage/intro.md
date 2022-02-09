# End Users
An end user is someone who uses your OutSystems application(s). Each non-anonymous end user who interacts with your apps counts toward the user limits established in your subscription. 

## Internal and External End Users
Each end user of your OutSystems applications is classified as internal or external. Internal is intended for employees and contractors of your organization. External is for your customers, partners, or other external parties whom you serve with the apps you build.

Within the OutSystems platform, the classification of internal or external is based on the end user's email address. When the end user's email address uses a domain name that matches a domain that you own, the user is considered internal. For example if your organization owns somecompanyname.com and the end user's email is someone@somecompanyname.com, then the user will be classified as internal. The user will also be classified as internal in situations where no email address is stored on their profile, such as when you only capture a mobile phone number for the end user, but not an email address. All other users are classified as external.

## Anonymous Users
Anonymous users do not count toward the user limits specified in your subscription. Users who use your app and who don't log in and also don't share any personally-identifiable information (name, email, mobile phone, etc.) are anonymous. For example, people who visit your website (an OutSystems app) and just browse the information without logging in or providing personal information are anonymous end users.

## End User Limits
OutSystems subscriptions typically include rights to run applications serving up to a specified number of end users, with options for upgrading end user capacity that vary by subscription. You can review your end user limits within the Customer Portal and you can see the current internal and external end user count displayed for each runtime environment within Service Center. If you have multiple production runtime environments, you'll sum the end user counts for each to determine your total end user count. When your end user count exceeds the end user limit specified in your subscription (internal or external), you need to upgrade to remain in compliance with the license terms. Please contact your OutSystems sales representative for assistance.

## Managing your End Users
You may periodically de-activate users who you know will not continue to use your applications and these users will no longer count toward your user limits. For example, when an employee quits, you would de-activate this user because they will no longer need access to apps you've built for your employees.

- [Manage end users](accessing-users.md) through the **Users** console, which is available at `http://<environment address>/Users`.
- Manage end users programmatically using the [Users API](<../../../ref/apis/auto/users-api.md>) 

## Older Subscription Models
In the past, some OutSystems subscriptions did not distinguish between internal and external end users, the limits were based on the total non-anonymous users. Some customers may still have an active subscription under the prior model. These users were labeled as named or registered users.

## Related resources
- [Classify Users as Internal Users](classify-internal-users.md): includes information on configuring the email domains that will be recognized as your own, for purposes of classifying users as internal or external
- [End User Authentication](end-user-authentication/intro.md): information on external authentication methods
- [Managing IT users](../../../managing-the-applications-lifecycle/manage-it-teams/intro.md): manage developer access, administrators, and other roles with access to OutSystems management tools
- [Group management](groups.md): creating and managing groups of users
- [Multi-tenant applications](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/How_to_Build_a_Multi-tenant_Application#Managing_Tenants_and_End-Users): managing different cohorts of users from different tenants
