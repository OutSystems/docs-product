Use the **Ajax Refresh** element in your flow to refresh parts of the screen without reloading the entire page.

Keep the following key points in mind when using **Ajax Refresh**:

One element
:   You can only select one element to refresh in each **Ajax Refresh** node. To refresh more than one interface element at the same time wrap them inside a **Container** and then refresh that **Container**.

Ajax Submit
:   Set Ajax Submit as the `Navigation Method` of the Link/Button that triggers the **Ajax Refresh**.

Name
:   The element you want to refresh using **Ajax Refresh** must have a `Name`.

Web Block Preparation
:   If you use **Ajax Refresh** to refresh a **Web Block**, the **Preparation** of the **Web Block** will be re-executed.

Refresh order
:   Multiple **Ajax Refresh** nodes in the same action flow are executed in the order defined in the action flow.
