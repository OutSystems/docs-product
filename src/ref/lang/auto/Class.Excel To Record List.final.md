---
kinds: ServiceStudio.Model.Nodes+ExcelToRecordList+Kind
helpids: 10001
summary: Use Excel To Record List when you need to load data from an Excel file in your app at runtime.
locale: en-us
guid: 65e7dfbe-2def-4858-85fb-adaf71d7c774
---

# Excel To Record List


Converts an Excel object to a Record List. Use this logic tool when you need to load data from an Excel file in your app at runtime.

<div class="info" markdown="1">

We've been working on this article. Please let us know how useful this new version is by voting.

</div>

To use Excel To Record List you need an Entity or Structure that matches the Excel file content you want to import. OutSystems matches the attributes of the Entity/Structure specified in the **Record Definition** property with column headings in the Excel file.

Check the following example of an Entity named Address and a valid Excel file containing data to import:

![Entity attributes and Excel file with data to import](images/exceltorecordlist-entity-excel.png)

Entity attributes without a corresponding column in the Excel file get the default value of their data type (for example, `""` for a Text attribute).

To use the tool, provide the content of the Excel file to import in the **File Content** property as binary data. To import data from a specific sheet in the Excel file, specify the sheet name in the **Sheet Name** property. OutSystems imports data from the first sheet, by default.

To iterate over the successfully imported records, use a For Each and set the **Record List** property of the For Each to the name of the Excel to Record List element.

Here's an example flow for handling the data you're importing using Excel to Record List:

![Example flow for importing data from an Excel file](images/exceltorecordlist-example-flow-ss.png)

Excel To Record List doesn't validate if the Excel file data has values for all the mandatory attributes of the Entity. You can use a Server Action (in this example, ValidateAddress) to check if the imported data complies with business rules like mandatory attributes, or handle the exception thrown by the CreateAddress entity action.

<div class="info" markdown="1">

Tip: If you need to import data from an Excel file at **design time**, when developing your application, check the following topics:

* [Create an Entity from an Excel file and import data](../../../getting-started/create-reactive-web.md#create-entity-from-excel), if you don't have an Entity to hold the imported Excel data yet
* [Bootstrap an Entity Using an Excel File](../../../develop/data/excel-bootstrap.md), if you want to import data to an existing Entity

</div>

## Availability

Excel To Record List is only available in **Server Actions**. In Reactive Web and Mobile apps you must send the uploaded file to the server and then process that file in a Server Action. Check [Enable End Users to Upload Files](../../../develop/ui/inputs/upload.md) for more information.

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Record Definition">Record Definition</td>
<td>Entity or structure that defines the structure of the data that you want to load.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="File Content">File Content</td>
<td>Holds the Excel file.</td>
<td>Yes</td>
<td></td>
<td>The expected data type is Binary Data.</td>
</tr>
<tr>
<td title="Sheet Name">Sheet Name</td>
<td>Name of the Excel sheet to import. By default, the first sheet is imported, unless a sheet named 'Sheet1' exists in the file.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

