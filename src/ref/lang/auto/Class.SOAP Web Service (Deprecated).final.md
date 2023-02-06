---
kinds: ServiceStudio.Model.WebReference+Kind, ServiceStudio.Model.WebService+Kind
helpids: 11003, 11001
locale: en-us
guid: c2e59d22-6ed6-4982-a9fd-5ce8e440d660
app_type: traditional web apps, mobile apps, reactive web apps
---

# SOAP Web Service - Deprecated

Consumed SOAP Web Service based on the SOAP 1.1 protocol.  

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
<tr>
<td title="URL">URL</td>
<td>The URL where the WSDL is obtained.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr >
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
<td title="Integrated Authentication">Integrated Authentication</td>
<td>Set to Yes to use Integrated Authentication to validate user access.</td>
<td>Yes</td>
<td>No</td>
<td></td>
</tr>
<tr>
<td title="WSDL">WSDL</td>
<td>WSDL with the definition of the functionality provided by this SOAP Web Service.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Endpoint">Endpoint</td>
<td>Endpoint of the SOAP Web Service.</td>
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

