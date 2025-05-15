---
summary: Explore infrastructure design examples for OutSystems 11 (O11) tailored for on-premises or private cloud deployments.
guid: 48d54fc2-feb6-4aeb-ad2a-d40b306757f5
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/ZDYZVg9kmMXl758XX7ytXc/Setup-and-maintain-your-OutSystems-Infrastructure?node-id=3011-805&t=GvLiKHXITRsPv8hn-1
tags: infrastructure design, on-premises deployment, private cloud deployment, high availability, sql server
audience:
  - platform administrators
  - infrastructure managers
  - architects
  - full stack developers
  - tech leads
outsystems-tools:
  - service studio
  - platform server
coverage-type:
  - evaluate
---

# Infrastructure design examples

<div class="info" markdown="1">

**Important:** The information in this guide applies only to OutSystems Platform on-premises or private cloud deployments.

</div>

<div class="info" markdown="1">

Some parts of this content may look out of context without reading the remaining content in this section. Please make sure to read the [whole section](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures) for complete understanding of the topics discussed here.

</div>

The following examples display typical scenarios and are applicable only to self managed infrastructures.

## Example 1: Non-productive environments

The following diagram represents a development portion of an OutSystems  factory with a team of 8 developers and a **Quality Assurance** environment.

Since predicted team growth was considered in advance, a dedicated **Deployment Controller** was set up and the development database was isolated on a dedicated SQL Server instance.

![Diagram of a non-productive OutSystems infrastructure with development and quality assurance environments, including a dedicated deployment controller and isolated databases.](images/infra-design-example1-diag.png "Non-productive Environments Infrastructure Diagram")

## Example 2: Production environment

The following example depicts a .NET Production environment with 3 **Front-ends**. These machines are serving requests through a load balancer and on top of a SQL Server database cluster for high availability.

![Diagram of a .NET production environment for OutSystems with three front-ends, a load balancer, and a SQL Server database cluster for high availability.](images/infra-design-example2-diag.png "Production Environment Infrastructure Diagram")

## Example 3 - LifeTime environment

This example shows a standard **LifeTime** setup.

![Diagram showing a standard LifeTime setup for OutSystems with a front-end server and a dedicated database server.](images/infra-design-example3-diag.png "LifeTime Environment Infrastructure Diagram")

## Example 4 - Production environment with zones

An OutSystems zone is a logical separation of applications across **Front-ends** within the same infrastructure. Each zone is paired with network security segments that are isolated from the remaining network.

This example shows an environment with isolated zones for public access, for partners via a secure VPN, and for internal users.

![Diagram of an OutSystems production environment with isolated zones for public access, partners via secure VPN, and internal users, including front-ends and load balancers.](images/infra-design-example4-diag.png "Production Environment with Zones Infrastructure Diagram")

## More information

To learn more about how to set up your OutSystems Platform check the [Designing OutSystems infrastructures guide](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures).


