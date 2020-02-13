# Audit Suggestion Warning

Message
:   `'Log Error' should be set to 'Yes' for 'AllExceptions" error handler at screen flow level`

Cause
:   You have an Error Handler, in a screen flow, to catch general exceptions and the Log Error property is set to No.

Recommendation
:   You should change the Log Error property to Yes because, since the Error Handler is catching all exceptions. It is advisable that detailed information about that exception is logged by OutSystems. This might allow you to discover the reason for the exception.
