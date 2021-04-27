
Use Session Variables to store data server-side in a key-value format. Use it to cache, for example, for configurations and app context data. Session Variables are cleared when the user logs out of the app or when the user closes all browser windows.

<div class="info" markdown="1">

INFO GOES HERE

</div>

Session Variables are available in Traditional Web Apps only. Avoid referencing elements with Session Variables in Reactive Web or Mobile Apps, as the platform can't keep the values of Session Variables in this scenario between requests. This is due to the runtime differences in the Reactive Web Apps / Mobile Apps on one side, which run in the client-side context, and Traditional Web Apps that run in the server-side context.

You can use the variables with many data types, but avoid using them for the [compound data types](<../../data/data-types/available-data-types.md>) due to performance considerations.

Add a Session Variable by clicking **Data** tab > **Session Variables** > **Add Session Variable**.

