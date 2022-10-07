---
tags: Workflow Builder; Case Management; OutSystems; Business Users; Citizen Developers; Citizen Dev; Workflow; FAQ; Business developers
summary: Frequently Asked Questions about Workflow Builder.
guid: d6e18346-5ecc-4178-9bf2-15e82ff891f6
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
---

# Workflow Builder FAQs

Find answers to frequently asked questions about [Workflow Builder](http://workflowbuilder.outsystems.com/) in the following sections.

## General

### How can I register users for a certain environment?

Workflow Builder always authenticates users against the target environment's Service Center users previously configured through LifeTime.

If new users need access to Workflow Builder, you need to add them through LifeTime. If they want to publish applications, you must grant them publishing permissions in that environment too.

### Can I configure different roles for users inside the Workflow Builder?

Yes. The first user registering in the Workflow Builder gets administrator access. This user can grant access to additional users after their first login to the Workflow Builder.

<div class="info" markdown="1">

You can configure accesses in LifeTime using a service account. You need to have administrator privileges on LifeTime to perform this operation.

</div>

All valid LifeTime users with access to the target environment can log in and use the Workflow Builder. However, if they don't have publishing permissions for that environment, they can't publish applications using Workflow Builder.

Refer to [How to set up the users Governance Model](how-setup-governance.md) for more information.

### Can I use my Personal Environment for testing purposes?

No, you can use Workflow Builder using the **Basic**, **Standard**, or **Enterprise** OutSystems editions only. Refer to the [Workflow Builder prerequisites](how-setup.md).

### Can I use Outsystems Entities as a form field on all supported platform versions?

No, to use OutSystems Entities, your development environment must use Platform Server 11.9 (July 2020). Refer to the [Workflow Builder prerequisites](how-setup.md).

## Security, legal and compliance - registration in Workflow Builder {#data-faq}

### What information is sent to Workflow Builder, what information is stored, and how is it stored?

Workflow Builder collects the following data from the customer’s infrastructure (only):

* Connected environment URL and Activation Code.

* Workflow Builder components installed and their respective versions - this information is not stored on Workflow Builder and it is used for validation purposes.

* Upon acceptance of the Agreement: IT User information (username, permissions).

Data of each installation is kept in the OutSystems cloud and isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

### For how long is data kept in Workflow Builder?

Connected environment URL and Activation Code are currently stored until the Customer exercises the right to have it removed from Workflow Builder.

OutSystems has the right to change this policy, conditions of access, as well as the nature, features, or functioning of the tool.

### How is this data used?

Data is used exclusively for the operation of Workflow Builder. Aggregated, sanitized (anonymized) information can also be used for statistical purposes. Under no circumstances will personal or Customer data be used for any other purposes besides the OutSystems platform usage.

### Does Workflow Builder have access or processes sensitive data?

Workflow Builder does not have access or process sensitive data.

### What are the backup/restore procedures?

Workflow Builder follows the same backup/restore procedures as other OutSystems cloud Customers. Procedure and timeframes can be found [here - OutSystems cloud access to database backup](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Access_the_database_of_your_OutSystems_Cloud/Temporary_OutSystems_Cloud_database_backup).

In the event that a database restore is necessary, there will be some data loss.

## Security, legal and compliance - personal information {#personal-data-faq}

### When a user agrees to share personal data are they doing it on behalf of all users of that infrastructure?

No. Each user will be required to give consent to OutSystems for the collection of the personal data, that is described in the acceptance form, which only includes name, username and email address.

### Is it possible to use Workflow Builder without giving consent to share the personal information?

No.

### Will Workflow Builder users only see their applications in Workflow Builder or will they see all applications developed in the same environment?

Applications created in the Customer’s infrastructure with Service Studio will not be visible in Workflow Builder. Applications created with Workflow Builder will be visible to all Workflow Builder users in that infrastructure (including Service Studio).

### For how long will the user’s personal data be stored in Workflow Builder?

Personal data is stored until one of the following events occur:

* The user requests to have its data erased from Workflow Builder.

* The OutSystems Customer requests that their infrastructure is removed from Workflow Builder.

* The OutSystems Customer withdraws its consent in any other way by opening a ticket on the [Support Portal](https://www.outsystems.com/goto/submit-support-case).

### If a user wants to exercise any right to access, correct or erase its personal data, including obtaining information about what type of personal data is stored in Workflow Builder, what should the user do?

The user should read [OutSystems Privacy Policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/) and send an email with its request to [dpo@outsystems.com](mailto:dpo@outsystems.com).

### If a user wants to have its data erased from Workflow Builder, what should the user do?

Users can unsubscribe from Workflow Builder, at any time, by creating a ticket in the [Support Portal](https://www.outsystems.com/goto/submit-support-case).

### If an OutSystems Customer wants to prevent a developer from accessing Workflow Builder what should the user do?

When a user is deactivated in LifeTime, it will stop having access to that infrastructure in Workflow Builder once that information is synchronized from LifeTime to Workflow Builder. The user will regain access to Workflow Builder if the LifeTime user is reactivated. 
In any case, unless the user requests to have its data erased from Workflow Builder, all of its  findings will continue to be identified associated with the user.

## Disclaimers

### Registration disclaimer

Workflow Builder is a SaaS tool that enables developers, business users to develop applications through an easy to use tool that interfaces between the user and OutSystems platform, following development best practices.

Access to Workflow Builder will be given upon registration to all OutSystems Customers and Partners as long as they are running a supported version of the OutSystems platform.

OutSystems has the right to change these rules, conditions of access, as well as the nature, features, or functioning of the tool.

Workflow Builder collects the following data from the Customer’s infrastructure:

* Connected environment URL and Activation Code;

* Workflow Builder components installed and their respective versions - this information is not stored on Workflow Builder it is used for validation purposes;

* From the all users that connect to a specific environment collects: username and permissions on the target environment.

Data of each installation is kept isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

This data is used exclusively for the operation of Workflow Builder. Aggregated, sanitized (anonymized) information can also be used for statistical purposes. Under no circumstances will personal or customer data be used for any other purposes besides the OutSystems platform usage.

By clicking accept and continue, you agree and give your express consent to OutSystems to process your user data in these infrastructures (Only username) to provide you the ability to set up connectivity between OutSystems infrastructure and external systems. This personal information is only required for this purpose, and without it OutSystems is not able to provide you the aforementioned service. We’ll keep your data while it’s needed to deliver the service or until the customer exercises the right to have it removed from Workflow Builder. We’ll process such personal data according to our privacy policy. [Open the privacy policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/). You can unsubscribe this Service at any time by creating a ticket on the support portal. [Open Support Portal](https://www.outsystems.com/goto/submit-support-case).

Should you have any questions or wish to exercise any rights pursuant to privacy/data protection laws, contact us at [dpo@outsystems.com](mailto:dpo@outsystems.com).

### GDPR consent form

By clicking accept and continue, you agree and give your express consent to OutSystems to process your user data in these infrastructures (Only username) to provide you the ability to set up connectivity between OutSystems infrastructure and external systems. This personal information is only required for this purpose, and without it OutSystems is not able to provide you the aforementioned service. We’ll keep your data while it’s needed to deliver the service or until the customer exercises the right to have it removed from Workflow Builder. We’ll process such personal data according to our privacy policy. [Open the privacy policy](https://www.outsystems.com/legal/terms-of-use/privacy-statement/). You can unsubscribe this Service at any time by creating a ticket on the support portal. [Open Support Portal](https://www.outsystems.com/goto/submit-support-case).

Should you have any questions or wish to exercise any rights pursuant to privacy/data protection laws, contact us at [dpo@outsystems.com](mailto:dpo@outsystems.com).
