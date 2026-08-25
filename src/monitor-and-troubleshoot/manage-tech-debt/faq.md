---
tags:
  - Infrastructure
  - IT Users
  - Mentor
  - Mentor Studio
  - Technical Debt
  - Troubleshooting
summary: OutSystems 11 (O11) Code Quality FAQs covering licensing, probe setup, data storage, GDPR consent, and LifeTime team filters.
locale: en-us
guid: d7db51a1-9917-4baa-a36e-716dc0c75d96
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - Developer
  - Platform administrator
  - Architect
outsystems-tools:
  - code quality
  - lifetime
coverage-type:
  - unblock
isautopublish: true
---

# Code Quality FAQs

<div class="info" markdown="1">

AI Mentor Studio is now Code Quality.

</div>

Find answers to frequently asked questions about Code Quality in the following sections.

## General

### Can I do code analysis in multiple development environments?

According to our licensing model one License, corresponding to one Activation Code, can have several environments but only one development environment.

In Code Quality, for each Activation Code, you are allowed to have one code analysis environment (usually the development environment). This means that:

* You can do code analysis on two different development environments if both have different Activation Codes. They will appear in Code Quality as two separate infrastructures.

* You can't have more than one code analysis environment (usually development environment) per installation, i.e, with the same activation code.

### Can I customize the technical debt analysis - defining which patterns to analyze and their weights, adding their own patterns?

No, this isn't currently planned.

### Are there APIs to integrate Code Quality with third-party tools?

Yes, you can use [Code Quality API](../../ref/apis/auto/ai-mentor-studio-api.final.md) to integrate technical debt data with other technical debt and BI tools you already use.

### Do I need to give access to the developers in LifeTime so they can associate their users with Code Quality?

All developers have access to LifeTime, therefore the customer isn't "giving access just to use Code Quality". The reason why all developers always have to access LifeTime is that it's where the IT users are set up.

The Code Quality Plugin doesn't require the user to have any particular permissions on LifeTime. So, any user that can login to LifeTime (all active users), can see and open Code Quality Plugin to associate their infrastructure user with Code Quality.

### Why can't I see any findings after selecting a specific team?

For the filter of teams to work it needs that the teams are created in LifeTime, and have Applications associated with them.

Go to LifeTime, and under the Menu **User Management** > **Teams** make sure the teams are correctly created, then, **for each team** (click on the team's name to enter that team's detail page) make sure the team has Users and Applications associated with it.

After all the changes are done you’ll have to wait for the next synchronization for the results to be updated.

### What should I do when I believe that a recommendation is wrong?

Snooze it with the "False Positive" reason and explain in the comments why you believe a specific case is wrong. The Code Quality team is actively monitoring recommendations marked as "False Positive" to decide and implement corrections where needed.

## Probes

### How do I check the current version of my Code Quality probes?

To check the version of your probes, click the **Help** icon on the top-right corner of Code Quality and then select **About Code Quality**.

### How do I know if the Code Quality probes need to be updated?

If an environment has outdated probes, Code Quality displays a warning message and users with [**Full Control** permissions assigned as a default role](how-works.md#update-probes) can update them autonomously. Users without Full Control permissions must contact their infrastructure administrator to update the Code Quality's probes.

Check out [how to update the Code Quality probes](how-update-probes.md).

If there's a previous version of the probes installed there's no need to uninstall them before installing the new version of the probes.

### How do I uninstall Code Quality probes?

To uninstall Code Quality probes, delete the following applications from both the LifeTime and code analysis environments:

* **Code Quality Environment Probe**
* **Code Quality LifeTime Probe**
* **Code Quality Shared**

<div class="info" markdown="1">

Uninstalling Code Quality probes won't unregister your infrastructure from Code Quality. Your infrastructure remains registered, although there are no more syncs between your infrastructure and Code Quality. If you want to unregister your infrastructure or make a new registration, [contact OutSystems Support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support).

</div>

### Can I change the target environment of a code analysis probe?

You can change the target environment, but before doing so contact [technical support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support) to delete existing data from Code Quality. Otherwise, data inconsistencies may occur. After data is deleted, follow the [setup procedure](how-setup.md) to configure a new target environment.

## Security, legal and compliance - registration in Code Quality {#data-faq}

### What information is sent to Code Quality, what information is stored, and how is it stored?

Code Quality collects the following data from the customer’s infrastructure:

* Platform metamodel data, including infrastructure activation code, environments information (name and Platform Server version), teams, list of apps and modules (including name and identifier), and platform configurations.

* Modules and dependency information for code analysis.

* Upon acceptance of the agreement, during Code Quality set up: users information (name, username, email address, user creation date, last login date) and LifeTime permissions.

* Optionally: Discovery snapshot data (architectural references, applications, and modules) for architecture analysis.

Data of each installation is kept in the OutSystems cloud and isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

### For how long is data kept in Code Quality?

Source information for code analysis (OutSystems modules) is kept only during the code analysis procedure and then it is deleted, only the byproducts of the code analysis (the technical debt findings and technical debt scores) are kept.

Technical debt information is currently stored without limitation until a customer exercises the right to have it removed from Code Quality.

OutSystems has the right to change this policy, conditions of access, as well as the nature, features, or functioning of the tool.

### How is this data used?

This data is used exclusively for the operation of Code Quality and to provide the reports and dashboards that the user can access and for nothing else. Aggregated, sanitized (anonymized) information can also be used for statistical purposes. Under no circumstances will specific personal or customer data be used for any other purposes besides the OutSystems platform usage.

### How does Code Quality handle sensitive data?

As explained previously, Code Quality doesn't deal with any sensitive data.

### What are the backup/restore procedures?

Code Quality follows the  same backup/restore procedures as other OutSystems cloud Customers, the procedure and timeframe can be found [here - OutSystems cloud access to database backup](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Access_the_database_of_your_PaaS/Temporary_Access_to_Database_Backup).

If a database restore is necessary, there will be some data loss. The synchronization processes between Code Quality and the registered infrastructure are executed based on synchronization timestamps. Therefore, all the changes since the last synchronization stored in Code Quality will be sent back and hence the technical debt information will be recreated accordingly.

## Security, legal and compliance - personal information {#personal-data-faq}

### When a user agrees to share personal information are they doing it on behalf of all users of that infrastructure?

No. Each user that wants to have access to Code Quality to manage the technical debt of their OutSystems infrastructure, will be required to give consent for OutSystems to collect the personal information that is described in the acceptance form, which includes name, username, and email address.

### Where is the personal information shared with Code Quality sent from?

Within the OutSystems platform, the LifeTime environment is the only one that connects and sends information to Code Quality.

As long as there has been prior consent, information about the user is sent to Code Quality on each synchronization to ensure information is updated.

### Is it possible to use Code Quality without giving consent to share personal information?

No.

### Will the users only see their findings in Code Quality or will they see all the findings? And in the latter case, will they be able to identify the users of those findings?

A user will see all the findings for an infrastructure they have access to. Nonetheless, only the findings of users of that infrastructure who gave consent to share their personal information will be identified by their username. All other findings will be anonymous.

### For how long will the user’s personal information be stored in Code Quality?

Personal information is stored until one of the following events occurs:

* The user requests to have its data erased from Code Quality.

* The OutSystems Customer requests that their infrastructure is removed from Code Quality.

* The OutSystems Customer withdraws its consent in any other way.

### If a user wants to exercise any right to access, correct, or erase their personal data, including obtaining information about what type of personal data is stored in Code Quality, what should the user do?

The user should read [OutSystems Privacy Policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/) and send an email with its request to [dpo@outsystems.com](mailto:dpo@outsystems.com).

### If a user wants to have their data erased from Code Quality, what should the user do?

Users can unsubscribe from Code Quality, at any time, by creating a ticket in the [Support Portal](https://www.outsystems.com/goto/submit-support-case).

### If an OutSystems Customer wants to prevent a developer from accessing Code Quality what should the user do?

When a user is deactivated in LifeTime, it will stop having access to that infrastructure in Code Quality once that information is synchronized from LifeTime to Code Quality. The user will regain access to Code Quality if the LifeTime user is reactivated.
In any case, unless the user requests to have its data erased from Code Quality, all of its  findings will continue to be identified and associated with the user.

## Disclaimers

### Registration disclaimer

Code Quality is a SaaS tool that enables developers, team leads, and architects to view and manage technical debt - improving the apps they develop by following development best practices for code quality and performance.

Access to Code Quality will be given upon request to all OutSystems Customers and Partners as long as they are running a supported version of the OutSystems platform.

OutSystems has the right to change these rules, conditions of access, as well as the nature, features, or functioning of the tool.
Code Quality collects the following data from the Customer’s infrastructure:

* Platform metamodel data, including infrastructure activation code, environments information (name and OutSystems platform version), teams, and OutSystems platform configurations;
* Applications, modules for code analysis;
* Discovery snapshot data (architectural references, applications, and modules) for architecture analysis;
* Upon acceptance of the Agreement: Users information (name, username, email address, last login date).

Data of each installation is kept isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

This data is used exclusively for the operation of the tool, and to provide the reports and dashboards that the user can access, and for nothing else. Aggregated, sanitized information can also be used for statistical purposes. Under no circumstances will specific personal or Customer data be used for any other purposes besides platform usage.

Should you have any questions or wish to exercise any rights regarding privacy/data protection laws, contact us at <dpo@outsystems.com>.

### GDPR consent form

By ticking this box, you agree and give your express consent to OutSystems to process your IT user data in these infrastructures (including name, username, email, creation date, and identifier) and your OutSystems account data (including name, username, email, creation date and identifier), to inform you about best practices you should be following regarding code and architecture in OutSystems. This personal information is only required for this purpose, and without it, OutSystems is not able to provide you the aforementioned service. We’ll keep your data while it’s needed to deliver the service, and for an additional two years in case you make any further queries. We’ll process such personal data according to our privacy policy. [Open the privacy policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/). You can unsubscribe from this Service at any time by creating a ticket on the support portal. [Open Support Portal](https://www.outsystems.com/goto/submit-support-case).
