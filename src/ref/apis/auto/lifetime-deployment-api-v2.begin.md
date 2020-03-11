---
summary: Allows you to manage applications, modules, environments and deployments of your OutSystems infrastructure. Version 2 of the API adds support for deployment zones, users, teams and roles.
tags: support-application_development; support-Application_Lifecycle; support-devOps; support-Integrations_Extensions
---

<pre class="script-css">
/* HIDE H3, H4 AND H5 FROM TOC */
#mt-toc-container li li li {
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


The LifeTime API allows you to manage applications, modules, environments and deployments of your OutSystems infrastructure. Version 2 of the API adds support for deployment zones, users, teams and roles.

Follow the guidelines presented in [REST API Authentication](<../lifetime-deployment/rest-api-authentication.md>) to authenticate your API requests.

<div class="info" markdown="1">

Check [LifeTime API Examples](<../lifetime-deployment/api-use-cases.md>) to learn how to perform common tasks using the LifeTime API.

</div>
