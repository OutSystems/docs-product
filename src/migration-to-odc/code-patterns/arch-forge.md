---
guid: 1986c6da-443a-438a-b144-f4db01b20a42
locale: en-us
summary: Learn how to solve the findings for the conversion code pattern "Asset consuming a Forge component".
figma: 
coverage-type:
  - unblock
topic: 
app_type: mobile apps,reactive web apps
platform-version: o11
audience:
  - architects
  - full stack developers
  - mobile developers
tags: Forge,forge,forge component,outsystems forge
outsystems-tools:
  - forge
  - odc portal
  - service studio
  - odc studio
helpids: 30555
---

# Asset consuming a Forge component

[Forge](https://www.outsystems.com/forge/) components are reusable software assets that help overcome technical challenges and solve business use cases. Forge is available in ODC via the ODC Portal. However, not all O11 Forge components are yet available in the ODC version.

## How to solve

This pattern can be solved in O11 or in ODC. Start by checking if the Forge component is already [available in ODC](https://www.outsystems.com/forge/list?q=&t=&o=latest-submitted&tr=False&oss=False&c=%20&a=&v=odc&hd=False&tn=&scat=forge).

If the Forge component that your asset consumes is **already available in ODC**, you can choose to [solve this pattern in ODC](#solve-in-odc).

If the Forge component that your asset consumes **isn’t yet available in ODC**, you should [solve this pattern in O11](#solve-in-o11).

### Solve in ODC

To solve this pattern in ODC:

1. Remove the reference to the O11 Forge component from any ODC asset.

1. Proceed with the conversion.

1. Once the consumer asset is converted to ODC, add the reference to the ODC Forge asset that offers the same functionality as the O11 Forge component your asset was consuming.

1. After adding the reference, fix any outstanding issues.

### Solve in O11

To solve this pattern in O11:

1. Clone the Forge component.

1. In the consumer modules, replace the O11 Forge component usage with your clone.

1. Map the clone into an ODC asset, so it is included in your O11 to ODC architecture mapping.

1. Proceed with the conversion.

By doing the above, your asset is no longer consuming an O11 Forge component. Instead, it is consuming the clone, which is also mapped to an ODC asset.

After converting the component, consider [submitting the asset to ODC Forge](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/forge/submit_assets_to_forge/).

<div class="info" markdown="1">

Note that, by cloning and converting the Forge component yourself, you’ll own it after the conversion. This means you'll have to consider any further improvements or bug fixing.

</div>
