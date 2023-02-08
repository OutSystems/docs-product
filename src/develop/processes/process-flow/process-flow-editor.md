---
summary: Learn more about this specific editor where you can define the process flow of your processes.
locale: en-us
guid: 3b354b39-f6fa-46a2-9ee0-95f82dedbff1
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Process Flow Editor

OutSystems provides you with a specific editor to define the process flow of your processes. This editor is called the **Process Flow Editor** and is divided into the following areas:

* **Process Flow Toolbox**: at the left hand side of Service Studio's workspace, it provides a set of tools that can be dragged and dropped on your **Content Canvas** to define the behavior of the process.  
The tools are elements that execute process activities, other processes or flow control tools. When a tool is dragged onto the Content Canvas, a new process activity in the process flow is created.

* **Content Canvas**: this is the central area of Service Studio's workspace where you drop the tools from the **Process Flow Toolbox** to define the logic of your process.  
To see the properties of a process activity, select it on the Content Canvas and they'll be displayed in the Property window.

## Defining the Flow

To define the flow of a process connect the elements on the Content Canvas starting in the **Start** element - only one Start element is allowed in a process flow. To finish a flow path use the **End** element - depending on the elements you are using in the process flow you can have a single or multiple paths.

In a process flow you are allowed to use other start tools to define alternative flows to handle specific events.
