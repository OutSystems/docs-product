---
summary: LifeTime is the centralized console for managing the infrastructure, environments, applications, IT users, and security.
tags: support-Application_Lifecycle; support-Cloud_Platform; support-devOps; support-Infrastuture_Architecture-overview
locale: en-us
guid: 5f21d5c6-f612-4ac0-835d-3a468b82c45b
---

# Manage Your OutSystems Infrastructure

LifeTime is the centralized console for managing your OutSystems environments, applications, IT users, and security, covering the full application life cycle from development to deployment.

A typical OutSystems infrastructure comprises the following environments:

* **Development**: The environment where applications are initially developed and tested
* **Quality**: The environment where testers and business users experiment applications to perform quality assurance
* **Production**: The environment that hosts the application version end users interact with

You can manage your OutSystems infrastructure in the **INFRASTRUCTURE** tab of LifeTime console (`https://<your_lifetime_server>/lifetime`).

## Set up the infrastructure

To execute the initial setup of your OutSystems infrastructure in LifeTime, follow the instructions in [Configure the infrastructure management console](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/Configure_the_infrastructure_management_console>).

## Add or remove environments

At any time, you can add or remove environments to your OutSystems infrastructure in LifeTime.

To add a new OutSystems environment to your infrastructure, do the following:

1. Click the **Register an Existing Environment** link.
1. Register your environment as described in [Configure the infrastructure management console](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/Configure_the_infrastructure_management_console>).

To remove one of your OutSystems environments from the infrastructure:

* On OutSystems Cloud, contact OutSystems Support to remove or unregister an environment.
* In a self-managed infraestructure, do the following:

    1. Click the **Edit Environment** link for the environment you want to remove.
    1. Click the **Unregister environment** link.

## Switch the environments order

In an OutSystems Cloud infraestructure, contact OutSystems support and request to change the order of deployment.

In a self-managed infraestructure, you can switch the order of two environments in the infrastructure using the **Switch Order** icon placed between those environments.


![](images/manage-infrastructure-1.png)

## Manage an environment

To manage an environment individually, use the links available in each environment:

* **Environment Health**: To monitor the health of elements like timers, processes, or the status of the mobile apps build service. This link redirects to the Service Center console of the environment.
* **Configuration**: To configure the environment behaviors like the purpose of the environment in the infrastructure, date formats or building mobile apps. This link redirects to the Service Center console of the environment.
* **Environment Security**: To configure security settings for applications, like HTTPS or Content Security Policy.
* **Edit Environment**: To configure specific settings like the connection between the environment and LifeTime. You can enable or disable [maintenance mode](maintenance-mode.md) in an environment.
