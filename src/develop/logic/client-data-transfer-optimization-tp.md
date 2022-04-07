---
summary: Server-to-client data transfer optimization reduces the data the client-side of the app receive.
tags:
locale: en-us
guid: cad64443-6400-41a9-98e4-154162e790fa
---

# Server-to-client data transfer optimization

<div class="info" markdown="1">

Available in Platform Server 11.12.0 or later.

</div>

Server-to-client data transfer optimization uses a sophisticated data flow algorithm that analyses how the data flows and then optimizes the transfer from the server. It works in Mobile Apps and Reactive Web Apps.

With the optimization the apps receive only the information that users of the app need. This reduces the data that the app gets and improves the performance. In particular, the users of data-demanding apps with complex database joins should notice that the apps work faster. 

The optimization works for:

* Screen Aggregates
* Data Actions
* Server Actions in the logic of the client-side Screen Actions
