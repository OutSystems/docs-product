---
summary: Learn how to make elements of your module available for reuse by other modules and how to to use elements exposed by other modules.
tags: support-Mobile_Apps; support-webapps
---

# Expose and Reuse Functionality Between Modules

When developing your OutSystems applications, elements are implemented and reused anywhere inside the same module. However, you can expose some elements in your module to be reused by other modules.

The module that implements and exposes functionality is the **producer** module. On the other hand, the module that reuses the exposed functionality is the **consumer** module. The functionality exposed by a **producer** module is considered as **dependencies** in the **consumers**.

![](images/expose-and-reuse-1.png?width=400)

Changes made in the producer module to the signature or implementation of the exposed elements may have impact in the consumer module. Check [this topic](handle-changes.md) to learn how the changes made in the producer in the exposed elements will impact the consumer modules.

## Expose Functionality to Other Modules { #expose }

When you expose functionality to other modules of the environment, your module is the **producer** module. Most of the elements you create in the module, such as actions or entities, are not exposed by default. You have to make them **Public** in order to expose them to other modules.

To expose an element to other modules, do the following:

1. Set the element’s Public property to ‘Yes’:

    ![](images/expose-and-reuse-2.png?width=300)

1. Publish your module. After publishing your module, the public elements can be reused by other modules in the environment.

By definition, Service Actions will always be public to other modules, so you don’t need to set them public. This also happens for the elements exposed by [Extensions](../../extensibility-and-integration/integration-studio/getting-started/extension.md).

Depending on the type of elements that you expose, OutSystems will generate a **strong dependency** or a **weak dependency** between your module and the consumer modules. Check [this topic](strong-weak-dependencies.md) to understand the differences between strong and weak dependencies and how each element is exposed.

## Reuse Functionality From Other Modules { #reuse }

When you reuse functionality from other modules of the environment, your module is the **consumer** module.

To reuse elements from other modules, do the following:

1. Open the **Manage Dependencies** window.

    ![](images/expose-and-reuse-3.png?width=300)

1. Select the producer module and then select the element you want to use.

    ![](images/expose-and-reuse-4.png?width=600)

1. Press **OK** to make the element available in your module.

    ![](images/expose-and-reuse-5.png?width=300)

1. Use the element exposed by the producer as any other element in your module.

    ![](images/expose-and-reuse-6.png?width=600)


In the consumer module, you will see all the details you need to reuse the exposed element, such as the element name, the description or the input/output parameters - this is called the element’s signature. You will not be able to modify the exposed elements.
