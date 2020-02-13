---
kinds: ServiceStudio.Model.Nodes+Download+Kind, ServiceStudio.Model.NRNodes+Download+Kind
helpids: 0
---

# Download

Sends a file to the user.  
Triggers an action for the browser to download the file.  

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
<td title="File Content">File Content</td>
<td>Holds the file selected by the user.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="File Name">File Name</td>
<td>Text literal or expression with the name of the file, including the extension.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Mime-Type">Mime-Type</td>
<td>Text literal or expression specifying the media type of the file.</td>
<td>Yes</td>
<td>"application/octet-stream"</td>
<td>Example values:<br/>
– "application/x-msexcel";<br/>
– "application/msword";<br/>
– "application/pdf";<br/>
– "image/gif";<br/>
– "text/html";<br/>
– "video/avi";<br/>
– "audio/wav".</td>
</tr>
<tr>
<td title="Save to Disk">Save to Disk</td>
<td>Set to Yes to allow the user to open or save the file.</td>
<td>Yes</td>
<td>Yes</td>
<td></td>
</tr>
</tbody>
</table>

