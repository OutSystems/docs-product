---
summary: Explore disk space management on OutSystems 11 (O11) servers, detailing storage locations, content types, and cleanup processes.
guid: 787114b3-a4af-452a-8acf-2644624e8cbe
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: disk space management, on-premises deployment, cloud deployment, server administration, performance optimization
audience:
  - platform administrators
  - full stack developers
  - infrastructure managers
  - tech leads
outsystems-tools:
  - platform server
coverage-type:
  - evaluate
  - understand
---

# Guide to disk space usage and control on OutSystems Platform servers

<div class="info" markdown="1">

**Important:** The information in this guide applies only to OutSystems Platform on-premises or private cloud deployments.

</div>

## Introduction

This article explains how OutSystems Platform Server uses the disk to store objects, and enables our customers to understand, control, and manage that disk space usage.

## Knowing the commonly largest directories

First, let's clarify on the most commonly growing folder locations under the Platform Server installation directory, in the context of a Platform Server installed with the .NET stack version of the platform. Each of these folder locations can reach to several tenths of GB, depending on the factory size, the purpose of the environment, and the folder.

On the table below, you'll find detailed information about what it's stored on each of the folders that usually take more disk space. You'll also find the purpose of those folders and in which server profiles and environment types we can find them. For this table, take into consideration the following server profiles:

* Controller: A controller is the server that's responsible for the 1-Click Publishing process, and we assume here that's a pure controller, without the front-end server role.

* Front-end: It's the server responsible for the runtime execution of OutSystems applications, and thus, where applications are deployed (either in the public or personal areas).

<table markdown="1">
<thead>
<tr>
<th>Type of content</th>
<th>Description</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr>
<td rowspan="2">Full compilation cache</td>
<td><ul><li>Generated source code (.oml, .cs,.csproj, etc) files</li><li>Application release binary files (.dll, .aspx, .asmx ,etc)</li><li>Application resources files (.js,.css,.png,.gif, etc) in a full compilation.</li></ul></td>
<td><strong>Path:</strong> <code>&lt;platformserver&gt;\share\&lt;espacename&gt;\full</code><br/><strong>In controller:</strong> yes<br/><strong>In front-end:</strong> no<br/><strong>Environment type:</strong> all</td>
</tr>
<tr>
<td>Release application files package (zip)</td>
<td><strong>Path:</strong> &lt;platformserver&gt;\share\&lt;espacename&gt;<br/><strong>In controller:</strong> yes<br/><strong>In front-end:</strong> no<br/><strong>Environment type:</strong> all</td>
</tr>
<tr>
<td>Partial compilation cache</td>
<td><ul><li>Generated source code (.oml, .cs,.csproj, etc) files</li><li>Application release binary files (.dll, .aspx, .asmx ,etc)</li><li>Application resources files (.js,.css,.png,.gif, etc) in a partial compilation for each developer that runs/debugs the espace.</li></ul></td>
<td><strong>Path:</strong> &lt;platformserver&gt;\share\&lt;espacename&gt;\partial\&lt;developer&gt;<br/><strong>In controller:</strong> yes<br/><strong>In front-end:</strong> no<br/><strong>Environment type:</strong> all that have debug enabled</td>
</tr>
<tr>
<td rowspan="2">Release application files</td>
<td><ul><li>All release application files, deployed to be loaded by the front-ends application server (IIS).<br/>These files include all application files for this espace (.dll, .aspx, .asmx, .js, .css, images and other included resources).</li><li>All application compiled files (DLLs and JARs) that are shared between applications are hard links to the actual files stored in the \repository folder.</li></ul></td>
<td><strong>Path:</strong><code>&lt;platformserver&gt;\running\&lt;espacename&gt;.&lt;versionid&gt;</code><br/><strong>In controller:</strong> no<br/><strong>In front-end:</strong> yes<br/><strong>Environment type:</strong> all</td>
</tr>
<tr>
<td>All application compiled files (DLLs and JARs) that are shared between applications are stored in a shared server library, along with other platform libraries.<br/>This replaces the local copy of the DLLs/ JARs of all its producer applications in the \running folder, reducing the required disk space and the number of files that need to be distributed to the front-end servers.</td>
<td><strong>Path:</strong><code>&lt;platformserver&gt;\repository\</code><br/><strong>In controller:</strong> yes<br/><strong>In front-end:</strong> yes<br/><strong>Environment type:</strong> all</td>
</tr>
<tr>
<td>Personal Test Area Files</td>
<td>All release application files for a specific version that a specific user is running/debugging.<br/>These files include all application files for this espace (.dll, .aspx, .asmx, .js, .css, images and other included resources).</td>
<td><strong>Path:</strong><code>&lt;platformserver\test\&lt;espacename&gt;\&lt;developer&gt;</code><br/><strong>In controller:</strong> no<br/><strong>In front-end:</strong> yes<br/><strong>Environment type:</strong> all that have debug enabled</td>
</tr>
<tr>
<td>Temporary Asp.Net Files</td>
<td>These files are automatically generated by the .Net Framework, and not the Platform Server, but they are a part of every ASP.NET application.</td>
<td><strong>Path:</strong><code>C:\windows\microsoft.net\framework\v4.0.30319\Temporary Asp.Net Files\&lt;espacename&gt;</code> or <code>C:\windows\microsoft.net\framework64\v4.0.30319\Temporary Asp.Net Files\&lt;espacename&gt;</code><br/><strong>In controller:</strong> no<br/><strong>In front-end:</strong> yes<br/><strong>Environment type:</strong> all</td>
</tr>
</tbody>
</table>

A server can have both roles, and in that case, it would have both server role contents. Usually, the non-production environments use more disk space then production, mainly due to the number of developers, and due to the personal test areas for debugging.

## What folder contents can be deleted?

Ultimately, based on the architecture of the Platform Server where applications are defined by single OML files and extensions, any folder content can be deleted and then recovered through internal processes, such as 1-Click publishing. However, as you might be aware, this takes time, and it's not recommended for most environments, so let's elaborate on the side-effect of deleting each one of the presented contents:

| Type of content | Side Effect of deleting it | How to recover it |
|-----------------|----------------------------|-------------------|
| Full compilation cache | This compilation cache is used when 1-Click publishing or debugging modules with references. The Platform Server will fetch the producer references from this location. If they aren't here, compilation errors or runtime errors on the consumer espaces due to broken references may occur. | One needs to do 1-Click publishing of the producer modules to rebuild the producers' compilation cache. The best way is to build an all content solution in Service Center and publish it. |
| Partial compilation cache | This compilation cache is used during the creation of a personal test area for Debugging purposes. If missing, it shouldn't impact the debugging process. | By attempting to debug the module again, the partial content will be recreated again. |
| Release application files | These are the resulting OutSystems application files, mapped on the IIS application server. If they're missing the applications will go offline. There's an automatic internal thread maintaining the content on this folder, so it should never be deleted. | One needs to redeploy all modules again to restore the application files. This can be done by restarting the OutSystems Deployment Service on the server, or 1-Click publishing an all content solution in Service Center, or even use the re-deploy button for every module on Service Center. |
| Personal test area files  | These are the actual application files of the personal test areas for each module and developer. Deleting them will make the developer lose the ability to run/debug the application by accessing it on the web browser. | In order for the developer to restore it's own personal test area for that module, he needs to perform a run/debug from Service Studio again. |
| Temporary `Asp.Net` Files | These are the actual `ASP.NET` application files loaded in memory by IIS, and if in use, they can't be deleted until IIS is stopped. Deleting these files will cause a slower first load on the application. | Automatically generated by IIS upon the first access to the application. |

So, based on the tables above, and if you're concerned about disk space usage on your servers to the point of attempting to delete some content, do the following:

* Regularly (daily or weekly) clean up the **temporary `ASP.NET` files**.

* In the development environment, coordinate with your developers to clean up periodically (weekly or monthly) the **personal test area files** and eventually, the **partial compilation cache**

* Avoid deleting the **Full Compilation Cache** or the **Release Application Files** at all on a regular basis. If necessary on one particular occasion, and an all content solution publication is scheduled, you might want to coordinate with the involved teams, but keep in mind that deleting the release application files will cause application downtime, and should be scheduled accordingly.

## Let's talk numbers

Finally, let's try to pass on some highlights about some recommended disk sizes.

Estimating the disk space usage of a factory isn't easy since it depends greatly on the number of application objects or software units, eSpaces, and developers that work on one environment. Additionally, the type of application (and thus the resources included on that application) can really offset any metrics. From our experience, and considering the disk fragmentation impact on server performance, we recommend the following, based only on application objects / software units metric:

* 36 GB for small factories (< 250 application objects / 150 000 software units)

* 73 GB for medium size factories ( < 500 application objects / 300 000 software units)

* 146 GB for large size factories (> 500 application objects / 300 000 software units)

It has been more than enough so far, for both non-production and production environments. Ultimately, a good best practice is to install the Platform Server on a partition other than the system partition, to avoid system drive fragmentation.

## Automatic clean-up process for the release application files

The automatic cleanup process of the running directory is performed periodically by the OutSystems deployment service. The service will delete any folder within `<platformserver>\running\` that is currently not being used by any IIS virtual directory, and currently by default:

* On development environments (server mode = Development) it will clear any folder older than 15 minutes

* On production environments (server mode = Production) it will clear any folder older than 24 hours

The same service also deletes any compiled application files within `<platformserver>\repository\` that aren't being used by any application in that Front-End and that are older than 30 minutes.

If you have the need to tweak these values, you may reach out to OutSystems support for solutions on how to change the defaults.

Regarding the period of the cleanup thread, you actually can set it on the Monitoring page of Service Center, and if you access the deployment service details, you'll find the **Unused Folders Removal** thread and the time since the last execution.

Regarding the logs, you might find some General Logs from the (system) espace, related to this cleanup thread, if anything was deleted. [OSTrace](http://www.outsystems.com/goto/ostrace) (for on-premises environments only) also allows you to monitor this activity.
