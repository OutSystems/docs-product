---
locale: en-us
guid: de5bd7ca-83d5-45be-b0b3-ee9f729a9931
---

# Licensing Error

The `Licensing` error is issued in the following situation:

* `No license was found for this server`

    The Platform Server you are using either does not have an OutSystems license or it is not possible to interpret the license file that was found.

    Contact your Service Center administrator to request a new license from OutSystems.

* `Cannot perform the operation. No license was found for this server`

    You are trying to perform an operation (like publishing a module) and the Platform Server you are using either does not have an OutSystems license or it is not possible to interpret the license file that was found.

    Contact your Service Center administrator to request a new license from OutSystems.

* `The license found is not valid for this server because it was issued to a server with serial number '<number>'`

    The Platform Server you are using does not have a valid license because the license was issued for another Platform Server.

    Contact your Service Center administrator to upload the correct license file or, if necessary, to request a new license from OutSystems.

* `Cannot perform the operation. The license found is not valid for this server`

    You are trying to perform an operation (like publishing a module) and the Platform Server you are using does not have a valid license.

    Contact your Service Center administrator to upload the correct license file or, if necessary, to request a new license from OutSystems.

* `This server license has expired. Your Service Center administrator must request a new license`

    You won't be able to use any of the licensed features for this server with an expired license.

    Contact your Service Center administrator to request a new license from OutSystems.

* `This server is consuming more resources than allowed by its license. Either the license contract must be changed or the features usage decreased`

    The Platform server you're using has exceeded the licensed limit of one or more features. You won't be able to use any of the licensed features until the situation is solved.

    Check with your Service Center administrator for information about which feature(s) exceeded their licensed usage limit. This may help you to do your share in cleaning up old or obsolete information like users or modules. Otherwise, ask him/her to change the license contract.

* `Cannot perform the operation. Either this server license has expired or it is consuming more resources than allowed`

    You are trying to perform an operation (like publishing a module) and the Platform Server you are using has either an expired license or it has exceeded the licensed limit of one or more features. You won't be able to use any of the licensed features for this server, for example, testing queries, running, debugging or publishing your module, until the situation is solved.

    Contact your Platform Server administrator to do one of the following:
    
    * Request a new license from OutSystems.
    * Check for information about which feature(s) exceeded their licensed usage limit. This may help you to do your share in cleaning up old or obsolete information like users or modules. Otherwise, ask him/her to change the license contract.

* `You cannot publish more modules because you reached the limit of <number> Software Units that this server license allows`

    You are trying to publish a module and the Platform Server you're using has exceeded its licensed limit of Software Units. You won't be able to publish more modules until the situation is solved.

    Clean up old or obsolete modules or contact your Service Center administrator to change the license contract.

* `Cannot perform the operation. The <Test Query/Run/Debugger> feature is not licensed in this server. To change the license contract ask your Service Center administrator`

    You are trying to test a query or to run/debug a module and this feature is not licensed in the platform server you're using.

    Contact your Service Center administrator to change the license contract.
