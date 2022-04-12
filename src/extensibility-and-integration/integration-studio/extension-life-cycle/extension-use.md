---
locale: en-us
guid: 7fe4a4ad-7c65-4fce-9c54-8720bede33b1
---

# Use the Extension in a Module

Service Studio developers can use all the extensions [published](<extension-1-cp.md>) in Platform Server to expand the functionality or extend the database model of their modules.

To use an extension in your module you must add this extension as a Reference. A module reference is an element (Action, Entity, or Structure) exposed and implemented in a Producer module or extension, but that can be invoked from another module, called a Consumer.

## Add an Extension Reference to Your Module  
  
Do the following:

1. Launch Service Studio and open your module. Make sure you're connected to the Platform Server where you published the extension.

1. Launch the **Manage Dependencies** window, available in the **Module** menu or in the toolbar, and select the extension that you want to use.

1. Select the actions, structures, or entities from this window and press **Apply**.

## Use the Extension in Your Module

After adding these references to your module, they become available as follows:

* The entities and structures are available in the module tree in **Entities** and **Structures** folders, respectively.

* The actions are available in the **Logic** tab under the extension name. All actions with the **Function** property set to **Yes** are also available when editing expressions.

To use these elements, drag and drop them as you'd normally do if they were owned by your module.
