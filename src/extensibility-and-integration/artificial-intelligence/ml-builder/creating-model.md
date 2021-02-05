---
summary: How to create a model for text classification and attribute prediction. 
tags:
---

# Creating a model

When you start creating a model, ML Builder guides you through several steps. What follows is an overview with some additional information.

<div class="info" markdown="1">

ML Builder is currently in a public **early access program (EAP)** and you need to register at the [ML Builder registration page](https://www.outsystems.com/eap-ml-builder/) to try it out.

</div>

## Selecting use case

This section explains which use cases ML Builder supports and when to select each.

![Use cases selection screen in ML Builder](images/use-cases.png?width=700)

### Text classification

Text classification is about predicting a text category according to a single attribute. Use it when you want to classify a text value without additional information. Or, to classify a very long text like a support ticket description or a message in a forum post.

For example, you can use text classification to speed up the support ticket processing and help your users faster. Use the support ticket subject or description to create a model, and then let the app classify the case before it reaches busy support agents. 

For text classification ML Builder needs only **one text attribute** to predict the target.

### Attribute prediction

Attribute prediction is about predicting outcomes based on one or more attributes. It works by using attributes with different data types to predict a value from a predetermined set of values.

For example, you can use attribute prediction to help support agents prioritize tickets faster. By creating a model that uses the information from the previously created support tickets, you can predict the priority of the new tickets (low, normal, high).

With attribute prediction, keep in mind potential issues such as data leak or concept drift. See [Data considerations](data-considerations.md#data-considerations) for more information.

## Selecting data { #selecting-data }

After you choose a use case for creating a model, the next step is selecting data from an Entity. See [Data considerations](data-considerations.md#data-considerations) for more information.

### Selecting target attribute

In the attribute selection step you select the attribute corresponding to **what you want to predict**. Depending on the use case, you may select one or more attributes, or one or more data types of attributes. For example, for text classification you can select only the text fields.

### Selecting text attribute to classify

Applies to **Text classification**.

This is the attribute for which your model predicts a category based on the data you provide.

### Selecting attributes to learn from

ML Builder recommends automatically the attributes that fit the use case for your model. You can modify this selection.

In the **text classification** use case, you select the single text attribute to classify.

In the **attribute classification** use case, you can select one or more attributes. Check out the [Data considerations](data-considerations.md#general) section to read more about the impact the attribute selection can have.