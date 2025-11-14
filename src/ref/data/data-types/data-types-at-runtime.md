---
summary: Explore how OutSystems 11 (O11) maps its data types to .NET data types at runtime.
tags: data mapping, .net integration, data types, application development, outsystems best practices
locale: en-us
guid: 671a69c4-3fe2-4a6a-9627-2eae9526aece
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# Data Types at Runtime

OutSystems maps its data types to .NET at runtime. You can check the
mapping done in the following table:

| OutSystems data types  |  .NET data types  |
| ---|---|
| Text | System.String |
| Integer | System.Int32 |
| Long Integer | System.Int64 |
| Decimal | System.Decimal |
| Boolean | System.Boolean |
| Date Time | System.DateTime |
| Date | System.DateTime |
| Time | System.DateTime |
| Phone Number | System.String |
| Email | System.String |
| Binary Data | System.Byte [] |
| Currency | System.Decimal |
| Object | System.Object |
| Entity Reference Integer | System.Int32 |
| Entity Reference Long Integer | System.Int64 |
| Entity Reference Text | System.String |
