---
summary: Invalid character in a page name when working with SEO. 
tags:
---

# Invalid Format

Service Studio shows **Invalid Format** errors when the page name contains invalid characters:

* Invalid Format | Page name can't start or end with special characters. Delete any special characters in the beginning or end of the page name and try again.
* Invalid Format | Page name can't include double slashes "//". Delete any double slashes in the page name and try again.

The **Page Name** property contains double forward slashes (`//`) or starts or ends with one the reserved special characters, and Service Center can't create the URL.

Check the examples of correct and incorrect **Page Names**:

| Correct   | Incorrect                   |
| --------- | --------------------------- |
| `Buy`     | `Buy!`                      |
| `About`   | `\\About`                   |
| `Product` | ` Product` (space at start) |


<div class="info" markdown="1">

This error is part of [SEO-friendly URLs for Reactive Web Apps](../../../develop/seo/intro.md).

</div>