# Unexpected Error Handler Warning

Message
:   `'Abort Transaction' should be set to 'Yes' for 'AllException' error handler at screen flow level`

Cause
:   You have an Error Handler in a Screen Flow to catch general exceptions and the Abort Transaction property is set to 'No'.

Recommendation
:   You should change the Abort Transaction property to 'Yes' because, since the Error Handler is catching all exceptions, the current database transactions should be aborted to avoid committing  inconsistent data.
