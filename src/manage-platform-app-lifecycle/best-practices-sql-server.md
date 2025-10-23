---
summary: Explore best practices for optimizing SQL Server performance with OutSystems 11 (O11), including hardware recommendations and maintenance strategies.
guid: c337cff4-b4f5-454f-85d5-57fd31f67d2c
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: sql server optimization, performance tuning, database management, hardware recommendations, system maintenance
audience:
  - platform administrators
  - full stack developers
  - infrastructure managers
  - tech leads
  - backend developers
outsystems-tools:
  - platform server
coverage-type:
  - evaluate
---

# Best practices for SQL Server

This article presents the current best practices recommended when operating OutSystems Platform Server with a SQL Server database.

## Hardware recommendations

In this section you have a list of subjects that you should consider before buying the hardware or when re-evaluating the hardware platform.

### CPU

SQL Server can take advantage of multiple CPU's, with the advent of dual core technology this is a boon to every system as it allows you to almost double the CPU capacity of your server easily.

When choosing a CPU, choose one with a large L2 cache. The bigger the cache the less the CPU has to access main memory thus improving performance. This is even more important when you use more than one socket in your server. The more sockets you have the more L2 cache you should seek to have.

Keep in mind, however, that a smaller server (2 sockets, each with a dual core CPU's installed) and only a hand full of databases may have better performance than a large 8 way server. It will depend on the load being generated against the server and how much your load will be close to the kinds of database loads the other server has been designed to handle.

### Memory

By default, SQL Server will attempt to use as much memory as possible. Configure SQL Server memory usage leave 256MB for the operating system.

### Hard disk

I/O bottlenecks are the most common bottlenecks on SQL Server. As the amount of data stored increases so does the load placed on the I/O subsystem. Strategies to address this are detailed below.

#### RAID overview

There are several levels of RAID to choose from when configuring your server's I/O subsystems.

Regardless of which RAID level you choose, the recommended stripe size for SQL Server is 64Kb.

Below we'll discuss briefly each of the most common levels as they pertain to SQL Server performance.

| **Raid Level** | **Description** |
|----------------|------|
| 0 | Known as a Stripe Set, the disks taking part in the set will each own a separate chunk of information that's distributed over the disks. While not fault tolerant it provides the best read and write performance. RAID 0 disk sets start at 2 drives, however can be extended to improve I/O performance. Adding drives however will being to provide less and less performance improvements as you add disks. Recovery isn't possible once one of the drives fails. |
| 1  | Also known as a Mirrored Set, the disks taking part in the set mirror each other. This provides the best fault tolerance at the expense of disk space and some performance as all the drives need to read and write the information. RAID 1 disk sets begin with 2 drives.As long as one non-failed drive is left on the array the array can be recovered.|
| 5  | Using block-level striping with parity data distributed across all members, RAID 5 has become popular due to the low cost of redundancy. RAID 5 disk sets begin with 3 drives, letting you add drives as you go. Arrays that lose one drive continue to operate and once the failed drive is replaced, the array will be rebuilt. Rebuilding the array will however result in performance degradation as the disks use I/O capacity to rebuild the new disk. Loss of a second drive up until the rebuild is complete will result in data loss. |
| 10 (1+0)| This is a nested RAID level where two different RAID levels are used together to boost performance and/or fault tolerance. In this case a RAID 0 stripe will be created over two or more sets of RAID 1 drive arrays. Disk sets begin with 4 drives, distributed over two drive arrays. You may increase the number of drives present in the disk arrays to improve fault tolerance, or increase the number of arrays to improve performance. Data loss won't occur until all drives in one of the mirror set fail. This means the array can continue to operate correctly with multiple failures as long as no single mirror is completely wiped out. |

#### Storage subsystem design

Careful thought and consideration should be put into designing your storage subsystem. Once you've settled on a design choice, changing it will be costly so careful planning should be exercised.

Please consider the following:

* Avoid running SQL Server on a server with other major applications. SQL will be forced to share I/O capacity with those applications.

* Placing the OutSystems Platform Database on a common SQL Server platform.

When designing your storage subsystem it's easier to divide it in smaller parts that we can then assign particular storage needs.

We can divide storage needs in three parts, by looking at the I/O requirements of three different sets of files:

* System Files

* Data Files

* Log Files  

| **File Type** | **Description** |
|--------------|-----------------|
| System Files | System files are the files for Windows, including your pagefile, as well as the SQL Server binaries. This subsystem is mostly oriented towards read operations. However your main concern is ensuring integrity and fault tolerance, than I/O performance. RAID levels 1, 5, and 10 are appropriate, although RAID 1 is the most common. |
| Data Files (*.mdf,*.ndf) | Data files (*.mdf,*.ndf) are the files where SQL stores all of your database data and schema information.The load placed on these files will depend on whether your database is mostly transaction oriented, create a higher write load, or if it has a more analytical role which usually mean a higher read load.RAID 10 is the recommended level as it provides the best fault tolerance as well as the best speed |
| Log Files (*.ldf) | Transaction Log files (*.ldf) are where the database journaling takes place and is critical to ensuring proper database recovery. Except for database recovery actions, the load is mostly write oriented. RAID 1 or RAID 10 are recommended.|

To get the maximum performance, with these set of files, you should use the NTFS block size of 64k (recommended). For 64-bit systems this can be set higher, but note that when going beyond 64k you should try it first on a test system.

For the operating system you should use block sizes of about 4k to 32k.

When using a SAN consult with your vendor on its recommended best practices for configuring the optimal stripe size for the type of RAID you are using.  

## SQL Server recommendations

### Database files

#### File sizing

When creating your database you'll need to say how much space your database files will occupy on this. You should make the files large enough to contain the initial amount of data you expect, plus allow for some file growth.

You should also configure your database files to grow automatically by a fixed disk space amount. This will allow you DB to grow overtime, however care should be taken to ensure your database does not need to grow more than once a week. If that happens then increase the size of the grow amount.

Unless you know you'll be loading more data, make your datafile size 2GB, and set the transaction log file size to 512MB. Both files should be set to autogrow by 512MB.

If you'll be having more than 8GB datafiles, consider splitting the data between 8GB datafiles so that you take advantage of SQL Servers simultaneous access to different datafiles.

#### File placement

Since each set of files has different I/O needs it's best to place them on separate volumes that have been designed to provide the necessary performance.

Even if your server is already built, make sure you understand the needs of each file set and use that to optimize your current installation. In particular separating your logfiles and datafiles over different physical I/O subsystems will usually result in big performance gains.

Disk volumes that share physical disks will however result in degraded performance.

When using a SAN consult with your vendor on its recommended best practices for configuring the SAN for SQL Server usage.

#### Defragmentation

Database files should be placed on volumes with large chunks of free space to minimize file fragmentation.

Normal database use will result in file growth which may lead to further file fragmentation. You should schedule a defragmentation task to be run on a regular basis, so fragmentation is kept to minimum. See also the notes below on Database Shrinking.

### SQL Server maintenance plans

Correctly configured maintenance plans will help your database maintain its peak performance level while allowing you to have regular backups of your data.

#### Integrity checks

Integrity checks should be done at least on a weekly basis before a full backup is executed. This will prevent backups from occurring after database corruption has occurred and will prompt for DBA intervention.

However the option of fixing small errors should be not used as this will require the database to go into single user mode which isn't recommended for production environments.

#### Index reorganization

As indexes grow they will become fragmented. Configuring Index Reorganization will make SQL Server reorganize those indexes. This process makes low usage of system resources and can be used with the index online allowing SELECTs to be executed. However if your indexes are highly fragmented you'll achieve better results by rebuilding the index.

Index reorganization should be evaluated by the DBA considering the level of fragmentation present. This will also be more necessary if you have a higher number of changes to your data per day. Usually this is done weekly or monthly.

#### Index rebuild

Rebuilding the index makes SQL Server drop the existing index, reclaim resources used by the index and then recreate the index in contiguous pages. This is a more resource intensive operation that achieves a similar result to Index Reorganization.

Index rebuild should be evaluated by the DBA considering the level of fragmentation present. This will also be more necessary if you have a higher number of changes to your data per day. Usually this is done weekly or monthly.

#### Statistics update

SQL Server's query governor uses table and index statistics to guide its decisions on which indexes are better suited to each query. If your statistics become out of date, better indexes that would yield faster query times may not be used.

Depending on how often your data changes you should rebuild the statistics with your maintenance plan. Typical values are daily for systems where there are significant changes to table contents each day to weekly if your data is mostly constant.

#### Backups

SQL Server places some restrictions on the kind of backups available to you depending on which database you are using. Namely, the MASTER database does not support Differential Backups.

It's a good idea to have separate maintenance plans for your system and user databases. This enables you to fine tune each maintenance plan to your specific database needs. It also prevents a maintenance plan from failing for one database and then not running for all the others. Master database is critical for recovery procedures and it's recommended that you keep a separate maintenance plan for it.

| **Database**                        | **Recommended Initial Backup Strategy**           | **Optional Backup Strategy**                                            |
|-------------------------------------|---------------------------------------------------|-------------------------------------------------------------------------|
| Master                              | Weekly full backup, daily transaction log backups | Weekly full backup, daily transaction log backups                       |
| Model, MSDB, other system databases | Weekly full backup, daily transaction log backups | Weekly full backup, daily transaction log backups                       |
| OutSystems Platform database        | Weekly full backup, daily transaction log backups | Weekly full backups, daily differential, hourly transaction log backups |

If you have a high number of transactions per day, you may wish to introduce a differential backup for the OutSystems platform database in the middle of the backup week. This may provide you with a lower recovery time since it could be faster to simply restore the last full backup, restore the last partial and restore only the transaction log backups that occurred after the last partial.

You could also consider making more frequent transaction log backups. You could have a smaller data loss window, by making transaction log backups every three hours for instance.

Having more frequent full backups would also decrease the amount of space needed for you transaction logs.

#### Database shrink

Maintenance plans shouldn't perform database shrink operations. Shrinking the database will cause it to release diskspace, this will result in SQL Server having to grow the files later. Over time this will result in large scale file fragmentation.

When needed the DBA should evaluate the free space of the database and perform a manual shrink operation. After such operations, rebuilding your indexes and updating statistics is recommended.
