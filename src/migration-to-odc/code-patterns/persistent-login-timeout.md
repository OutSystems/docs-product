---
guid: ab121785-da19-482f-8e76-cb6eba34e7d8
locale: en-us
summary: Learn the recommendations for aligning the persistent login duration between O11 and ODC.
figma:
coverage-type:
  - unblock
topic:
  - authentication-mechanisms
app_type: reactive web apps,mobile apps
platform-version: o11
audience:
  - backend developers
  - full stack developers
  - architects
  - tech leads
tags: persistent login, session timeout, access tokens, single sign-on, security enhancement
outsystems-tools:
  - service center
  - service studio
helpids:
---

# Align persistent login timeout

In ODC’s [authorization mechanism](https://www.outsystems.com/tk/redirect?g=5f50a67f-d8c9-444a-9615-090062255870), access tokens have a maximum lifespan of 12 hours. Thus, the session timeout in ODC is set to 12 hours and is not customizable. This 12-hour limit enhances security by regularly re-authenticating users, reducing the window of opportunity for unauthorized access.

In O11, Reactive Web and Mobile apps have a default [persistent login](../../user-management/end-user-manage/end-user-authentication/persistent-login.md) session duration of 30 days. This duration is customizable. However, note that increasing the persistent login session duration can reduce security.

## Recommendations

If your O11 Reactive Web and Mobile apps have a persistent login duration different than 12 hours, consider aligning that duration to the ODC's 12-hour limit to ensure compatibility and a smooth transition to ODC. This is especially important if you plan to have single sign-on (SSO) between ODC and O11 apps.

Make this change in a non-production O11 environment and test your apps to ensure they work as expected. Aligning session timeout behavior with ODC's 12-hour limit will help identify and address any potential app logic adjustments needed for a shorter session. If everything works as expected, propagate that change into the O11 production environment and validate it in production before converting to ODC.