---
locale: en-us
guid: 59ec2532-1c5b-4011-a042-2edd112da5b0
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Possible Data Loss Warning

Message
:   `The [parameter_name] parameter in SAP is of [parameter_type] type, and is mapped to Decimal. This can result in data loss. Review if your data fits into the boundaries of the Decimal data type`

Cause
:   The parameter mentioned in the warning can have values that are out of the range of the Decimal data type of OutSystems. As the parameter is currently mapped to Decimal, this can lead to the following behavior:

    * If the remote function receives a value lower than -2<sup>96</sup>+1, or higher than 2<sup>96</sup>-1, you receive an error message at runtime.
    * If the received value is longer than the number of digits that the system supports, it will be rounded to the maximum length.

Recommendation
:   Check if your SAP data contains values that lead to the above situations. To avoid them, you can use Text data type instead of Decimal.