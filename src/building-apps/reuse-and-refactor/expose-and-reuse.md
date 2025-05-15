---
summary: OutSystems 11 (O11) enables the exposure and reuse of module functionalities, distinguishing between producer and consumer modules.
tags: module interactions, service architecture, application development, dependencies management, functionality exposure
locale: en-us
guid: 4b07ffa2-b09c-4ce8-a7b0-7b18aef4ca47
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/iBD5yo23NiW53L1zdPqGGM/Developing%20an%20Application?node-id=280:11
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - understand
  - apply
topic:
  - add-module-dependency
---

# Expose and reuse functionality between modules

When developing your OutSystems applications, elements are implemented and reused anywhere inside the same module. However, you can expose some elements in your module to be reused by other modules.

The module that implements and exposes functionality is the **producer** module. On the other hand, the module that reuses the exposed functionality is the **consumer** module. The functionality exposed by a **producer** module is considered as **dependencies** in the **consumers**.

![Diagram illustrating the relationship between producer and consumer modules in OutSystems](images/expose-and-reuse-diag.png "Producer and Consumer Modules Diagram")

Changes made in the producer module to the signature or implementation of the exposed elements may have impact in the consumer module. Check [this topic](handle-changes.md) to learn how the changes made in the producer in the exposed elements will impact the consumer modules.

## Expose functionality to other modules { #expose }

When you expose functionality to other modules of the environment, your module is the **producer** module. Most of the elements you create in the module, such as actions or entities, aren't exposed by default. You have to make them **Public** to expose them to other modules.

To expose an element to other modules, do the following:

1. Set the element's **Public** property to **Yes**.

    ![Screenshot showing how to set the Public property to Yes in a Server Action within OutSystems](images/expose-and-reuse-2.png "Setting Public Property to Yes")

1. Publish your module. After publishing your module, you can reuse the public elements in other modules in the environment.

By definition, Service Actions are always public to other modules, so you don't need to set them as public. This also happens for the elements exposed by [Extensions](../../integration-with-systems/integration-studio/getting-started/extension.md).

Depending on the type of elements that you expose, OutSystems generates a **strong dependency** or a **weak dependency** between your module and the consumer modules. Check [Understand Strong and Weak Dependencies](strong-weak-dependencies.md) to understand the differences between strong and weak dependencies and how each element is exposed.

## Reuse functionality from other modules { #reuse }

When you reuse functionality from other modules of the environment, your module is the **consumer** module.

To reuse elements from other modules, do the following:

1. Open the **Manage Dependencies** window.

    ![Image depicting the Manage Dependencies option in the OutSystems IDE toolbar](images/expose-and-reuse-3.png "Manage Dependencies Toolbar Option")

1. Select the producer module and then select the element you want to use.

    ![Screenshot of the Manage Dependencies window in OutSystems showing how to select producer modules and elements](images/expose-and-reuse-4.png "Manage Dependencies Window")

1. Press **Apply** to make the element available in your module.

    ![Image showing an element in the tree structure defined in a producer module within the Manage Dependencies window](images/expose-and-reuse-5.png "Element Defined in Producer Module")

1. Use the element exposed by the producer as any other element in your module.

    ![Screenshot demonstrating the use of a Server Action defined in a producer module within a consumer module in OutSystems](images/expose-and-reuse-6.png "Using a Server Action from Another Module")

In the consumer module, you can see all the details you need to reuse the exposed element, such as the element name, the description, or the input/output parameters — called the **element's signature**.

You can't modify the exposed elements in the consumer module, you must edit them in the producer module.
