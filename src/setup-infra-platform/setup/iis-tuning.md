---
summary: OutSystems 11 (O11) tuning guide for IIS focuses on optimizing thread management for on-premises deployments.
guid: 9705fd12-e670-49a6-b669-b2a52a7bbe94
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: iis configuration, performance optimization, thread management, system administration, on-premises deployment
audience:
  - platform administrators
  - infrastructure managers
  - backend developers
outsystems-tools:
  - none
coverage-type:
  - evaluate
---

# Tuning IIS for OutSystems

<div class="info" markdown="1">

**Important:** The information in this guide applies only to OutSystems Platform on-premises or private cloud deployments.

</div>

ASP.Net allows system administrators to manage aspects of the ASP.NET worker process. Examples include the size of the CLR thread pool to service requests, and the number of instances created at a time. 


The element to configure these behaviors is the **processModel** element, present in the machine.config.
All configurations should start with the parametrization `<processModel autoConfig="true" />`


This is set by the OutSystems platform when running the configuration tool. By setting the **autoConfig** to true, IIS worker process will manage the following attributes:

* maxWorkerThreads;
* maxIoThreads;
* minFreeThreads;
* minLocalRequestFreeThreads;
* maxConnection.

IIS worker process will manage these attributes by controlling their values. Therefore, the values assigned to these attributes will be irrelevant once autoConfig is set to true. 

The values of the attributes above are set based on the following rules:

* maxWorkerThreads = 100 (per CPU)
* maxIoThreads = 100 (per CPU)
* minFreeThreads = 88 x `<Number of CPUs>`
* minLocalRequestFreeThreads = 76 x `<Number of CPUs>`
* maxConnection = `Int32.MaxValue`

Even though setting autoconfig to true is the recommended setting, this doesn't work well with bursts of requests. IIS worker process analyses its state in a period of time too slow for it to react to handle a burst of requests. This configuration works better in steady increases in the workload. 

* **minIoThreads**: to a value between `89` and `<maxIoThreads>`
* and **minWorkerThreads**: to a value between `89` and `<maxWorkerThreads>`


To further explain these values: 

* The minimum should be `89` because we shouldn't have fewer threads configured than the 88 in the **minFreeThreads**
* The maximum values should be `<maxIoThreads>` and `<maxWorkerThreads>` (set by default to 100 per CPU) because it's the maximum value for the number of Io and worker threads.

<div class="info" markdown="1">

Since Platform Server 11.10.0 the values of **minIoThreads** and **minWorkerThreads** are automatically set by configuration tool to 100. However, you may need to tune them further. If the values are already set by the system administrator, configuration tool will honor them.

</div>

The **minWorkerThreads** and **minIoThreads** define the minimal number of threads the IIS worker process will spin up in a short amount of time. After this threshold is reached, spinning up a new thread takes longer. This is the point referred above about the adaptive nature of the autoConfig attribute. Under unusual circumstances, like a burst of requests, the request count can go up quickly making IIS struggle to spin new threads leading to queued requests. This point is important because OutSystems’ Mobile and Reactive applications are "bursty" in nature. Accessing a single page can generate multiple requests in burst to the server. If you have a Front End dedicated to one of these types of applications, tuning **minWorkerThreads** and **minIoThreads** values is of particular importance.

<div class="info" markdown="1">

Changes to the **ProcessModel** element are only effective after restarting the IIS worker service.

</div>

Now, lets see the impact of setting the values of **minIoThreads** and **minWorkerThreads** in a front end. For clarity, let's assume we have a front end with 4 CPUs and that we set minIoThreads and minWorkerThreads to 100, what we are saying is that the IIS worker process will be fast to spin up 100 threads per CPU and have them ready to handle requests. This implies that if we take the magic thread number of 88 into account, we have 12 "dedicated" threads to handle requests per CPU. Meaning that with this configuration, your Front End would have 48 threads capable of handling requests in parallel available at the start of the worker process.

A note, we suggest that **minIoThreads** and **minWorkerThreads** attributes share the same value.

Increasing the number of threads readily available to handle requests impact the overall system. More requests handled per second means that the resources (databases, external SOAP and REST services, for example) that support those requests are also under increased load. For this reason there are some considerations when tweaking the values of **minIoThreads** and **minWorkerThreads** attributes:

* By default OutSystems sets the Max Pool Size to 100. If your configuration is capable of more than 100 request in parallel you can exhaust all the connections in the pool.
* Every service connected to or consumed by the application will have it’s load increased.
* For OutSystems 10, you might need to increase the message queue size.
