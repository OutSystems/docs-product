---
summary: Upgrading the cache invalidation service in a fault-tolerant environment.
tags: version-11; support-Installation_Configuration
locale: en-us
guid: 54a92414-2911-11ed-b1a1-00155d847f89
app_type: traditional web apps, mobile apps, reactive web apps
---

# Upgrade OutSystems cache invalidation with high-availability

This guide shows how to upgrade your [previously created RabbitMQ
cluster](high-availability.md).

There are two strategies for upgrading a simple RabbitMQ cluster. They're
described with the pros and cons of each. The first is the more recommended
approach:

* Cluster Full-Stop

    * Pros

        * The process is more secure

        * The process updates the data in queues

    * Cons

        * The process has downtime

* Rolling Upgrade

    * Pros

        * No downtime is necessary

    * Cons

        * If your current RabbitMQ version is older than 3.7.18, you’ll need to proceed with an intermediary upgrade to version 3.7.18 and then to 3.8.3. Version 3.7.18 and later 3.7.x versions support rolling upgrades with feature flags allowing mixed-version clusters

        * The process includes an Erlang upgrade, which recreates the queues

<div class="info" markdown="1">

Ensure the new Erlang version is compatible with the RabbitMQ version being
installed. See [here](https://www.rabbitmq.com/which-erlang.html) for details.
The RabbitMQ version needs to fulfill your OutSystems [system
requirements](../system-requirements.md).

</div>

During upgrades, it's helpful to do a HealthCheck at various moments. The
management UI enables this. A [management
plugin](https://www.rabbitmq.com/management.html) installation is required. A
HealthCheck is done at http://localhost:15672 (15672 is the default port, you
may have configured it differently). Alternatively, go to the `sbin` folder
under the RabbitMQ installation directory and use the command `rabbitmqctl
cluster_status`.

## Cluster Full-Stop upgrade strategy

In this example, a simple RabbitMQ cluster with two nodes running on separate
servers, “ServerA” and “ServerB,” is upgraded. This strategy requires a
cluster full-stop, and so downtime is expected. The order of server upgrades is
important. Proceed with the following approach:

* Do a health check

* Stop the nodes

    * For each server, open a command line with administrator privileges,
change the working directory to the sbin folder and run the following command:
`rabbitmqctl stop_app` (there is a possibility that you have to specify the
node, add `--node rabbit` at the end of the previous command)

* Upgrade the first node

    * Uninstall the old version of Erlang

    * Install the new version of Erlang

    * Install the new RabbitMQ version

* Upgrade the second node

    * Uninstall the old version of Erlang

    * Install the new version of Erlang

    * Install the new RabbitMQ version

* Start the first node

    * `rabbitmqctl start_app`

* Start the second node

    * `rabbitmqctl start_app`

* Perform a health check

## Rolling upgrade strategy

Rolling upgrades between some versions are unsupported. Version 3.7.18 and
later 3.7.x versions support rolling upgrades to 3.8.x using feature flags. For
more information about upgrade version jumps, without downtime, check
[here](https://www.rabbitmq.com/upgrade.html).

We highly recommend that you do a full-stop upgrade if coming from versions
earlier than 3.7.18 and intend to do a major upgrade. Check if your upgrade is
supported [here](https://www.rabbitmq.com/upgrade.html#rolling-upgrades).

In this example, a simple RabbitMQ cluster with two nodes
running on separate servers, "ServerA" and "ServerB," is upgraded.

* Do a health check

* Stop the first node

    * Go to the `sbin` folder and execute `rabbitmqctl` stop_app

* Upgrade the first node

    * Uninstall the old version of Erlang
    * Install the new version of Erlang
    * Install the new RabbitMQ version

* Start the first node

    * Go to the `sbin` folder and execute `rabbitmqctl start_app`

* Do a health check

* Stop the second node

    * Go to the `sbin` folder and execute: `rabbitmqctl stop_app`

* Upgrade the second node

    * Uninstall the old version of Erlang
    * Install the new version of Erlang
    * Install the new RabbitMQ version

* Start the second  node

    * Go to the `sbin` folder and execute `rabbitmqctl start_app`

* Do a health check
