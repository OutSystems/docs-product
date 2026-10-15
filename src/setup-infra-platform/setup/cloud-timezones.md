---
summary: OutSystems platform time zones use UTC, so you keep server, database, and display times consistent across O11 and ODC.
tags:
  - Data
  - Debugging
  - Forge
  - Infrastructure
  - Settings
locale: en-us
guid: 77232a2e-2305-4174-b25f-492f13b60b55
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
coverage-type:
  - understand
audience:
  - Front-end developer
  - Developer
  - Platform administrator
outsystems-tools:
  - service studio
  - forge
isautopublish: true
---

# OutSystems Cloud and time zones

The OutSystems platform requires the front-end servers and databases in an environment to use the same time, with only small offsets. For more details, refer to [Timezone considerations in the OutSystems platform](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Timezone_considerations_in_the_OutSystems_Platform).

## OutSystems 11

All servers in OutSystems Cloud are set to the UTC time zone. You cannot change this configuration.

Applications that must deal with time zone differences from UTC need to account for them from the early phases of development. You can use the Timezone forge component (unsupported) or other techniques to achieve the same result.

## OutSystems Developer Cloud

OutSystems Developer Cloud (ODC) also uses UTC for date and time values. Date and time values are saved and retrieved in UTC, and ODC Studio shows UTC in the debugger.

For self-hosted ODC environments, the database instance time zone must be set to UTC so that date and time handling stays consistent across all ODC components.
