---
kinds: ServiceStudio.Model.Timer+Kind
helpids: 13001
---

# Timer

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
<td title="Action">Action</td>
<td>Action that is executed when the Timer is awakened.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Schedule">Schedule</td>
<td>Schedule the start time and frequency of the Timer.</td>
<td></td>
<td></td>
<td>The value of this property can only be specified using the Timer Schedule Editor. Open it by double-clicking on the property name or by clicking on "...".</td>
</tr>
<tr class="separator">
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Timeout in Minutes">Timeout in Minutes</td>
<td>Maximum time in minutes that Platform Server waits for the timer execution to end.</td>
<td>Yes</td>
<td>20</td>
<td></td>
</tr>
<tr>
<td title="Priority">Priority</td>
<td>Defines the order by which the Timers are prioritized.</td>
<td>Yes</td>
<td>3 - Normal</td>
<td></td>
</tr>
<tr>
<td title="Is Multi-tenant">Is Multi-tenant</td>
<td>Set to Yes to run the Timer isolatedly for each tenant or 'No' to run once for data shared among tenants. If not set, it inherits the module setting.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Runtime Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Read Only</th>
<th>Type</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td>Schedule</td>
<td>Indicates the time and the frequency that the Timer is awakened.</td>
<td></td>
<td>Text</td>
<td>When setting this runtime property, you must use one of the supported schedule formats. The schedule formats are case-sensitive. Examples:<br/>
        <code>"16:15"</code> (awake the Timer every day at 16:15);<br/>
        <code>"22:00 Mon Fri"</code> (awake the Timer every Monday and Friday at 22:00);<br/>
        <code>"15:30 16"</code> (awake the Timer on the 16<sup>th</sup> day of every month at 15:30);<br/>
        <code>"00:15 2nd Tue"</code> (awake the Timer on the 2<sup>nd</sup> Tuesday of every month at 00:15);<br/>
        <code>"When Published"</code> (awake the Timer after each 1-Click Publish operation).<br/>
        Be aware that no format validations are done at development time. You must be careful to use the correct format when assigning a value to the Schedule runtime property, otherwise the Timer might not run.</td>
</tr>
<tr>
<td>LastRun</td>
<td>Indicates the last calendar day and time when the Timer awoke, automatically or explicitly.</td>
<td>Yes</td>
<td>Date Time</td>
<td></td>
</tr>
<tr>
<td>NextRun</td>
<td>Indicates the next calendar day and time when the Timer is schedule to awaken.</td>
<td>Yes</td>
<td>Date Time</td>
<td></td>
</tr>
</tbody>
</table>

