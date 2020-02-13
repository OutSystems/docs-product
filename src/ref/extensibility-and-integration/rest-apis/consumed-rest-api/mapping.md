---
tags: 
---

# Mapping REST Data Types to OutSystems Data Types

When [consuming REST API Methods](<../../../../extensibility-and-integration/rest/consume-rest-apis/consume-a-rest-api.md>) in your module, OutSystems automatically generates the Structures for the Request and Response from the example you provide for them and maps the attributes into OutSystems Data Types as follows:

JSON example  |  OutSystems Data Type  |  Comments  
---|---|---  
`{"quantity": 123456789}`  |  Long Integer  |  Highest value: 2^63-1  
`{"totalprice": 12345678901, "amount": -3935.120}`  |  Decimal  |  If the value is an integer, but greater than or equal to 2^63, a decimal parameter is created.  
`{"createdon": "2014-12-31T23:59:59+01:00", "shippedon": "2015-01-01T19:00:00.256"}`  |  Date Time  |  If the ISO date contains information about the time zone, it is automatically converted to the local time of the server, with daylight savings applied.  
`{"scheduledstart": "/Date(1388534400000)/"}`  |  Date Time  |  WCF format  
`{"createdon": "2014-12-24"}`  |  Date  |  Format: YYYY-MM-DD  
`{"canupdate": true}`  |  Boolean  |  
`{"name": "Christine Sharp"}`  |  Text  |  
  
Data that cannot be converted to one of the above data types is converted to
Text.
