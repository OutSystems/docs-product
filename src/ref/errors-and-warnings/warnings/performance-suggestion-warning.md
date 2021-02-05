# Performance Suggestion Warning

<a id="helpid-30136"></a>

Message
:   `Fetching data from the server in a splash screen may cause performance issues. Move '<aggregate | data action>' to the default screen.`

Cause
:   Fetching data from the server is typically a slow operation because it requires a request to a remote machine. Executing a slow operation in a splash screen will increase the time that the users must wait to use the app.

Recommendation
:   Fetch data from the server only when needed. If you really need to fetch data from the server in the app initialization stage, add your server Aggregates or Data Actions to the default screen instead. [Keeping the splash screen simple](https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Mobile_Best_Practices#Keep_the_Splash_Screen_Simple_and_Fast) allows your users to navigate faster to the default screen. Data will then be fetched from the server concurrently while the default screen is loading.

---

<a id="helpid-30137"></a>

Message
:   `The '<client action name>' Client Action calls several Server Actions. To avoid performance issues, group them all in a single Server Action and call it instead.`

Cause
:   Each time a Server Action is executed in a Client Action there is a request going from the user device to the server. Having several Server Actions in the same Client Action will result in multiple requests to the server, which can slower the application.

Recommendation
:   Group all the Server Actions executed in your Client Action in a single Server Action and use that Server Action insted. This will reduce the number of requests to the server to one single request.

---

<a id="helpid-30138"></a>

Message
:   `Iterating '<server action>' generates several requests to the server. To avoid performance issues, execute the For Each iteration inside another Server Action and use it instead.`

Cause
:   Each time a Server Action is executed in a Client Action there is a request going from the user device to the server. Iterating a Server Actions in a Client Action will result in multiple requests to the server, which can slower the application.

Recommendation
:   Execute the For Each iteration in a Server Action and call it in your Client Action. This will reduce the number of requests to the server to one single request.

---

<a id="helpid-30140"></a>

<a id="helpid-30141"></a>

Message
:   `'<OnInitialize action>' contains accesses to the local storage or server, which delays the <screen | block >'s render. To avoid performance issues, use Aggregates or Data Actions instead.`

Cause
:   The rendering of the screen/block only starts after the OnInitialize action finishes. If you access the local storage or execute requests to the server during this stage, you may delay the rendering of the screen/block and make the app look unresponsive.

Recommendation
:   Move all logic that accesses local storage or server into Screen Aggregates or Data Actions. This way the rendering starts sooner and the fetching of the data or running other server operations runs concurrently, while the screen/block is rendering. For more information, see the [Screen and Block Lifecycle Events](<../../../develop/logic/screen-block-lifecycle-events.md>) documentation.

---

<a id="helpid-30146"></a>

Message
:   `'<JavaScript element>' seems to include a JavaScript library, as it contains a large amount of code. To use an external JavaScript library, add it as a Script element instead.`

Cause
:   You seem to be including an external JavaScript library in a JavaScript flow element, which is not recommended. External JavaScript libraries can be too complex to run on mobile devices.

Recommendation
:   If you really need to use a JavaScript library, [add it as a Script element](<../../../extensibility-and-integration/javascript/mobile/use-external-lib.md>) instead of a JavaScript flow element. However, you should [avoid using external JavaScript libraries](https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Mobile_Best_Practices#Avoid_Using_External_JavaScript_Libraries). 

---

<a id="helpid-30149"></a>

Message
:   `Image '<name>' is bigger than 500 KB. To avoid performance issues, reduce the image size in bytes.`

Cause
:   Using big image files in your mobile app can increase the download time, or even block the download, and lead to poor performance.

Recommendation
:   Reduce the image size (in bytes) and adapt its dimensions (height/width) considering your target user's experience. Check the [best practices for optimizing images in mobile apps](https://success.outsystems.com/Documentation/Best_Practices/OutSystems_Mobile_Best_Practices#Optimize_the_File_Size_of_Images).
