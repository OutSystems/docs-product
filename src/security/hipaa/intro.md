---
summary: OutSystems 11 (O11) facilitates HIPAA compliance by enabling secure healthcare application development and deployment across various platforms.
tags: healthcare application development, hipaa compliance
locale: en-us
guid: 13c94c45-4142-48f8-a06b-733675577c1e
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/vTtFn5nl44ZLjUBYo2anCO/Security?node-id=210:728
audience:
  - full stack developers
  - platform administrators
  - architects
outsystems-tools:
  - service studio
coverage-type:
  - understand
---

# HIPAA compliance - how OutSystems can help

## Introduction

This document describes how OutSystems can help you develop and secure your healthcare applications and data while complying with HIPAA security and privacy requirements.

### About OutSystems

OutSystems dramatically accelerates the development of secure applications, and their deployment in a secure runtime environment. OutSystems’ built-in application lifecycle management capabilities promote a clear assignment of responsibilities in the DevOps processes, laying the foundation for a secure Software Development Lifecycle.

OutSystems was designed for several deployment models, including third-party cloud vendors and on-premises. Regardless of deployment model, the OutSystems architecture ensures the same functionality is available to developers.

### How OutSystems helps healthcare providers

OutSystems empowers healthcare providers to move to a patient-centric model by giving them the ability to rapidly build patient-facing apps for purposes such as researching their prescribed drugs, evaluating their treatment options, accessing and controlling their medical information, and more. Applications can be pushed across any platform for any device on a single code base that’s secure and HIPAA compliant.

## HIPAA compliance

OutSystems applications dealing with protected health information may be subject to compliance with HIPAA.
Medical records and other personal health information that both:

* Identifies an individual
* Is maintained or exchanged electronically or in hard copy (for example, photocopied or printed from the database)

HIPAA considers such personally identifiable information protected if it's possessed by a covered entity or business associate. 

The US Department of Health and Human Services (HHS) issued the HIPAA Privacy Rule to implement the requirements of HIPAA. The HIPAA Security Rule protects a subset of information covered by the Privacy Rule. More information is available [here](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html#:~:text=The%20Security%20Rule%20protects%20a,%22%20(e%2DPHI).). 


### What do I have to do to be HIPAA compliant? 

<div class="info" markdown="1">

This is an overview that doesn't replace the Health Insurance Portability and Accountability Act of 1996 (HIPAA).
Customers are required to be aware and up-to-date on [Health Information Privacy](https://www.hhs.gov/hipaa/index.html).

</div>

The Privacy Rule standards address the use and disclosure of individuals’ health information (known as “protected health information”) by entities subject to the Privacy Rule. These individuals and organizations are called “covered entities”. The Privacy Rule also contains standards for individuals’ rights to understand and control how their health information is used.

While the HIPAA Privacy Rule safeguards protected health information (PHI), the Security Rule protects a subset of information covered by the Privacy Rule. This subset is all individually identifiable health information a covered entity creates, receives, maintains, or transmits in electronic form. This information is called “electronic protected health information” (ePHI). 

HIPAA safeguards can result in a HIPAA violation when the standards of the HIPAA Security Rule aren’t properly followed. In order to maintain compliance with the HIPAA Security Rule, covered entities must have proper Physical, Administrative, and Technical safeguards in place to keep PHI and ePHI secure.

Read more about HIPAA in the [Health Insurance Portability and Accountability Act of 1996 (HIPAA) from CDC](https://www.cdc.gov/phlp/publications/topic/hipaa.html).

We provide you with the proper tools and documentation to comply with HIPAA regulations while using OutSystems and foster the development of enterprise web and mobile applications.

### HIPAA-compliant hosting options for the OutSystems platform

OutSystems gives you the flexibility to manage and host your HIPAA-compliant apps. Read more about [how OutSystems supports HIPAA compliance](https://www.outsystems.com/evaluation-guide/security/certifications/).

![Diagram illustrating the OutSystems platform's HIPAA-compliant hosting architecture, including customer applications, OutSystems platform layers, and infrastructure components.](images/HIPAA.png "OutSystems HIPAA-Compliant Hosting Architecture")

Check next the [Checklist of HIPAA safeguards](hipaa-tech-safeguards.md).

### HIPAA compliant apps in the OutSystems Cloud { #hipaa-cloud }


The OutSystems Cloud HIPAA offering is available for OutSystems Sentry and provides you:

* A Business Associate Agreement (BAA) certifying that your OutSystems Cloud is compliant with HIPAA requirement.
* Access to the **Cryptographic Services** app so that you can protect all sensitive data. You can build, deploy, and use business applications that utilize Protected Health Information (PHI). 
* Attestation by an independent auditor that OutSystems technology, Cloud, policies and procedures ensure that PHI is handled correctly even in the unlikely event of a data breach. Check more at [OutSystems Compliance Portal](https://security.outsystems.com/).

Contact your account manager to subscribe. 
You can check if you're on the OutSystems Cloud HIPAA offering by looking for the **Cryptography Services** app in your environments. If it's not there, contact support or your account manager.
