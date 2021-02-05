---
summary: An introduction to ML Builder. 
tags:
---

# Early Access Program - ML Builder

ML Builder is an OutSystems cloud tool that helps you create apps with predictive capabilities thanks to its built-in machine learning features. The user interface guides you through to the steps of connecting to your data and training a model. When a model is ready, ML Builder exposes server actions for you to build the logic of an app. You can also create back ends for administrators and more sophisticated UI for users, or even further expose the prediction capabilities through a REST API.

"ML" in ML Builder stands for "machine learning". OutSystems is developing ML Builder to be straightforward to use for most OutSystems developers. Therefore, ML Builder requires only basic knowledge of machine learning concepts.

ML Builder currently requires **Microsoft Azure** as the AI provider. You need an Azure subscription and sufficient permissions to create and manage the Azure resources. Note that you need to manage the costs of your Azure subscription, as it isn't included into the pricing of ML Builder.

For usable predictions based on machine learning, you need to have **good data** and the more data you have, the better. 

<div class="info" markdown="1">

## Prerequisites

ML Builder is currently in a public **early access program (EAP)** and you need to register at the [ML Builder registration page](https://www.outsystems.com/eap-ml-builder/).

To use ML Builder, you need to meet the following requirements:

* Platform Server 11.10 or later.
* Your development environment has OutSystems UI 2.5.2 or later.
* Allowed inbound traffic from https://mlbuilder.outsystems.com/ on the port 443. If your infrastructure is running in the OutSystems Cloud with the default network settings, you already fulfill this prerequisite.

</div>

## What ML Builder can do for your business

ML Builder can help you with several use cases. Here are some examples related to the currently **supported prediction capabilities**: binary, multi-class, and text classification.

* **Request approval.** A company has a process for submitting requests by their employees. Based on the existing company data, ML Builder can speed up the decision and group requests into those that might qualify for approval or rejection.

* **Ticket prioritization.** A company has a large support center with many incoming tickets. The support staff needs to quickly set the priority of each ticket as "low", "medium", or "high". ML Builder can learn from the existing tickets how to prioritize a new ticket. An app can then use the model to set the priority immediately after the support staff receives the ticket.

* **Customer feedback classification.** A company has several channels through which customers send feedback about what they want to see in a new product version. ML Builder can analyze the feedback and show what's the most common topic customers talk about. Are customers mentioning design, support, a feature, support?

For more examples, check out the blog post [What is Predictive Modeling?](https://www.outsystems.com/blog/posts/predictive-modeling/)