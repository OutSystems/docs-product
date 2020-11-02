---
tags: support-devOps; support-Security; support-Security-featured; runtime-traditionalweb
---

# Restrict Access to an Internal Network

<div class="info" markdown="1">

We’ve been working on this article. Please let us know how useful this new version is by voting.

</div>

You can tighten the security of your applications, or part of them, by only allowing the access to end users who have authenticated themselves in an IP belonging to an internal network.

You can restrict internal network access to the following elements:

* UI Flows of a Web application (restricts the access of the Web Screens within the Flow)
* Exposed SOAP Web Services
* Exposed REST APIs

To restrict these elements to internal network access, set its **Internal Access Only** property to `Yes`.

![restrict internal network](images/internal-network-set-ss.png)
