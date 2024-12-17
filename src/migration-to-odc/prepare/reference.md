---
summary: This article provides detailed reference tables comparing code elements and database type mappings between O11 and OutSystems Developer Cloud (ODC) apps and libraries, aiding in migration planning.
locale: en-us
guid: d94495a3-acd0-4030-bc6c-acedbf794702
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: cloud migration, database mapping, application modernization, migration planning, outsystems development
audience:
  - mobile developers
  - frontend developers
  - full stack developers
  - architects
  - platform administrators
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Reference

This page consists of reference information to move your O11 apps to the cloud-native ODC types of apps.

## Application code elements reference tables

This section contains information about O11 vs. ODC applications-related reference tables on Code Elements.

### Code elements in App layer tabs at the module and application level

The following table represents information about the Code Elements availability in O11 (Traditional module) vs O11 (Reactive Module and Service Module) vs ODC (Application) in App layer tabs.

**Application code elements available in the Processes App layer tab**

| Code Elements |O11 (Traditional web) | O11 (Reactive Module) | O11 (Service Module) | ODC (Application) |
|---------------|--------------------|---------------------|--------------------|-----------------|
| Timer | Yes | Yes | Yes | Yes |
| Processes (BPT) | Yes | Yes | Yes | N/A |

**Application Code Elements available in the Interface App layer tab**

| Code Elements | O11 (Traditional web) | O11 (Reactive Module) | O11 (Service Module) | ODC (Application) |
|---------------|----------------|---------------------|--------------------|-----------------|
| Flow (Traditional) | Yes | N/A | N/A| N/A| 
| Screen (Traditional)| Yes | N/A | N/A| N/A| 
| External Site (Traditional)| Yes | N/A | N/A| N/A| 
| Block (Traditional)| Yes | N/A | N/A| N/A| 
| Theme (Traditional)| Yes | N/A | N/A| N/A| 
| UI Flow | Yes | Yes | N/A | Yes |
| Screen | Yes | Yes | N/A | Yes |
| External Site | Yes | Yes | N/A | Yes |
| Block |Yes | Yes | N/A | Yes |
| Image | Yes |Yes | N/A | Yes |
| Theme | Yes | Yes | N/A | Yes |
| Script | Yes | Yes | N/A | Yes |
| Email | Yes | Yes | N/A | Yes |

**Application Code Elements available in the Logic App layer tab**

| Code Elements | O11 (Traditional Web) | O11 (Reactive Module) | O11 (Service Module) | ODC (Application) |
|---------------|----------------|---------------------|--------------------|-----------------|
| Server Action | Yes | Yes | Yes | Yes |
| Client Action | N/A |Yes | Yes | Yes |
| Service Action | N/A | N/A | Yes | Yes |
| Rest Expose | Yes |Yes | Yes | Yes |
| Rest Consume | Yes |Yes | Yes | Yes |
| Role | Yes | Yes | Yes | Yes |
| Exception | Yes | Yes | Yes | Yes |
| SOAP Expose | Yes | Yes | Yes | N/A |
| SOAP Consume | Yes | Yes | Yes | N/A |
| Extension | Yes | Yes | Yes | N/A |
| SAP | Yes | Yes | Yes | N/A |

**Application Code Elements available in the Data App layer tab**

| Code Elements | O11 (Traditional web) | O11 (Reactive Module) | O11 (Service Module) | ODC (Application) |
|---------------|---------------|---------------------|--------------------|-----------------|
| Entity | Yes | Yes | Yes | Yes |
| Static Entity | Yes | Yes | Yes | Yes |
| Entity Diagram | Yes | Yes | Yes | Yes |
| Structure | Yes | Yes | Yes | Yes |
| Site Prop/Settings | Yes | Yes | Yes | Yes |
| Resource | Yes | Yes | Yes | Yes |
| Session Variable | Yes | N/A | N/A | N/A |
| Client Variable | N/A | Yes | N/A | Yes |
| Translations | Yes | Yes | Yes | Yes |


## Library Code Elements reference tables

This section consists of information about O11 vs ODC libraries related reference tables on Code Elements.

### Library Code Elements in App layer tabs

The following table represents information about the Library Code Elements availability in O11 (Library Module) vs ODC (Library) in App layer tabs.

**Library Code Elements available in the Interface App layer tab**

| Code Elements | O11 (Library Module) | ODC (Library) |
|---------------|:--------------------:|:-------------:|
| UI Flow | Yes | Yes |
| External Site | Yes | Yes |
| Block | Yes | Yes |
| Image | Yes | Yes |
| Theme | Yes | Yes |
| Email | Yes | Yes |

**Library Code Elements available in the Logic App layer tab**

| Code Elements | O11 (Library Module) | ODC (Library) |
|---------------|:--------------------:|:-------------:|
| Server Action | Yes | Yes |
| Client Action | Yes | Yes |
| Rest Consume | Yes | Yes |
| Exception | Yes | Yes |
| SOAP Consume | Yes | No |
| Extension | Yes | No |
| SAP | Yes | No |

**Library Code Elements available in the Data App layer tab**

| Code Elements | O11 (Library Module) | ODC (Library) |
|---------------|:--------------------:|:-------------:|
| Static Entity | Yes | Yes |
| Entity Diagram | Yes | Yes |
| Structure | Yes | Yes |
| Site Prop/Settings | Yes | Yes |
| Resource | Yes | Yes |
| Translations | Yes | Yes |

## Database type mapping

This section maps the ODC data type to Aurora PostgreSQL database type.

| ODC Type | DB Type |
|----------|:-------|
| Text | Varchar  (if length <= 2000) |
| Text | Text (if length > 2000) |
| Binary Data | byte |
| Boolean | numeric(1) |
| Integer | integer |
| Long Integer | bigint |
| Decimal | numeric |
| DateTime, Date & Time | timestamp |
