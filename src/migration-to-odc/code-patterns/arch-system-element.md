---
summary: 
locale: en-us
guid: 397c91b5-97d7-4184-8ab5-b9f42cb2dd66
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30538
---
# Asset consuming O11 system elements

Most of the functionality provided by O11 system elements is available in ODC, except for functionality that either doesn't work with the cloud-native architecture of ODC or that relates to functionality that isn't available in ODC.

System elements includes functionality exposed as Actions and built-in functions, and also includes [system Entities](https://success.outsystems.com/documentation/how_to_guides/data/data_migration_from_production_to_non_production_environment/outsystems_platform_metamodel).

In ODC, system entities don't exist. Therefore, any reference to these entities must be removed except for the User entity that exists as a cache but with a simpler field structure.

The following sections list the system actions that still exist in ODC and don't haven't changed, the system elements that still exist but that changed, and finally the system elements that aren't available in ODC.

## Functionality available in ODC without changes { #no-changes }

|Producer|Action|
|---|---|
|Binary Data|BinaryDataToHex|
|Date Time|DiffMonths(Datetime1, Datetime2)|
|Date Time|DiffQuarters(Datetime1, Datetime2)|
|Date Time|DiffWeeks(Datetime1, Datetime2)|
|Date Time|DiffYears(Datetime1, Datetime2)|
|Date Time|GetTicks(Datetime)|
|Date Time|IsLepYear(Datetime)|
|Date Time|Quarer(Datetime)|
|Logic|Sleep|
|Math|Ceiling(Number)|
|Math|Floor(Number)|
|Math|Log10(Number)|
|Math|Log2(Number)|
|Math|LogE(Number)|
|Math|Random(MinVal, MaxVal)|
|REST|Request_AddHeader|
|REST|Request_GetActionName|
|REST|Request_GetHeaders|
|REST|Request_GetURL|
|REST|Request_RemoveHeader|
|REST|Request_SetCookie|
|REST|Request_SetURL|
|REST|Response_GetActionName|
|REST|Response_GetBodyAsBinary|
|REST|Response_GetBodyAsText|
|REST|Response_GetCookie|
|REST|Response_GetStatusCode|
|REST|Response_SetBodyAsBinary|
|REST|Response_SetBodyAsText|
|Security|AES_Decrypt(Cyphertext, Key)|
|Security|AES_Encrypt(Plaintext, Key)|
|Security|AES_NewKey(NrBits)|
|Security|ComputeBinaryHash|
|Security|ComputeMAC|
|Security|ComputeTextHash|
|Security|CryptoRandomInt|
|Security|GenerateSecurePassword|
|Security|JWT_CreateToken|
|Security|JWT_ReadToken|
|Security|JWT_SetShowPII|
|Security|RSA_Decrypt(Cyphertext, Key, Padding)|
|Security|RSA_Encrypt(Plaintext, Key, Padding)|
|Security|RSA_GetPublicKey(Key)|
|Security|RSA_KeyFromPEM|
|Security|RSA_NewKey(NrBits)|
|Security|RSA_Sign(Plaintext, Key, Algorithm, Padding)|
|Security|RSA_VerifySignature(Data, Signature, PublicKey, Algorithm, Padding)|
|URL|DecodeURL(URL)|
|URL|EncodeURL|
|URL|GetRelativeURL(URL)|
|URL|GetURLHost(URL)|
|URL|GetURLProtocol(URL)|
|URL|IsURLRelative|

## Functionality available in ODC with changes { #changes }

### Deleted system extension actions with custom workarounds

The following actions have no equivalent logic in ODC and should be deleted. However, you can implement your custom code to achieve the same functionality.

#### Richmail

If your logic in O11 required a connection to the email server to manage an account, you can implement it using custom code. For more information, refer to [Extend your apps with external logic using custom code](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/extend_your_apps_with_external_logic_using_custom_code/).

* HtmlToText
* Pop3DeleteMails
* Pop3GetBody
* Pop3GetMails
* Pop3GetUIDs
* Pop3TestAccount
* PopGetMailHeader

#### UserLocalManagement

User management in ODC is different from O11. For detailed information about user management in ODC, refer to [User Management](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/).

* Group_AddUser
* Group_Create
* Group_CreateOrUpdate
* Group_CreateOrUpdateMultiple
* Group_Delete
* Group_Get
* Group_HasUser
* Group_RemoveUser
* Group_SetUsers
* Group_Update
* User_CreateOrUpgrade
* User_Delete
* User_Get
* User_SetGroups
* User_Update

#### XML

If you want to implement the same logic in ODC, you can create an external library with the actions logic and consume it. YOu can also use a JSON serialization to cover data migration use cases.

* Serialization_ObjectToXml
* Serialization_RecordListToXml
* Serialization_RecordToXml
* Serialization_XmlToRecordList

### Deleted system extension actions but can apply manual transformation

The following actions were removed or changed. You can use the manual transformations to keep the logic working in ODC.

#### HttpRequestHandler

The following list of actions in the RequestHandler extension require transformation.

* **GetRawURL**: Replace with **GetRelativeURL** from the URL library, and enter the respective URL as input. You may need to call Request_GetUrl.
* **URLEncode**: Replace with EncodeURL (part of the URL library)
* **PostRequest_AddBinaryArgument**: This transformation requires you to:
  
1. Create a Server Action with the same signature as PostRequest_AddBinaryArgument.
1. Convert the **ArgumentsIn** and **Value** input parameters to Text using BinaryDataToText (BinaryData Library).
1. Assign the ArgumentsOut to **If(Length(BinaryDataToTextArgumentsIn.Text) = 0, Name + "=" + BinaryDataToTextValue.Text, BinaryDataToTextArgumentsIn.Text + "&" + Name + "=" + BinaryDataToTextValue.Text)** and convert it to binary using the TextToBinaryData (BinaryData Library).

* **Request_SUbmit**: Replace with REST Consume (POST request). Adapt the app logic taking into account that the REST Consume action returns only the Response with the respective type instead of TextContent, BinaryContent and BinaryContentType returned by PostRequest_Submit.

#### PlatformRuntime_AppLogInfo

* **Session_GetMobileAppLoginInfo**:  Replace with GetUserProfile.
This function returns a UserInfo structure containing information that identifies the user (Name, Email and PhotoURL) instead of the userId. Therefore, you need to change the logic of the app  so it's  compatible with the UserInfo structure.

#### RichMail

* **HttpBinaryGet**: Replace with Request_SubmitGetRequest (HTTP Library) and adapt the app logic to use BinaryContent returned.
* **HttpGet**: Replace with Request_SubmitGetRequest (HTTP Library) and change  the app logic to use TextContent returned.
* **RichMailAuthenticate,RichMailCreate, RichMailForward, RichMailPart, RichMailSend**: Replace this with [ODC email logic](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/emails/). The logic offered in this extension it's an outdated version of the current email logic available in ODC.

#### Sample_JWTUtils

* **Create Token**:  Replace with the ODC JWT_CreateToken. The signatures of the O11 and ODC actions are different, therefore, you need to change the logic to the signature of the new action. This transformation is only required if you are using a JSON Web Key (JWK).
* **ReadToken**: Replace with the ODC JWT_ReadToken. The signatures of the O11 and ODC actions are different, therefore, you need to change the logic to the signature of the new action. This transformation is only required if you are using a JSON Web Key (JWK).

### Built-in functions but can apply manual transformation

The following lists built-in functions by category that were deleted, but you can apply manual transformations to keep the logic working in ODC.

The information is divided by category and lists the action name and the manual transformation that can be applied.

#### Text

The following list provides information on built-in actions in the Text category that should be deleted. However, you can apply the described manual transformation to retain the logic.

* **Concat(t1, t2):** Replace by t1 + t2

#### Email

The following list provides information on built-in actions in the Email category that should be deleted. However, you can apply the described manual transformation to retain the logic.

* **EmailAddressConcatenate:** Similar to the concatenation but with a different format, that includes name and e-mail.

#### Miscellaneous

The following list provides information on built-in actions in the Miscellaneous category that should be deleted. However, you can apply the described manual transformation to retain the logic.

* **Generate Password:** Use the new function called **GenerateSecurePassword** . For detailed information, refer to GenerateSecurePassword.
* **GetUserId:** In ODC, the Users table has changed, and the UserID is a text (Guid) and not an integer. Therefore, you must review all use cases where you have used GetUserId and UserId and change the data type. For example, if you have assigned User ID to an integer local variable now you modify it to text.
Roles
* **CheckRoles:** On creating a role, the corresponding sever and client actions are created . Since there isn't a generic CheckRole, you must replace it with the function of that specific role.

#### Environment

The following list provides information on built-in actions in the Environment category that should be deleted. However, you can apply the described manual transformation to retain the logic.

* **GetExceptionURL**  This action is typically used in Logout flow. You must delete it manually.

### Built in functions not supported inside aggregates

The following list provides information on built-in functions that are still available in ODC but can't be used inside aggregates to filter attributes in entities. They aren't supported inside aggregate, such as when used to compute information of an entity attribute. For example, it's not possible to do `Round(Entity1.Attribute1)`. The information is divided by category and lists the action name that can't be used inside an aggregate.

#### Date Time

The following list provides information on built-in actions in the Date Time category that can't be used inside aggregates.

* BuildDateTime
* NewDate
* NewDateTime
* NewTime

#### Text

Under Text category, you can't use **Replace** built-in function inside an aggregate.

#### Math

Under Math category, you can't use **Round** built-in function inside an aggregate.

## System Elements not available in ODC { #not-available }

### System extension actions incompatible with ODC Architecture

Following are extension actions presented in alphabetical order that aren't available in ODC, because they use logic that's no longer supported in ODC. You must revisit your code and delete these actions. The information is divided by the O11 extension name and lists the corresponding action name and why they can't be transformed.  

#### AsynchronousLogging

The following action was deleted in ODC, because **you can't log records** into the database.

* Logrecord

#### Authentication

The following actions were deleted because ODC doesn't support **windows accounts querying**.

* ActiveDirectory_GetAccountDetails
* ActiveDirectory_GetAccountGroups
* ActiveDirectory_ValidateLogin
* CheckIsInternalNetwork
* LdapFilterEncode
* LDAP_Login
* LDAP_PropertyGetList
* LDAP_PropertyGetList_WithAuthenticationType
* LDAP_Search
* LDAP_Search_WithAuthenticationTypeLDAP_ValidateLogin
* LDAP_ValidateLogin_WithAuthenticationType
* SplitDomainAndUser

#### BPT API

The following actions were deleted because ODC doesn't support Processes (BPTs)

* Activity_Discard
* Activity_IsValidId
* HumanActivity_AssignToUser
* HumanActivity_CheckRole
* HumanActivity_FlushPendingEvents
* HumanActivity_SetDueDate
* Process_BulkDelete
* Process_Delete
* Taskbox_Hide

#### ECT_Controller

The following actions were deleted because ODC doesn't support Embedded Change Technology (ECT)

* GetEnvironmentUID
* RemoveScreenFeedback

#### ECT_PageRetriever

The following actions were deleted because ODC doesn't support Embedded Change Technology (ECT)

* BinaryToTextUTF8
* ComputeHash
* GetFramesFromRequest
* GetRequestCookieHeader
* RetrievePersistentWebPage
* TextToBinaryUTF8

#### EnhancedWebReferences

The following actions were deleted because ODC doesn't support SOAP.

* ClearWebReferenceHeaders
* GetWebReferenceSoapHeaders
* GetWebServiceSoapHeaders
* SetWebReferenceCredencials
* SetWebReferenceProxy
* SetWebReferenceSoapHeaders
* SetWebReferenceURL
* SetWebServiceSoapHeaders

#### EPA_TaskboxExtension

The following actions were deleted it applies only to traditional web apps.

* GetActivities
* GetActivityCount
* GetNewOpenActivity
* SetSessionUserId

#### HtmlRenderer

The following actions were deleted it applies only to ECT and Embedded Process Automation (EPA)

* AddWebBlockInputParameter
* ClearPasswordFromInputTags
* DecodeHTML
* GetMachineInternalName
* GetMachineName
* MakeAbsoluteHTML
* MakeAbsoluteURL
* ProcessHTML
* ProcessHTMLObjectTag
* RemoveAllJavascript
* RenderWebBlock

#### HttpRequestHandler

The following actions were deleted it applies only to traditional web apps.

* AddAttributeToHtmlTag
* AddFaviconTag
* AddJavaScriptTag
* AddLinkTag
* AddMetaHttpEquivTag
* AddMetaTag
* AddPostProcessingFilter
* AddSessionToURL
* AddStyleSheetTag
* GetEntryURL
* GetFormValue
* GetPageExtension
* GetPageName
* GetRunningESpaceJQueryVersion
* GetSessionId
* GetURLWithSession
* GetValueFromInputId
* GetValueFromInputIdDecoded
* IsAjaxRequest
* RunJavaScript
* SetBaseTag
* SetPageTitle

The following actions were deleted since unlike O11, in ODC, extensions are executed out-of-process. Therefore, you can't access the request using extensions. Therefore, you must analyze on case-by-case basis and make suitable changes. For instance, the usage of the GetIP action may be replaced with the IP Filtering feature accessible on the portal.

* GetIP
* GetReferrerURL
* GetRequestContent
* GetURLMethod
* GetUserAgent
* GetUserLanguages
* IsSecureConnection
* SetLastModified
* SetRequestTimeout
* ValidateRequestSource

#### IncludeJavascript_API

The following actions were deleted it applies only to traditional web apps.

* Application_AddExclusionRule
* Application_RemoveExclusionRule
* Espace_AddExclusionRule
* Espace_RemoveExclusionRule
* Script_CreateOrUpdate
* Script_Delete
* Script_Get
* Script_List
* Script_SetActive
* Script_SetInactive

#### PlatformPasswordUtils

The following actions were deleted as ODC doesn't manage passwords.

* GenerateSaltedMD5Hash
* GenerateSaltedSHA512Hash
* ValidatePassword

#### PlatformRuntime_API

* The action **Audit_CreateAuditLog** was deleted as ODC doesn't log audit records.
* The actions **DatabaseConnection_SetConnectionStringForSession**, **Database_WriteInParallelTransaction** were deleted as it doesn't apply to ODC architecture.
* The action **Request_GetKey** was deleted since LogError and LogRequestEvent that uses this action isn't available in ODC.
* The action **Session_GetWebAppLoginInfo** was deleted as it applies only to traditional web apps.

#### SAMLAuthentication

The following actions were deleted as ODC doesn't support SAML authentication.

* KeyStore_ExtractPublicCertificate
* KeyStore_Generate
* SAML_BuildSHA256Signature
* SAML_Compress
* SAML_CreateAuthnRequest  
* SAML_CreateLogoutRequest
* SAML_CreateLogoutResponse
* SAML_Decompress
* SAML_KillSession
* SAML_ParseLogoutRequest
* SAML_ParseLogoutResponse
* SAML_ValidateCertificate
* SAML_ValidateResponse
* SAML_ValidateURI
* Users_GetTraditionalAppsSessionTimeout

### System actions incompatible with ODC architecture

The following section provides details on system actions presented in alphabetical order that aren't available in ODC and why they can't be transformed. Therefore, you must revisit your code and delete these system actions without applying any transformation.

**Action**
* ActivityClose
* ActivityGetUrl
* ActivityOpen
* ActivityReset
* ActivitySchedule
* ActivitySetGroup
* ActivitySkip
* ActivityStart
* ProcessTerminate
**Reason**
ODC doesn't support BPTs.

**Action:**
* ClientCertificateGetDetails
* ClientCertificateValue
**Reason:**
These actions are used only on on-prem environments and doesn't apply to ODC.

**Action:**
* Deprecated_Notify
* Deprecated_NotifyGetMessage
* Deprecated_NotifyWidget
* InboundSmsGetDetails
**Reason:** These actions are already deprecated in O11

**Action:**
* IntegratedSecurityCheckRole
* IntegratedSecurityGetDetails
**Reason:** ODC doesn't support integrated authentication

**Action:**
* Login
* LoginPassword
* Logout
**Reason:** The login and logout logic is different in ODC

**Action:**
* TenantCreate
* TenantInvalidateCache
* TenantSwitch
**Reason:** ODC doesn't support multi-tenant applications.

### Built-in functions incompatible with ODC Architecture

Following are actions that are no longer available in ODC. You must revisit your code and delete these built-in functions. The information is divided by category and lists the action name and why they can't be transformed.

#### Environment 
The following list provides information on built-in actions in the environment category that aren't available in ODC. You can't apply manual transformations. 

*  **GetApplicationServerType:** This function was used in O10 or earlier to check whether the server was .NET or Java but the server type in ODC is always the same. So this action is not necessary.
*  **GetDatabaseProvider:** In ODC, the DB engine is always Aurora Postgres so this function is no longer required.
* **GetEntryEspaceId:** In ODC, apps are run in containers so this function is not needed.
* **GetObsoleteTenantId:** ODC doesn't support multi-tenant applications so this function is not needed.
*  **GetOwnerEspaceIdentifier:** ODC doesn't have system tables so this function is not needed.

#### URL

The following list provides information on built-in actions in the URL category that aren't available in ODC. However, you can't apply manual transformations. 

* **AddPersonalAreaToURLPath:** ODC doesn't support personal areas.
* **GetPersonalAreaName:** ODC doesn't support personal areas.

## How to solve

You must solve this pattern in ODC, after proceeding with the code migration to ODC.

### Solve in ODC

Depending on the scenario, do one of the following:

* For functionality exposed as actions or built-in functions:

    * If the [functionality of the system element is available in ODC without changes](#no-changes), ensure the dependencies are defined correctly.
    
    * If the [functionality of the system element is available in ODC with changes](#changes), implement the changes in your ODC Assets.
    
    * If the [functionality of the system element isn't available in ODC](#not-available), revisit your code since it no longer has access to these O11 functionalities.

* For [System entities](https://success.outsystems.com/documentation/how_to_guides/data/data_migration_from_production_to_non_production_environment/outsystems_platform_metamodel/):

     * If there's a dependency to the User entity, check that your code dependent on this entity works properly. In ODC the cache based User entity has a simpler field structure when compared to the O11 User entity, so some fields aren't available.
 
     * Otherwise, refactor your code to avoid the dependency to the system entity.
