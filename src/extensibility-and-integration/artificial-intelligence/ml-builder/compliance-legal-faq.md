---
summary: Frequently asked questions about security and legal matters.
tags:
---

# Security, Legal and Compliance FAQ

This document contains information about how ML Builder handles data.

<div class="info" markdown="1">

ML Builder is currently in a public **early access program (EAP)** and you need to register at the [ML Builder registration page](https://www.outsystems.com/eap-ml-builder/) to try it out.

</div>

## Registration in ML Builder

1. What is ML Builder?

    ML Builder empowers customers to easily automate processes and create rich personalized experiences using Machine Learning models trained with their own data and accessible to all developers.

2. What information is sent to ML Builder, what information is stored, and how is it stored?

    ML Builder collects the following data from the customer's infrastructure:

    * Connected environment URL and Activation Code.
    * Upon acceptance of the Agreement: IT User information (username).
    * AI provider connection and authorization keys.
    * ML Builder plugin installed and its respective version.
    * The machine learning models and their metadata (including entity and attributes labels) will be stored and kept by ML Builder.
    * Calls to the deployed ML models will be sent to the AI provider, via ML Builder, in a synchronous process. No request data is stored.
    * Temporarily, the ML Builder will store the data from the Customer's infrastructure. Only data selected by the user will be transferred. It will be deleted after successfully transferred to the AI provider.

    All Data is kept in the OutSystems cloud and isolated from all other customers using the platform's multi-tenant mechanisms. This ensures such data from one customer is not accessible by users of other customers.

3. For how long is data kept in ML Builder?

    Connected environment URL, Activation Code and machine learning model information are currently stored without limitation until a customer requests to have it removed from ML Builder.

    OutSystems reserves the right to change these conditions of access, as well as the nature, features, or functioning of the tool.

4. How is this data used?

    Data required to train the machine learning model will be sent and stored in the AI provider, following its own security and compliance practices ([Find here the link to the security report and compliance of Microsoft Azure](https://servicetrust.microsoft.com/ViewPage/MSComplianceGuideV3?docTab%3D7027ead0-3d6b-11e9-b9e1-290b1eb4cdeb_SOC_/_SSAE_16_Reports)). This may include PII data, if selected by the user.

    All the remaining data is used exclusively for the operation of ML Builder.

    Aggregated, sanitized (anonymized) information can also be used for statistical purposes and for the improvement of our services.

5. What are the backup/restore procedures?

    ML Builder follows the same backup/restore procedures as other OutSystems cloud Customers. Procedure and timeframes can be found [here - OutSystems cloud access to database backup](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Access_the_database_of_your_PaaS/Temporary_Access_to_Database_Backup).

    Regarding data stored in the AI provider, it follows its own security and compliance practices ([Find here the link to the security report and compliance of Microsoft Azure](https://servicetrust.microsoft.com/ViewPage/MSComplianceGuideV3?docTab%3D7027ead0-3d6b-11e9-b9e1-290b1eb4cdeb_SOC_/_SSAE_16_Reports)).

## Personal Information

1. What personal data does ML Builder use?

    ML Builder does not use personal data. However, Data required to train the machine learning model will be temporarily stored, to be sent and stored in the AI provider.This may include PII data, if selected by the user[b].

2. When a user agrees to share personal data is he doing it on behalf of all users of that infrastructure?

    No. Each user will be required to give consent to OutSystems for the collection of the personal data that is described in the acceptance form, which may include username and email address.

3. For how long will the user's data be stored in ML Builder?

    Information is stored until one of the following events occur:

    * The user requests to have its data erased from ML Builder. 
    * The OutSystems Customer requests that their infrastructure is removed from ML Builder.
    * The OutSystems Customer withdraws its consent in any other way by opening a ticket on the [Support Portal](https://www.outsystems.com/goto/submit-support-case).


4. If an OutSystems Customer wants to prevent a developer from accessing ML Builder what should the user do?

    When a user is deactivated in LifeTime, it will stop having access to that infrastructure in ML Builder. The user will regain access to ML Builder if the LifeTime user is reactivated.

    In any case, unless the user requests to have its data erased from ML Builder, all of its machine learning models will continue to be identified associated with the user.