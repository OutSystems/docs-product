---
summary: How to scale OutSystems container-based applications.
tags: support-Application_Lifecycle; 
--- 

# Scaling Container-deployed Applications 

To be able to scale OutSystems container-based applications you should follow the [application architecture recommendations](<intro.md#recommended-application-architecture-for-containers>) while developing and maintaining them.

In the sections below we present some general guidelines on how to scale OutSystems container-bound applications according to your hosting technology.

## Docker Containers

### Scale using Docker Swarm

In Docker Swarm you create a service for your application and then scale the created service. Follow these general steps:

1. Create and configure a swarm, adding and configuring as many nodes as needed, creating a swarm cluster;
1. Create a containers deployment zone using the address of the swarm cluster manager;
1. Associate the application to this deployment zone;
1. Publish the application, so that you can generate the container image;
1. Deploy the application as a service in the swarm cluster, specifying the required scalability parameters;
1. Configure the reverse-proxy for the swarm cluster to map the application URL to the application service in the swarm;
1. Finish the deployment.

Check the [Docker Swarm documentation](<https://docs.docker.com/engine/swarm/>) for more information.

### Scale using Kubernetes

Scaling in Kubernetes is done by specifying or changing the number of replicas in a deployment.

Follow these guidelines to use Kubernetes with OutSystems:

1. Create and configure a cluster, adding and configuring as many nodes as needed;
1. Create a containers deployment zone using the public address of the cluster;
1. Associate the application to this deployment zone;
1. Publish the application, so that you can generate the container image;
1. Deploy the application into the cluster, specifying the number of replicas;
1. Create a load balancer service for the application that you want to expose;
1. Create an ingress service for the application that you want to expose to map the application URL to the application service;
1. Finish the deployment.

We recommend you to check the official Kubernetes documentation for detailed instructions on [using Kubernetes with a cluster](<https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/>).

## Pivotal Cloud Foundry

Use the features provided by PCF to scale your application. Follow the instructions provided by Pivotal to [scale applications](<http://docs.pivotal.io/pivotalcf/2-1/console/manage-apps.html#scale>) manually or automatically (based on a set of rules or a schedule).
