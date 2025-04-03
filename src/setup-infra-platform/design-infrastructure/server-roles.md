---
summary: Explore server roles in OutSystems 11 (O11) for effective infrastructure design in on-premises or private cloud deployments.
guid: 729b4d15-ee4c-4e1e-8ac7-8a487818703b
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/ZDYZVg9kmMXl758XX7ytXc/Setup-and-maintain-your-OutSystems-Infrastructure?node-id=3010-682&t=GvLiKHXITRsPv8hn-1
tags: infrastructure design, server roles, on-premises deployment, private cloud deployment
audience:
  - platform administrators
  - infrastructure managers
  - full stack developers
  - architects
outsystems-tools:
  - platform server
coverage-type:
  - evaluate
  - understand
---

# OutSystems Platform Server Roles

<div class="info" markdown="1">

**Important:** The information in this guide applies only to OutSystems Platform on-premises or private cloud deployments.

</div>

<div class="warning" markdown="1">

Some parts of this content may look out of context without reading the remaining content in this section. Please make sure to read the [whole section](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures) for complete understanding of the topics discussed here.

</div>

An understanding of the existing server roles is key to design the OutSystems platform infrastructure. A server can have more than a role, or you can use a single server/single role approach, but each environment needs the following roles:

## Front-end Role

***

![Illustration of the Front-end server role in OutSystems infrastructure, showing its functions and resource distribution.](images/server-roles_0.png "Front-end Server Role")

**Front-end** role handles both application logic and delivery to end-user. It can be installed as a standalone server or sharing a server
with one of the following roles:

* **Deployment Controller**
* **Scheduler**

The Front-end resource usage is distributed through the CPU, Memory and Network as follow:

* Application logic runs on CPU resources.
* Application objects need to be held in memory to ensure fast content delivery.
* Network delivers content according to communication throughput demand.

***

## Deployment Controller Role

***

![Diagram of the Deployment Controller server role in OutSystems infrastructure, detailing its responsibilities and resource usage.](images/server-roles_1.png "Deployment Controller Server Role")

The ***Deployment Controller*** handles the application compilation for deployment in Front-ends and license validation.
Each of the following environments must have one server with this role:

* **Development**
* **Quality Assurance**
* **Pre-Production**
* **Production**

The Deployment Controller can be installed as a standalone or sharing a server with a **Front-end Role**.

When compiling application code, its resource usage depends on:

* CPU for each application compilation process that consumes resources on one core.
* Memory for each compilation process.
* Network to deliver compiled applications to **Front-ends**.

***

## Scheduler Role

***

![Graphic representation of the Scheduler server role in OutSystems infrastructure, highlighting its purpose and CPU resource consumption.](images/server-roles_2.png "Scheduler Server Role")

The **Scheduler** role provides asynchronous execution of background tasks called timers, BPT processes and outbound email to an
SMTP server.

It is activated by default in all **Front-ends** but can be deactivated in the Service Center administration console.

It is possible to select which Front-ends also have this role in the Service Center administration console on the **Front-end** servers
menu in the Administration top menu.

The resource consumption of the Scheduler role happens at CPU level only and depends on the timer and BPT logic.


## More Information

To learn more about how to set up your OutSystems Platform check the [Designing OutSystems infrastructures guide](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures).

<div class="info" markdown="1">


**Important:** The information in this article applies only to OutSystems Platform on-premises or private cloud deployments.
</div>
