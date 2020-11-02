---
summary: Check how you can gather information from your OutSystems applications running in containers.
tags: support-monitoring
---

# Monitoring Applications Running in Containers

<div class="warning" markdown="1">

Container deployment is available as an [Early Access Program](<https://www.outsystems.com/goto/technical-preview>).

</div>

All OutSystems application logs are available in Service Center, including logs for applications running inside containers.

If you need to obtain more information, check the corresponding section below according to your hosting technology.

## Docker Containers

If you need to get further information, retrieve it using the `docker logs` command. Check the [official documentation](<https://docs.docker.com/engine/reference/commandline/logs/>) for more information.

Additionally, the ["OutSystems-CollectInfo-wdocker" GitHub repository](<https://github.com/OutSystems/OutSystems-CollectInfo-wdocker>) contains some PowerShell scripts that will help you gather information from both the host machine and the container for troubleshooting purposes. Check the `README.md` file available in the repository for more information.

## Pivotal Cloud Foundry

If you need to get further information, you must retrieve it from Cloud Foundry Client or Pivotal Apps Manager.
