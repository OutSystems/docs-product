# Invalid URL Path Error

The `Invalid URL Path` error is issued in the following situation:

* `URL path needs to start with '/'`

    The URL path doesn't start with '/' in the definition of the REST API.

    Review the syntax of the URL path.

* `Unexpected or mismatching braces in URL Path`

    The opening and closing curly braces ('{' and '}') do not match in the URL of the REST API.

    Review the syntax of the URL path.

* `Empty braces in the URL path. Either add a parameter inside the braces, or delete them`

    In the URL of the REST API, there are curly braces ('{' and '}') without the parameter name inside.

    Review the syntax of the URL path.

* `(<method name>) method needs to have an (<parameter name>) input parameter. Either add an (<parameter name>) input parameter to the method, or remove the parameter from the URL path`

    You deleted an input parameter from the REST Method, but it is still in the URL of the REST API.

* `(<parameter name>) input parameter is used in the URL, but is being placed in the Body of the request`

    An input parameter has the 'Sent In' property set to Body, but it should be URL because the method of the REST API has the 'HTTP Method' set to GET.

* `The URL Path must be either http://host/path or https://host/path`

    You have an invalid URL set in the 'URL Path' property of a method from a REST API.

    Review the syntax of the URL path.
    
* `Invalid URL characters in property 'URL Path' of the (<method name>) REST API method.`

    Within the 'URL Path', "/", ";", "?" are reserved.
    
    The "/" character may be used within HTTP to designate a hierarchical structure.

    The "{" and "}" are used in the ServiceStudio 'URL Path' to designate an input variable to the method.
    
    The hyphen (-} is currently a restricted character in ServiceStudio for the "Name" properties and cannot be used in the 'URL Path'.

Double-click on the error line to take you directly to the REST API method's property list where the problem was detected.
