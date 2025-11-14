---
summary: This article provides guidelines for refactoring the usage of system elements in O11 apps to ensure compatibility with OutSystems Developer Cloud (ODC).
locale: en-us
guid: 397c91b5-97d7-4184-8ab5-b9f42cb2dd66
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
helpids: 30538
tags: cloud-native applications, system entities, api development, data integration, app conversion
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - unblock
  - understand
---

# Asset consuming O11 platform system elements

Most of the functionality provided by O11 platform system elements is available in ODC, except for functionality that doesn't work with the cloud-native architecture of ODC.

Platform system elements include [system actions](../../ref/apis/auto/system-actions.final.md) or actions of other [OutSystem APIs](../../ref/apis/intro.md), and [system entities](https://success.outsystems.com/documentation/how_to_guides/data/data_migration_from_production_to_non_production_environment/outsystems_platform_metamodel).

## How to solve

You must solve this pattern in ODC, after proceeding with the code conversion to ODC.

### Solve in ODC

Depending on the scenario, do one of the following:

* If the functionality of the system element is [available in ODC without changes](#no-changes), ensure the dependencies are defined correctly.
  
* If the functionality of the system element is [available in ODC with changes](#changes), implement the changes in your ODC Assets.
  
* If the functionality of the system element [isn't available in ODC](#not-available), adapt your code in alignment with ODC architecture.

The following sections list:

* [Functionality available in ODC without changes](#no-changes)
* [Functionality available in ODC with changes](#changes)
* [Functionality not available in ODC](#not-available)

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

#### XML

If you want to implement the same logic in ODC, you can create an external library with the actions logic and consume it. You can also use a JSON serialization to cover data migration use cases.

* Serialization_ObjectToXml
* Serialization_RecordListToXml
* Serialization_RecordToXml
* Serialization_XmlToRecordList

### Deleted system extension actions with possible manual transformation

The following actions were removed or changed, but you can use manual transformations to keep the logic working in ODC.

#### HttpRequestHandler

The following list of actions in the RequestHandler extension require transformation.

* **GetRawURL**: Replace with **GetRelativeURL** from the URL library, and enter the respective URL as input. You may need to call Request_GetUrl.
* **URLEncode**: Replace with EncodeURL (part of the URL library).
* **PostRequest_AddBinaryArgument**: This transformation requires you to:
    1. Create a Server Action with the same signature as PostRequest_AddBinaryArgument.
    1. Convert the **ArgumentsIn** and **Value** input parameters to Text using BinaryDataToText (BinaryData Library).
    1. Assign the ArgumentsOut to **If(Length(BinaryDataToTextArgumentsIn.Text) = 0, Name + "=" + BinaryDataToTextValue.Text, BinaryDataToTextArgumentsIn.Text + "&" + Name + "=" + BinaryDataToTextValue.Text)** and convert it to binary using the TextToBinaryData (BinaryData Library).
* **Request_SUbmit**: Replace with REST Consume (POST request). Adapt the app logic taking into account that the REST Consume action returns only the Response with the respective type instead of TextContent, BinaryContent and BinaryContentType returned by PostRequest_Submit.

#### PlatformRuntime_API

* **Session_GetMobileAppLoginInfo**:  Replace with GetUserProfile.

This function returns a UserInfo structure containing information that identifies the user (Name, Email and PhotoURL) instead of the userId. Therefore, you need to change the logic of the app  so it's  compatible with the UserInfo structure.

#### RichMail

* **HttpBinaryGet**: Replace with Request_SubmitGetRequest (HTTP Library) and adapt the app logic to use BinaryContent returned.
* **HttpGet**: Replace with Request_SubmitGetRequest (HTTP Library) and change  the app logic to use TextContent returned.
* **RichMailAuthenticate,RichMailCreate, RichMailForward, RichMailPart, RichMailSend**: Replace this with [ODC email logic](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/emails/). The logic offered in this extension it's an outdated version of the current email logic available in ODC.

#### Sample_JWTUtils

* **Create Token**:  Replace with the ODC JWT_CreateToken. The signatures of the O11 and ODC actions are different, therefore, you need to change the logic to the signature of the new action. This transformation is only required if you are using a JSON Web Key (JWK).
* **ReadToken**: Replace with the ODC JWT_ReadToken. The signatures of the O11 and ODC actions are different, therefore, you need to change the logic to the signature of the new action. This transformation is only required if you are using a JSON Web Key (JWK).

## Functionality not available in ODC { #not-available }

### System extension actions incompatible with ODC Architecture

Following are extension actions that aren't available in ODC because they use logic that's no longer supported in ODC. You must revisit your code and adapt it to ODC architecture. The information is divided by the O11 extension name and lists the corresponding action name and why they can't be transformed.

#### AsynchronousLogging

The following action was deleted in ODC because **you can't log records** into the database:

* Logrecord

#### ECT_Controller

The following actions don’t exist in ODC because ODC doesn't support Embedded Change Technology (ECT):

* GetEnvironmentUID
* RemoveScreenFeedback

#### ECT_PageRetriever

The following actions don’t exist in ODC because ODC doesn't support Embedded Change Technology (ECT):

* BinaryToTextUTF8
* ComputeHash
* GetFramesFromRequest
* GetRequestCookieHeader
* RetrievePersistentWebPage
* TextToBinaryUTF8

#### EnhancedWebReferences

The following actions don’t exist in ODC because ODC doesn't support SOAP:

* ClearWebReferenceHeaders
* GetWebReferenceSoapHeaders
* GetWebServiceSoapHeaders
* SetWebReferenceCredencials
* SetWebReferenceProxy
* SetWebReferenceSoapHeaders
* SetWebReferenceURL
* SetWebServiceSoapHeaders

#### HtmlRenderer

The following actions don’t exist in ODC because they are connected only to ECT and Embedded Process Automation (EPA):

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

The following actions don’t exist in ODC because they apply only to O11 traditional web apps:

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

The following actions don’t exist in ODC since unlike O11, in ODC, extensions are executed out-of-process. Therefore, you can't access the request using extensions. You must analyze on a case-by-case basis and make the suitable changes. For instance, the usage of the GetIP action may be replaced with the IP Filtering feature accessible on the portal.

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

The following actions don’t exist in ODC because they apply only to O11 traditional web apps:

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

#### PlatformRuntime_API

* The action **Audit_CreateAuditLog** doesn’t exist in ODC as ODC doesn't log audit records.
* The actions **DatabaseConnection_SetConnectionStringForSession**, **Database_WriteInParallelTransaction** don’t exist in ODC as they don't apply to ODC architecture.
* The action **Request_GetKey** doesn’t exist in ODC since LogError and LogRequestEvent that use this action aren't available in ODC.
* The action **Session_GetWebAppLoginInfo** doesn’t exist in ODC as it applies only to O11 traditional web apps.

### System actions incompatible with ODC architecture

The following section provides details on system actions presented in alphabetical order that aren't available in ODC and why they can't be transformed. Therefore, you must revisit your code and adapt it to ODC architecture.

The following actions don’t exist in ODC because they don't apply to ODC architecture, as they are used only on on-prem environments:

* ClientCertificateGetDetails
* ClientCertificateValue

The following actions don’t exist in ODC because they are already deprecated in O11:

* Deprecated_Notify
* Deprecated_NotifyGetMessage
* Deprecated_NotifyWidget
* InboundSmsGetDetails

The following actions don’t exist in ODC because ODC doesn't currently support multi-tenant applications:

* TenantCreate
* TenantInvalidateCache
* TenantSwitch

### System entities not available in ODC { #system-entities }

Except the **User** system entity, which is available in ODC as a cache with a simpler field structure, and a limited set of workflow-related entities, all the remaining [O11 system entities](https://success.outsystems.com/documentation/how_to_guides/data/data_migration_from_production_to_non_production_environment/outsystems_platform_metamodel/) are no longer available in ODC.

For any dependency to a system entity that is not available in ODC, you need to remove the reference to that system entity and refactor your code to use ODC capabilities instead.
