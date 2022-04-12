---
summary: OutSystems gives you the capability to convert existing logic, modules and applications to Services in a systematic way.
tags: support-application_architecture
locale: en-us
guid: a82f9d7f-70bf-43b2-a291-dd56905f35b2
---

# Convert to Services

OutSystems gives you the capability to convert existing logic, modules and applications to Services in a systematic way, that does not involve error prone actions (cut and copy) and that does not require the use of data migration tools to avoid loss of versioning and history data.

## Convert a Web or a Mobile module to a Service module

Converting a Web or a Mobile module to a Service module changes the type of the original module, it does not clone the module.

The conversion to a Service module is done locally in Service Studio and you must publish the converted module to make this conversion effective.  Furthermore, it is not possible to merge modules of different types.  
If there are other developers working on the module you are converting, make sure that they publish their work and close the module before you start the conversion. After you publish the converted modules, other developers must reopen the module before resuming work.

Service modules help enforce stricter segmentation of modules and to encapsulate core business services, by not allowing the following elements:

* Interface elements and properties, for example UI flows, Web Screens, Blocks and Images.
* Module properties for interface, for example JavaScript and Global Event Handler.
* Email elements, for example Emails and Send Email in Processes.
* Session Variables.
* Client side logic and Local Storage Entities.
* Human Activities in Processes.

Before converting a Web or Mobile module to a Service module, remove these elements from the module and make sure that there are no TrueChange errors.

To convert a Web or Mobile module to a Service module follow these steps:

1. In the target module, open the **Module** menu and select **Convert to Service**.

    <div class="info" markdown="1">

    If your module has elements that are not allowed in a Service module, the conversion stops and the unallowed elements are listed in an error message. Remove the listed elements from your module and repeat step 1.<br/>
    If your module has TrueChange errors, the conversion is stopped and an error message is shown. Fix the errors and repeat step 1.

    </div>

1. On the **Convert to Service Module** confirmation window, click **Yes**.

1. Do one of the following:

    * To publish the converted Service module, click **PUBLISH NOW**. 
    * To continue working before publishing the converted module, click **PUBLISH LATER**.

## Convert a Server Action to a Service Action

You can only define Service Actions in Service modules. 

Before refactoring your Server Actions to Service Actions, read more about [using Service Actions, how they are different from Server Actions and how you should adapt your logic](services.md#using-service-actions).

To convert a Server Action to a Service Action, open the **Logic** tab and drag the Server Action to the **Service Actions** folder.

After converting the Server Action to a Service Action, in each consumer module, use the **Manage Dependencies** window to remove the reference to the original Server Action and to add a new reference to the converted Service Action.

## Convert a Web or Mobile application to a Service application

Service applications can only contain Service modules and Extension modules.
As such, before converting an application to a Service application you need to remove Web modules and Mobile modules or convert them to Service modules.

<div class="info" markdown="1">

The conversion to a Service application is irreversible, you will not be able to convert the application back to a Web or Mobile application.

</div>

To convert an application to a Service application, open the application, click **Convert to Service** and click **Yes** in the confirmation window.
