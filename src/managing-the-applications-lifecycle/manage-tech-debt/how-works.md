---
tags: Architecture Dashboard; how-to; manual
summary: Learn how Architecture Dashboard works and how your infrastructure communicates with the SaaS.
en_title: How does Architecture Dashboard work
---

# How does Architecture Dashboard work

Architecture Dashboard includes the following pieces:

Architecture Dashboard SaaS
:   A "Software as a Service" that processes and shows all data collected by the Architecture Dashboard LifeTime Plugin.

Architecture Dashboard LifeTime Plugin
:   A LifeTime plugin that's published in a platform installation (on-premises or cloud) with **environment probes** to collect data and communicate with the Architecture Dashboard SaaS.

![Architecture Dashboard diagram](images/how-works-diag.png)

## Communication

Communications between the Architecture Dashboard plugin and the Architecture Dashboard SaaS are always initiated by the plugin. This reduces connectivity requirements on your side since all that needs to be ensured is connectivity from the Plugin in the LifeTime environment to the Architecture Dashboard SaaS endpoint.

The plugin can use a forward proxy to connect to the Architecture Dashboard SaaS endpoint.

### Data collected in plugin and sent to SaaS

Architecture Dashboard collects the following data from your infrastructure:

* Platform metamodel data, including infrastructure activation code, environments information (name and Platform Server version), teams, list of apps and modules (including name and identifier), and platform configurations.

* Modules and dependency information for code analysis.

* Upon acceptance of the agreement, during Architecture Dashboard set up: users information (name, username, email address, user creation date, last login date) and LifeTime permissions.

* Optionally: Discovery snapshot data (architectural references, applications, and modules) for architecture analysis.

Data of each installation is kept in the OutSystems cloud and isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation is not accessible by users of other installations.

### Data in transit

* The Plugin and SaaS share data in binary format through a well-known HTTPS endpoint.

* IP or DNS addresses aren't transmitted.

* No ports besides the defaults need to be open for the correct use of Architecture Dashboard Probes.

* No firewall issues should arise, although you need to be able to access the endpoint detailed in [How to set up Architecture Dashboard](how-setup.md).

### Data at rest in SaaS

* Data of each installation is kept isolated from all other installations using the platform's multi-tenant mechanisms. This ensures data from one installation isn't accessible by users of other installations.

### More information about security and compliance

Read more about security and compliance in the following FAQ sections:

* [Security, legal and compliance - registration in Architecture Dashboard](faq.md#data-faq)

* [Security, legal and compliance - personal information](faq.md#personal-data-faq)

## Permissions

The permissions that IT users have while using Architecture Dashboard with an infrastructure, depend on the [role and permissions set in LifeTime](..\manage-it-teams\about-permission-levels.md#permissions) for the **code-analysis environment** of that infrastructure.

<div class="info" markdown="1">

The set of permissions that an IT user has for the **code-analysis environment** is determined by the permissions of the assigned roles, and also by how the roles are assigned.

Roles and their permissions can be assigned as a default role, as a role for a team, or as role for an app.

The permissions of a role assigned for a team override the permissions for the team's apps assigned by the default role.

The permissions of a role assigned for an app override the permissions for the specific app assigned by the default role and of roles assigned for a team.

</div>

The following tables map the Architecture Dashboard permissions to the LifeTime permissions and to the way the roles are assigned to IT users.

### Main features permissions

<pre class="script-css">
th {word-wrap: normal !important;}
table {min-width: 650px;}
</pre>

<table>
<thead>
<tr>
<th rowspan="2">LifeTime permission</th>
<th rowspan="2">LifeTime role assignment</th>
<th colspan="6">Architecture Dashboard permission</th>
</tr>
<tr>
<th>View teams</th>
<th>View apps and modules</th>
<th>Open findings report</th>
<th>Export findings report</th>
<th>Resolve findings</th>
<th>Overview dashboard</th>
</tr>
</thead>
<tbody>
<tr>
<th rowspan="3">No Access /<br/>Access</th>
<th>Assigned as default role</th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th rowspan="3">List Applications /<br/>Monitor and Add Dependencies</th>
<th>Assigned as default role</th>
<td>No</td>
<td>All apps<sup>A</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>Assigned team</td>
<td>Team's apps<sup>B</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>No</td>
<td>Assigned app</td>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th rowspan="3">Open and Debug Applications </th>
<th>Assigned as default role</th>
<td>No</td>
<td>All apps<sup>A</sup></td>
<td>All apps<sup>A</sup></td>
<td>No</td>
<td>No</td>
<td>All apps<sup>A</sup></td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>Assigned team</td>
<td>Team's apps<sup>B</sup></td>
<td>Team's apps<sup>B</sup></td>
<td>No</td>
<td>No</td>
<td>Team's apps<sup>B</sup></td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>No</td>
<td>Assigned app</td>
<td>Assigned app</td>
<td>No</td>
<td>No</td>
<td>Assigned app</td>
</tr>
<tr>
<th rowspan="3">Change and Deploy Applications /<br/>Full Control</th>
<th>Assigned as default role</th>
<td>All teams</td>
<td>All apps<sup>A</sup></td>
<td>All apps<sup>A</sup></td>
<td>All apps<sup>A</sup></td>
<td>All apps<sup>A</sup></td>
<td>All apps<sup>A</sup></td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>Assigned team</td>
<td>Team's apps<sup>B</sup></td>
<td>Team's apps<sup>B</sup></td>
<td>Team's apps<sup>B</sup></td>
<td>Team's apps<sup>B</sup></td>
<td>Team's apps<sup>B</sup></td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>No</td>
<td>Assigned app</td>
<td>Assigned app</td>
<td>Assigned app</td>
<td>Assigned app</td>
<td>Assigned app</td>
</tr>
</tbody>
</table>

A- Specific apps may not appear if a lower permission is granted by a role assigned specifically for those apps or assigned for teams assigned to those apps.

B- Specific apps may not appear if a lower permission is granted by a role assigned specifically for those apps.

### Maintenance and operations permissions { #maint-op-permissions }

<table>
<thead>
<tr>
<th rowspan="2">LifeTime permission</th>
<th rowspan="2">LifeTime role assignment</th>
<th colspan="4">Architecture Dashboard permission</th>
</tr>
<tr>
<th>Ignore modules</th>
<th>Enable AI auto-classification</th>
<th>Override module AI auto-classification</th>
<th>Update probes</th>
</tr>
</thead>
<tbody>
<tr>
<th rowspan="3">Open and Debug Applications or lower</th>
<th>Assigned as default role</th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>No</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th rowspan="3">Change and Deploy Applications</th>
<th>Assigned as default role</th>
<td>All modules<sup>A</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>Team's modules<sup>B</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>Assigned app's modules</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th rowspan="3">Full Control</th>
<th>Assigned as default role</th>
<td>All modules<sup>A</sup></td>
<td>Yes</td>
<td>All modules</td>
<td>Yes</td>
</tr>
<tr>
<th>Assigned for a team</th>
<td>Team's modules<sup>B</sup></td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr>
<th>Assigned for an app</th>
<td>Assigned app's modules</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
</tbody>
</table>
A- Specific modules may not appear if a lower permission is granted by a role assigned specifically for those modules' apps or by a role assigned for teams assigned to those modules' apps.

B- Specific modules may not appear if a lower permission is granted by a role assigned specifically for those modules' apps.
