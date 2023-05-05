---
summary: Social Login plugin - reference page
tags: runtime-mobile
locale: en-us
guid: 126ae5a9-3ac9-4f2c-a40d-a1cd4f107b5a
app_type: mobile apps
platform-version: o11
---

# Social Login plugin - reference page

## Plugin elements

### Client actions

#### CheckSocialLoginPlugin

Verifies if the Social Login Mobile Plugin is available or properly installed in the application.

Parameter|Type|Data Type|Description
---|---|---|---
IsAvailable|Output|Boolean|Returns a boolean value based on plugin availability: "true" if the plugin is available, "false" if not.
Error|Output|Error|Displays detailed information of an error, if applicable.

#### StartLogin

Lets you request access to a subset of your user's data stored by Apple, Google, Facebook, or LinkedIn - including name, email, profile picture, user ID, and the user's access token. This is information you can use to create or start a user session on your app.

Parameter|Type|Data Type|Description
---|---|---|---
Provider|Input|Provider Identifier|Lets you set the social login provider to use on your login flow.
ClientID|Input|Text|Lets you set the Client ID (Google and Linkedin), AppID (Facebook), or Identifier (Apple) of your app. This is a text type value available to any registered developer on each specific provider development platform.
RedirectUri|Input|Text|Lets you set the RedirectURI; a URL type value that will send you the authorization result for the service by the Social Login Mobile plugin.

#### Provider Identifier

Holds static information about the available social login providers: Apple, Facebook, Google, and LinkedIn.

Id|Social login provider
---|---
1|Apple
2|Facebook
3|Google
4|LinkedIn

### Web blocks

#### Authenticate

Lets you handle the output information of the StartLogin action. After defining your handler, you’ll need to match the handler’s input parameters to the input parameters of the block’s OnAuthenticationCompleted event.

##### Authenticate Event Handler

This handler has the input parameters stored by the social login provider.

Parameter|Type|Data Type|Description
---|---|---|---
Authenticated|Input|Boolean|Shows if the authentication with the provider was successful (true) or not (false).
ID|Input|Text|The user's ID.
FirstName|Input|Text|The user's first name.
LastName|Input|Text|The user's last name.
Email|Input|Text|The user's email address.
Token|Input|Text|The user's token.
Picture|Input|Text|The URL of the user's profile photo.
Error|Input|Error|Displays detailed information of an error, if applicable.

## Rest APIs and Others

The Social Login Plugin uses the following APIs:

API|Documentation
---|---
[Google API](https://developers.google.com/apis-explorer)|Read documentation about Google authentication [here](https://developers.google.com/identity/protocols/oauth2#2.-obtain-an-access-token-from-the-google-authorization-server.).
[Graph API Facebook](https://developers.facebook.com/docs/graph-api/)|Read documentation about Facebook authentication [here](https://developers.facebook.com/docs/facebook-login/guides/access-tokens/).
[LinkedIn API](https://learn.microsoft.com/en-us/linkedin/)|Read documentation about LinkedIn authentication [here](https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication?context=linkedin%2Fcontext).

## Error Codes

Code|Platform|Social Login Provider|Message
---|---|---|---
OS-PLUG-SOCI-0100|iOS/Android|Apple|Couldn’t login with Apple.
OS-PLUG-SOCI-0101|iOS/Android|All|Couldn’t login because the process was canceled.
OS-PLUG-SOCI-0102|Android/Web|Apple|Couldn’t log in with Apple because Apple Sign-In configuration is missing.
OS-PLUG-SOCI-0103|Android|Apple|Couldn’t login with Apple because the access token is invalid.
OS-PLUG-SOCI-0104|iOS/Android|All|Couldn’t login because some input parameters are missing.
OS-PLUG-SOCI-0105|Android|Apple|Couldn’t login with Apple because the user’s ID is missing.
OS-PLUG-SOCI-0106|Android|Apple|Couldn’t login with Apple because the access token is missing.
OS-PLUG-SOCI-0199|Android|Apple|Couldn’t login with Apple because its configurations are not properly set.
OS-PLUG-SOCI-0200|iOS/Android|Google|Couldn’t login with Google.
OS-PLUG-SOCI-0201|iOS|Google|Couldn’t login with Google because Google Sign-In configuration is missing.
OS-PLUG-SOCI-0202|iOS/Android|Google|Couldn’t login with Google because the access token is missing.
OS-PLUG-SOCI-0203|iOS/Android|Google|Couldn’t login with Google because the user’s ID is missing.
OS-PLUG-SOCI-0204|iOS/Android|Google|Couldn’t login with Google because Google Sign-In configuration is invalid.
OS-PLUG-SOCI-0300|iOS/Android|Facebook|Couldn’t login with Facebook.
OS-PLUG-SOCI-0301|Web (PWA)|Facebook|Couldn’t log in with Facebook because Facebook Sign-In configuration is missing.
OS-PLUG-SOCI-0302|iOS/Android|Facebook|Couldn’t login with Facebook because the access token wasn’t found.
OS-PLUG-SOCI-0303|iOS/Android|Facebook|Couldn’t login with Facebook because no results were returned.
OS-PLUG-SOCI-0304|iOS/Android|Facebook|Couldn’t login with Facebook due to an error when fetching the information for all the parameters requested.
OS-PLUG-SOCI-0305|iOS/Android|Facebook|Couldn’t login with Facebook due to an error while requesting the user's data.
OS-PLUG-SOCI-0399|iOS/Android|Facebook|Couldn’t login with Facebook because its configurations are not properly set.
OS-PLUG-SOCI-0400|iOS/Android|LinkedIn|Couldn’t login with LinkedIn.
OS-PLUG-SOCI-0401|iOS|LinkedIn|Couldn’t login with LinkedIn due to an error while creating the request.
OS-PLUG-SOCI-0402|iOS|LinkedIn|Couldn’t login with LinkedIn due to an error while creating the web authentication session.
OS-PLUG-SOCI-0403|iOS|LinkedIn|Couldn’t login with LinkedIn due to an error when fetching the information for all the parameters requested.
OS-PLUG-SOCI-0404|Android|LinkedIn|Couldn’t login with LinkedIn because the access token is missing.
OS-PLUG-SOCI-0405|Android|LinkedIn|Couldn’t login with LinkedIn because the user ID is missing.
OS-PLUG-SOCI-0406|All|LinkedIn|Couldn’t log in with LinkedIn because LinkedIn Sign-In configuration is missing.
OS-PLUG-SOCI-0499|iOS/Android|LinkedIn|Couldn’t login with LinkedIn because its configurations are not properly set.
OS-PLUG-SOCI-0500|OS Wrapper|All|Couldn’t log in because the access token isn’t valid.
