---
summary: How to use model predictions in your app. 
tags:
---

# Implement model in your app

After you train your model and you're happy with the model performance, use the model in your app logic.

<div class="info" markdown="1">

To use the model in your app, you need to install **ML Builder plugin**. You can download the plugin during the setup, as described in [Getting started](getting-started.md).

</div>

In Service Studio, open the app where you want to implement the model and do the following:

1. Reference the ML Builder plugin. Press **Ctrl+Q** and in the **Manage Dependencies** window search for `MLBuilderPlugin`. Then, select the Service Actions in the right pane. 

   ![Manage Dependencies and ML Builder plugin](images/reference-plugin-ss.png?width=450)

1. In the logic of your app, use the Actions from **Logic** > **Service Actions** > **MLBuilderPlugin** > **ModelScore** to get the scores from your models:

    * **GetAttributePrediction** for attribute models
    * **GetTextClassification** for text classification models

    Explore the parameters of the actions to learn more about the values they require and return.

    ![ML Builder actions](images/ml-actions-ss.png?width=450)

<div class="info" markdown="1">

ML Builder is currently in a public **early access program (EAP)** and you need to register at the [ML Builder registration page](https://www.outsystems.com/eap-ml-builder/) to try it out.

</div>