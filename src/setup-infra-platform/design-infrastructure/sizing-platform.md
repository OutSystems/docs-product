---
summary: Learn to size and scale infrastructure for OutSystems 11 (O11) by evaluating application logic, user concurrency, data size, and integrations.
guid: 9fe9358a-9bfb-458d-bea1-c984ff641797
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: infrastructure scaling, performance optimization, application deployment, hardware recommendations, capacity planning
audience:
  - platform administrators
  - infrastructure managers
  - full stack developers
  - tech leads
outsystems-tools:
  - none
coverage-type:
  - evaluate
  - remember
---

# Sizing OutSystems Platform

<div class="info" markdown="1">

The information in this article applies only to **on-premises** or **private cloud** infrastructures.

</div>

To account for the expected impacts of scaling your applications, you need to know upfront which hardware best supports this growth.

There are four major factors you need to consider when sizing and [scaling OutSystems Platform](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures/03_Scaling_and_high_availability_for_OutSystems_Platform_servers):

1. **Application logic** - It keeps changing throughout the application life cycle from Development to Production. It has a major impact on server load.

1. **Concurrent Users** - The more users are using applications, the more HTTP connections are kept open to the web server and database. This is measured by the requests per second. How many requests per second can one user do? Verify against the application(s) being served.

1. **Data size** - Tends to grow in a predictable manner.

1. **Integrations** - Test all integrations on QA or Pre-Production environments for their response time. This gives you an idea of how they will behave in Production and of the impact on the application response time.

The following hardware recommendations ensure that your infrastructure is properly sized.

## Production environment

### Application server

The recommendations below apply to any of the [server roles](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures/01_OutSystems_Platform_server_roles) you have in your OutSystems infrastructure.

#### Mobile and Reactive Web

The table below indicates the recommended setup for application servers hosting mainly Mobile or Reactive Web Apps:

| **# Requests per second** | **120 (\*)** | **250 (\*)** | **250+** |
|---------------------------|--------|--------|---------|
| **Recommended setup**     | - Dual Core CPU<br/> - 4 GB RAM<br/> - 80 GB HD (Dedicated) | - Quad Core CPU<br/> - 8 GB RAM<br/> - 80 GB HD (Dedicated)| Horizontal grow with multiple server building blocks with the same specs.|

(\*) Values taken from tests executed with a CRUD application. Load tests are strongly recommended with a working version of the application that will be served by the systems. Variations are expected.

#### Traditional Web

The table below indicates the recommended setup for application servers hosting mainly Traditional Web Apps:

| **# Requests per second** | **40** | **60** | **60+** |
|---------------------------|--------|--------|---------|
| **Recommended setup**     | - Dual Core CPU<br/> - 4 GB RAM<br/> - 80 GB HD (Dedicated) | - Quad Core CPU<br/> - 8 GB RAM<br/> - 80 GB HD (Dedicated)| Horizontal grow with multiple server building blocks with the same specs.|

### Database server

The table below indicates the recommended setup for database servers:

| **# Transactions per second** | **250 (\*)** | **400 (\*)** | **400+** |
|-------------------------------|-------------|-------------|----------|
| **Recommended setup**         | - Dual Core CPU (4 threads)<br/> - 16 GB RAM| - Quad Core CPU<br/> - 32 GB RAM| Vertical grow with SQL Server. (\*\*)<br/> Horizontal grow with Oracle RAC. (\*\*)|

(\*) Values taken from tests executed with a CRUD application. Variations are expected according to development, query optimization, and database system tuning by a database administrator. Load tests are strongly recommended with a working version of the application that will be served by the systems.

(**) You may use other scalability approaches. Please check [OutSystems system requirements](https://success.outsystems.com/Documentation/11/Setting_Up_OutSystems/OutSystems_system_requirements) and contact your database administrator.

## Development environment

If you have many developers (16+) or you detect slowness in your non-production environment, you might want to use a dedicated Deployment Controller server to segregate the code compilation process.

| **# Active developers** | **5+** | **8+** | **16+** |
|-------------------------|--------|--------|---------|
| **Recommended setup** | **Front-end + Deployment Controller:**<br/> - Dual Core CPU<br/> - 8 GB RAM<br/> - 100 GB HD (Dedicated)| **Front-end + Deployment Controller:**<br/> - Quad Core CPU<br/> - 12 GB RAM<br/> - 200 GB HD (Dedicated)| **Front-end:**<br/> (Where the developers connect to)<br/> - Quad Core CPU<br/> - 12 GB RAM<br/> - 300 GB HD (Dedicated)<br/><br/> **Deployment Controller:**<br/> (Where code compilation occurs)<br/> - Quad Core CPU<br/> - 16 GB RAM<br/> - 500 GB HD (Dedicated)|
| **Additional developer** | - 0.25 core<br/> - 512 MB RAM<br/> - Up to 8 Developers| - 0.25 core<br/> - 0.5 GB RAM<br/> - Up to 16 Developers| **Front-end:**<br/> (Where the developers connect to)<br/> - 0.25 core<br/> - 0.5 GB RAM<br/><br/> **Deployment Controller:**<br/> (Where code compilation occurs)<br/> - 0.25 core<br/> - 0.5 GB RAM |

## Single server versus farm architecture

For critical Production and Development sites, OutSystems recommends a farm architecture.

Single-server architectures depend on the available technology upgrades at the time. Additionally, a single server that is super powerful may cost ten times as much as two servers with half the capabilities.

On the other hand, a farm architecture guarantees reliability and uptime in failure or maintenance events. That's not possible with a single server.

## More information

To learn more about how to set up your OutSystems infrastructure, check the [Designing OutSystems infrastructures guide](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Designing_OutSystems_Infrastructures).

