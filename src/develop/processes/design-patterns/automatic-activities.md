# Designing Automatic Activities

Use this pattern to design action flows, adding automated business logic to your processes with the [Automatic Activity](<../../../ref/lang/auto/Class.Automatic Activity.final.md>) as, for example:

* Integrate with external systems through extensions.

* Change the behavior of applications using, for example, Entity actions.

* Manage the activities in the process flow or even launch other processes using [Process Extended Actions](../actions-extended/intro.md).


## Handling Transactions

A transaction begins when the **Automatic Activity** starts and is committed when the activity ends.

If the activity has elements of integration with external systems, the transaction handling may require extra care to ensure coherency.


## Assuring Safe Re-Execution

When the execution of an **Automatic Activity** fails due to an error, OutSystems re-executes it after some time (which increases from re-execution to re-execution to avoid overloading the server). This re-execution of the **Automatic Activity** is usually safe because all changes are rolled back in case of error.

However, if for example, transactions are explicitly committed in the activity flow (using **CommitTransation** system action) or there's an integration with external systems, the activity may require safeguards to avoid inconsistency in the re-execution.

### Example

As an example, think of an **Automatic Activity** that, at some point, creates entity records in an external system: a safeguard has to be added for not creating duplicated records in case of re-execution.
