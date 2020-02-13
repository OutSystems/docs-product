# JavaScript Injection Warning

Message
:   `Ensure the expression is protected by using EncodeJavaScript(), or VerifyJavascriptLiteral() from the Sanitization extension, to avoid security flaws.`

Cause
:   The expression mentioned in the warning has a value that comes from the end-user input and that is susceptible to contain malicious content.

Recommendation
:   Do one of the following:

    * Use the **EncodeJavascript()** built-in function to replace all JavaScript reserved characters by their escaped counterpart;
    * Use the **VerifyJavascriptLiteral()** function from the Sanitization extension module to ensure that the value entered by the end-user only contains valid JavaScript or JSON literals.
