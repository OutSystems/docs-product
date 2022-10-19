---
summary: Allows you to get the technical debt details of an OutSystems infrastructure.
tags: article-page; support-application_development; support-Application_Lifecycle; support-devOps; support-Integrations_Extensions
locale: en-us
guid: 29A5FD23-8A6E-4B2B-853F-58AD0A34C560
app_type: traditional web apps, mobile apps, reactive web apps
---

# Architecture Dashboard API

<style>

/* Styles for API doc */
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
            content: "List of";
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
        .sw-info {
            font-weight: bold
        }

        .sw-info span {
            font-family: monospace;
            font-weight: normal;
            font-size: 1.1em
        }
                .sw-responses p {
            margin-bottom: 0px !important;
        }
        .sw-responses dd {
            margin-bottom: 10px !important;
        }
</style>

Architecture Dashboard API helps you manage technical debt, allowing you to use its data in third-party tools. This enables you to:

* Integrate technical debt data from [Architecture Dashboard](../../../managing-the-applications-lifecycle/manage-tech-debt/intro.md) with other technical debt and BI tools you already use.

* Use technical debt data as a quality gate of an automated CI/CD pipeline. This ensures that deploys meet a predefined technical debt value.   

<div class="info" markdown="1">

Note: New findings are only processed every 12 hours.

</div>

To authenticate your API requests, follow the guidelines in the [Architecture Dashboard API authentication](../architecture-dashboard/ad-api-authentication.md) article.

You can access the Swagger file from the [Architecture Dashboard API page](https://architecture.outsystems.com/ArchitectureDashboardAPI/rest/V1/):

![Architecture Dashboard API page, where you can download the swagger by clicking **swagger.json**.](images/api-swagger-ad.png)

<div class="container">
<h1>V1</h1>
<p class="sw-info">
Base URL: <span class="sw-info-basePath">/ArchitectureDashboardAPI/rest/V1</span>,
Version: <span class="sw-info-version">1</span>
</p>
<p><p>Provides technical debt details of an OutSystems infrastructure.</p>
</p>

<div id="sw-schemes" class="sw-default-value">
<span class="sw-default-value-header">Schemes:</span>
https
</div>

<h2 id="swagger--summary-no-tags">Summary</h2>
<table class="table table-bordered table-condensed swagger--summary">
<thead>
<tr>
<th>Path</th>
<th>Operation</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td class="swagger--summary-path" rowspan="1">
<a href="#path--TechnicalDebt_Application">/TechnicalDebt_Application</a>
</td>
<td>
<a href="#operation--TechnicalDebt_Application-get">GET</a>
</td>
<td>Retrieves a list of applications and modules, with technical debt information.</td>
</tr>
<tr>
<td class="swagger--summary-path" rowspan="1">
<a href="#path--TechnicalDebt_Category">/TechnicalDebt_Category</a>
</td>
<td>
<a href="#operation--TechnicalDebt_Category-get">GET</a>
</td>
<td>Retrieves the list of pattern categories, to be used as reference in other methods.</td>
</tr>
<tr>
<td class="swagger--summary-path" rowspan="1">
<a href="#path--TechnicalDebt_LastAnalysisDate">/TechnicalDebt_LastAnalysisDate</a>
</td>
<td>
<a href="#operation--TechnicalDebt_LastAnalysisDate-get">GET</a>
</td>
<td>Retrieves the date and time when the last analysis was performed.</td>
</tr>
<tr>
<td class="swagger--summary-path" rowspan="1">
<a href="#path--TechnicalDebt_Level">/TechnicalDebt_Level</a>
</td>
<td>
<a href="#operation--TechnicalDebt_Level-get">GET</a>
</td>
<td>Retrieves the list of technical debt levels, to be used as reference in other methods.</td>
</tr>
<tr>
<td class="swagger--summary-path" rowspan="1">
<a href="#path--TechnicalDebt_Team">/TechnicalDebt_Team</a>
</td>
<td>
<a href="#operation--TechnicalDebt_Team-get">GET</a>
</td>
<td>Retrieves a list of teams and their associated applications, to be used as reference in other methods.</td>
</tr>
</tbody>
</table>

<h2>Paths</h2>

<span id="path--TechnicalDebt_Application"></span>
<div id="operation--TechnicalDebt_Application-get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/TechnicalDebt_Application</strong></h3>
Tags:
<a href="#tag-V1">V1</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Retrieves a list of applications and modules, with technical debt information.</p>

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
ApplicationGUID
</td>
<td><p>Optional filter by application guid.</p>
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
ModuleGUID
</td>
<td><p>Optional filter by module guid.</p>
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
Date
</td>
<td><p>Optionally request data for a specific date. If absent, the call returns the most recent data available.</p>
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
Limit
</td>
<td><p>Maximum number of applications to return. Defaults to 20. The maximum allowed is 200.</p>
</td>
<td>query</td>
<td>
<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>

</td>
<td>
</td>
</tr>
<tr>
<td>
Offset
</td>
<td><p>Starting position from which to return the results. Defaults to 0.</p>
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

<!-- List of response codes -->
<dl>    

<!-- 200 -->
<dt class="sw-response-200">
200 OK

</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of applications and modules, with technical debt information.</p>

</div>
</div>
<div class="row">

<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/ApplicationTechnicalDebt">ApplicationTechnicalDebt</a>
</div>
</div></div>

</div>                </dd>

<!-- 400 -->
<dt class="sw-response-400">
400 Bad Request

</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Missing authentication headers, or parameters out of bounds.</p>

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

<!-- 401 -->
<dt class="sw-response-401">
401 Unauthorized

</dt>
<dd class="sw-response-401">
<div class="row">
<div class="col-md-12">
<p>Invalid credentials</p>

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

<!-- 403 -->
<dt class="sw-response-403">
403 Forbidden

</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Infrastructure is inactive, or the Architecture Dashboard API feature isn't licensed.</p>

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

<!-- 404 -->
<dt class="sw-response-404">
404 Not Found

</dt>
<dd class="sw-response-404">
<div class="row">
<div class="col-md-12">

<ul>
  <li>No data available for the requested date</li>
  <li>No application found with a key matching the Application input parameter</li>
  <li>No module found with a key matching the Module input parameter</li>
</ul>

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

<!-- 429 -->
<dt class="sw-response-429">
429 Too many requests

</dt>
<dd class="sw-response-429">
<div class="row">
<div class="col-md-12">
<p>The customer has exceeded their request quota.</p>

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

<!-- 500 -->
<dt class="sw-response-500">
500 Internal Server Error

</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>The data analysis for the requested date was unsuccessful; other internal problems (customer should contact OutSystems support if the problem persists).</p>

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

<!-- 503 -->
<dt class="sw-response-503">
503 Service Unavailable

</dt>
<dd class="sw-response-503">
<div class="row">
<div class="col-md-12">
<p>The data for the requested date is currently being analyzed. The server includes a Retry-After header in the response.</p>

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

<span id="path--TechnicalDebt_Category"></span>
<div id="operation--TechnicalDebt_Category-get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/TechnicalDebt_Category</strong></h3>
Tags:
<a href="#tag-V1">V1</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Retrieves the list of pattern categories, to be used as reference in other methods.</p>

</section>

<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>

<!-- List of response codes -->
<dl>

<!-- 200 -->
<dt class="sw-response-200">
200 OK

</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of categories and the patterns they contain.</p>

</div>
</div>
<div class="row">

<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/CategoryTechnicalDebt">CategoryTechnicalDebt</a>
</div>
</div></div>

</div>                </dd>

<!-- 400 -->
<dt class="sw-response-400">
400 Bad Request

</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Missing authentication headers.</p>

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

<!-- 401 -->
<dt class="sw-response-401">
401 Unauthorized

</dt>
<dd class="sw-response-401">
<div class="row">
<div class="col-md-12">
<p>Invalid credentials</p>

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

<!-- 403 -->
<dt class="sw-response-403">
403 Forbidden

</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Infrastructure is inactive, or the Architecture Dashboard API feature isn't licensed.</p>

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

<!-- 429 -->
<dt class="sw-response-429">
429 Too many requests

</dt>
<dd class="sw-response-429">
<div class="row">
<div class="col-md-12">
<p>The customer has exceeded their request quota.</p>

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

<!-- 500 -->
<dt class="sw-response-500">
500 Internal Server Error

</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Other internal problems (customer should contact OutSystems support if the problem persists).</p>

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

<span id="path--TechnicalDebt_LastAnalysisDate"></span>
<div id="operation--TechnicalDebt_LastAnalysisDate-get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/TechnicalDebt_LastAnalysisDate</strong></h3>
Tags:
<a href="#tag-V1">V1</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Retrieves the date and time when the last analysis was performed.</p>

</section>

<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>

<!-- List of response codes -->
<dl>

<!-- 200 -->
<dt class="sw-response-200">
200 OK

</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>Infrastructure information, including the last analysis date.</p>

</div>
</div>
<div class="row">

<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/InfrastructureInfo">InfrastructureInfo</a>
</div>
</div></div>

</div>                </dd>

<!-- 400 -->
<dt class="sw-response-400">
400 Bad Request

</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Missing authentication headers.</p>

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

<!-- 401 -->
<dt class="sw-response-401">
401 Unauthorized

</dt>
<dd class="sw-response-401">
<div class="row">
<div class="col-md-12">
<p>Invalid credentials</p>

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

<!-- 403 -->
<dt class="sw-response-403">
403 Forbidden

</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Infrastructure is inactive, or the Architecture Dashboard API feature isn't licensed.</p>

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

<!-- 429 -->
<dt class="sw-response-429">
429 Too many requests

</dt>
<dd class="sw-response-429">
<div class="row">
<div class="col-md-12">
<p>The customer has exceeded their request quota.</p>

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

<!-- 500 -->
<dt class="sw-response-500">
500 Internal Server Error

</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Other internal problems (customer should contact OutSystems support if the problem persists).</p>

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

<span id="path--TechnicalDebt_Level"></span>
<div id="operation--TechnicalDebt_Level-get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/TechnicalDebt_Level</strong></h3>
Tags:
<a href="#tag-V1">V1</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Retrieves the list of technical debt levels, to be used as reference in other methods.</p>

</section>

<section class="sw-responses">
<p><span class="label label-default">application/json</span> 
</p>

<!-- List of response codes -->
<dl>

<!-- 200 -->
<dt class="sw-response-200">
200 OK

</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of technical debt levels.</p>

</div>
</div>
<div class="row">

<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/TechnicalDebtLevels">TechnicalDebtLevels</a>
</div>
</div></div>

</div>                </dd>

<!-- 400 -->
<dt class="sw-response-400">
400 Bad Request

</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Missing authentication headers.</p>

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

<!-- 401 -->
<dt class="sw-response-401">
401 Unauthorized

</dt>
<dd class="sw-response-401">
<div class="row">
<div class="col-md-12">
<p>Invalid credentials</p>

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

<!-- 403 -->
<dt class="sw-response-403">
403 Forbidden

</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Infrastructure is inactive, or the Architecture Dashboard API feature isn't licensed.</p>

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

<!-- 429 -->
<dt class="sw-response-429">
429 Too many requests

</dt>
<dd class="sw-response-429">
<div class="row">
<div class="col-md-12">
<p>The customer has exceeded their request quota.</p>

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

<!-- 500 -->
<dt class="sw-response-500">
500 Internal Server Error

</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Other internal problems (customer should contact OutSystems support if the problem persists).</p>

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

<span id="path--TechnicalDebt_Team"></span>
<div id="operation--TechnicalDebt_Team-get" class="swagger--panel-operation-get panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">GET</span> <strong>/TechnicalDebt_Team</strong></h3>
Tags:
<a href="#tag-V1">V1</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Retrieves a list of teams and their associated applications, to be used as reference in other methods.</p>

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
Team
</td>
<td><p>Optional filter by team external id.</p>
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

<!-- List of response codes -->
<dl>

<!-- 200 -->
<dt class="sw-response-200">
200 OK

</dt>
<dd class="sw-response-200">
<div class="row">
<div class="col-md-12">
<p>List of teams and their associated applications.</p>

</div>
</div>
<div class="row">

<div class="col-md-6 sw-response-model">
<div  class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/TeamTechnicalDebt">TeamTechnicalDebt</a>
</div>
</div></div>

</div>                </dd>

<!-- 400 -->
<dt class="sw-response-400">
400 Bad Request

</dt>
<dd class="sw-response-400">
<div class="row">
<div class="col-md-12">
<p>Missing authentication headers.</p>

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

<!-- 401 -->
<dt class="sw-response-401">
401 Unauthorized

</dt>
<dd class="sw-response-401">
<div class="row">
<div class="col-md-12">
<p>Invalid credentials</p>

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

<!-- 403 -->
<dt class="sw-response-403">
403 Forbidden

</dt>
<dd class="sw-response-403">
<div class="row">
<div class="col-md-12">
<p>Infrastructure is inactive, or the Architecture Dashboard API feature isn't licensed.</p>

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

<!-- 429 -->
<dt class="sw-response-429">
429 Too many requests

</dt>
<dd class="sw-response-429">
<div class="row">
<div class="col-md-12">
<p>The customer has exceeded their request quota.</p>

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

<!-- 500 -->
<dt class="sw-response-500">
500 Internal Server Error

</dt>
<dd class="sw-response-500">
<div class="row">
<div class="col-md-12">
<p>Other internal problems (customer should contact OutSystems support if the problem persists).</p>

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

<h2>Schema definitions</h2>

<div id="definition-ApplicationDetails" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationDetails"></a>ApplicationDetails:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Application details with its modules and findings.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="GUID">
<span class="json-property-name">GUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique application identifier.</p>

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
<p>Application name.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="LevelGUID">
<span class="json-property-name">LevelGUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique identifier of the application&#39;s technical debt level.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Findings">
<span class="json-property-name">Findings:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Technical debt - list of finding counts per pattern.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/PatternFinding">PatternFinding</a>
</span>
<span class="json-property-range" title="Value limits"></span>

<div class="json-inner-schema">

</div>
</section>                </div>
</dd>
<dt data-property-name="Modules">
<span class="json-property-name">Modules:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>List of modules and their technical debt.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ModuleDetails">ModuleDetails</a>
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
<div id="definition-ApplicationTechnicalDebt" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ApplicationTechnicalDebt"></a>ApplicationTechnicalDebt:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Applications, modules and their technical debt.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="InfrastructureInfo">
<span class="json-property-name">InfrastructureInfo:</span>

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/InfrastructureInfo">InfrastructureInfo</a>
</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Applications">
<span class="json-property-name">Applications:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Applications, modules and their technical debt.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/ApplicationDetails">ApplicationDetails</a>
</span>
<span class="json-property-range" title="Value limits"></span>

<div class="json-inner-schema">

</div>
</section>                </div>
</dd>
<dt data-property-name="Page">
<span class="json-property-name">Page:</span>

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Page">Page</a>
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
<div id="definition-CategoryDetails" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/CategoryDetails"></a>CategoryDetails:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Category details and its patterns.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="GUID">
<span class="json-property-name">GUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique category identifier.</p>

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
<p>Category name.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Patterns">
<span class="json-property-name">Patterns:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>List of patterns belonging to this category.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/PatternDetails">PatternDetails</a>
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
<div id="definition-CategoryTechnicalDebt" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/CategoryTechnicalDebt"></a>CategoryTechnicalDebt:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Technical debt categories and their patterns.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="InfrastructureInfo">
<span class="json-property-name">InfrastructureInfo:</span>

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/InfrastructureInfo">InfrastructureInfo</a>
</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Categories">
<span class="json-property-name">Categories:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>List of categories and their code patterns.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/CategoryDetails">CategoryDetails</a>
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
<section class="json-schema-description">
<p>Exception details.</p>
</section>
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

<div id="definition-InfrastructureInfo" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/InfrastructureInfo"></a>InfrastructureInfo:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Infrastructure information.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="ActivationCode">
<span class="json-property-name">ActivationCode:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Activation Code.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="LastAnalyzedOn">
<span class="json-property-name">LastAnalyzedOn:</span>

<span class="json-property-type">string</span>    <span class="json-property-format">(date-time)</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Date and time of the last analysis.</p>

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
<div id="definition-Level" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Level"></a>Level:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Technical debt level.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="GUID">
<span class="json-property-name">GUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique identifier of the technical debt level.</p>

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
<p>Name of technical debt level.</p>

<div class="json-inner-schema">

</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-ModuleDetails" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/ModuleDetails"></a>ModuleDetails:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Module details and its patterns.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="GUID">
<span class="json-property-name">GUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique identifier of the module.</p>

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
<p>Module name.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="LevelGUID">
<span class="json-property-name">LevelGUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique identifier of the module&#39;s technical debt level.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Findings">
<span class="json-property-name">Findings:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Technical debt - list of finding counts per pattern.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/PatternFinding">PatternFinding</a>
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
<div id="definition-Page" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/Page"></a>Page:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Pagination information.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="Limit">
<span class="json-property-name">Limit:</span>

<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Maximum number of records returned.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Offset">
<span class="json-property-name">Offset:</span>

<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Offset of the first record in this page.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="NextPageOffset">
<span class="json-property-name">NextPageOffset:</span>

<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Offset of the first record in the next page.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="TotalResults">
<span class="json-property-name">TotalResults:</span>

<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Total count of results in the result set.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="TotalPages">
<span class="json-property-name">TotalPages:</span>

<span class="json-property-type">integer</span>    <span class="json-property-format">(int32)</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Total number of pages in the result set.</p>

<div class="json-inner-schema">

</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-PatternDetails" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/PatternDetails"></a>PatternDetails:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Code pattern details.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="GUID">
<span class="json-property-name">GUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>Unique pattern identifier.</p>

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
<p>Pattern name.</p>

<div class="json-inner-schema">

</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-PatternFinding" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/PatternFinding"></a>PatternFinding:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Technical debt of the code pattern.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="CategoryGUID">
<span class="json-property-name">CategoryGUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Unique identifier of the pattern&#39;s category.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="PatternGUID">
<span class="json-property-name">PatternGUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Unique identifier of the pattern.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Count">
<span class="json-property-name">Count:</span>

<span class="json-property-type">integer</span>    <span class="json-property-format">(int64)</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Count of findings for the current pattern.</p>

<div class="json-inner-schema">
<section class="json-schema-example">
<pre><code class="language-json">1234567891234567</code></pre>

</section>

</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-TeamApplicationInfo" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TeamApplicationInfo"></a>TeamApplicationInfo:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Unique application identifier of a team.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="GUID">
<span class="json-property-name">GUID:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>Unique identifier of the application.</p>

<div class="json-inner-schema">

</div>
</dd>
</dl>
</section>
</div>
</div>        
<div id="definition-TeamDetails" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TeamDetails"></a>TeamDetails:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>Team details and its applications.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="ExternalId">
<span class="json-property-name">ExternalId:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>The team&#39;s external id (ID in LifeTime), which acts as a unique identifier.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Name">
<span class="json-property-name">Name:</span>

<span class="json-property-type">string</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>The name of the team.</p>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Applications">
<span class="json-property-name">Applications:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>List of applications which belong to this team.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/TeamApplicationInfo">TeamApplicationInfo</a>
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
<div id="definition-TeamTechnicalDebt" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TeamTechnicalDebt"></a>TeamTechnicalDebt:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>List of teams and their applications.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="InfrastructureInfo">
<span class="json-property-name">InfrastructureInfo:</span>

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/InfrastructureInfo">InfrastructureInfo</a>
</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Teams">
<span class="json-property-name">Teams:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>
<p>List of teams and their applications.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/TeamDetails">TeamDetails</a>
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
<div id="definition-TechnicalDebtLevels" class="panel panel-definition">
<div class="panel-heading">
<h3 class="panel-title"><a name="/definitions/TechnicalDebtLevels"></a>TechnicalDebtLevels:
<span class="json-property-type">
<span class="json-property-type">object</span>
<span class="json-property-range" title="Value limits"></span>

</span>
</h3>
</div>
<div class="panel-body">
<section class="json-schema-description">
<p>List of technical debt levels.</p>

</section>

<section class="json-schema-properties">
<dl>
<dt data-property-name="InfrastructureInfo">
<span class="json-property-name">InfrastructureInfo:</span>

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/InfrastructureInfo">InfrastructureInfo</a>
</span>
<span class="json-property-range" title="Value limits"></span>

</dt>
<dd>

<div class="json-inner-schema">

</div>
</dd>
<dt data-property-name="Levels">
<span class="json-property-name">Levels:</span>

<span class="json-property-type">object[]</span>
<span class="json-property-range" title="Value limits"></span>

<span class="json-property-required"></span>
</dt>
<dd>
<p>List of technical debt levels.</p>

<div class="json-inner-schema">

<section class="json-schema-array-items">

<span class="json-property-type">    <a class="json-schema-ref" href="#/definitions/Level">Level</a>
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
</div>
