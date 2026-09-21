---
summary: 'LDAP filter injection warning in OutSystems 11 (O11): encode end-user values with LdapFilterEncode to avoid LDAP injection in LDAP_Search and LDAP_Login filters.'
helpids: 30786
locale: en-us
guid: 07c40401-46c4-4f16-a535-fa7aecbc6b11
topic:
  - fix-ldap-injection-warning
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags:
  - LDAP
  - OWASP
  - Security
  - Troubleshooting
audience:
  - Developer
  - Front-end developer
outsystems-tools:
  - service studio
coverage-type:
  - unblock
isautopublish: true
---

# LDAP filter injection warning

Message
:   `Ensure the value used to build the <LDAP action> Filter is protected by using LdapFilterEncode(), to avoid LDAP injection vulnerabilities.`

Cause
:   The **Filter** argument of the LDAP action (LDAP_Search, LDAP_Search_WithAuthenticationType, or LDAP_Login) might be unsafe.

This warning is shown when at least one part of the **Filter** expression is possibly unsafe on its own. A part is safe when it is one of the following:

* A hardcoded literal.
* A non-text value converted to text with a [data conversion function](<../../lang/auto/builtinfunction-data-conversion.md>), such as `IntegerToText()`.
* The output of the **LdapFilterEncode** action.

Recommendation
:   If any part of your **Filter** argument isn't encoded yet, use the **LdapFilterEncode** action to encode it (also available in the Authentication extension). To encode the possibly unsafe parts (such as user input) from which you build the filter, pass those parts into the **SearchFilter** input parameter of **LdapFilterEncode**, then use the **EscapedSearchFilter** output to build the **Filter** argument of the LDAP action you are using. For example: `"(uid=" + LdapFilterEncode.EscapedSearchFilter + ")"`.

Keep the following in mind
:

    * Only encode the parts of the filter that are built dynamically. Static parts of the filter, such as a template configured by you or an administrator, don't need encoding.
    * Encode each value separately before you assemble the filter. Don't encode the complete filter, because that also encodes the structural characters of the LDAP filter and makes the filter invalid.
    * Encode each value only once. Encoding a value that has already been encoded changes it again and can corrupt the filter.
