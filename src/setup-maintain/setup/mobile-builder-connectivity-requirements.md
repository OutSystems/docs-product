---
summary: Meeting Mobile Apps Build Service (MABS) requires access to Amazon CloudFront. Check out this document for information on how to use a proxy or firewall to ensure that MABS works correctly.
locale: en-us
guid: 9b32edb6-a14d-46d5-b180-10b6bc0eff3f
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Meeting Mobile Apps Build Service connectivity requirements

The Mobile Apps Build Service (MABS) is an OutSystems cloud service for building native mobile apps. Thanks to MABS, all Android and iOS mobile building tools run in the cloud.

MABS uses **nativebuilder.api.outsystems.com** as the hostname. The service is available 24x7 to all customers around the world. MABS needs to be low-latency, scalable, and redundant. To meet these requirements, OutSystems has built MABS on top of Amazon CloudFront and related Amazon technologies.

These are important notes about MABS network requirements:

* Any server with the front-end role needs to have access to MABS.
* The platform always initiates connection to MABS.
* As part of the distributed architecture of the platform, you can't control which front-end accesses MABS and when.

You may have security policies in place and want to limit, as much as possible, network access to outside resources and APIs. This document offers guidelines for meeting MABS network requirements while complying with security policies. Your solution depends on your infrastructure and potential restrictions. For added security, you can combine the approaches from this document. For example, use a proxy server and control access to the API via a firewall.

If you have any questions on whether a specific approach would work in your case, feel free to reach out to [OutSystems Support](https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support).

## Use a proxy

Amazon CloudFront, which MABS uses, is a distributed service with the endpoint IP addresses that can change over time. You may allow access to an external service in your organization by opening an exception to a specific IP in the firewall, but this approach isn't viable with Amazon CloudFront.

The simplest, and potentially most secure way, of meeting this requirement and is a proxy. When using a proxy to mediate the access with the internet, ensure it allows access to the **nativebuilder.api.outsystems.com** URL and any other URL the MABS service might require from the Internet for normal functioning.

## Use a firewall to limit access to a domain

If you have a firewall which allows limiting access by domain, use the firewall to limit access to the MABS domain. This opens your infrastructure only to the Cloud Front's IPs.

## Use a firewall to limit access to IPs

If you don't have a proxy or a firewall to restrict access to a specific domain, you need to get the list of relevant Amazon CloudFront IPs and allow access to it on your firewall.

Amazon provides a JSON with the [list of IP ranges their services use](http://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html). You only need to provide access to the ones used by the CloudFront service. Search in the JSON for CLOUDFRONT, as mentioned in [Locations and IP address ranges of CloudFront edge servers](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html).


