---
tags: outsystems, outsystems platform, security, application development, access control
summary: Learn how to enable access control in OutSystems 11 (O11) for case definitions within the Case Management framework.
guid: 6b9969e1-6771-4e7a-9c5b-d639b0d08d62
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=4376:1914
audience:
  - backend developers
  - full stack developers
  - tech leads
  - architects
  - platform administrators
outsystems-tools:
  - service studio
  - case management framework
coverage-type:
  - apply
---

# How to enable access control

In the Case Management framework, access control is managed at the case definition level.

Before granting access to a single case instance or to all instances of a case definition, you must start by enabling access control for that case definition.

If your case management app includes more than one case definition, you must enable access control for each of the case definitions that you want to restrict access to.

To enable access control for a case definition, follow these steps:

1. In the **&lt;business-entity&gt;_CS** module, go to the **Logic** tab, and open the **Bootstrap_CaseConfiguration** action flow.

    <div class="info" markdown="1">

    The &lt;business-entity&gt;_CS module is the module that contains the case definition for which you want to enable access control, where &lt;business-entity&gt; is the name of the business entity associated with that case definition.

    </div>

1. In the action flow select the **Assign** and set the **HasAccessControl** to `True`.

    ![Screenshot showing the process of setting HasAccessControl to True in the Bootstrap_CaseConfiguration action flow](images/enable-access-con-ss.png "Enabling Access Control")

1. Publish the module by selecting **1-Click Publish**.

After publishing the app, the Bootstrap_CaseConfiguration timer runs, updating the configuration of the case definition and enabling access control for all case instances of that case definition. After enabling access control for a case definition, when using the [Case Management framework actions take access rights into account to interact with that case definition](permission-actions-ac.md).
