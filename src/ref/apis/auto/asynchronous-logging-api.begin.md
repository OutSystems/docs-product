---
summary: The Asynchronous Logging API provides actions to asynchronously insert records into the database or register request events of your applications in an asynchronous way.
tags: support-application_development; support-Application_Troubleshooting; support-devOps; support-monitoring
---

The Asynchronous Logging API provides actions to perform the following asynchronously:

* insert records into the database
* register request events of your applications

The record or request event gets added to a message queue. Then the OutSystems log service processes it, and adds it to the database.

The message queue is non-persistent. This means that in case of a system failure, pending records and request events get lost.

To use this API, simply reference the AsynchronousLogging module in your application.
