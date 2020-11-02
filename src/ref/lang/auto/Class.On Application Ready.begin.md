---
tags: runtime-mobileandreactiveweb
---

You app runs the **On Application Ready** during the loading of the home module. Use **On Application Ready** to set up the app, for example, to initialize variables and mobile plugins.

The **On Application Ready** action runs asynchronously, and doesn't block the render of the screens.

Note again that **On Application Ready** by design runs only during the loading of the home module. This means that the app ignores this action in the non-home modules.

To add the **On Application Ready** action to a Mobile or Reactive Web App do the following in Service Studio:

1. In the home module of your app, open the **Logic** tab.

1. Right-click the **Client Actions** node in the tree and select **Add System Event** > **On Application Ready**.

    ![Systems Event in the context menu](images/ss-add-system-event-reactive.png)
