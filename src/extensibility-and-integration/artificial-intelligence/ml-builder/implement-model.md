---
summary: Check out how to use model predictions in your app. Example of a use case. ML Builder plugin reference. 
tags:
---

# Integrating a model in your app

After you create and deploy a model, reference the ML Builder plugin in your app. Use the actions from the plugin in your logic by entering the model name and data for a prediction. Here is an overview.

![Integration overview](images/integration-overview-diag.png?width=850)

Check out this document for more details about using the model in your app.

<div class="info" markdown="1">

To use the model in your app, you need to:

* Install the **ML Builder plugin**. You can download the plugin during the setup, as described in [Getting started](getting-started.md).
* Deploy at least one model. You can deploy a model by clicking on the **Deploy** button on the model overview page.

</div>

## Referencing the plugin 

In Service Studio, open the app where you want to use the model and do the following:

1. Reference the ML Builder plugin. Press **Ctrl+Q** and in the **Manage Dependencies** window search for `MLBuilderPlugin`. Then, select the Service Actions in the right pane. 

    ![Manage Dependencies and ML Builder plugin](images/reference-plugin-ss.png?width=550)

1. In the logic of your app, use the Actions from **Logic** > **Service Actions** > **MLBuilderPlugin** > **ModelScore** to get the information from your models:

    * **GetAttributePrediction** for attribute models
    * **GetTextClassification** for text classification models

    Explore the [parameters of the actions](#reference) to learn more about the values they require and return.

    ![ML Builder actions](images/ml-actions-ss.png?width=300)

## Example

Here is an example of how you can use ML Builder. A telecom company wants to predict the chances of breaking the contract (churn). With historical data about contracts you can start training a prediction model.

### Sample data structure

In this example, the Entity is **SampleCustomerData** with the following Attributes:

* CustomerId
* CreditScore
* Geography
* Gender
* Age
* Tenure
* Balance
* NumOfProducts
* HasCrCard
* IsActiveMember
* EstimatedSalary
* Churned

You can train a model for the attribute prediction, and predict a binary decision (**True** or **False**) for **Churned**. The score in this example returns the likelihood on the scale from 0 to 1, or 0% to 100%.

You should exclude **CustomerId** (from your customer data) and **Id** (Entity record identifier) as they don't contribute to the model. Check also how to prevent [data bias](data-considerations.md#data-bias).


### Sample logic

After you reference the plugin, create logic that asks your model for predictions. In this example, there's **GetAttributePrediction** that uses a record of an Entity as the input.


1. Prepare the data for sending it to the model. As the model accepts structured JSON data, use ***JSONSerialize** to convert a record from the Entity to a JSON.
    
    ![Serialize data to JSON](images/json-serialize-record-ss.png?width=400)

    In the example, the action requires an input parameter of the data type **SampleCustomerData**, which is then the **Data** for **JSONSerializeCustomer**.
  

2.  Send the data to the model by using **Logic** > **Service Actions** > **MLBuilderPlugin** > **ModelScore** > **GetAttributePrediction** action with the value **JSONSerializeCustomer.JSON** in the **RecordToPredictInJSON** property.

    ![Calling action to query the prediction model](images/server-action-model-ss.png?width=500)

    You also need to enter the name of the model in the property **ModelName**. Get the name of the model you want to use from the list of trained and deployed models in ML Builder.

    <div class="info" markdown="1">

    Notes

    * Make sure you **deploy a model** you want to use in your app. 
    * The **ModelName** in the actions and the model name in ML Builder must be the same. For example, if the model name in ML Builder is **My Model**, then enter `My Model` in the **ModelName** field.

    </div>

3. Check if the model returns data. The value of **GetAttributePrediction.IsSuccess** should be **True**. The example shows an error if the request to the model isn't successful.

    ![Check if response is valid](images/condition-success-ss.png?width=550)

4. Get the top result of the prediction. Do that by evaluating `GetAttributePrediction.TopPrediction[0].score` and assigning the value to a variable. In the example, the variable is **TopPrediction**.

    ![Getting the top prediction](images/top-prediction-ss.png?width=400)

    The data type of **TopPrediction** is decimal because you're predicting the likelihood of the customer ending the contract (churning), on a scale from **0** to **1**. This is because you trained the model with the data where the churn value is **0** or **1**.

5. Decide whether you want to show the prediction by checking how "confident" the prediction is. For example, you can show results when the top score is above 0.3, or 30%.

     ![Prediction confidence](images/prediction-confidence-ss.png?width=500)

6. Finally, update the user interface to show the result. In a production app you could show customer data in red if there's a risk of churn, or green, if there's no risk. For testing, you can use notification with the prediction result. 

**Steps overview**

Here is the summary of the logic. The numbers match the steps of the instructions.

![Sample logic](images/sample-logic-prediction-ss.png?width=700)


##  Reference

Reference **MLBuilderPlugin** to use the ML Builder plugin. Here is an overview of the actions, parameters, and data structures.

### Service actions

The available service actions are in **Logic** > **Service Actions** > **MLBuilderPlugin** > **ModelScore**. Here is more information about the actions.

| Action                     | Description                                                 |
| -------------------------- | ----------------------------------------------------------- |
| **GetAttributePrediction** | Returns values for models trained for attribute prediction. |
| **GetTextClassification**  | Returns values for models trained for text classification.  |

### Parameters

Here is more information about the parameters you can use in the ML Builder plugin actions.

| Name                      | Type   | Action                 | Data                 | Description                                                   |
| ------------------------- | ------ | ---------------------- | -------------------- | ------------------------------------------------------------- |
| **ErrorMessage**          | Output | All                    | Text                 | If the call fails, the parameter returns the error details.   |
| **IsSuccess**             | Output | All                    | Boolean              | Flag telling if the call was successful.                      |
| **ModelName**             | Input  | All                    | Text                 | The name of the model that must match the name in ML Builder. |
| **RecordToPredictInJSON** | Input  | GetAttributePrediction | Text                 | A JSON with the information to query the model.               |
| **ScoreResult**           | Output | All                    | ModelScore Structure | Data structure with the results of a scored model.            |
| **TextToClassify**        | Input  | GetTextClassification  | Text List            | Text you classify with the text classification model.         |
| **TopPrediction**         | Output | All                    | PredictionItem List  | Data structure with the top-scored result of a model.         |

### Structures

You can check the structures in **Data** > **Structures** > **MLBuilderPlugin**.

| Name          | Description                                           |
| ------------- | ----------------------------------------------------- |
| **ScoreItem** | Consists of **class** (Text) and **score** (Decimal). |

The meaning of **class** and **score** in the **ScoreItem** depends on the prediction: 

| Prediction         | **class**       | **score**             |
| ------------------ | --------------- | --------------------- |
| Numeric value      | `prediction`    | the value             |
| Boolean value      | `True`, `False` | indicates probability |
| A value from a set | `<value>`       | indicates probability |


Here are some examples:

When you want to predict a numeric value, the **class** in the response is always `prediction`: 

`{"class": "prediction", "score": 12.567}`

If you predict a boolean or a value from a set of values, **class** in the response for **ScoreResult** holds a value, while **score** indicates **probability**:

`{"class": "Green", "score": 0.25}`

`{"class": "Yellow", "score": 0.35}`

`{"class": "Blue", "score": 0.40}`


`{"class": "True", "score": 0.40}`

`{"class": "False", "score": 0.60}`


In **TopPrediction**, **class** is a boolean or a value from a set of values, and the score is the probability.

`{"class": "Blue", "score": 0.40}`

`{"class": "False", "score": 0.60}`
