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
