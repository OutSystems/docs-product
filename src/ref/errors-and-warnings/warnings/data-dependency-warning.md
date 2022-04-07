---
locale: en-us
guid: 85799d04-70f9-41a2-8f2e-fb4f457747c5
---

# Data Dependency Warning

Message
:   `'{0}' won't fetch data until the data is explicitly requested. Consider using a Refresh Data element in a Client Action.`

Cause
:   Depending on how you set up your data sources, they can fetch data when the screen loads, or only when the fetching is triggered. In this case, you have data source in your app that never fetches data: the Fetch property is set to Only on demands, but there's no event that triggers getting the data.  

Recommendation
:    A way of fixing this warning is to place a Refresh Data element in the flow, which triggers the data fetching and then populates the UI the data source is bound to. Another way is to set the **Fetch** property to **At start**, to have the data loaded automatically.
