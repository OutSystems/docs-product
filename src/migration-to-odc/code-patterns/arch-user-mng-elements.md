---
guid: 8dba8e8c-d3aa-4c9b-8a0f-16c7aa608aca
locale: en-us
summary: This article provides guidelines for refactoring your user management strategy to ensure compatibility with OutSystems Developer Cloud (ODC).
figma: 
coverage-type:
  - unblock
  - understand
topic: 
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - full stack developers
  - mobile developers
  - frontend developers
tags: cloud-native applications,system entities,api development,data integration,platform version migration
outsystems-tools:
  - service studio
helpids: 30629
---

# Asset consuming O11 user management elements

In ODC, [user management and authentication](https://success.outsystems.com/documentation/outsystems_developer_cloud/user_management/) is different [from O11](../../user-management/intro.md). Sitting in a modern architecture, the entire user management premises were redesigned in ODC to address modern challenges.

## How to solve

You must solve this pattern in ODC, after proceeding with the code migration to ODC.

### Solve in ODC

After migrating your apps, you need to redesign how your applications support user management and authentication:

* Adjust your user management logic to [comply with ODC architecture](#changes).

* If you have access to the Migration Kit, [adapt the login and logout flows of your migrated apps](https://success.outsystems.com/documentation/11/outsystems_11_to_odc_migration/execute_one_shot_migration/adapt_login_and_logout_flow_of_migrated_apps/) to ODC.

## User management functionality changes in ODC { #changes }

This section describes the user management functionality that changed in ODC due to its different architecture when compared to O11.

### User entity available in ODC with changes { #user-entity }

In ODC, system entities are read-only views with no entity actions available. The **User** system entity is available as a cache with a simpler field structure when compared to the O11 User entity. If there's a dependency to this entity, check that your code works properly, as some O11 attributes aren't available in ODC.

All the remaining [O11 user management system entities](https://success.outsystems.com/documentation/how_to_guides/data/data_migration_from_production_to_non_production_environment/application_users_groups_and_roles/) are no longer available in ODC.

### User management functionality not available in ODC { #not-available }

Following are O11 user management system actions, extensions and APIs that aren't available in ODC because they are incompatible with ODC architecture. 

#### System actions incompatible with ODC architecture

The following actions don’t exist in ODC because ODC doesn't support integrated authentication:

* IntegratedSecurityCheckRole
* IntegratedSecurityGetDetails

The following action doesn’t exist in ODC because the login logic is different in ODC:

* LoginPassword

#### Authentication

The following actions don’t exist in ODC because ODC doesn't support **windows accounts querying**:

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

#### PlatformPasswordUtils

The following actions don’t exist in ODC because ODC doesn't manage passwords:

* GenerateSaltedMD5Hash
* GenerateSaltedSHA512Hash
* ValidatePassword

#### SAMLAuthentication

The following actions don’t exist in ODC because ODC doesn't support SAML authentication:

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

#### Users

User management and authentication in ODC doesn’t map directly to the functionality provided by the [O11 Users API](../../ref/apis/auto/users-api.final.md) due to its different architecture.

Refer to the [user management API](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/#user-and-access-management) to evaluate how to achieve some user and access management functionality in ODC.

#### UsersLocalManagement

The following actions don’t exist in ODC because their logic is incompatible with ODC architecture:

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

Refer to the [user management API](https://success.outsystems.com/documentation/outsystems_developer_cloud/odc_rest_apis/#user-and-access-management) to evaluate how to achieve some user and access management functionality in ODC.
