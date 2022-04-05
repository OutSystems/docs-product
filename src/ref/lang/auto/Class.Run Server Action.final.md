---
kinds: ServiceStudio.Model.Nodes+ExecuteAction+Kind
helpids: 30107
summary: Executes a Server Action, which contains logic that's executed on the server.
---

# Run Server Action


Executes a Server Action that runs logic on the server. Server Actions usually encapsulate logic that implements the business rules of your application.

You can use the Run Server Action element in the logic flow of actions such as:

* Client Actions
* Data Actions
* other Server Actions
* Automatic Activities
* methods of exposed REST APIs and SOAP Web Services
* Preparations and Screen Actions (only available in Traditional Web Apps)

When the Server Action you wish to run has input parameters, you provide their values in the properties of the Run Server Action element. This is also called **providing the arguments** for running the Server Action.

![Fill in input parameters](images/run-server-action-properties-ss.png)

When the Server Action you wish to run has output parameters, you can use them in the logic that follows the Run Server Action element. There must be a logical path from the Run Server Action element to the place where the output parameter is used.

In the following example, we used the **Valid** output parameter of the **ValidateAPIKey** Server Action in an expression:

![Expression containing a Server Action output parameter](images/run-server-action-use-output-ss.png)

## How to use the Run Server Action tool

1. In the action flow where you want to run the Server Action, drag the **Run Server Action** tool and drop it in the action flow.

    ![Drag Run Server Action to action flow](images/run-server-action-drag-ss.png)

    Alternatively, open the **Logic** tab, expand the **Server Actions** folder, and drag the Server Action you want to run and drop it in the action flow.  
    In this case, skip the next step because you already selected the desired Server Action.

    ![Drag Server Action to action flow](images/run-server-action-drag-2-ss.png)

1. In the pop-up window, select the Server Action that you want to run from the **Server Actions** folder in the tree, and click **OK**.

    ![Select Server Action to run](images/run-server-action-select-ss.png)

1. Provide the arguments for the Run Server Action element by filling in the values in the properties editor. You must enter a value at least for the mandatory input parameters of the Server Action.

    ![Fill in input parameters](images/run-server-action-properties-ss.png)

1. If the Server Action has output parameters, you can use them in the logic flow after the Run Server Action element.

    ![Expression containing a Server Action output parameter](images/run-server-action-use-output-ss.png)

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Action">Action</td>
<td>Action with logic to run on the server.</td>
<td>Yes</td>
<td></td>
<td>It might be necessary to specify additional action input arguments.</td>
</tr>
<tr>
<td title="Animation Effect">Animation Effect</td>
<td>Type of animation applied to the widget when refreshed.</td>
<td>Yes</td>
<td>None</td>
<td>The possible values are: None, Highlight, Fade, Vertical Slide.</td>
</tr>
<tr>
<td title="Server Request Timeout">Server Request Timeout</td>
<td>Maximum time in seconds to wait for the Execute Action to complete before triggering a Communication Exception. Overrides the default timeout defined on the module.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

