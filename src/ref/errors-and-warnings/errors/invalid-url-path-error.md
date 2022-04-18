---
locale: en-us
guid: c4e418eb-f299-41a2-a476-80ff44258482
app_type: traditional web apps, mobile apps, reactive web apps
---

# Invalid URL Path Error

The `Invalid URL Path` error is issued in the following situations:

Message
:   `'URL Path' property must start with '/'.`

Cause
:   The specified **URL Path** value doesn't start with `/` in the definition of the REST API.

Recommendation
:   Review the syntax of the URL path.

---

Message
:   `Mismatching braces in property 'URL Path' of the (<method name>) REST API method.`

Cause
:   The opening and closing curly braces (`{` and `}`) don't match in the URL of the REST API.

Recommendation
:   Review the syntax of the URL path.

---

Message
:   `Empty braces found in property 'URL Path' of the (<method name>) REST API method. Put a parameter name or delete braces.`

Cause
:   In the URL of the REST API, there are curly braces ('{' and '}') without the parameter name inside.

Recommendation
:   Review the syntax of the URL path.

---

Message
:   `Parameter (<parameter name>) in property 'URL Path' must be an input parameter of the (<method name>) REST API method.`

Cause
:   You entered an input parameter placeholder in the URL path of the REST API method, but that input parameter doesn't exist in the REST method.

Recommendation
:   Either remove the input parameter placeholder from the URL of the REST API, or add the expected input parameter to the REST API method.

---

Message
:   `(<parameter name>) input parameter is used in the URL, but is being placed in the Body of the request.`

Cause
:   An input parameter has the **Sent In** property set to `Body`. It should be `URL` because the method of the REST API has the **HTTP Method** set to `GET`.

Recommendation
:   Change the **Sent In** property to `URL`.

---

Message
:   `The URL Path must be either http://host/path or https://host/path`

Cause
:   You have an invalid URL set in the **URL Path** property of a method from a REST API.

Recommendation
:   Review the syntax of the URL path.

---

Message
:   `Invalid URL characters in property 'URL Path' of the (<method name>) REST API method.`

Cause
:   You used reserved characters like `;`, `?`, or `=` in the **URL Path** property.

Recommendation
:   Review the URL set in the **URL Path** property, removing any reserved characters.

    Notes:

    * Even though you can use the `/` character in **URL Path** values, this character is usually reserved for specifying hierarchical structures in REST methods.
    * OutSystems reserves the `{` and `}` characters for including the value of REST method input parameters in the URL. Check [Customize REST URLs](../../../extensibility-and-integration/rest/expose-rest-apis/customize-rest-urls.md) for more information.

<div class="info" markdown="1">

**Tip:** Double-click on the error line to take you directly to the REST API method's property list where the problem was detected.

</div>
