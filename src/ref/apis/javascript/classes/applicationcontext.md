---
tags: runtime-mobileandreactiveweb
summary: Provides contextual information based on the screen that is being presented. Used to identify the screen, module and application that is currently running.
---

# ApplicationContext

Provides contextual information based on the screen that is being presented. Used to identify the screen, module and application that is currently running.

## Hierarchy

**ApplicationContext**

## Summary

<table markdown="1">
<thead>
<tr>
<th colspan="2">Methods</th>
</tr>
</thead>
<tbody>
<tr>
<td>[getCurrentContext](applicationcontext.md#getcurrentcontext)</td>
<td>
Gets the current context based on the screen being presented.
</td>
</tr>
</tbody>
</table>

## Methods

### &lt;Static&gt; getCurrentContext

**getCurrentContext(): object**

Gets the current context based on the screen being presented.

Returns: object

Returns an object with the following attributes: `applicationKey`, `applicationName`, `moduleKey`, `moduleName`, `screenKey`, `screenName`.

