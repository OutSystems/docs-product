# Concurrent Publishing Error

The `Concurrent Publishing` error is issued in the following situation:

* `Your module is currently being locked by another operation. Please try again later. User <user> is publishing module <module> (in Personal Area) since <date/time>`
  
    It can be one the following situations:

    * You are trying to Run the module in your Personal Area while a 1-Click Publish is being processed in the server or another developer with your credentials is also updating your Personal Area.

    * You are trying to execute the 1-Click Publish operation while a Run is being processed in the server or another developer is also publishing the module.

    Wait a few moments and try the operation again.
    
If the issue still persists after a while, try [restarting the OutSystems Services](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Restart_Services_on_OutSystems_PaaS) in LifeTime. This resets the service that got stuck during a publishing step.
