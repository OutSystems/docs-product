# Invalid Transition

The `Invalid Transition` error is issued in the following situations:

* `(Reverse Transition) is not a valid transition for <Screen>. This transition is only applicable to (Previous Screen) destinations.`

    You have a Destination node with the property Transition set to `(Reverse Transition)`, but this transition can only be used if the property Destination is `(Previous Screen)`.

    Change the property Destination to `(Previous Screen)` or choose another transition.

Double-click on the error line to take you directly to the source of the error.
