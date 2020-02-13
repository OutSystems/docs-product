# Open Redirect Warning

Message
:   `Enclose the input parameters with a ReplaceURLDomain() function from HttpRequestHandler to avoid open redirect vulnerabilities.`

Cause
:   The input parameter mentioned in the warning has a value that comes from the end-user input and that is susceptible to contain a malicious URL.

Recommendation
:   Do one of the following:

    * Use the **ReplaceURLDomain()** function from the HTTPRequestHandler extension module to enclose the value of the parameter.
    * Replace the 'External Site' element with a well-known page in your application.
    * Replace the 'External Site' element with another 'External Site' element that does not receive a URL as an input and that redirects to a static URL instead.
  