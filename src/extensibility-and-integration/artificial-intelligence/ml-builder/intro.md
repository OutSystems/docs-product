---
summary: An introduction to ML Builder. 
tags:
---

# Early Access Program - ML Builder

<div class="info" markdown="1">

## Prerequisites

ML Builder is currently in a public **early access program (EAP)** and you need to register at the [ML Builder registration page](https://www.outsystems.com/eap-ml-builder/).

To use ML Builder, you need to meet the following requirements:

* Platform Server 11.10 or later.
* Your development environment has OutSystems UI 2.5.2 or later.
* Allowed inbound traffic from https://mlbuilder.outsystems.com/ on the port 443. If your infrastructure is running in the OutSystems Cloud with the default network settings, you already fulfill this prerequisite.

You also need:

* An Azure subscription and sufficient permissions to create and manage the Azure resources. ML Builder uses **Microsoft Azure** as the AI provider.
* Good data and the more data you have, the better. Predictions based on machine learning depend on good data. 


</div>

ML Builder is an OutSystems cloud tool that helps you create apps with predictive capabilities thanks to its built-in machine learning features. The user interface guides you through to the steps of connecting to your data and training a model. When a model is ready, ML Builder exposes server actions for you to build the logic of an app. You can also create back ends for administrators and more sophisticated UI for users, or even further expose the prediction capabilities through a REST API.

"ML" in ML Builder stands for "machine learning". OutSystems is developing ML Builder to be straightforward to use for most OutSystems developers. The tool requires only basic knowledge of machine learning concepts.

Here is an overview of how ML Builder works and how you integrate the model predictions in an app.

![ML Builder overview](images/overview-diag.png?width=900)

## What ML Builder can do for your business

ML Builder can help you with several use cases. Here are some examples related to the currently **supported prediction capabilities**: binary, multi-class, and text classification.

* **Request approval.** A company has a process for submitting requests by their employees. Based on the existing company data, ML Builder can speed up the decision and group requests into those that might qualify for approval or rejection.

* **Ticket prioritization.** A company has a large support center with many incoming tickets. The support staff needs to quickly set the priority of each ticket as "low", "medium", or "high". ML Builder can learn from the existing tickets how to prioritize a new ticket. An app can then use the model to set the priority immediately after the support staff receives the ticket.

* **Customer feedback classification.** A company has several channels through which customers send feedback about what they want to see in a new product version. ML Builder can analyze the feedback and show what's the most common topic customers talk about. Are customers mentioning design, support, a feature, support?

For more examples, check out the blog post [What is Predictive Modeling?](https://www.outsystems.com/blog/posts/predictive-modeling/)

## Costs of using an AI provider

ML Builder uses **Microsoft Azure** as the AI provider. You need to manage the costs of your Azure subscription, as it isn't included into the OutSystems pricing of ML Builder. Here is some information that can help you predict costs.

* The cost of training of a model depends on the time Azure spends to train a model ("pay as you go").
* The Storage costs depend on usage.
* Each model you deploy deployed uses a separate container (for example, for two models you would be using 2 containers). You can delete a model by [following these instructions](https://docs.google.com/document/d/167TZlQ4RIx1-Dm_3GEY9oO_sFQYsSuhHVTQXav73Bko/edit#heading=h.gzg7hefg9yzg).

For detailed information about Azure costs, check out [Microsoft Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/).