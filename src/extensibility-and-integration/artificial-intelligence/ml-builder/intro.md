---
summary: An introduction to ML Builder, a machine learning tool to create predictive capabilities into your apps.
tags:
---

# Early Access Program - ML Builder

<div class="info" markdown="1">

The early access program for ML Builder is now closed. Thank you very much for your interest.

</div>

The OutSystems ML Builder cloud tool has machine learning features that allow you to build predictive capabilities into your apps. ML Builder guides you through the process of connecting your data and training a machine learning model. When your model is ready, ML Builder exposes server actions that allow you to apply the model's logic to your OutSystems app. You can also create back-ends for administrators and sophisticated UI experiences for users. Additionally, you can further expose predictive capabilities through a REST API.

ML Builder is designed for OutSystems developers who only need a basic knowledge of machine learning concepts.

The following graphic shows how ML Builder works and how you integrate the model predictions into an app.

![ML Builder overview](images/overview-diag.png?width=900)

## What ML Builder can do for your business

ML Builder can help with several use cases. The following examples relate to the currently **supported prediction capabilities**: binary, multi-class, and text classification.

* **Request approval.** A company has a process for submitting requests by their employees. Based on the existing company data, ML Builder can speed up the decision and group requests into those that might qualify for approval or rejection.

* **Ticket prioritization.** A company has a large support center with many incoming tickets. The support staff needs to quickly set the priority of each ticket as "low", "medium", or "high". ML Builder can learn from the existing tickets how to prioritize a new ticket. An app can then use the model to set the priority immediately after the support staff receives the ticket.

* **Customer feedback classification.** A company has several channels through which customers send feedback about what they want to see in a new product version. ML Builder can analyze the feedback and show the most popular topics. Are customers mentioning design, support, or a feature?

For more examples, check out the blog post [What is Predictive Modeling?](https://www.outsystems.com/blog/posts/predictive-modeling/)

## Costs of using an AI provider

ML Builder uses **Microsoft Azure** as the AI provider. Azure subscription costs aren't included in the OutSystems ML Builder pricing and are your responsibility to manage. Here is some information that can help you predict costs.

* The cost of training a machine learning model depends on the time Azure spends to train it ("pay as you go").
* Storage costs depend on usage.
* Each model you deploy uses a separate container. For example, for two models you would use two containers. You can delete a model by [following these instructions](https://docs.google.com/document/d/167TZlQ4RIx1-Dm_3GEY9oO_sFQYsSuhHVTQXav73Bko/edit#heading=h.gzg7hefg9yzg).

For detailed information about Azure costs, check out [Microsoft Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/).
