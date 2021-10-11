---
summary: Information on what data to use and how to a solid model. 
tags:
---

# Data considerations { #data-considerations }

This section explains how ML Builder handles data, what data you can use, and how to avoid common issues.

## Data sources

You can use the Entities in your environment to train a model, but you can also use remote CSV data. Whether you use Entities or CSV, ML Builder extracts the data and then securely sends it to Azure, to the default blob storage. The file with your data has the following path: **datasets\[model-name].csv**, where **[model-name]**.

### OutSystems Entities

ML Builder connects to your environment and lets you select your business data for creating a model that works for your use cases. Here are some notes about how ML Builder handles Entities in the UI during data selection.

* The Entity must contain the target Attribute and all Attributes for generating the model.
* Only Entities with at least one attribute of the following types show in the UI: integer, decimal, long integer, boolean, and static attribute.
* ML Builder ignores the ID fields of the records, as the ID fields don't add value to the model.
* The minimum number of records ML Builder considers depends on the AI provider. 

### Remote CSV

You can use CSV data with the Azure blob storage as the data source. Start creating a new model from an Entity, and at the review screen click **Change data source (optional**). You have the following options:

* **Current environment**. The default setting.
* **Remote CSV file**. If the data is already in Azure, enter the relative path to your default blob storage.

![Change data source dialog](images/change-data-source.png?width=450)

## General

As a rule of thumb, the more data you have for training the model, the better. However, the quality of that data is very important. Here are some general notes about issues that machine learning experts identified, and of which you should be aware when selecting data for training a model. You should spend some time analyzing your data to make sure you can identify potential issues. 

### Data leak

Data leak occurs when you use data, to train your model, that you want to predict or data that doesn't exist when you use the model in production. In the support portal use case, the data set fields like priority, ticket type, and responsible team are only available after a support agent creates a ticket. If one of those fields is the target for the prediction, ML Builder excludes it as the attribute to predict the target. You should also not include those attributes to predict the target.

This is what you can do to prevent data leak. **Identify** and then **exclude from the training**:

* The attributes that contain information about the future.
* Any fields that don't exist at the moment of prediction.

How to **recognize** data leak:

* Analyze your model performance. Unrealistically good performance can be a sign of data leak.

### Concept drift     

Be careful not to introduce a concept drift due to the changes in the historical data. As a simple example, consider the support portal use case. If you're trying to predict the ticket priority, and you have the category "Urgent" in the data of the last six months only, you shouldn't include data older than that for training.

### Data bias

It's important to know that the data used to train the model is what an algorithm considers to be the undeniable truth. If you introduce bias in your data, you introduce bias in the model as well.

To prevent bias:

* Know your data and structure it in a way that allows different opinions.
* Have a diverse and multidisciplinary group to analyze and annotate data.
* Be aware of societal biases and remove them by monitoring and continuous improvement.

### About sensitive data  and GDPR

Be aware of the data you are using to train your model. Protect and use sensitive data according to GDPR and data protection policies that are applicable to your company.

For example, instead of using the credit card number, use only the last four digits. The four digits may produce a model of lower quality, but it's GDPR compliant.
