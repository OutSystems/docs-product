---
tags: runtime-mobileandreactiveweb
summary: Provides the ability to perform normal and history navigations, and to override some navigation behaviors (e.g. back). Used to create new transition animations instead of overriding the existing ones using CSS.
locale: en-us
guid: c274f0ef-e0b8-4093-bd87-049cda15248d
---

# Navigation

Provides the ability to perform normal and history navigations, and to override some navigation behaviors (e.g. back). Used to create new transition animations instead of overriding the existing ones using CSS.

The methods below related with BackHandlers ([registerBackNavigationHandler](navigation.md#registerbacknavigationhandler) and [unregisterBackNavigationHandler](navigation.md#unregisterbacknavigationhandler)) are used to manipulate the behavior of back actions, e.g. pressing the 'Back' button in Android. A common use case is when the 'Back' button is pressed just to close a menu instead of navigating to the previous screen.

## Hierarchy

**Navigation**

## Summary

|Methods|Description|
|---|---|
|[navigateBack](navigation.md#navigateback)|Performs a back navigation, using an optional transition animation.|
|[navigateForward](navigation.md#navigateforward)|Performs a forward navigation, using an optional transition animation.|
|[navigateTo](navigation.md#navigateto)|Performs a navigation to a provided URL using an optional transition animation.|
|[navigatedFromHistory](navigation.md#navigatedfromhistory)|Checks if the current screen was loaded from the browser's history.|
|[registerBackNavigationHandler](navigation.md#registerbacknavigationhandler)|Registers a callback function in a queue to be called when navigating back.|
|[unregisterBackNavigationHandler](navigation.md#unregisterbacknavigationhandler)|Unregisters a previously registered callback.|

## Methods

### navigateBack

**navigateBack([transition: TransitionAnimation \| string]): void**

Performs a back navigation, using an optional transition animation.

If there are registered back event handlers, the last registered one is executed; otherwise, a navigation to the previous screen is performed, reversing the transition animation used to reach the current screen, if one was used. If the current screen is the first one opened in the application, the application is closed.

Example:

```javascript
// navigate to the previous screen using a 'Slide from Left' transition animation
$public.Navigation.navigateBack(3);
```

Parameters:

* (Optional) **transition**: TransitionAnimation \| string<br/> Either a known transition type (0 = None, 1 = Default, 2 = Fade, 3 = Slide from Left, 4 = Slide from Right, 5 = Slide from Bottom, 6 = Slide from Top) or a string representing the prefix of the CSS classes used to animate the transition. If a value is not provided, the animation used to enter the current screen is reversed and used.

Returns: void

### navigateForward

**navigateForward([transition: TransitionAnimation \| string]): void**

Performs a forward navigation, using an optional transition animation.

The forward navigation is performed if the current screen was entered using a back navigation; otherwise, no navigation is performed.

Example:

```javascript
// perform a forward navigation using a 'Slide from Right' transition animation
$public.Navigation.navigateForward(4);
```

Parameters:

* (Optional) **transition**: TransitionAnimation \| string<br/> Either a known transition type (0 = None, 1 = Default, 2 = Fade, 3 = Slide from Left, 4 = Slide from Right, 5 = Slide from Bottom, 6 = Slide from Top) or a string representing the prefix of the CSS classes used to animate the transition. If a value is not provided, the same animation used to enter the next screen for the last time is used.

Returns: void

### navigateTo

**navigateTo(url: string, [transition: TransitionAnimation \| string], [replace: boolean]): void**

Performs a navigation to a provided URL using an optional transition animation.

Parameters:

* **url**: string<br/> Relative or absolute URL to navigate to. If the URL points to a screen of the application, the transition will be animated according to the value of the `transition` parameter. Otherwise, a normal browser navigation is done.
* (Optional) **transition**: TransitionAnimation \| string<br/> Either a known transition type (0 = None, 1 = Default, 2 = Fade, 3 = Slide from Left, 4 = Slide from Right, 5 = Slide from Bottom, 6 = Slide from Top) or a string representing the prefix of the CSS classes used to animate the transition. If a value is not provided, the default transition of the application’s entry module will be used.
* (Optional) **replace**: boolean<br/> Indicates if the navigation should replace the current history entry, instead of creating a new one that the user can navigate back to. If a value is not provided, the default is `false`.

Returns: void

### navigatedFromHistory

**navigatedFromHistory(): boolean**

Checks if the current screen was loaded from the browser's history.

Returns: boolean

Returns `true` if the current screen was loaded from the browser's history, `false` otherwise.

### registerBackNavigationHandler

**registerBackNavigationHandler(handlerCallback: function): number**

Registers a callback function in a queue to be called when navigating back.

When the 'back' event is triggered, the last inserted handler is called and removed from the queue. If no event handler is registered, it performs a navigation to the previous screen, reversing the transition animation used to reach the current screen, if one was used.

Example:

```javascript
// prevent the user from navigating back when a custom sidebar menu is being displayed

var menuBackHandler = function() {
  hideSidebarMenu();
};

showSidebarMenu();
$public.Navigation.registerBackNavigationHandler(menuBackHandler);

// this back navigation will just hide the menu
$public.Navigation.navigateBack();
```

Parameters:

* **handlerCallback**: function<br/> Callback to be called when a 'back' event occurs.

Returns: number

Id of the registered callback.

### unregisterBackNavigationHandler

**unregisterBackNavigationHandler(id: number): void**

Unregisters a previously registered callback.

If no callback exists with the provided id, no action is taken.

Parameters:

* **id**: number<br/> Id of the callback to be unregistered.

Returns: void

