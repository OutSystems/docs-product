---
summary: Allows you to manage applications, modules, environments and deployments of your OutSystems infrastructure. Version 2 of the API adds support for deployment zones.
tags: support-application_development; support-Application_Lifecycle; support-devOps; support-Integrations_Extensions
---
<pre class="script-css">
.json-schema-description:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Description";
            padding-bottom: .5em;
            display: block
        }

        .json-schema-description:not(:last-child) {
            padding-bottom: 1.5em
        }

        .json-schema-properties:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Properties";
            padding-bottom: .5em;
            display: block
        }

        .json-schema-properties:not(:last-child) {
            padding-bottom: 1.5em
        }

        .json-schema-properties dd:not(:last-child) {
            padding-bottom: 1em
        }

        .json-schema-properties dl {
            margin: 0
        }

        .json-schema-example:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Example";
            padding-bottom: .5em;
            display: block
        }

        .json-schema-example:not(:last-child) {
            padding-bottom: 1.5em
        }

        .json-schema-array-items:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Items";
            padding-bottom: .5em;
            display: block
        }

        .json-schema-array-items:not(:last-child) {
            padding-bottom: 1.5em
        }

        .json-schema-allOf-inherited:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Inherited";
            padding-bottom: .5em;
            display: block
        }

        .json-schema-allOf-inherited:not(:last-child) {
            padding-bottom: 1.5em
        }

        .json-schema-allOf-inherited ul {
            padding-left: 0;
            list-style: none
        }

        .json-schema-anyOf>dl {
            border-left: 2px solid #a2a2a2;
            padding-left: 1em
        }

        .json-schema-anyOf>dl dt:not(:first-child):before {
            content: "or "
        }

        .json-schema-anyOf>dl dt:first-child:before {
            content: "either "
        }

        .json-schema-additionalProperties:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Additional properties";
            padding-bottom: .5em;
            display: block
        }

        .json-schema-additionalProperties:not(:last-child) {
            padding-bottom: 1.5em
        }

        .json-inner-schema .json-schema-properties,
        .json-inner-schema .json-schema-array-items,
        .json-inner-schema .json-schema-description,
        .json-inner-schema .json-schema-example {
            padding-left: 1em;
            margin-top: .5em;
            padding-bottom: .5em;
            border-left: 2px solid #a2a2a2
        }

        .json-property-discriminator:before {
            display: inline;
            padding: .2em .6em .3em;
            font-size: 75%;
            font-weight: 700;
            line-height: 1;
            color: #fff;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: .25em;
            background-color: #777;
            content: "discriminator"
        }

        a.json-property-discriminator:before:hover,
        a.json-property-discriminator:before:focus {
            color: #fff;
            text-decoration: none;
            cursor: pointer
        }

        .json-property-discriminator:before:empty {
            display: none
        }

        .btn .json-property-discriminator:before {
            position: relative;
            top: -1px
        }

        .json-property-discriminator:before[href]:hover,
        .json-property-discriminator:before[href]:focus {
            background-color: #5e5e5e
        }

        .json-property-required:before {
            display: inline;
            padding: .2em .6em .3em;
            font-size: 75%;
            font-weight: 700;
            line-height: 1;
            color: #fff;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: .25em;
            background-color: #777;
            content: "required"
        }

        a.json-property-required:before:hover,
        a.json-property-required:before:focus {
            color: #fff;
            text-decoration: none;
            cursor: pointer
        }

        .json-property-required:before:empty {
            display: none
        }

        .btn .json-property-required:before {
            position: relative;
            top: -1px
        }

        .json-property-required:before[href]:hover,
        .json-property-required:before[href]:focus {
            background-color: #5e5e5e
        }

        .json-property-read-only:before {
            display: inline;
            padding: .2em .6em .3em;
            font-size: 75%;
            font-weight: 700;
            line-height: 1;
            color: #fff;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: .25em;
            background-color: #777;
            content: "read only"
        }

        a.json-property-read-only:before:hover,
        a.json-property-read-only:before:focus {
            color: #fff;
            text-decoration: none;
            cursor: pointer
        }

        .json-property-read-only:before:empty {
            display: none
        }

        .btn .json-property-read-only:before {
            position: relative;
            top: -1px
        }

        .json-property-read-only:before[href]:hover,
        .json-property-read-only:before[href]:focus {
            background-color: #5e5e5e
        }

        .json-property-pattern {
            font-weight: lighter;
            font-size: small
        }

        .json-schema--regex:before,
        .json-schema--regex:after {
            color: #808080;
            content: '/'
        }

        .json-property-type {
            font-weight: 100
        }

        .json-property-format {
            font-size: smaller
        }

        .json-property-enum {
            font-weight: lighter;
            font-size: small
        }

        .json-property-default-value {
            font-weight: lighter;
            font-size: small
        }

        .json-property-default-value:before {
            content: '(default: "'
        }

        .json-property-default-value:after {
            content: '")'
        }

        .json-property-enum-item {
            font-weight: lighter;
            font-size: small
        }

        .json-property-enum-item:before,
        .json-property-enum-item:after {
            content: "\""
        }

        .json-schema--reference {
            font-size: 90%
        }

        .table.swagger--summary>tbody>tr>td.swagger--summary-path {
            vertical-align: middle
        }

        .table.swagger--summary>tbody>tr>td p {
            margin: 0
        }
        .swagger--panel-operation-head {
            border-color: #f3ff34
        }

        .swagger--panel-operation-head>.panel-heading {
            color: #333;
            background-color: #fcffcd;
            border-color: #f3ff34
        }

        .swagger--panel-operation-head>.panel-heading+.panel-collapse>.panel-body {
            border-top-color: #f3ff34
        }

        .swagger--panel-operation-head>.panel-heading .badge {
            color: #fcffcd;
            background-color: #333
        }

        .swagger--panel-operation-head>.panel-footer+.panel-collapse>.panel-body {
            border-bottom-color: #f3ff34
        }

        .swagger--panel-operation-head .operation-name {
            font-weight: bold
        }

        .swagger--panel-operation-head .operation-summary {
            float: right !important
        }

        .sw-operation-description:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Description";
            padding-bottom: .5em;
            display: block
        }

        .sw-operation-description:not(:last-child) {
            padding-bottom: 1.5em
        }

        .sw-request-params:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Request parameters";
            padding-bottom: .5em;
            display: block
        }

        .sw-request-params:not(:last-child) {
            padding-bottom: 1.5em
        }

        .sw-request-body:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Request body";
            padding-bottom: .5em;
            display: block
        }

        .sw-request-body:not(:last-child) {
            padding-bottom: 1.5em
        }

        .sw-responses:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Responses";
            padding-bottom: .5em;
            display: block
        }

        .sw-responses:not(:last-child) {
            padding-bottom: 1.5em
        }

        .swagger--global:before {
            display: inline;
            padding: .2em .6em .3em;
            font-size: 75%;
            font-weight: 700;
            line-height: 1;
            color: #fff;
            text-align: center;
            white-space: nowrap;
            vertical-align: baseline;
            border-radius: .25em;
            background-color: #777;
            content: 'global'
        }

        a.swagger--global:before:hover,
        a.swagger--global:before:focus {
            color: #fff;
            text-decoration: none;
            cursor: pointer
        }

        .swagger--global:before:empty {
            display: none
        }

        .btn .swagger--global:before {
            position: relative;
            top: -1px
        }

        .swagger--global:before[href]:hover,
        .swagger--global:before[href]:focus {
            background-color: #5e5e5e
        }

        table.table th.sw-param-key {
            width: auto
        }

        table.table th.sw-param-key:before {
            content: "Key"
        }

        table.table th.sw-param-name {
            width: auto
        }

        table.table th.sw-param-name:before {
            content: "Name"
        }

        table.table th.sw-param-description {
            width: auto
        }

        table.table th.sw-param-description:before {
            content: "Description"
        }

        table.table th.sw-param-data-type {
            width: auto
        }

        table.table th.sw-param-data-type:before {
            content: "Data type"
        }

        table.table th.sw-param-type {
            width: auto
        }

        table.table th.sw-param-type:before {
            content: "Type"
        }

        table.table th.sw-request-security-schema {
            width: auto
        }

        table.table th.sw-request-security-schema:before {
            content: "Schema"
        }

        table.table th.sw-request-security-scopes {
            width: auto
        }

        table.table th.sw-request-security-scopes:before {
            content: "Scopes"
        }

        table.table th.sw-response-header-name {
            width: auto
        }

        table.table th.sw-response-header-name:before {
            content: "Header"
        }

        table.table th.sw-response-header-description {
            width: auto
        }

        table.table th.sw-response-header-description:before {
            content: "Description"
        }

        table.table th.sw-response-header-data-type {
            width: auto
        }

        table.table th.sw-response-header-data-type:before {
            content: "Data type"
        }

        .sw-response-name-value {
            font-weight: bold
        }

        .sw-response-description-text {
            padding-bottom: .5em
        }

        code.highlight {
            padding: 0
        }

        .panel-security-definition {
            border-color: #a2a2a2
        }

        .panel-security-definition>.panel-heading {
            color: #000;
            background-color: #eee;
            border-color: #a2a2a2
        }

        .panel-security-definition>.panel-heading+.panel-collapse>.panel-body {
            border-top-color: #a2a2a2
        }

        .panel-security-definition>.panel-heading .badge {
            color: #eee;
            background-color: #000
        }

        .panel-security-definition>.panel-footer+.panel-collapse>.panel-body {
            border-bottom-color: #a2a2a2
        }

        .sw-request-security:before {
            font-weight: bold;
            color: #555;
            text-transform: uppercase;
            content: "Security";
            padding-bottom: .5em;
            display: block
        }

        .sw-request-security:not(:last-child) {
            padding-bottom: 1.5em
        }

        .sw-security-definition-basic:before {
            color: #555;
            font-size: smaller;
            content: "(HTTP Basic Authentication)"
        }

        span.sw-default-value-header {
            font-weight: bold
        }

        .sw-info {
            font-weight: bold
        }

        .sw-info span {
            font-family: monospace;
            font-weight: normal;
            font-size: 1.1em
        }
</pre>

# LifeTime REST API

<p class="sw-info">
Base URL: <span class="sw-info-basePath">/lifetimeapi/rest/v2</span>,
Version: <span class="sw-info-version">v2</span>
</p>
<p><p>The Deployment API allows you to manage applications, modules, environments, deployments, users, team and roles of your OutSystems infrastructure.</p>
</p>
<div id="sw-schemes" class="sw-default-value">
<span class="sw-default-value-header">Schemes:</span>
https
</div>
<h2 id="swagger--summary-tags">Summary</h2>
<h3 id="tag--applications" class="swagger-summary-tag">/applications</h3>
<p class="sw-tag-external-doc"></p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--applications--get">GET /applications/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--applications--ApplicationKey---get">GET /applications/{ApplicationKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--applications--ApplicationKey--versions--get">GET /applications/{ApplicationKey}/versions/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--applications--ApplicationKey--versions--VersionKey---delete">DELETE /applications/{ApplicationKey}/versions/{VersionKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--applications--ApplicationKey--versions--VersionKey---get">GET /applications/{ApplicationKey}/versions/{VersionKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--applications--ApplicationKey--versions--VersionKey--content--get">GET /applications/{ApplicationKey}/versions/{VersionKey}/content/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="tag--environments" class="swagger-summary-tag">/environments</h3>
<p class="sw-tag-external-doc">
</p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--environments--get">GET /environments/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey---get">GET /environments/{EnvironmentKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--applications--get">GET /environments/{EnvironmentKey}/applications/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--applications--post">POST /environments/{EnvironmentKey}/applications/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--applications--ApplicationKey---get">GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--applications--ApplicationKey--content--get">GET /environments/{EnvironmentKey}/applications/{ApplicationKey}/content/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--applications--ApplicationKey--versions--post">POST /environments/{EnvironmentKey}/applications/{ApplicationKey}/versions/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--deploymentzones--get">GET /environments/{EnvironmentKey}/deploymentzones/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--templates--get">GET /environments/{EnvironmentKey}/templates/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="tag--deployments" class="swagger-summary-tag">/deployments</h3>
<p class="sw-tag-external-doc">
</p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--deployments--post">POST /deployments/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--deployments--get">GET /deployments/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--deployments--DeploymentKey---delete">DELETE /deployments/{DeploymentKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--deployments--DeploymentKey---put">PUT /deployments/{DeploymentKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--deployments--DeploymentKey---get">GET /deployments/{DeploymentKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--deployments--DeploymentKey---Command---post">POST /deployments/{DeploymentKey}/{Command}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--deployments--DeploymentKey--status--get">GET /deployments/{DeploymentKey}/status/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="tag--modules" class="swagger-summary-tag">/modules</h3>
<p class="sw-tag-external-doc">
</p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--modules--get">GET /modules/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--modules--ModuleKey---get">GET /modules/{ModuleKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--modules--ModuleKey--versions--get">GET /modules/{ModuleKey}/versions/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--modules--ModuleKey--versions--ModuleVersionKey---get">GET /modules/{ModuleKey}/versions/{ModuleVersionKey}/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="tag--roles" class="swagger-summary-tag">/roles</h3>
<p class="sw-tag-external-doc">
</p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--roles--get">GET /roles/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--roles--post">POST /roles/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--roles--RoleKey---get">GET /roles/{RoleKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--roles--RoleKey---put">PUT /roles/{RoleKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--roles--RoleKey---delete">DELETE /roles/{RoleKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--roles-permissionlevels--get">GET /roles/permissionlevels/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="tag--teams" class="swagger-summary-tag">/teams</h3>
<p class="sw-tag-external-doc">
</p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--teams--get">GET /teams/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--post">POST /teams/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey---get">GET /teams/{TeamKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey---put">PUT /teams/{TeamKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey---delete">DELETE /teams/{TeamKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey--applications--post">POST /teams/{TeamKey}/applications/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey--applications--ApplicationKey--delete">DELETE /teams/{TeamKey}/applications/{ApplicationKey}</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey--users--post">POST /teams/{TeamKey}/users/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--teams--TeamKey--users--UserKey---delete">DELETE /teams/{TeamKey}/users/{UserKey}/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h3 id="tag--users" class="swagger-summary-tag">/users</h3>
<p class="sw-tag-external-doc">
</p>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--users--get">GET /users/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--users--post">POST /users/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--users--UserKey---get">GET /users/{UserKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--users--UserKey---put">PUT /users/{UserKey}/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--users--UserKey--setpassword--post">POST /users/{UserKey}/setpassword/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--users--UserKey--applications--post">POST /users/{UserKey}/applications/</a></td>
<td></td>
</tr>
<tr>
<td><a href="#operation--users--UserKey--applications--ApplicationKey---delete">DELETE /users/{UserKey}/applications/{ApplicationKey}/</a></td>
<td></td>
</tr>
</tbody>
</table>
<h2>Endpoints</h2>
<span id="path--applications-"></span>
<div id="operation--applications--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/applications/</strong></h3>
Go to 
<a href="#tag--applications">/applications</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a list of applications that exist in the infrastructure.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
IncludeModules
</td>
<td><p>When set to true, the modules are also returned. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeEnvStatus
</td>
<td><p>When set to true, the application status per environment is also returned. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>A list of Application records including AppStatusInEnv sub-lists, if requested.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>A list of Application records including AppStatusInEnv sub-lists, if requested.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Application">Application</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No applications available in the infrastructure.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve applications because IncludeModules was requested but IncludeEnvStatus was not, or invalid request when listing all applications.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to list the applications.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--applications--ApplicationKey--"></span>
<div id="operation--applications--ApplicationKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/applications/{ApplicationKey}/</strong></h3>
Go to 
<a href="#tag--applications">/applications</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given application.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the desired application.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeModules
</td>
<td><p>When set to true, the modules details are also retrieved. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeEnvStatus
</td>
<td><p>When set to true, the application status per environment is also returned. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>An Application record including an AppStatusInEnv sub-list, if requested.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Application">Application</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve applications because IncludeModules and IncludeEnvStatus parameters were incorrect.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed listing all applications because user has insufficient permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed getting running applications because one of the environments was not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--applications--ApplicationKey--versions-"></span>
<div id="operation--applications--ApplicationKey--versions--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/applications/{ApplicationKey}/versions/</strong></h3>
Go to 
<a href="#tag--applications">/applications</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a list of versions of a given application.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the desired application.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ChangeLogFilter
</td>
<td><p>Optional filter. If present, only versions containing this string in the change log will be returned.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
MaximumVersionsToReturn
</td>
<td><p>The maximum number of versions to return. The default value is 5.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>A list of ApplicationVersion records.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>A list of ApplicationVersion records.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationVersion_v2">ApplicationVersion_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Invalid request due to invalid max versions to return (less than 0).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application with key <code>&lt;ApplicationKey&gt;</code>. The user does not have the required permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application with key <code>&lt;ApplicationKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to list the application versions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--applications--ApplicationKey--versions--VersionKey--"></span>
<div id="operation--applications--ApplicationKey--versions--VersionKey---delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/applications/{ApplicationKey}/versions/{VersionKey}/</strong></h3>
Go to 
<a href="#tag--applications">/applications</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Discards an application version, if possible. Running versions, or versions used in Deployments cannot be deleted.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application whose version to be deleted.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
VersionKey
</td>
<td><p>The key of the application version to be deleted.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>Application version successfully deleted.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Service Account doesn&#39;t have permissions to delete the specified application version.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Application or application version not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to delete application version <code>&lt;VersionKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--applications--ApplicationKey--versions--VersionKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/applications/{ApplicationKey}/versions/{VersionKey}/</strong></h3>
Go to 
<a href="#tag--applications">/applications</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given version of the specified application.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application whose version is being requested.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeModules
</td>
<td><p>When set to true, the modules details are also retrieved. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
VersionKey
</td>
<td><p>The key of the desired application version.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>An ApplicationVersion record.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationVersion_v2">ApplicationVersion_v2</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application with key <code>&lt;ApplicationKey&gt;</code>. The user does not have the required permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application with key <code>&lt;ApplicationKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application version.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--applications--ApplicationKey--versions--VersionKey--content-"></span>
<div id="operation--applications--ApplicationKey--versions--VersionKey--content--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/applications/{ApplicationKey}/versions/{VersionKey}/content/</strong></h3>
Go to 
<a href="#tag--applications">/applications</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a link where the binary file for a given application version can be downloaded. The link will expire in 60 minutes.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application for which to get the binary file link.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
VersionKey
</td>
<td><p>The key of the application version for which to get the binary file link.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>The link for the application binary file.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/DownloadLink">DownloadLink</a>
</div>
</div></div>
<div class="col-md-12">
<section class="sw-response-headers">
<table class="table">
<thead>
<tr>
<th class="sw-response-header-name"></th>
<th class="sw-response-header-description"></th>
<th class="sw-response-header-data-type"></th>
</tr>
</thead>
<tbody>
<tr class="sw-response-header-Expires">
<td>
Expires</td>
<td><p>The expiration date and time of the returned link.</p>
</td>
<td>
<span class="json-property-type">string</span><span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</td>
</tr>
</tbody>
</table>
</section>
</div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No binary available for given keys.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>The request is invalid for the given keys (Application:<code>&lt;ApplicationKey&gt;</code>; ApplicationVersionKey <code>&lt;ApplicationVersionKey&gt;</code>).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn’t have permissions for the given keys (Application:<code>&lt;ApplicationKey&gt;</code>; ApplicationVersionKey <code>&lt;ApplicationVersionKey&gt;</code>).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the application with key <code>&lt;ApplicationKey&gt;</code> or the application version with key <code>&lt;ApplicationVersionKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to download the oap of the application version.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--deployments-"></span>
<div id="operation--deployments--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/deployments/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a list of deployments ordered by creation date, from newest to oldest.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
MinDate
</td>
<td><p>The minimum creation date of the deployments to return. The default value is 1 week before the current date.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">string</span>    <span class="json-property-format">(date)</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
MaxDate
</td>
<td><p>The maximum creation date of the deployments to return. The default value is the current date.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">string</span>    <span class="json-property-format">(date)</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
TargetEnvironmentKey
</td>
<td><p>The key of the target environment to return the deployments from. If the user does not have access to the environment, the list returned will be empty. If no environment key is passed, the list will not be filtered by any target environment.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Deployments list successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>A list of Deployment records.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Deployment_v2">Deployment_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>There are no deployments created between <code>&lt;MinDate&gt;</code> and <code>&lt;MaxDate&gt;</code> for environment key <code>&lt;TargetEnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Invalid request for list of deployments created between <code>&lt;MinDate&gt;</code> and <code>&lt;MaxDate&gt;</code> for environment key <code>&lt;TargetEnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn&#39;t have access to any environment.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to list the deployments.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--deployments--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/deployments/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Creates a deployment to a target environment. An optional list of applications to include in the deployment can be specified. The input is a subset of deployment object.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>A Deployment record.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord">ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Deployment successfully created.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>The key of the newly created deployment.</p>
</section>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Invalid request.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Invalid user permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Source or target environment not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to create deployment from environment <code>&lt;SourceEnvironmentKey&gt;</code> to environment <code>&lt;TargetEnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--deployments--DeploymentKey--"></span>
<div id="operation--deployments--DeploymentKey---delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/deployments/{DeploymentKey}/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Discards a deployment, if possible. Only deployments whose state is “saved” can be deleted.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
DeploymentKey
</td>
<td><p>The key of the deployment to delete.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>Deployment successfully deleted.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Deployment with key <code>&lt;DeploymentKey&gt;</code> cannot be deleted</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Service Account doesn&#39;t have permissions to the deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Deployment with key <code>&lt;DeploymentKey&gt;</code> not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to delete deployment <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--deployments--DeploymentKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/deployments/{DeploymentKey}/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given deployment. The returned information contains the included applications and the possible conflicts that can arise from the deployment of the current applications.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
DeploymentKey
</td>
<td><p>The key of the desired deployment.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Deployment details successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationConflictListTextListDeployment_v2Record">ApplicationConflictListTextListDeployment_v2Record</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn&#39;t have permissions to the deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Deployment with key <code>&lt;DeploymentKey&gt;</code> not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to access the details of deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--deployments--DeploymentKey---put" class="swagger--panel-operation-put panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">PUT</span> <strong>/deployments/{DeploymentKey}/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Updates a given deployment. An optional list of applications to include in the deployment can be specified. The input is a subset of deployment object.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>The deployment information to update.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord">ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
DeploymentKey
</td>
<td><p>The key of the deployment to update.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Deployment successfully updated.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/DeploymentData_v2">DeploymentData_v2</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Invalid request.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Invalid user permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Deployment plan not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to update deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--deployments--DeploymentKey--status-"></span>
<div id="operation--deployments--DeploymentKey--status--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/deployments/{DeploymentKey}/status/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given deployment execution, including the deployment status and messages.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
DeploymentKey
</td>
<td><p>The key of the deployment whose status is being requested.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Deployment status successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/DeploymentMessageListTextTextRecord">DeploymentMessageListTextTextRecord</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn&#39;t have permissions to the deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Deployment with key <code>&lt;DeploymentKey&gt;</code> not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the status of the deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--deployments--DeploymentKey---Command--"></span>
<div id="operation--deployments--DeploymentKey---Command---post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/deployments/{DeploymentKey}/{Command}/</strong></h3>
Go to 
<a href="#tag--deployments">/deployments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Executes the given command in a specified deployment. The allowed commands are “start”, “continue” and “abort”.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
DeploymentKey
</td>
<td><p>The key of the deployment where the command will be executed.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
Command
</td>
<td><p>The command to execute. One of “start”, “continue” or “abort”. </p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
RedeployOutdated
</td>
<td><p>If True, outdated applications in the target environment will be redeployed.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-202">
202 Accepted
</dt>
<dd class="sw-response-202">
<div class="row">
<div class="col-md-12">
<p>Command <code>&lt;Command&gt;</code> executed successfully for deployment <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Command <code>&lt;Command&gt;</code> can&#39;t be executed for deployment <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Service Account doesn&#39;t have permissions to the deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Deployment with key <code>&lt;DeploymentKey&gt;</code> not found, or command not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to execute command <code>&lt;Command&gt;</code> for deployment with key <code>&lt;DeploymentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments-"></span>
<div id="operation--environments--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Lists all the environments in the infrastructure.</p>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Environments list successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>Environments list successfully retrieved.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Environment">Environment</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No environments found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to list the environments.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--"></span>
<div id="operation--environments--EnvironmentKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/{EnvironmentKey}/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given environment.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the desired environment.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Environment details successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Environment">Environment</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the environment with key: <code>&lt;EnvironmentKey&gt;</code>. The user does not have the required permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the environment with key: <code>&lt;EnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to access the details of environment.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--applications-"></span>
<div id="operation--environments--EnvironmentKey--applications--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/{EnvironmentKey}/applications/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns information about the running versions of all applications in a given environment.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment whose list of running applications is being requested.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeModules
</td>
<td><p>When set to true, the modules details are also retrieved. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeEnvStatus
</td>
<td><p>When set to true, the applications’ status information in the environment is included in the result. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Applications list for the given environment successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>Applications list for the given environment successfully retrieved.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Application">Application</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No applications found in environment with key <code>&lt;EnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve applications published in environment because IncludeModules and IncludeEnvStatus parameters were incorrect, or Invalid request when getting running applications for environment with key <code>&lt;EnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the running applications for environment with key <code>&lt;EnvironmentKey&gt;</code> because user has insufficient permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve running applications for environment with key <code>&lt;EnvironmentKey&gt;</code> because it was not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--environments--EnvironmentKey--applications--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/environments/{EnvironmentKey}/applications/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Creates a new application in the environment.</p>
</section>
<section class="sw-request-body">
<div class="row">
<div class="col-md-6">
<p><p>A structure holding the name, description and other attributes of the new application.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/NewApplication">NewApplication</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment to create the application.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>The key of the newly created application.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/TextRecord2">TextRecord2</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to create application due to invalid application name, runtime kind, template, color or team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to create an application because user has insufficient permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to create an application for environment with key <code>&lt;EnvironmentKey&gt;</code> because it was not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to create application due to an internal error.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--applications--ApplicationKey--"></span>
<div id="operation--environments--EnvironmentKey--applications--ApplicationKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/{EnvironmentKey}/applications/{ApplicationKey}/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns information about the running version of the specified application in a given environment.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment from which to get the running application details.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application whose details are being requested.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeEnvStatus
</td>
<td><p>When set to true, the applications’ status information in the environment is included in the result. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeModules
</td>
<td><p>When set to true, the modules details are also retrieved. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Application information successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Application">Application</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Request asked for Modules but not for Status.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn’t have permissions for the given keys (EnvironmentKey:<code>&lt;EnvironmentKey&gt;</code>; Application:<code>&lt;ApplicationKey&gt;</code>).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the environment with key <code>&lt;EnvironmentKey&gt;</code> or the application with key <code>&lt;ApplicationKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to access the running version of an application.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--applications--ApplicationKey--content-"></span>
<div id="operation--environments--EnvironmentKey--applications--ApplicationKey--content--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/{EnvironmentKey}/applications/{ApplicationKey}/content/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a link where the binary file for a given application can be downloaded. The link will expire in 60 minutes.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment from which to get the application binary file link.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application for which to get the binary file link.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
Type
</td>
<td><p>The type of binary file to return, when applicable. One of “oap”, “apk” or “ipa”.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Binary file download link successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/DownloadLink">DownloadLink</a>
</div>
</div></div>
<div class="col-md-12">
<section class="sw-response-headers">
<table class="table">
<thead>
<tr>
<th class="sw-response-header-name"></th>
<th class="sw-response-header-description"></th>
<th class="sw-response-header-data-type"></th>
</tr>
</thead>
<tbody>
<tr class="sw-response-header-Expires">
<td>
Expires</td>
<td><p>The expiration date and time of the returned link.</p>
</td>
<td>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</td>
</tr>
</tbody>
</table>
</section>
</div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No binary available for given type and keys.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>The required type <code>&lt;Type&gt;</code> is invalid for given keys (EnvironmentKey:<code>&lt;EnvironmentKey&gt;</code>; Application:<code>&lt;ApplicationKey&gt;</code>).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn’t have permissions for the given keys (EnvironmentKey:<code>&lt;EnvironmentKey&gt;</code>; Application:<code>&lt;ApplicationKey&gt;</code>).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the environment with key <code>&lt;EnvironmentKey&gt;</code> or the application with key <code>&lt;ApplicationKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to download <code>&lt;Type&gt;</code> of an application.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--applications--ApplicationKey--versions-"></span>
<div id="operation--environments--EnvironmentKey--applications--ApplicationKey--versions--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/environments/{EnvironmentKey}/applications/{ApplicationKey}/versions/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Creates a new version of the application based on the current running application.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>A structure holding the new version name for the application and for its native applications, if applicable.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationVersionCreate">ApplicationVersionCreate</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment from which to get the application.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application for which to generate a new version.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>Application version successfully created.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/TextRecord">TextRecord</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Invalid request.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Invalid user permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Environment or application not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to tag an application, or Failed to create a new version for application <code>&lt;ApplicationName&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--deploymentzones-"></span>
<div id="operation--environments--EnvironmentKey--deploymentzones--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/{EnvironmentKey}/deploymentzones/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns information about the deployment zones available in a given environment.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment from which to get the running application details.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Deployment zone information successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>Deployment zone information successfully retrieved.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/DeploymentZone_v2">DeploymentZone_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to access the deployment zones of environment.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the deployment zones of environment <code>&lt;EnvironmentName&gt;</code> (key: <code>&lt;EnvironmentKey&gt;</code>). Error: The user does not have the required permissions, or Feature not Licensed.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the deployment zones of environment with key: <code>&lt;EnvironmentKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to access the deployment zones of environment.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--environments--EnvironmentKey--templates-"></span>
<div id="operation--environments--EnvironmentKey--templates--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/environments/{EnvironmentKey}/templates/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns information about the templates available in a given environment.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
EnvironmentKey
</td>
<td><p>The key of the environment from which to get the running application details.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>A list of Templates.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>A list of Templates.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Template">Template</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Environment doesn&#39;t support list templates.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn&#39;t have permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Environment not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--modules-"></span>
<div id="operation--modules--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/modules/</strong></h3>
Go to 
<a href="#tag--modules">/modules</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a list of modules that exist in the infrastructure.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
IncludeEnvStatus
</td>
<td><p>When set to true, the module status per environment is also returned. The default value is false.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Modules list successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>Modules list successfully retrieved.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Module">Module</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No modules found in the infrastructure.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to list modules.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--modules--ModuleKey--"></span>
<div id="operation--modules--ModuleKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/modules/{ModuleKey}/</strong></h3>
Go to 
<a href="#tag--modules">/modules</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given module.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ModuleKey
</td>
<td><p>Key of the module to list the details from.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeEnvStatus
</td>
<td><p>Boolean to indicate if status per env should be returned. Default is false</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Module details successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Module">Module</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key: <code>&lt;ModuleKey&gt;</code>. The user does not have the required permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key: <code>&lt;ModuleKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key <code>&lt;ModuleKey&gt;</code></p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--modules--ModuleKey--versions-"></span>
<div id="operation--modules--ModuleKey--versions--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/modules/{ModuleKey}/versions/</strong></h3>
Go to 
<a href="#tag--modules">/modules</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns a list of versions of a given module.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ModuleKey
</td>
<td><p>The module from where to retrieve the versions from.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
MaximumVersionsToReturn
</td>
<td><p>Maximum number of versions to return. Default is 5.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of module versions successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>List of module versions successfully retrieved.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ModuleVersion_v2">ModuleVersion_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Invalid request due to invalid max versions to return (less than 0).</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key: <code>&lt;ModuleKey&gt;</code>. The user does not have the required permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key: <code>&lt;ModuleKey&gt;</code>.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to list module versions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--modules--ModuleKey--versions--ModuleVersionKey--"></span>
<div id="operation--modules--ModuleKey--versions--ModuleVersionKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/modules/{ModuleKey}/versions/{ModuleVersionKey}/</strong></h3>
Go to 
<a href="#tag--modules">/modules</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given module version.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
ModuleKey
</td>
<td><p>The module from where to retrieve the versions from.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ModuleVersionKey
</td>
<td><p>Key of the module version to return.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Module version details successfully retrieved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ModuleVersion_v2">ModuleVersion_v2</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key: <code>&lt;ModuleKey&gt;</code>. The user does not have the required permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Failed to retrieve the module with key: <code>&lt;ModuleKey&gt;</code>, or Failed to retrieve the module version with key: <code>&lt;ModuleKey&gt;</code></p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Failed to access the details of a module version.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--roles-"></span>
<div id="operation--roles--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/roles/</strong></h3>
Go to 
<a href="#tag--roles">/roles</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Lists all the roles.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
IncludeEnvPermissions
</td>
<td><p>Defines if it is to include a list of environment permissions for each role.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of Roles</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Role">Role</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User has no permissions to retrieve roles list.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--roles--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/roles/</strong></h3>
Go to 
<a href="#tag--roles">/roles</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Creates a role with the specified permissions.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>The role to be created.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Role">Role</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>Role created with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>The key of the newly created role.</p>
</section>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to create role because invalid role name, role is protected, wrong combination of infrastructure and manage teams flags or not defined/wrong permissions for all environments.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to create a new role.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--roles-permissionlevels-"></span>
<div id="operation--roles-permissionlevels--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/roles/permissionlevels/</strong></h3>
Go to 
<a href="#tag--roles">/roles</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Gets available permission levels.</p>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of permission levels.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/PermissionLevels">PermissionLevels</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to manage users and roles.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--roles--RoleKey--"></span>
<div id="operation--roles--RoleKey---delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/roles/{RoleKey}/</strong></h3>
Go to 
<a href="#tag--roles">/roles</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Deletes a role.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
RoleKey
</td>
<td><p>Role key to delete.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
UsersNewRoleKey
</td>
<td><p>Indicates the role that should replace the deleted role, for the users that have this role assigned (both as defaullt, application and team role). Needed if there are users with the role assigned.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>Role deleted with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Role can&#39;t be deleted because it is reserved.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to delete the role.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Role not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--roles--RoleKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/roles/{RoleKey}/</strong></h3>
Go to 
<a href="#tag--roles">/roles</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given role.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
RoleKey
</td>
<td><p>Role key to retrieve.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeEnvPermissions
</td>
<td><p>Defines if it is to include a list of environment permissions for role.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Record of Role</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Role">Role</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn&#39;t have permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Role not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--roles--RoleKey---put" class="swagger--panel-operation-put panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">PUT</span> <strong>/roles/{RoleKey}/</strong></h3>
Go to 
<a href="#tag--roles">/roles</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Updates a role with the specified permissions.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>The role to be update.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Role">Role</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
RoleKey
</td>
<td><p>Role key to update.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Role updated with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>The key of the updated role.</p>
</section>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to update role because invalid role name, role is protected, wrong combination of infrastructure and manage teams flags or not defined/wrong permissions for all environments.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the role.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Role not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--teams-"></span>
<div id="operation--teams--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/teams/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Lists all the teams.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
IncludeUsers
</td>
<td><p>Defines if it is to include a list of users that belong to the team.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeApplications
</td>
<td><p>Defines if it is to include a list of applications that belong to the team.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of Teams</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>A list of Team records including Users and Applications sub-lists, if requested.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Team">Team</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No teams defined</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User has no permissions to retrieve teams list.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--teams--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/teams/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Creates a team with the specified details. The operation only creates the team. Users and Applications should be associated using specific endpoints.</p>
</section>
<section class="sw-request-body">
<div class="row">
<div class="col-md-6">
<p><p>The team to be created.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Team">Team</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-responses">
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>Team created with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Team">Team</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to create team due to invalid team name.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to create a new team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--teams--TeamKey--"></span>
<div id="operation--teams--TeamKey---delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/teams/{TeamKey}/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Deletes a team.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>Team key to delete.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>Team deleted with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to delete a team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--teams--TeamKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/teams/{TeamKey}/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given team.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>Team key to retrieve.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
IncludeUsers
</td>
<td><p>Defines if it is to include a list of users that belong to the team.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeApplications
</td>
<td><p>Defines if it is to include a list of applications that belong to the team.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Record of Team</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Team">Team</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User don&#39;t have permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--teams--TeamKey---put" class="swagger--panel-operation-put panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">PUT</span> <strong>/teams/{TeamKey}/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Updates a team with the specified details. The operation only affects the Team details. Users and Applications should be associated or dissociated using specific endpoints.</p>
</section>
<section class="sw-request-body">
<div class="row">
<div class="col-md-6">
<p><p>The team to be updated.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Team">Team</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>Team key to update.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Team updated with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Team">Team</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to update team due to invalid team name.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--teams--TeamKey--applications-"></span>
<div id="operation--teams--TeamKey--applications--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/teams/{TeamKey}/applications/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Adds the specified application to a given team.</p>
</section>
<section class="sw-request-body">
<div class="row">
<div class="col-md-6">
<p><p>The application information to be added.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationShortInfo">ApplicationShortInfo</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>The key of the team where the add the applications.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>Application added with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to add application to team because application doesn&#39;t exist.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--teams--TeamKey--applications--ApplicationKey-"></span>
<div id="operation--teams--TeamKey--applications--ApplicationKey--delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/teams/{TeamKey}/applications/{ApplicationKey}</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Removes application from the given team.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>The team unique identifier.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ApplicationKey
</td>
<td><p>The application unique identifier.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Application removed with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to remove application to team because application doesn&#39;t exist.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team or application not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--teams--TeamKey--users-"></span>
<div id="operation--teams--TeamKey--users--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/teams/{TeamKey}/users/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Adds a user to a team with a specified role.</p>
</section>
<section class="sw-request-body">
<div class="row">
<div class="col-md-6">
<p><p>The user and role information to be added.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/UserRoleShortInfo">UserRoleShortInfo</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>The key of the team where the add the user.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>User added with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to add user to team because user doesn&#39;t exist or role doesn&#39;t exist.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--teams--TeamKey--users--UserKey--"></span>
<div id="operation--teams--TeamKey--users--UserKey---delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/teams/{TeamKey}/users/{UserKey}/</strong></h3>
Go to 
<a href="#tag--teams">/teams</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Removes a user from the given team</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
TeamKey
</td>
<td><p>The key of the team where the remove the user.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
UserKey
</td>
<td><p>The key of the user to be removed.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>User removed with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to remove user from team because user doesn&#39;t exist or role doesn&#39;t exist.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the team.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>Team or user not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--users-"></span>
<div id="operation--users--get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/users/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Lists all the users. By default shows only active users.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
IncludeInactive
</td>
<td><p>Defines if it is to include a list of inactive users.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeTeams
</td>
<td><p>Defines if it is to include a list of teams that the users belong to.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
IncludeApplicationRoles
</td>
<td><p>Defines if it is to include a list of applications that the users are associated with.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of Users</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>A list of User records.</p>
</section>
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/User">User</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>    </div>
</div></div>
</div>                </dd>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>No Users defined</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User has no permissions to retrieve users list.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--users--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/users/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Creates a user with the specified details. The operation only creates the user. Teams and Applications should be associated using specific endpoints.</p>
</section>
<section class="sw-request-body">
<div class="row">
<div class="col-md-6">
<p><p>The user to be created.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/User">User</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-responses">
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>User created with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>The key of the newly created user.</p>
</section>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to create user due to invalid username, name or role.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to create a new user.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--users--UserKey--"></span>
<div id="operation--users--UserKey---get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/users/{UserKey}/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Returns the details of a given user.</p>
</section>
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
UserKey
</td>
<td><p>User key to retrieve.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
includeTeams
</td>
<td><p>Defines if it is to include a list of teams that the user belong to.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
<tr>
<td>
includeApplicationRoles
</td>
<td><p>Defines if it is to include a list of applications that the user is associated with.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Record of User</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/User">User</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>User doesn&#39;t have permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>User not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<div id="operation--users--UserKey---put" class="swagger--panel-operation-put panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">PUT</span> <strong>/users/{UserKey}/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Updates a user with the specified details. The operation only updates the user details. Teams and Applications should be associated using specific endpoints.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>The user to be updated.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/User">User</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
UserKey
</td>
<td><p>User key to update.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>User updated with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<section class="json-schema-description">
<p>The key of the updated user.</p>
</section>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to update user due to invalid username, name or role.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the user.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>User not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--users--UserKey--applications-"></span>
<div id="operation--users--UserKey--applications--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/users/{UserKey}/applications/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Grants a given role to the given application to the user.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>The key of the application and Role to grant permissions.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationRole">ApplicationRole</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
UserKey
</td>
<td><p>User key to grant permissions.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-201">
201 Created
</dt>
<dd class="sw-response-201">
<div class="row">
<div class="col-md-12">
<p>Permissions granted with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to add application to user because application or role are invalid.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to change User permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>User not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--users--UserKey--applications--ApplicationKey--"></span>
<div id="operation--users--UserKey--applications--ApplicationKey---delete" class="swagger--panel-operation-delete panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">DELETE</span> <strong>/users/{UserKey}/applications/{ApplicationKey}/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Revokes user&#39;s role in application permission.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
UserKey
</td>
<td><p>User key to grant permissions.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
<tr>
<td>
ApplicationKey
</td>
<td><p>The key of the application to grant permissions.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-204">
204 No Content
</dt>
<dd class="sw-response-204">
<div class="row">
<div class="col-md-12">
<p>Permissions revoked with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to change User permissions.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>User or permission not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<span id="path--users--UserKey--setpassword-"></span>
<div id="operation--users--UserKey--setpassword--post" class="swagger--panel-operation-post panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/users/{UserKey}/setpassword/</strong></h3>
Go to 
<a href="#tag--users">/users</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Allows to change a password of a given user.</p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="row">
<div class="col-md-6">
<p><p>The new password value.</p>
</p>
</div>
<div class="col-md-6 sw-request-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Password">Password</a>
</div>
</div></div>
</div>
</section>        
<section class="sw-request-params">
<table class="table">
<thead>
<tr>
<th class="sw-param-name"></th>
<th class="sw-param-description"></th>
<th class="sw-param-type"></th>
<th class="sw-param-data-type"></th>
<th class="sw-param-annotation"></th>
</tr>
</thead>
<tbody>
<tr>
<td>
UserKey
</td>
<td><p>User key to update.</p>
</td>
<td>path</td>
<td>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</td>
<td>
<span class="json-property-required"></span>
</td>
</tr>
</tbody>
</table>
</section>
<section class="sw-responses">
<p><span class="label label-default">text/plain</span> 
</p>
<dl>
<dt class="sw-response-200">
200 OK
</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>User password updated with success.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
</div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Failed to change password because password is invalid.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>No permissions to update the user password.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">
<p>User not found.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-405">
405 Method Not Allowed
</dt>
<dd class="sw-response-405">
<div class="row">
<div class="col-md-12">
<p>Failed to change password because external authentication provider is in use.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="row">
<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
<h2>Structures</h2>
<div id="definition-Application" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Application"></a>Application:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>An application with its details and its status in the environments were it is running.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>Application unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<p>Name of the application.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Kind">
<span class="json-property-name">Kind:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<p>Identifies the kind of application. [Mobile|WebResponsive]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Team">
<span class="json-property-name">Team:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The team that owns the application.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Description">
<span class="json-property-name">Description:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Description of the application.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="URLPath">
<span class="json-property-name">URLPath:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>Relative URL path of the application, starting from the hostname.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IconHash">
<span class="json-property-name">IconHash:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>Hash of the application icon. Can be used to detect changes in the application icon.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IconURL">
<span class="json-property-name">IconURL:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>The URL for the application icon.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsSystem">
<span class="json-property-name">IsSystem:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>Indicates if the application is a built-in component of the AgilePlatform (e.g. ServiceCenter, LifeTime, ...).</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="AppStatusInEnvs">
<span class="json-property-name">AppStatusInEnvs:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>Information about the status of the application in each environment it is running.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/AppStatusInEnv_v2">AppStatusInEnv_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationConflict" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationConflict"></a>ApplicationConflict:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>A depoyment conflict.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Message">
<span class="json-property-name">Message:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Description of the conflict.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ProducerApplicationOperation">
<span class="json-property-name">ProducerApplicationOperation:</span>
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationOperation">ApplicationOperation</a>
</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConsumerApplicationOperation">
<span class="json-property-name">ConsumerApplicationOperation:</span>
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationOperation">ApplicationOperation</a>
</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ModuleConflict">
<span class="json-property-name">ModuleConflict:</span>
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ModuleConflict">ModuleConflict</a>
</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationConflictListTextListDeployment_v2Record" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationConflictListTextListDeployment_v2Record"></a>ApplicationConflictListTextListDeployment_v2Record:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="Deployment">
<span class="json-property-name">Deployment:</span>
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Deployment_v2">Deployment_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationsToRedeploy">
<span class="json-property-name">ApplicationsToRedeploy:</span>
<span class="json-property-type">string[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="ApplicationConflicts">
<span class="json-property-name">ApplicationConflicts:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationConflict">ApplicationConflict</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationOperation" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationOperation"></a>ApplicationOperation:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Operation executed in the deployment over the application.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="ApplicationKey">
<span class="json-property-name">ApplicationKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationVersionKey">
<span class="json-property-name">ApplicationVersionKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application Version unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DeploymentOperation">
<span class="json-property-name">DeploymentOperation:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Label of the operation to be performed. Example: Deploy 1.5.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationOperation_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationOperation_v2"></a>ApplicationOperation_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Operation executed in the deployment over the application.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="ApplicationKey">
<span class="json-property-name">ApplicationKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationVersionKey">
<span class="json-property-name">ApplicationVersionKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application Version unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DeploymentOperation">
<span class="json-property-name">DeploymentOperation:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Label of the operation to be performed. Example: Deploy 1.5.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DeploymentZoneKey">
<span class="json-property-name">DeploymentZoneKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment Zone unique identifier</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationRole" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationRole"></a>ApplicationRole:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Represents a set of an application and a role.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="applicationKey">
<span class="json-property-name">applicationKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="applicationName">
<span class="json-property-name">applicationName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="roleKey">
<span class="json-property-name">roleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="roleName">
<span class="json-property-name">roleName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationShortInfo" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationShortInfo"></a>ApplicationShortInfo:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>A simplification of application structure.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<p>Application unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the application.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationVersion_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationVersion_v2"></a>ApplicationVersion_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Information about a specific version of an application and the versions of its modules.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<p>Application version unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationKey">
<span class="json-property-name">ApplicationKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Version">
<span class="json-property-name">Version:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Version of the application.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ChangeLog">
<span class="json-property-name">ChangeLog:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Change Log associated to this Application Version.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedOn">
<span class="json-property-name">CreatedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>When was the Application Version created.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="InUse">
<span class="json-property-name">InUse:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Defines if the Application Version is being used.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="MobileVersions">
<span class="json-property-name">MobileVersions:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>List of mobile versions.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/MobileVersion">MobileVersion</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="PrimaryColor">
<span class="json-property-name">PrimaryColor:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The primary color of the application interface.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="NativeHash">
<span class="json-property-name">NativeHash:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The native has relative to the mobile platform.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ModuleVersions">
<span class="json-property-name">ModuleVersions:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>List of module versions.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ModuleVersion_v2">ModuleVersion_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationVersionCreate" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationVersionCreate"></a>ApplicationVersionCreate:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>A structure holding the new version name for the application and for its native applications, if applicable.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="ChangeLog">
<span class="json-property-name">ChangeLog:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Change log of the version to be created.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Version">
<span class="json-property-name">Version:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Version of the application.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="MobileVersions">
<span class="json-property-name">MobileVersions:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>List of mobile versions.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/MobileVersion">MobileVersion</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="ModuleVersionKeys">
<span class="json-property-name">ModuleVersionKeys:</span>
<span class="json-property-type">string[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>[DEPRECATED] List of module version keys to validate if the current state of the application is still the expected. This parameter was deprecated on LifeTime Feb 2019 Release, there is no need to pass the module version keys. If the module version keys are passed, they will still be validated.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord"></a>ApplicationVersionKeyDeploymentZoneKeyRecordListTextTextTextRecord:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="Notes">
<span class="json-property-name">Notes:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SourceEnvironmentKey">
<span class="json-property-name">SourceEnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="TargetEnvironmentKey">
<span class="json-property-name">TargetEnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationOperations">
<span class="json-property-name">ApplicationOperations:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/TextTextRecord">TextTextRecord</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-AppStatusInEnv_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/AppStatusInEnv_v2"></a>AppStatusInEnv_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Status of application in a given environment.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="EnvironmentKey">
<span class="json-property-name">EnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="BaseApplicationVersionKey">
<span class="json-property-name">BaseApplicationVersionKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Base application version unique identifier. If app is not modified in environment, this is the application version deployed.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsModified">
<span class="json-property-name">IsModified:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>True if the application has been changed since the last tag, false otherwise.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsModifiedReason">
<span class="json-property-name">IsModifiedReason:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates the application status.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsModifiedMessage">
<span class="json-property-name">IsModifiedMessage:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates the application status.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConsistencyStatus">
<span class="json-property-name">ConsistencyStatus:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates the application consistency status.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConsistencyStatusMessages">
<span class="json-property-name">ConsistencyStatusMessages:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Messages regarding the consistency status of the application.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="MobileAppsStatus">
<span class="json-property-name">MobileAppsStatus:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Status of mobile apps in environment.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/MobileAppStatusInEnv">MobileAppStatusInEnv</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="ModuleStatusInEnvs">
<span class="json-property-name">ModuleStatusInEnvs:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Status of modules in environment.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ModuleStatusInEnv">ModuleStatusInEnv</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="DeploymentZoneKey">
<span class="json-property-name">DeploymentZoneKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment Zone unique identifier</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Deployment_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Deployment_v2"></a>Deployment_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Deployment information with the operations executed.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SourceEnvironmentKey">
<span class="json-property-name">SourceEnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Source environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="TargetEnvironmentKey">
<span class="json-property-name">TargetEnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Target environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Notes">
<span class="json-property-name">Notes:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment notes.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedOn">
<span class="json-property-name">CreatedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Date and time when the deployment plan was created.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="CreatedBy">
<span class="json-property-name">CreatedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who created the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedByUsername">
<span class="json-property-name">CreatedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who created the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SavedOn">
<span class="json-property-name">SavedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The date and time when the deployment plan was saved.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="SavedBy">
<span class="json-property-name">SavedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who last saved the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SavedByUsername">
<span class="json-property-name">SavedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who last saved the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="StartedOn">
<span class="json-property-name">StartedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The date and time when the deployment started.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="StartedBy">
<span class="json-property-name">StartedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who started the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="StartedByUsername">
<span class="json-property-name">StartedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who started the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="AbortedOn">
<span class="json-property-name">AbortedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The date and time when the deployment was aborted.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="AbortedBy">
<span class="json-property-name">AbortedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who aborted the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="AbortedByUsername">
<span class="json-property-name">AbortedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who aborted the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationOperations">
<span class="json-property-name">ApplicationOperations:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>List of Application Operations included in the deployment.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationOperation_v2">ApplicationOperation_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-DeploymentData_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/DeploymentData_v2"></a>DeploymentData_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Deployment information with the operations executed.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SourceEnvironmentKey">
<span class="json-property-name">SourceEnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Source environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="TargetEnvironmentKey">
<span class="json-property-name">TargetEnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Target environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Notes">
<span class="json-property-name">Notes:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment notes.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedOn">
<span class="json-property-name">CreatedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Date and time when the deployment plan was created.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="CreatedBy">
<span class="json-property-name">CreatedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who created the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedByUsername">
<span class="json-property-name">CreatedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who created the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SavedOn">
<span class="json-property-name">SavedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The date and time when the deployment plan was saved.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="SavedBy">
<span class="json-property-name">SavedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who last saved the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="SavedByUsername">
<span class="json-property-name">SavedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who last saved the deployment plan.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="StartedOn">
<span class="json-property-name">StartedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The date and time when the deployment started.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="StartedBy">
<span class="json-property-name">StartedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who started the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="StartedByUsername">
<span class="json-property-name">StartedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who started the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="AbortedOn">
<span class="json-property-name">AbortedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The date and time when the deployment was aborted.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="AbortedBy">
<span class="json-property-name">AbortedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user who aborted the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="AbortedByUsername">
<span class="json-property-name">AbortedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user who aborted the deployment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationOperations">
<span class="json-property-name">ApplicationOperations:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>List of Application Operations included in the deployment.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/TextTextRecord">TextTextRecord</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-DeploymentMessage" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/DeploymentMessage"></a>DeploymentMessage:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Message from a deployment operation log.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Instant">
<span class="json-property-name">Instant:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Date and time when the message was logged.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="Message">
<span class="json-property-name">Message:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Details of the message.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-DeploymentMessageListTextTextRecord" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/DeploymentMessageListTextTextRecord"></a>DeploymentMessageListTextTextRecord:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="DeploymentStatus">
<span class="json-property-name">DeploymentStatus:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Info">
<span class="json-property-name">Info:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DeploymentLog">
<span class="json-property-name">DeploymentLog:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/DeploymentMessage">DeploymentMessage</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-DeploymentTechnology_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/DeploymentTechnology_v2"></a>DeploymentTechnology_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Deployment Hosting technology of the Deployment Zone.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment Technology unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of deployment technology</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-DeploymentZone_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/DeploymentZone_v2"></a>DeploymentZone_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Deployment Zone of an environment.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Deployment Zone unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of deployment zone</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsDefault">
<span class="json-property-name">IsDefault:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>True if the deployment zone is the default one in the environment</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DeploymentTechnology">
<span class="json-property-name">DeploymentTechnology:</span>
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/DeploymentTechnology_v2">DeploymentTechnology_v2</a>
</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-DownloadLink" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/DownloadLink"></a>DownloadLink:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>The link for the application binary file.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="url">
<span class="json-property-name">url:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The link for the application binary file.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="expires">
<span class="json-property-name">expires:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The expiration date and time of the returned link.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Environment" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Environment"></a>Environment:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>An environment and its information.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Unique identifier of the environment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the environment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="OSVersion">
<span class="json-property-name">OSVersion:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Platform Server version. [X.X.X.X]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Order">
<span class="json-property-name">Order:</span>
<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The order of the environment as registered in Lifetime.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="HostName">
<span class="json-property-name">HostName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Hostname of the environment as registered.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="UseHTTPS">
<span class="json-property-name">UseHTTPS:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates if connections to the environment are made using HTTPS.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="EnvironmentType">
<span class="json-property-name">EnvironmentType:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates the type of the environment. [Development | Test | Production]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="NumberOfFrontEnds">
<span class="json-property-name">NumberOfFrontEnds:</span>
<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Number of front-end servers in the environment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationServerType">
<span class="json-property-name">ApplicationServerType:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Stack of the application server. [.NET | JAVA]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationServer">
<span class="json-property-name">ApplicationServer:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application server in use. [IIS | JBoss | WebLogic]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DatabaseProvider">
<span class="json-property-name">DatabaseProvider:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Type of database provider. [SqlServer | Oracle]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsCloudEnvironment">
<span class="json-property-name">IsCloudEnvironment:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates if the environment is running on a cloud service.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-EnvironmentPermission" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/EnvironmentPermission"></a>EnvironmentPermission:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">

<section class="json-schema-description">
<p>Definition of Environment Permissions</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="environmentKey">
<span class="json-property-name">environmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Key of the environment that refers to the permission.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="environmentName">
<span class="json-property-name">environmentName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the environment that refers to the permission.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="level">
<span class="json-property-name">level:</span>
<span class="json-property-type">integer</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Level of permission.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="levelLabel">
<span class="json-property-name">levelLabel:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Short description of the permission level.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="createApplications">
<span class="json-property-name">createApplications:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Allows to create new applications.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="addDependenciesToSystem">
<span class="json-property-name">addDependenciesToSystem:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Allows to add depedencies to System application.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Exception" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Exception"></a>Exception:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="Errors">
<span class="json-property-name">Errors:</span>
<span class="json-property-type">string[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
<section class="json-schema-description">
<p>Full detail of the error</p>
</section>
</div>
</section>                </div>
</dd>
<dt data-property-name="StatusCode">
<span class="json-property-name">StatusCode:</span>
<span class="json-property-type">integer</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-default-value">500</span>
</dt>
<dd>
<p>Status code raised with the error.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-MobileAppStatusInEnv" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/MobileAppStatusInEnv"></a>MobileAppStatusInEnv:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Status of mobile application in a given environment.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="EnvironmentKey">
<span class="json-property-name">EnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="NativePlatform">
<span class="json-property-name">NativePlatform:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of native platform. [Android | iOS]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="VersionNumber">
<span class="json-property-name">VersionNumber:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The version number, like for example 1.5.4, of the native build. It is used to be able to map the version to the version in the Andoid or iOS store.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="HasBinaryAvailable">
<span class="json-property-name">HasBinaryAvailable:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>True if the binary of the application is available for the current configuration.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsConfigured">
<span class="json-property-name">IsConfigured:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>True if the application is configured.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsConfigurationChanged">
<span class="json-property-name">IsConfigurationChanged:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>True if the configuration of the Mobile Application has changed in the environment.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsModified">
<span class="json-property-name">IsModified:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>True if the Native Hash of the Mobile Application does not match the one in the AppVersionNativeBuild baseline.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-MobileVersion" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/MobileVersion"></a>MobileVersion:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>A mobile version and its information.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="NativePlatform">
<span class="json-property-name">NativePlatform:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of native platform. [Android | iOS]</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="VersionNumber">
<span class="json-property-name">VersionNumber:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The version number, like for example 1.5.4, of the native build. It is used to be able to map the version to the version in the Andoid or iOS store.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="VersionDescription">
<span class="json-property-name">VersionDescription:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>The description of the mobile version.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Module" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Module"></a>Module:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Module information and the status in the environments where the modules are running.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Module unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the module.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Description">
<span class="json-property-name">Description:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Description of the module.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Kind">
<span class="json-property-name">Kind:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Module type (eSpace or Extension).</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ModuleStatusInEnv">
<span class="json-property-name">ModuleStatusInEnv:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Status of the module in environments</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ModuleStatusInEnv">ModuleStatusInEnv</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ModuleConflict" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ModuleConflict"></a>ModuleConflict:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>A module conflict.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="ProducerModuleKey">
<span class="json-property-name">ProducerModuleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Producer Module unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConsumerModuleKey">
<span class="json-property-name">ConsumerModuleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Consumer Module unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="TotalRequiredElements">
<span class="json-property-name">TotalRequiredElements:</span>
<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Total number of required elements.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConflictType">
<span class="json-property-name">ConflictType:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Type of conflict. [Producer Module Missing|Producer Element Missing|Producer Element Incompatible|Consumer Module Outdated|Newer Producer Module Available|IncompatiblePlatformServer|ConsumerModuleMoved|ProducerModuleMoved|NameColision]</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ModuleStatusInEnv" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ModuleStatusInEnv"></a>ModuleStatusInEnv:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Status of module in a given environment.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="ApplicationKey">
<span class="json-property-name">ApplicationKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Application unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="EnvironmentKey">
<span class="json-property-name">EnvironmentKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Environment unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ModuleVersionKey">
<span class="json-property-name">ModuleVersionKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Module version unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConsistencyStatus">
<span class="json-property-name">ConsistencyStatus:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Indicates the module consistency status.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ConsistencyStatusMessages">
<span class="json-property-name">ConsistencyStatusMessages:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Messages regarding the consistency status of the module.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ModuleVersion_v2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ModuleVersion_v2"></a>ModuleVersion_v2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>A module version and its information.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Module version unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ModuleKey">
<span class="json-property-name">ModuleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Module unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedOn">
<span class="json-property-name">CreatedOn:</span>
<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Date and time of the module version creation.</p>
<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">&quot;2014-12-31T23:59:59.938Z&quot;</code></pre>
</section>
</div>
</dd>
<dt data-property-name="CreatedBy">
<span class="json-property-name">CreatedBy:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of the user that created the version.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="CreatedByUsername">
<span class="json-property-name">CreatedByUsername:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Username of the user that created the version.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="GeneralHash">
<span class="json-property-name">GeneralHash:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Non-unique hash of the module version. Can be used to validate if two module versions have semantic differences.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DirectUpgradeFromHash">
<span class="json-property-name">DirectUpgradeFromHash:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>If this module version is the result of a direct upgrade of another version, then this field contains the key of that version</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-NewApplication" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/NewApplication"></a>NewApplication:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="TemplateKey">
<span class="json-property-name">TemplateKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="TeamKey">
<span class="json-property-name">TeamKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Description">
<span class="json-property-name">Description:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Color">
<span class="json-property-name">Color:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Password" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Password"></a>Password:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Definition of a password.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="password">
<span class="json-property-name">password:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Password value.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-PermissionLevels" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/PermissionLevels"></a>PermissionLevels:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="level">
<span class="json-property-name">level:</span>
<span class="json-property-type">integer</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Value that identifies the permission level.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="levelLabel">
<span class="json-property-name">levelLabel:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Short description of the permission level.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="description">
<span class="json-property-name">description:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Full description of the permission level.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Role" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Role"></a>Role:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Full definition of a role.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="key">
<span class="json-property-name">key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<p>Identifier of a role.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="name">
<span class="json-property-name">name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of a role</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="manageInfrastructure">
<span class="json-property-name">manageInfrastructure:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Allows manage the infrastructure.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="manageTeams">
<span class="json-property-name">manageTeams:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Allows to manage teams and roles.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="environmentPermissions">
<span class="json-property-name">environmentPermissions:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Definition of permission levels per environment.</p>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/EnvironmentPermission">EnvironmentPermission</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Team" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Team"></a>Team:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Definition of a team</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="key">
<span class="json-property-name">key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="name">
<span class="json-property-name">name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="description">
<span class="json-property-name">description:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="users">
<span class="json-property-name">users:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/UserRole">UserRole</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="applications">
<span class="json-property-name">applications:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-read-only"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationShortInfo">ApplicationShortInfo</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-TeamRole" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TeamRole"></a>TeamRole:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Pair Team and Role information.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="TeamKey">
<span class="json-property-name">TeamKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="TeamName">
<span class="json-property-name">TeamName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="RoleKey">
<span class="json-property-name">RoleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="RoleName">
<span class="json-property-name">RoleName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-Template" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Template"></a>Template:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Template of an environment.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Template unique identifier.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Name of template.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Description">
<span class="json-property-name">Description:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Description of template.</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationKind">
<span class="json-property-name">ApplicationKind:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>Type of the application [Web|Mobile|Service|Reactive].</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-TextRecord" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TextRecord"></a>TextRecord:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="ApplicationVersionKey">
<span class="json-property-name">ApplicationVersionKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<p>The key of the newly created application version.</p>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-TextRecord2" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TextRecord2"></a>TextRecord2:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="ApplicationKey">
<span class="json-property-name">ApplicationKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>
<div id="definition-TextTextRecord" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TextTextRecord"></a>TextTextRecord:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-properties">
<dl>
<dt data-property-name="ApplicationVersionKey">
<span class="json-property-name">ApplicationVersionKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="DeploymentZoneKey">
<span class="json-property-name">DeploymentZoneKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-required"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>
<div id="definition-User" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/User"></a>User:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Definition of a user. Also includes the teams to which the user belongs and the roles in specific applications.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="Key">
<span class="json-property-name">Key:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>readonly</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Username">
<span class="json-property-name">Username:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Email">
<span class="json-property-name">Email:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="IsActive">
<span class="json-property-name">IsActive:</span>
<span class="json-property-type">boolean</span>
<span class="json-property-range" title="Value limits"></span>
<span class="json-property-default-value">true</span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="RoleKey">
<span class="json-property-name">RoleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="RoleName">
<span class="json-property-name">RoleName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<p>readonly</p>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="ApplicationRoles">
<span class="json-property-name">ApplicationRoles:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationRole">ApplicationRole</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
<dt data-property-name="Teams">
<span class="json-property-name">Teams:</span>
<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
<section class="json-schema-array-items">
<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/TeamRole">TeamRole</a>
</span>
<span class="json-property-range" title="Value limits"></span>
<div class="json-inner-schema">
</div>
</section>                </div>
</dd>
</dl>
</section>
</div>
</div>
<div id="definition-UserRole" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/UserRole"></a>UserRole:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Pair User and Role information.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="UserKey">
<span class="json-property-name">UserKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="Username">
<span class="json-property-name">Username:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="RoleKey">
<span class="json-property-name">RoleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="RoleName">
<span class="json-property-name">RoleName:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
</dl>
</section>
</div>
</div>
<div id="definition-UserRoleShortInfo" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/UserRoleShortInfo"></a>UserRoleShortInfo:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>
</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Pair User Key and Role Key minimal information.</p>
</section>
<section class="json-schema-properties">
<dl>
<dt data-property-name="userKey">
<span class="json-property-name">userKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div>
</dd>
<dt data-property-name="roleKey">
<span class="json-property-name">roleKey:</span>
<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>
</dt>
<dd>
<div class="json-inner-schema">
</div></dd></dl></section></div></div>
