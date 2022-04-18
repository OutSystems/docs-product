---
tags:
summary: Find answers to frequently asked questions about Architecture Dashboard in the following sections.
locale: en-us
guid: d7db51a1-9917-4baa-a36e-716dc0c75d96
app_type: traditional web apps, mobile apps, reactive web apps
---


# Architecture Dashboard FAQs

Find answers to frequently asked questions about Architecture Dashboard in the following sections.

## General

### Can I do code analysis in multiple development environments?

According to our licensing model one License, corresponding to one Activation Code, can have several environments but only one development environment.

In Architecture Dashboard, for each Activation Code, you are allowed to have one code analysis environment (usually the development environment). This means that:

* You can do code analysis on two different development environments if both have different Activation Codes. They will appear in Architecture Dashboard as two separate infrastructures.

* You can't have more than one code analysis environment (usually development environment) per installation, i.e, with the same activation code.

### Can I customize the technical debt analysis - defining which patterns to analyze and their weights, adding their own patterns?

No, this isn't currently planned.

### Are there APIs to integrate Architecture Dashboard with deployment processes (LifeTime or external CI/CD)?

No, this isn't currently planned.

### Do I need to give access to the developers in LifeTime so they can associate their users with Architecture Dashboard?

All developers have access to LifeTime, therefore the customer isn't "giving access just to use Architecture Dashboard". The reason why all developers always have to access LifeTime is that it's where the IT users are set up.

The Architecture Dashboard Plugin doesn't require the user to have any particular permissions on LifeTime. So, any user that can login to LifeTime (all active users), can see and open Architecture Dashboard Plugin to associate his infrastructure user with Architecture Dashboard.

### Why can't I see any findings after selecting a specific team?

For the filter of teams to work it needs that the teams are created in Lifetime, and have Applications associated with them.

Go to Lifetime, and under the Menu **User Management** > **Teams** make sure the teams are correctly created, then, **for each team** (click on the team's name to enter that team's detail page) make sure the team has Users and Applications associated with it.

After all the changes are done you’ll have to wait for the next synchronization for the results to be updated.

### What should I do when I believe that a recommendation is wrong?

Snooze it with the "False Positive" reason and explain in the comments why you believe a specific case is wrong. The Architecture Dashboard team is actively monitoring recommendations marked as "False Positive" to decide and implement corrections where needed.

## Probes

### How do I know if I need to update the Architecture Dashboard Probes?

If an environment has outdated probes, users with Full Control of the code analysis environment can update it autonomously see a warning message in Architecture Dashboard with a link to download the latest version.

![](images/probes-update-message-ad.png)

Check out [how to update the Architecture Dashboard probes](how-update-probes.md).

If there's a previous version of the probes installed there's no need to uninstall them prior to installing the new version of the probes.

### How do I uninstall Architecture Dashboard Probes?

Removing the probes from the infrastructure (both LifeTime and code analysis environments) is the only necessary step to uninstall Architecture Dashboard. Delete the following applications from both environments:

* **Architecture Dashboard Environment Probe**
* **Architecture Dashboard LifeTime Probe**
* **Architecture Dashboard Shared**

By doing this, the LifeTime Plugin is removed and the infrastructure will be deactivated on Architecture Dashboard, revoking the user's access.

### Can I change the target environment of a code analysis probe?

You can change the target environment, but before doing so contact [technical support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support) to delete existinig data from Architecture Dashboard. Otherwise, data inconsistencies may occur. After data is deleted, follow the [setup procedure](how-setup.md) to configure a new target environment. 


## Security, legal and compliance - registration in Architecture Dashboard {#data-faq}

### What information is sent to Architecture Dashboard, what information is stored, and how is it stored?

Architecture Dashboard collects the following data from the customer’s infrastructure:

* Platform metamodel data, including infrastructure activation code, environments information (name and Platform Server version), teams, list of apps and modules (including name and identifier), and platform configurations.

* Modules and dependency information for code analysis.

* Upon acceptance of the agreement, during Architecture Dashboard set up: users information (name, username, email address, user creation date, last login date) and LifeTime permissions.

* Optionally: Discovery snapshot data (architectural references, applications, and modules) for architecture analysis.

Data of each installation is kept in the OutSystems cloud and isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

### For how long is data kept in Architecture Dashboard?

Source information for code analysis (OutSystems modules) is kept only during the code analysis procedure and then it is deleted, only the byproducts of the code analysis (the technical debt findings and technical debt scores) are kept.

Technical debt information is currently stored without limitation until a customer exercises the right to have it removed from Architecture Dashboard.

OutSystems has the right to change this policy, conditions of access, as well as the nature, features, or functioning of the tool.

### How is this data used?

This data is used exclusively for the operation of Architecture Dashboard and to provide the reports and dashboards that the user can access, and for nothing else. Aggregated, sanitized (anonymized) information can also be used for statistical purposes. Under no circumstances will specific personal or customer data be used for any other purposes besides the OutSystems platform usage.

### How does Architecture Dashboard handle sensitive data?

As explained previously, Architecture Dashboard doesn't deal with any sensitive data.

### What are the backup/restore procedures?

Architecture Dashboard follows the  same backup/restore procedures as other OutSystems cloud Customers, the procedure and timeframe can be found [here - OutSystems cloud access to database backup](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Access_the_database_of_your_PaaS/Temporary_Access_to_Database_Backup).

In the event that a database restore is necessary, there will be some data loss. The synchronization processes between Architecture Dashboard and the registered infrastructure are executed based on synchronization timestamps. Therefore, all the changes since the last synchronization stored in Architecture Dashboard will be sent back and hence the technical debt information will be recreated accordingly.
 
## Security, legal and compliance - personal information {#personal-data-faq}

### When a user agrees to share personal information is he doing it on behalf of all users of that infrastructure?

No. Each user that wants to have access to Architecture Dashboard to manage the technical debt of their OutSystems infrastructure, will be required to give consent for OutSystems to collect the personal information that is described in the acceptance form, which includes name, username, and email address.

### Where is the personal information shared with Architecture Dashboard sent from?

Within the OutSystems platform, the LifeTime environment is the only one that connects and sends information to Architecture Dashboard.

As long as there has been prior consent, information about the user is sent to Architecture Dashboard on each synchronization to ensure information is updated.

### Is it possible to use Architecture Dashboard without giving consent to share the personal information?

No.

### Will the users only see their findings in Architecture Dashboard or will they see all the findings? And in the latter case, will they be able to identify the users of those findings?

A user will see all the findings for an infrastructure they have access to. Nonetheless, only the findings of users of that infrastructure that gave consent to share their personal information will be identified by their username. All other findings will be anonymous.

### For how long will the user’s personal information be stored in Architecture Dashboard?

Personal information is stored until one of the following events occur:

* The user requests to have its data erased from Architecture Dashboard.

* The OutSystems Customer requests that their infrastructure is removed from Architecture Dashboard.

* The OutSystems Customer withdraws its consent in any other way.

### If a user wants to exercise any right to access, correct or erase its personal data, including obtaining information about what type of personal data is stored in Architecture Dashboard, what should the user do?

The user should read [OutSystems Privacy Policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/) and send an email with its request to [dpo@outsystems.com](mailto:dpo@outsystems.com).

### If a user wants to have its data erased from Architecture Dashboard, what should the user do?

Users can unsubscribe from Architecture Dashboard, at any time, by creating a ticket in the [Support Portal](https://www.outsystems.com/goto/submit-support-case).

### If an OutSystems Customer wants to prevent a developer from accessing Architecture Dashboard what should the user do?

When a user is deactivated in LifeTime, it will stop having access to that infrastructure in Architecture Dashboard once that information is synchronized from LifeTime to Architecture Dashboard. The user will regain access to Architecture Dashboard if the LifeTime user is reactivated. 
In any case, unless the user requests to have its data erased from Architecture Dashboard, all of its  findings will continue to be identified associated with the user.

## Disclaimers

### Registration disclaimer

Architecture Dashboard is a SaaS tool that enables developers, team leads, and architects to view and manage technical debt - improving the apps they develop by following development best practices for code quality and performance.

Access to Architecture Dashboard will be given upon request to all OutSystems Customers and Partners as long as they are running a supported version of the OutSystems platform.

OutSystems has the right to change these rules, conditions of access, as well as the nature, features, or functioning of the tool.
Architecture Dashboard collects the following data from the Customer’s infrastructure:

* Platform metamodel data, including infrastructure activation code, environments information (name and OutSystems platform version), teams and OutSystems platform configurations;
* Applications, modules for code analysis;
* Discovery snapshot data (architectural references, applications, and modules) for architecture analysis;
* Upon acceptance of the Agreement: Users information (name, username, email address, last login date).

Data of each installation is kept isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

This data is used exclusively for the operation of the tool, and to provide the reports and dashboards that the user can access, and for nothing else. Aggregated, sanitized information can also be used for statistical purposes. Under no circumstances will specific personal or Customer data be used for any other purposes besides platform usage.
 
Should you have any questions or wish to exercise any rights pursuant to privacy/data protection laws, contact us at dpo@outsystems.com.
 
### GDPR consent form

By ticking this box, you agree and give your express consent to OutSystems to process your IT user data in these infrastructures (including name, username, email, creation date and identifier) and your OutSystems account data (including name, username, email, creation date and identifier), to inform you about best practices you should be following regarding code and architecture in OutSystems. This personal information is only required for this purpose, and without it OutSystems is not able to provide you the aforementioned service. We’ll keep your data while it’s needed to deliver the service, and for an additional two years in case you make any further queries. We’ll process such personal data according to our privacy policy. [Open the privacy policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/). You can unsubscribe this Service at any time by creating a ticket on the support portal. [Open Support Portal](https://www.outsystems.com/goto/submit-support-case).
