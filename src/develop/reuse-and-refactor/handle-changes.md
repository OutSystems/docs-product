---
summary: Handle the impact on modifications to elements that are being reused between modules.
locale: en-us
guid: 359c1979-6708-47f4-a628-4f66bb4ef56d
---

# Handle Changes in Exposed Functionality

One of the benefits of reusing elements is the ability to change their implementation and signature in a single place - the **producer** module - and have all its **consumer** modules benefit from the new implementation.

While some of the changes made in the producer module have an immediate effect on the consumer modules at runtime, in other cases the consumer modules need to be republished in order to use the latest implementation of their dependencies.

## Change Functionality in the Producer Module

When you change the functionality you are exposing in your **producer** module and you publish the changes, OutSystems performs an impact analysis of those changes in all the consumer modules.

The impact that those changes have on the consumer modules at runtime depends on the kind of change that you performed and the [type of dependency](strong-weak-dependencies.md) between your producer module and the consumers.

When you change the functionality in your **producer** and you publish the changed module, one of the following situations can happen in a **consumer module at runtime**:

* **No impact on Consumer**: The changes you performed in the producer causes no impact on the consumer module at runtime and the consumer immediately starts using your latest implementation. Example: Changing the content of a WebScreen ([weak dependency](strong-weak-dependencies.md#weak-dependencies)) with no changes to its signature.

* **Outdated Consumer**: The changes you performed in the producer module are compatible with the consumer, which means that there are no manual fixes to do in the consumer, but the consumer is now running an outdated version of your producer. Example: Changing the logic of an exposed Server Action ([strong dependency](strong-weak-dependencies.md#strong-dependencies)) with no changes to its signature.

    ![](images/handle-changes-1.png?width=700)
  
    In this case, the consumer module at runtime keeps using the previous logic of your producer module until a republish. The consumer module needs to be republished to start using the latest implementation of your producer module. There is no need to refresh the producer dependencies because the signature did not change.

* **Potential Incompatible Consumer**: You performed changes in the signature of exposed elements that **may be incompatible** with the consumer module and cause runtime errors. Example: Adding an optional Input Parameter to an exposed Server Action or Web Screen.

    ![](images/handle-changes-2.png?width=700)

    In this case, the consumer module needs to be republished in order to validate the compatibility of the performed changes. If the changes are compatible, the consumer module has no need to refresh the producer dependencies.

* **Incompatible Consumer**: You performed changes in the signature of exposed elements that **are incompatible** with the consumer module and will probably cause runtime errors. Example: An exposed element is no longer set as Public.

    ![](images/handle-changes-3.png?width=700)

    In this case, the consumer module needs to refresh its producer dependencies in Service Studio, handle the changes in the logic if necessary, and be republished.

## Handle Dependencies in the Consumer Module

When you reuse functionality from another module, your **consumer** module has a **dependency** to that producer module. Every time the producer module changes the signature of an exposed element, such as the element name, the description or the input/output parameters, your module may be impacted by those changes. Refreshing the dependencies in your consumer module will update the signature of the producer public elements.

The **Manage Dependencies** window is where you can see if any of your dependencies changed the signature of their exposed elements, and refresh the dependencies to get the updated signatures.

![](images/handle-changes-4.png?width=300)

The signature of an exposed element can change in one of the following ways:

* The element’s signature is **modified** but the change is compatible with the information known by the consumer module.
* The element’s signature is **incompatible** with the information known by the consumer module.
* The element is missing. 

### Modified Signature

The **signature of an exposed element has changed** but there is **no impact** on your consumer module, which means that you don't need to refresh the dependency. Example: Adding an optional Input Parameter to a Server Action. The changed element is marked with a blue **information** sign in the Manage Dependencies window.

![](images/handle-changes-5.png?width=600)

In this case, you don’t need to refresh the dependency. You only have to [refresh the dependency](#refresh-dependencies) if you want to use the latest version of the producer signature in your logic, such as passing a value to a new added optional Input Parameter.

The following changes made in the producer do not have impact on the consumer modules:

|**Scenario**|**Elements**|
|------------|------------|
|Add an optional Input Parameter<br/>Change a mandatory Input Parameter to optional<br/>Delete an Input Parameter<br/>Reorder Input Parameters|Server Action, Service Action, Web Block (Traditional Web only), Web Screen (Traditional Web only) *|
|Add an Output Parameter<br/>Delete an unused Output Parameter|Server Action, Service Action|
|Change a mandatory Attribute to optional<br/>Delete an unused Attribute<br/>Reorder Attributes|Entity (Database and Local Storage), Static Entity, Structure|
|Add an optional Attribute (any data type)|Entity (Database and Local Storage), Static Entity|
|Add an optional Attribute ([basic data types](../../ref/data/data-types/available-data-types.md#basic_data_types) only)|Structure|
|Add a Record<br/>Delete an unused Record|Static Entity|
|Rename|All elements, except Entity Attribute, Resource and Script|
|Change Description|All elements|

(*) The described scenario **doesn't apply to Blocks and Screens in Mobile and Reactive Web Apps**. When performing one of the listed operations over an Input Parameter of a Block or a Screen in a Mobile or Reactive Web App, the element’s signature is **incompatible** with the information known by the consumer module.

### Incompatible Signature

The **signature of an exposed element has changed** and the change **has impact** on your consumer module. Example: Adding a mandatory Input Parameter to a Server Action. The changed element is marked as **incompatible** in the Manage Dependencies window.

![](images/handle-changes-6.png?width=600)

The impact of this change on your consumer module depends on the **type of dependency** to the producer:

* If it is a [strong dependency](strong-weak-dependencies.md#strong-dependencies), the change will cause no impact on your consumer module at runtime. You will only get runtime errors if you republish your consumer module without refreshing the dependency.

* If it is a [weak dependency](strong-weak-dependencies.md#weak-dependencies), the change will cause runtime errors in your consumer module.

In both cases, you need to [refresh the dependency](#refresh-dependencies), adapt your logic to the latest version of the producer, and republish your consumer module.

### Missing Signature

An element previously exposed is **no longer available**, which **has impact** on your consumer module. Example: A Server Action is deleted from the producer module. The element is marked as **missing** in the Manage Dependencies window.

![](images/handle-changes-7.png?width=600)

The impact of this change on your consumer module depends on the type of dependency to the producer:

* If it is a [strong dependency](strong-weak-dependencies.md#strong-dependencies), the change will cause no impact on your consumer module at runtime. You will only get runtime errors if you republish your consumer module without refreshing the dependency.

* If it is a [weak dependency](strong-weak-dependencies.md#weak-dependencies), the change will likely cause runtime errors in your consumer module.

In both cases, you need to [refresh the dependency](#refresh-dependencies), remove the element from your module, adapt your logic to the latest version of the producer, and republish your consumer module.

This behavior can be caused by one of the following situations:

* The element was deleted from the producer module.
* The element is no longer set as Public.
* The producer module does not exist in the OutSystems environment you are connected to.
* You do not have permissions to reuse the exposed element.

## Refresh Dependencies

To refresh the dependencies in your consumer module, do the following:

1. Open the Manage Dependencies window.

    ![](images/handle-changes-4.png?width=300)

1. Click the refresh icon close to the producer name to refresh a single dependency, or use the REFRESH ALL button to refresh all dependencies.

    ![](images/handle-changes-8.png?width=600)

1. If the changes in the producer module have caused an impact on your module and you need to adapt your logic accordingly, the TrueChange tab will highlight the situations where you need to update the logic.

    ![](images/handle-changes-9.png?width=600)
