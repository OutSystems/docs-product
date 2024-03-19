---
summary: Learn how to use a For Each to iterate a list in your logic.
tags: support-webapps
locale: en-us
guid: 15a9d0fc-aef0-4d69-bfaa-edeefbecad36
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=266:9
---

# Use a For Each to Iterate a List

In your application logic, you may want to loop over each element in a collection to perform a piece of logic recursively. You can iterate lists using a For Each logic node.

To iterate through the elements of a List:

1. Add a **For Each** flow element to the action flow.

    ![Screenshot showing how to add a For Each flow element to the action flow](images/for-each-1-ss.png "Adding a For Each Element")
   
1. Set its **Record List** property to the list you want to iterate.

    ![Screenshot demonstrating setting the Record List property for the For Each element](images/for-each-2-ss.png "Setting the Record List Property")
1. Add the instructions you want to implement in the body of the loop. 
1. Create a connection from the For Each node to the first instruction in the logic you want to iterate. This first connector is called Cycle and marks the beginning of the cycle. 
1. Create a connection from the last step in your logic to the For Each Node to close the cycle. 

The Current runtime property of a List (`<List>.Current`) holds the item in the list currently being iterated. 

![Diagram illustrating the connections in a For Each loop with Cycle and Current runtime property](images/for-each.png "For Each Loop Connections")
