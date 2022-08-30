---
summary: Learn how to use Timers to execute asynchronous logic. 
locale: en-us
guid: 7b104f5a-3077-4eab-9dd0-90c28ade4b67
app_type: traditional web apps, mobile apps, reactive web apps
---

# Use Timers

You can use **Timers** to execute asynchronous logic in your OutSystems application. This is useful to execute batch tasks like sending emails at a predetermined time, or to execute logic to configure an application after its deployment.

## How Timers Are Handled

Timers are handled by the OutSystems Scheduler Service. This service checks for Timers that are ready to run and executes their actions. A Timer is ready to run when the current time is greater or equal to the Timer runtime property `NextRun`.

Since Timers usually invoke actions that take a while to run and are processor intensive, the OutSystems Scheduler Service only runs a fixed number of Timers at the same time. By default only three Timers can run at the same time per front-end server.

<div class="info" markdown="1">

For self-managed installations, the default number of Timers can be customized by using the OutSystems Configuration Tool.

</div>

When more than three Timers are scheduled to run at the same time, the Timers with higher priority run first.

When the Timer action ends successfully, the `NextRun` property of the Timer is updated to the next time that it should run. This time is computed according to the Schedule property of the Timer.

If a Timer is not executed, if an unhandled exception occurs, or if the action times out, the Timer's `NextRun` property is not updated. This means that the next time the OutSystems Scheduler Service checks for timers ready to run, the timer will be picked for execution.

<div class="info" markdown="1">

For Timers to operate correctly, make sure that the environment's database, controller and all front-end servers are in the [same timezone and their system clocks are synchronized](https://success.outsystems.com/Support/Enterprise_Customers/Maintenance_and_Operations/Timezone_considerations_in_the_OutSystems_Platform).

</div>

## Timers Timeout

The timeout of a Timer is set by default to 20 minutes, but you can change it by setting the `Timeout in Minutes` property of the timer.

If the action associated with a Timer does not end within a pre-defined time, the action is aborted and the Timer stops. This is considered an error and, therefore, the Timer will be executed again for the number of retries you set in the Environment Configuration area of Service Center (set by default to 3 retries).

## Sessions in Timers

Asynchronous logic, such as Timers and Process Activities, run in a separate session. All session variables will start with their default value when executing an action associated with a timer or process activity.
