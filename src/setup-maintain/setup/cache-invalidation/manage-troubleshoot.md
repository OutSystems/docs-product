---
summary: Instructions for enabling the management plugin and for troubleshooting Cache Invalidation Service (RabbitMQ) issues.
tags: version-11
locale: en-us
guid: 4b06ed06-572c-48c9-835c-f38db745052c
app_type: traditional web apps, mobile apps, reactive web apps
---

# RabbitMQ management and troubleshooting

The default RabbitMQ batch scripts folder mentioned in the sections below is the following:

`C:\<OutSystems Install Folder>\thirdparty\RabbitMQ Server\rabbitmq_server-<version>\sbin`

Adjust it if necessary.

## Enable the RabbitMQ management plugin

The best way to monitor and manage RabbitMQ is by using the management plugin included in the installation. To enable it, do the following:

1. Open a command-line console (run as Administrator) and change to the RabbitMQ batch scripts folder;

1. Execute the following command:
`rabbitmq-plugins.bat enable rabbitmq_management`

The management dashboard will be available at `http://localhost:15672/`. You can login using the administrator credentials that have been set during service configuration.

### Check the service status

You can use the CLI tools provided by RabbitMQ to check the service status.

Do the following:

1. Open a command-line console (run as Administrator) and change to the RabbitMQ batch scripts folder;

2. Execute the following command:
`rabbitmqctl.bat status`


## Troubleshooting

### Service installation issues

If you find any issues while installing the Cache Invalidation Service, which uses RabbitMQ as its underlying technology, follow these troubleshooting suggestions in order:

Check if Erlang was correctly installed on your machine
:   A) Check the installed version of Erlang by following these steps:

    1. Run the Erlang shell by executing the following command:
    `C:\<OutSystems Installation Folder>\thirdparty\Erlang\bin\werl.exe`

    1. Check the version information at the top of the screen; it should match the following:
    `Erlang/OTP 20 [erts-9.3] [64-bit]`

    B) Check if the `ERLANG_HOME` environment variable is defined and pointing to the Erlang installation folder.

Check the Erlang cookies
:   A) Make sure that the `.erlang.cookie` files in `%USERPROFILE%` and in the Windows system profile folders (`C:\Windows\System32\config\systemprofile`, `C:\Windows\SysWOW64\config\systemprofile`, `C:\Windows\SysNative\config\systemprofile`) are synchronized, i.e. they have the exact same content.

    If they're not the same, copy the contents of one file to the other, replacing its contents.

Check the RabbitMQ service status
:   A) Check if the RabbitMQ service is installed and running by opening the Task Manager.

    If it's not, do the following:

    1. Open a command-line console (run as Administrator) and change your directory to the RabbitMQ batch scripts folder.

    1. Execute the following commands to remove the currently running service, install a new one, and start it:
    `rabbitmq-service.bat remove`
    `rabbitmq-service.bat install`
    `rabbitmq-service.bat start`

Check if RabbitMQ port is being blocked
:    A) If you are using multiple front-end servers, check that the port used by RabbitMQ (port 5672, by default) is not being blocked by the firewall.

    To change the port used by the RabbitMQ service:

    1. Set the `RABBITMQ_NODE_PORT` environment variable to the desired port number;
    1. Reinstall the RabbitMQ service, execute the same commands described in the previous issue ("Check the RabbitMQ service status").

Check the logs for any errors
:   A) Check if there are any errors in the RabbitMQ service log files. The log files are stored in `%ALLUSERSPROFILE%\RabbitMQ\log`.

### Service upgrade issues

If you find any issues while upgrading the Cache Invalidation Service, check
the issues listed below. See if one matches the problem you're currently
experiencing, and follow the troubleshooting suggestions in order:

#### Unable to delete files in the installation directory: ‘path/fileName’ - access denied

When upgrading the platform server, the system requirements regarding RabbitMQ
and Erlang may need to be updated, check [here](
https://www.outsystems.com/goto/system-requirements-11) to confirm whether
yours have changed, referring to the section “Cache Invalidation Service”.

The cache invalidation service upgrade cleans the installation directory after
removing old versions of RabbitMQ and Erlang. One or more files in the
installation directory may have become locked. Locked files will throw access
denied errors while trying to remove them.

However, Erlang may lock files for a short time; it's worth repeating the
operation to see if it works a second time.

![error](https://user-images.githubusercontent.com/102377102/185116450-af2ae9e8-c80c-43d8-a4ff-9efff4547d64.png)

If this doesn’t solve the issue, follow the next steps in order:

1. Navigate to the directory and find which files haven't been able to be removed (C:\Program Files\OutSystems\Platform Server\thirdparty\Erlang\erts-XX.X\bin);
![folder](https://user-images.githubusercontent.com/102377102/185119006-4a2e1244-5bbc-4262-b53f-d90ef30b0662.png)

1. Open a program to view real-time resource information about software and
   hardware on your computer, like Resource Monitor (for Windows) and search
   for the file(s) which have access denied and couldn't be removed;

1. Right-click on the locked file and select “End Process”;
![endProcess](https://user-images.githubusercontent.com/102377102/185119206-ccd755f7-fe99-48bd-8e33-3ed092c7b786.png)

1. Once you stop the processes locking the folder, you can remove the files;

1. Retry the "Upgrade cache invalidation service" operation.

### High availability issues

Check the issues listed below if you find any issues while creating or upgrading Cache Invalidation Service with high availability. See if one matches your current problem and follow the troubleshooting steps in order:

#### ERLANG_HOME not set correctly

When upgrading RabbitMQ and Erlang, when you try to start the node you may encounter this error.

   A) Make sure the system variable “ERLANG_HOME” is setted correctly. The path should lead you to a directory that contains the bin folder. If it does not, please fix the path.

    If it is, do the following:

    1. Restart your machine.

    1. Try to start the node again.
    

### Common issues

The RabbitMQ service fails to start
:   A) Make sure that the `%ALLUSERSPROFILE%` folder is accessible by the user running Configuration Tool.

    B) If the `%ALLUSERSPROFILE%` folder is located in a network share, make sure that the "Workstation" Windows service is running.

    C) Check the log file (located in `%ALLUSERSPROFILE%\RabbitMQ\log`) for any fatal errors.

The RabbitMQ service crashes on start
:   _Description:_ The 'crash.log' file in the `%ALLUSERSPROFILE%\RabbitMQ` folder contains 'schema_integrity_check_failed' exceptions.

    **Note:** The following suggestion for solving this issue will destroy all your durable exchanges and queues, and all your persisted messages. This is especially important when you are using RabbitMQ for other purposes than just OutSystems.

    A) Delete the content of the `%ALLUSERSPROFILE%\RabbitMQ\db` folder and restart the service. You can use the "Create/Upgrade Service" operation available in Configuration Tool (Cache tab) to perform the restart.

The RabbitMQ service is not installed and its installation/removal procedure throws an error
:   _Description:_ The RabbitMQ service does not appear in the Windows Services list. Running `rabbitmq-service.bat install` or `rabbitmq-service.bat remove` throws an error: "The handle is invalid".

    A) Delete the RabbitMQ variables from the registry, located at `HKEY_LOCAL_MACHINE\SOFTWARE\Ericsson\Erlang\ErlSrv\1.1\RabbitMQ`, and reinstall the service.

The RabbitMQ broker is not starting
:   A) Ensure that the Erlang cookies are synchronized (follow the instructions in "Check the Erlang cookies" above).

    B) Ensure that the `ERLANG_HOME` variable is defined and pointing to the Erlang folder.

RabbitMQ crashes soon after failing and there's an error in the log file saying `{error,{already_started,<...>}}`
:   A) Ensure that there is no TLS listener using the same port as a non-TLS listener. Listeners can be configured in `%ALLUSERSPROFILE%\RabbitMQ\rabbitmq.conf` or `%ALLUSERSPROFILE%\RabbitMQ\advanced.config`.

    B) Ensure that `RABBITMQ_NODE_PORT` environment variable, which defines the default port used by non-TLS listeners, is not set to the same port as an TLS listener.

Applications cannot reach the RabbitMQ service. The "Test Connection" operation in Configuration Tool (Cache tab) fails.
:   A) Check if the RabbitMQ service is running.

    B) Check that there is a firewall exception for port number 5672.

    C) Check if there is a RabbitMQ node running by following these steps:

    1. Open a command-line console (run as Administrator) and change to the RabbitMQ batch scripts folder.

    1. Run the following command:
    `rabbitmqctl.bat status`

    3. If the `rabbitmq@<machine_name>` node is not running, run the following command to start it:
    `rabbitmqctl.bat start_app`

    D) Check if the RabbitMQ user was successfully created by following these steps:

    1. Open a command-line console (run as Administrator) and change to the RabbitMQ batch scripts folder.

    1. Run the following command:
    `rabbitmqctl.bat list_users`

    1. If the user it's not listed in the command output, run the following command to create it:
    `rabbitmqctl.bat add_user <admin_username> <admin_password>`

    E) Check if the RabbitMQ user has permissions for the virtual host (vhost) defined on installation script (`/outsystems` by default) by following these steps:

    1. Run the following command:
    `rabbitmqctl.bat list_permissions -p /<virtual_host>`

    2. If the user doesn't have permissions, run the following command:
    `rabbitmqctl.bat set_permissions -p /<virtual_host> <admin_username> ".*" ".*" ".*"`

    F) Make sure that the password of the user of the cache invalidation service doesn't contain any special characters (for example, `?`, `&`, `^`, `"`, `'`, `*`, `(`, `)`).

    G) If the issue persists, [contact Support](<https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support>).

Event Viewer contains messages like "Error executing PubSub jobs, X consecutive Jobs failed."
:   _Description:_ A job failed to complete due to a misconfiguration or inconsistent state. Jobs are: creating queues, creating exchanges, register a queue into an exchange.

    A) If it happens consistently and the number of consecutive jobs failed is high, try to redeploy the module.

    B) If the issue persists, [contact Support](<https://success.outsystems.com/Support/Enterprise_Customers/OutSystems_Support/01_Contact_OutSystems_technical_support>).

Event Viewer contains messages like "Error executing PubSub jobs, X consecutive connections failed."
:   _Description_: The module cannot reach the RabbitMQ service.

    A) Follow the instructions provided in "Applications cannot reach the RabbitMQ service" to troubleshoot this issue.
