---
kinds: ServiceStudio.Plugin.SOAP.SOAPActionDescriptor
helpids: -1
---

# Web Service Method (Consumed)

Method of a Consumed SOAP Web Service.

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
<td title="TimeoutInSeconds">Timeout in Seconds</td>
<td>Maximum time this method waits for a synchronous Web Service request to complete and after which an exception is raised. If unspecified, the timeout observed is 100 seconds.</td>
<td></td>
<td>100</td>
<td>The "Duration" field in integration logs can have higher values than the "Timeout in Seconds" value. For more information check [Log data reference](../../../managing-the-applications-lifecycle/monitor-and-troubleshoot/logging/reference.md#integration).</td>
</tr>
<tr>
<td title="OriginalName">Original Name</td>
<td>Name of the web service method as provided in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalDescription">Original Description</td>
<td>Description of the Web Service as provided in the WSDL.</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

