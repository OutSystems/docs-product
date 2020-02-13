# Invalid Action Flow Error

The `Invalid Action Flow` error is issued in the following situations:

* `'Cycle' path must return to the 'For Each' element in <action>`
  
    You have a For Each element with a Cycle loop path that does not return to the For Each element.

    Fix the Cycle loop to return to the For each element.

* `Ambiguous paths to <element> in <action>`
  
    You have an element that belongs simultaneously to different Start, Exception Handler, or For each paths.

    **Examples**  

    | Flow        | Description  |
    |:-----------:|:-------------|
    | ![](images/ambiguous-paths-1.png) | In this situation, the Assign element belongs to the Action flow and also to the Exception flow, therefore the Error handler flow is crossing the regular execution of the action. |
    | ![](images/ambiguous-paths-2.png) | In this situation, the Assign element belongs to the Action flow and also to the For Each flow. |

    Alternatively, there are missing paths in a node of your action. For example, you have a For Each node with no Cycle loop path.

    Edit the Action flow and fix the ambiguous paths.

* `If must have one (T)rue and one F(alse) link`
  
    You have an If element that is not well implemented.

    Fix the If element in this action to have True and False branches.

* `Switch condition for <path> connector must return a 'Boolean' value`
  
    You have a condition in your Switch element that does not return a Boolean value and therefore is not well implemented.

    Fix the Switch element in this action to have the conditions returning a Boolean value.

* `<switch> must have an otherwise optional connector in <action>`
  
    You have a Switch element that does not have the Otherwise path and therefore is not well implemented.

    Fix the Switch element in this action to have an Otherwise path.

* `Start is required in <action>`
  
    You have an action flow that does not have the Start element.

    Edit this action and add a Start element. Note that an action flow must have one and only one Start element.

* `More than one Start found in <action>`
  
    You have more than one Start element in your action.

    Edit this action and remove the duplicated Start elements.

Double-click the error line to take you to the action flow and highlight the element where the problem is occurring.
