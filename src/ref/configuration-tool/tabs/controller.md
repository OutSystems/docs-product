---
summary: Explore the communication settings between front-end servers and the deployment controller server in OutSystems 11 (O11) using the Controller tab.
locale: en-us
guid: 34809e50-82d5-4e93-a02e-a3bab8811b5d
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3301-122&p=f&t=pRvxEDvINAxPgBYK-0
tags: configuration, deployment, outsystems platform, server settings, application deployment
audience:
  - Platform administrator
  - Front-end developer
  - Developer
outsystems-tools:
  - service center
  - platform server
coverage-type:
  - remember
isautopublish: true
---

# Controller tab

In the **Controller** tab you define how front-end servers and the deployment controller server communicate.

![Screenshot of the Controller tab in the Configuration Tool](images/controller-tab-ct.png "Controller tab")

| Configuration | Description | Default value |
| -------------- | -------------- | --------------- |
| Deployment Controller Server | The hostname or IP address of the deployment controller server. | `localhost` |
| Deployment Controller Service Port | Port used by the Deployment Controller Service, in the Deployment Controller Server. | `12000` |
| Deployment Service Primary Port | Primary port used by the Deployment Service, in the Front-end Servers. | `12101` |
| Deployment Service Secondary Port | Secondary port used by the Deployment Service, in the Front-end Servers. | `12001` |
