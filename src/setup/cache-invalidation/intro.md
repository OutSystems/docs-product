---
summary: Check how cache invalidation works in OutSystems 11.
tags: article-page; version-11
helpids: 30176
---

# Cache Invalidation in OutSystems 11

Caching lets applications temporarily store a  subset of data making requests for the same data occur faster because reading data from cache is faster than reading the same data again from the database. Cache invalidation is the process where entries in the cache are replaced or removed.

OutSystems stores cached data in the application server's memory. OutSystems also stores a reference to the module that produced the data and the tenant where the module exists. To refresh cached data, cache invalidation operations are done for either a module or for a tenant. When cache invalidation runs, it checks each front-end server for old or stale data. If an old cached value is found, cache invalidation marks it as "dirty", and fetches new values from their original location.

Whenever a request is made, the application server gets the data required for processing from memory and, if that data doesn't exist or if it's marked as dirty, new data is fetched from the original source.

## How does it work?

The Cache Invalidation Service is the OutSystems component responsible for notifying front-end servers that cached values aren't up-to-date, forcing them to fetch new values when needed.

This service uses a publish/subscribe pattern: applications subscribe to queues that represent modules and tenants where data can come from. The underlying technology used by the Cache Invalidation Service is called **RabbitMQ**, a distributed message queue service that implements the publish/subscribe pattern.

You must configure the platform so applications can reach this service. You can install and configure a RabbitMQ instance using OutSystems Configuration Tool. Performing this operation installs RabbitMQ in the same machine that's running the Configuration Tool. Check the [Platform Server 11 Installation Checklist](<https://www.outsystems.com/goto/checklist-11>) for more information on how to install and configure the Cache Invalidation Service.

## When do I need High Availability? { #when-ha }

Every time a cache invalidation occurs for a module or a tenant, all applications watching for changes on these elements are notified, and they flag their local copies as dirty. When the Cache Invalidation Service is down or unavailable (for example, during configuration changes on this service), applications aren't notified of any cache invalidations that might have occurred. This may cause some inconsistent behavior until either these applications can reach the service again or new service configurations are applied. 

If your application makes use of [Object caching](https://success.outsystems.com/Documentation/11_x_platform/Developing_an_Application/Use_Data/Caching) or [Site Properties](https://success.outsystems.com/Documentation/11_x_platform/Developing_an_Application/Use_Data/Use_Site_Properties_to_Configure_Behaviors_at_Runtime) and has no tolerance to stale values of those objects or global variables in the case the Cache Invalidation Service is down or unavailable, you should consider configuring for high availability.

To improve the availability of the Cache Invalidation Service and mitigate the risk of a single point of failure you can [configure a RabbitMQ cluster and use a TCP load balancer](high-availability.md).
