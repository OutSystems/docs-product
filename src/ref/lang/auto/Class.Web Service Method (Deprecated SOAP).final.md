---
kinds: ServiceStudio.Model.Flows+WebServiceMethod+Kind, ServiceStudio.Model.WebReferenceMethod+Kind
helpids: 0
---

# Web Service Method (Deprecated SOAP)

Method of a consumed SOAP 1.1 Web Service.

<div class="info" markdown="1">

This consumed SOAP Web Service implementation is **deprecated** and it's only available in modules that have been upgraded to OutSystems 11. 

New Consumed SOAP Web Service elements created in OutSystems 11 modules follow the [new SOAP implementation](<ServiceStudio.Plugin.SOAP.SOAPClient.final.md>) supporting up to SOAP 1.2.

</div>

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
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Original Name">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td></td>
<td></td>
<td>This property is only visible for referenced elements.</td>
</tr>
<tr>
<td title="Timeout in Seconds">Timeout in Seconds</td>
<td>Maximum time this method waits for a synchronous Web Service request to complete and after which an exception is raised. If unspecified, the timeout observed is 100 seconds.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Cache in Minutes">Cache in Minutes</td>
<td>Maximum time content or results are stored in memory. When undefined, nothing is cached.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Original Description">Original Description</td>
<td>Description of the Web Service as provided in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

