<pre class="script-css">
/* HIDE H2, H3, H4 AND H5 FROM TOC */
#mt-toc-container li li {
    display:none;
}
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
</pre>

# Additions to LifeTime API

<table class="table table-bordered table-condensed swagger--summary"<thead>
<tr>
<th>Endpoint</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#operation--environments--EnvironmentKey--register_environment--post">POST /environments/{EnvironmentKey}/register_env ironment/</a></td>
<td>Register a new environment in LifeTime. <strong>This endpoint is available as of LifeTime Management Console 11.?.</strong></td>
</tr>
<tr>
<td><a href="#operation--environments--EnvironmentKey--unregister_environment--delete">DELETE /environments/{EnvironmentKey}/unregister_environment/</a></td>
<td>Unregister an environment in LifeTime. <strong>This endpoint is available as of LifeTime Management Console 11.?</strong></td>
</tr>
</table>

<div id="operation--environments--EnvironmentKey--register_environment--post" class="swagger--panel-operation-put panel">
<div class="panel-heading">
<div class="operation-summary"></div>
<h3 class="panel-title"><span class="operation-name">POST</span> <strong>/environments/{EnvironmentKey}/register-environment/</strong></h3>
Go to 
<a href="#tag--environments">/environments</a>
</div>
<div class="panel-body">
<section class="sw-operation-description">
<p>Register a new environment. <strong>This endpoint is available as of LifeTime Management Console 11.10.3.</strong></p>
</section>
<section class="sw-request-body">
<p><span class="label label-default">application/json</span> 
</p>
<div class="rowr">
<div class="col-md-6">
<p></p><p>Register a new environment.</p>
<p></p>
</div>
<div class="col-md-6 sw-request-model">
<div class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/CSPDirectives">CSPDirectives</a>
</div>
</div></div>
</div>
</section>      <br>
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
<td><p>The key of the environment to apply the Content Security Policy.</p>
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
<div class="rowr">
<div class="col-md-12">
<p>Content Security Policy successfully set.</p>
</div>
</div>
<div class="rowr">
<div class="col-md-6 sw-response-model">
<div class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Environment_CSP_Response">Environment_CSP_Response</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-400">
400 Bad Request
</dt>
<dd class="sw-response-400">
<div class="rowr">
<div class="col-md-12">
<p>Failed to set Content Security Policy.</p>
</div>
</div>
<div class="rowr">
<div class="col-md-6 sw-response-model">
<div class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-403">
403 Forbidden
</dt>
<dd class="sw-response-403">
<div class="rowr">
<div class="col-md-12">
<p>User doesn't have permissions.</p>
</div>
</div>
<div class="rowr">
<div class="col-md-6 sw-response-model">
<div class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-404">
404 Not Found
</dt>
<dd class="sw-response-404">
<div class="rowr">
<div class="col-md-12">
<p>Environment not found.</p>
</div>
</div>
<div class="rowr">
<div class="col-md-6 sw-response-model">
<div class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
<dt class="sw-response-500">
500 Internal Server Error
</dt>
<dd class="sw-response-500">
<div class="rowr">
<div class="col-md-12">
<p>Internal error raised.</p>
</div>
</div>
<div class="rowr">
<div class="col-md-6 sw-response-model">
<div class="panel panel-definition">
<div class="panel-body">
<a class="json-schema-ref" href="#/definitions/Exception">Exception</a>
</div>
</div></div>
</div>                </dd>
</dl>
</section>
</div>
</div>
