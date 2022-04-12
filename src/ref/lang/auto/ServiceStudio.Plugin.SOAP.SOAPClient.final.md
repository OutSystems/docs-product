---
kinds: ServiceStudio.Plugin.SOAP.SOAPClientDescriptor
helpids: -1
locale: en-us
guid: 2744cd5d-761e-45d7-a18c-7db6ffe1d7fb
---

# SOAP Web Service (Consumed)

Consumed Web Service based on the SOAP 1.1/1.2 protocol.

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
<td title="Image">Icon</td>
<td>Picture to be displayed to help identify this element.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Authentication</th>
</tr>
<tr>
<td title="AuthenticationType">Authentication Type</td>
<td>Authentication type for each request.</td>
<td>Yes</td>
<td>(None)</td>
<td></td>
</tr>
<tr>
<td title="AuthenticationUsername">Username</td>
<td>Username sent for authenticating requests. Can be customized at runtime using Dynamic Authentication or in the environment console.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="AuthenticationPassword">Password</td>
<td>Password sent for authenticating requests. Can be customized at runtime using Dynamic Authentication or in the environment console.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="OnRequestCallback">On Before Request</td>
<td>Action to modify the connection, request and/or response message by using extension actions that use the SOAP Extensibility API.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="WSDLLocation">WSDL Location</td>
<td>Location where the WSDL is obtained.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="WSDL">WSDL</td>
<td>WSDL with the definition of the functionality provided by this SOAP Web Service.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Binding">Binding</td>
<td>Binding of the SOAP Web Service.</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr>
<td title="OriginalName">Original Name</td>
<td>Name of the element as defined in the module which implements it (producer module). This property is read-only.</td>
<td></td>
<td></td>
<td>This property is only visible for referenced elements.</td>
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

