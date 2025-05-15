---
summary: Explore infrastructure performance best practices for OutSystems 11 (O11) including database maintenance, server tuning, and antivirus configuration.
guid: 791cbc71-42c8-4f9a-9dd2-0af2830baa08
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database maintenance, server optimization, performance tuning, antivirus configuration, sql query optimization
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - infrastructure managers
  - tech leads
outsystems-tools:
  - platform server
coverage-type:
  - evaluate
---

# Performance best practices for your OutSystems infrastructure

<div class="info" markdown="1">

This page applies only to self-managed installations.

</div>

Having applications designed to perform fast, running slower than a crawl due to bad configuration or inadequate/undersized hardware, is absolutely frustrating for any software developer.

Make sure to apply the best practices listed below during the OutSystems Platform installation and always involve your DBA in the process. 

## Setup database maintenance plans

### Description

Database queries over indexed attributes are still slow and there's evidence that the indexes are not being used by the database engine because they are too fragmented and full table scans are being performed instead. The indexes must be defragmented.

### Solution

Apply regular optimizations to reorganize or rebuild existing indexes; also update the database statistics. This will defragment the indexes and provides the database engine the information it needs to use indexes instead of doing full table scans. Depending on the level of fragmentation over time, you may have these plans scheduled to run one or more times a week.

### Importance

In an OLTP (Online Transaction Processing), SQL Queries which are not using the created indexes, table inserts, updates and deletes will tend to fragment the table's indexes and the database statistics will indicate that full table scans are the best choice to execute the query. Reorganizing the indexes and updating the statistics will keep the indexes defragmented will thus increase the probability of using them instead of doing full table scans thereby improving the overall query performance.

### Remarks

Index reorganization or rebuild takes time and resources so make sure to schedule it to run during lower load periods. Don't forget to involve the resident DBA.

## Configure web server memory settings

### Description

Apply the recommended tuning setting to decrease the number of worker process recycles, unless memory limits have been reach.

### Solution

The Frontend Server has large kernel CPU usage and slow overall performance.

### Importance

Frequent recycling of worker process(es) imply that applications are being unloaded from memory, forcing a runtime recompilation of the `ASP.NET` application, and a reload of its assemblies and cache. This causes a slow performance scenario.

### Remarks

Apply the recommended tuning setting to decrease the number of worker process recycles, unless memory limits have been reached.

## Backup database transaction logs often

### Description

Setup regular transaction log backups for databases with high volume of data changes.

### Solution

Setup a maintenance plan for regular backups of the transaction log file to avoid excessive file growth.

### Importance

Lack of transaction log backups can lead to lack of free disk space or even a very high level of file fragmentation. Regular backups free up space for new transaction information. Thus the log file size will usually remain the same, without significant growth.

### Remarks

Don't forget to involve the resident DBA. Please note that this should target all environments including development and QA.

## Tune database file growth

### Description

Place database data files and log files in separate physical storage and correctly configure file growths.

### Solution 

Apply recommended tuning settings for the database; for example: (a) set absolute and large file growth of the data and log files (like 512 MB); (b) isolate data files and log files in different disks (not just partition on the same disk, but a physically different disk or different storage partitions), etc.

### Importance

The most typical bottleneck of a highly loaded database is Input / Output (I/O). Since the memory can't grow to infinity, I/O is a constant in databases. By having the database files optimized to have less fragmentation and with optimal I/O accesses, the I/O bottleneck problem is minimized.

### Remarks

Like all other database best practices, please consult your resident DBA when implementing this.

## Apply Virtual Memory and System Settings

### Description

Tune virtual memory and system performance settings and disable/configure third party applications like indexers.

### Solution

Tune system settings like: same initial and max size for Virtual Memory; best performance for services; and System Cache memory priority. We should also disable: heavy system and third party analysis features/tools, like Data Execution Prevention (DEP) for all programs and indexers like Windows Desktop, Google Search and Microsoft Indexer.

### Importance

Components like DEP and indexers cause an additional load whenever files are read from the disk or written to the disk. This causes a severe overload in an environment where you have consistently automated processes to create and write files.

### Remarks

The DEP issue is particularly important when not natively supported by hardware or when hardware was under-estimated. Regarding Virtual Memory and System Performance, for preventing page file growth, it is important to make sure it's usage is reduced to a minimum. Please note that this is very important for the development servers too (if those limits are not set, the development servers may have several SystemOutOfMemory errors).

## Use dedicated Server for Timers

### Description

For heavy background processing applications that rely on timers, try to isolate those timers in eSpaces. Configure dedicated servers to run those timers.

### Solution

Avoid having large timer processing on the same server where the users are accessing the web applications. Isolate timers in eSpaces and use multiple zones to have timers running in dedicated servers. Or only activate the scheduler service in servers dedicated for timers.

### Importance

Isolating the timers to run in dedicated servers will avoid additional load on the FrontEnd Servers that serves up the application. This also improves screen load performance.

### Remarks

Please also consider configuring the "Max. Concurrent Timers", having a proper scheduled time, or maybe creating an eSpace and application pool for this if the previous solution is not applicable or did not provide optimum results.

## Prefer 64-bit Architectures

### Description

If available and for high load environments, use 64-bit architecture servers and operating systems, instead of 32-bit architectures.

### Solution

64-bit architectures allow managing the server's memory resources more efficiently, overcoming the short limits of memory usage of the 32-bit architecture environments.

### Importance 

Memory management in 32-bit architecture environments limits each worker process to a maximum of 2 GB of user Virtual Address Space (VAS) and another 2 GB for the kernel Virtual Address Space. This means that even if the server has more than 2GB of physical RAM, OutOfMemory exceptions are bound to happen due to VAS memory fragmentation which rapidly reaches the 2GB limit even when there's enough free memory on the system. The 64-bit architecture considerably increases the VAS memory limit (to 16 TB) allowing the worker process will take full advantage of every GB of memory available.

### Remarks

When using the web server tuning settings in 64-bit, the limits will only exist to avoid the worker process to reach the maximum physical memory.

## Exclude some folders from antivirus scanning

### Description

In OutSystems on-premises installations, some Windows Server operations are either slow to execute, with CPU usage reaching peaks, or have a high ["Content Download"](https://developers.google.com/web/tools/chrome-devtools/network/reference#timing-explanation) time when loading pages. You should minimize the system performance impact of your antivirus software.

### Solution

If Windows Defender is active, or any other antivirus protection, disable the real-time scanning of the following paths:

* OutSystems Platform Server installation folder (the default is `C:\Program Files\OutSystems\Platform Server\`)

* Temporary ASP.NET files location in `%WINDIR%\Microsoft.Net\Framework64\v4.0.30319\Temporary ASP.NET Files` (the default on a 64-bit system)

* .NET Framework configuration files in `%WINDIR%\Microsoft.Net\Framework64\v4.0.30319\Config` (on a 64-bit system)

* Temporary folder of the user account used to run the OutSystems Deployment Controller Service. This can either be the Windows Authentication account configured for Administrator access to the Platform database or a specific account depending on the Platform Server version installed, which can be determined in the [Default Platform Server and database configurations](https://success.outsystems.com/documentation/11/setup_and_maintain_your_outsystems_infrastructure/setting_up_outsystems/default_platform_server_and_database_configurations/#services) (typically `C:\Users\OutSystems Deployment Controller Service\AppData\Local\Temp`)

* Optionally, the system temporary folder (typically `C:\Windows\Temp`).

### Importance

The real-time scanning feature of antivirus software monitors file system for changes and access. The server can generate and access numerous files during a process, triggering antivirus scanning which in return consumes the system resources and severely reduces the server performance.

### Remarks 

You can occasionally run the antivirus manually to scan the excluded folders. For more details about .NET Framework and antivirus software, you can read the article [Folders to exclude from antivirus scanning in ASP.NET apps](https://support.microsoft.com/en-us/help/3126034/folders-to-exclude-from-antivirus-scanning-in-asp-net-apps) at the Microsoft Support website.

