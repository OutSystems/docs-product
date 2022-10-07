---
summary: This article describes how to ensure your OutSystems Installation on Azure using custom Azure Resource Manager (ARM) templates is associated with OutSystems.
locale: en-us
guid: fc966397-ce73-4217-bc1d-7a048bd65347
app_type: traditional web apps, mobile apps, reactive web apps
---

# Plan to Associate your OutSystems Installation on Azure with OutSystems

## Overview

OutSystems is a Microsoft ISV partner and as such, OutSystems has [templates available on the Azure Marketplace](https://azuremarketplace.microsoft.com/en-ca/marketplace/apps?search=outsystems&page=1) to make the installation process quick and seamless for Azure users. If you are just starting the installation process, you should leverage the standard OutSystems templates for your install.

If you plan to create your own Azure Resource Manager (ARM) templates to install OutSystems on Azure specific to your organization’s requirements, OutSystems and Microsoft won’t know that those underlying compute resources (VMs, Gateways, Storage, etc.) are associated with your OutSystems installation.

This article describes how to ensure your new installation is associated with OutSystems. Associating your installation on Azure with OutSystems will help us better support customers on Azure by understanding the data behind the installations, usage patterns, and ultimately working with Microsoft to fine-tune the experience.

## Adding OutSystems to your Custom ARM Template

Add the following resource definition to your templates resources section in the **mainTemplate.json** file:

```json
"resources": [
    {
        "apiVersion": "2018-08-01",
        "name": "pid-06762eb7-d82e-42b0-abbe-70552888340b",
        "type": "Microsoft.Resources/deployments",
        "properties": {
            "mode": "Incremental",
            "template": {
                "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
                "contentVersion": "1.0.0.0",
                "resources": []
            }
        }
    },
    ...
]
```
