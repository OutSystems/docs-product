---
tags: Case Management; Case Management framework; Subcase.
summary: Learn about subcases.
guid: 7a4bf141-060b-4cd8-bf99-a381f4e37d73
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Subcases introduction

A subcase is a case by itself that is linked to a main parent case. Subcases are triggered from the context of the parent case. You can use subcases when you need to ensure that end-users complete a complex set of steps that are abstracted from a parent case. For example, a parent case to review support tickets may lead to a subcase to handle an operation or service requested by the customer. To close the support ticket parent case, the service subcase must be resolved first.

A subcase can also be a parent case for other subcases.

The relationship between cases exists in the **CaseRelation** entity in the **CM_Case_CS** module. This entity also contains information about the top case in a case hierarchy.

The creation of a subcase instance is logged in the history of the parent case.

The parent case and the subcases run in different instances, so you need to query the subcase from the process of the parent case to know the status of the subcase. This is achieved by adding a **Wait** node to the parent’s Business Process Technology (BPT) flow. Then setting a timeout value that is relevant to your use case (if the subcase is expected to take a while to complete, add a higher value) and finally adding an **On Close** callback action to it.

For the full procedure on creating subcases, go to our [Creating a case management app with subcases article here](subcase.md#create-subcase).
