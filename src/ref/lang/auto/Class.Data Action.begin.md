Use Data Actions to fetch complex data from the database or external systems after the Screen loads. Data Actions run on the server.

Data Actions and client-side Aggregates concurrently start to fetch data after the Screen loads.

<div class="info" markdown="1">
Don't perform login operations in Data Actions expecting to use the GetUserId() function in its On After Fetch event. The parallel execution of Data Actions and client-side Agreggates in a Screen overrides the session authentication cookie. Using the GetUserId() function in the On After Fetch event might return an empty value.
</div>
