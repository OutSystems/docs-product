# Invalid Public Block Error

The `Invalid Public Block` error is issued in the following situations:

* `Block '<Block>' cannot be public. It cannot navigate to Screens using Destination elements or use other blocks that do so.`

    You have a public Block that uses the node Destination to navigate to a Screen or uses another Block that does this. Public Blocks cannot navigate to screens. 

    Remove the navigation to the Screen or set the property Public of the Block to `No`.

Double-click on the error line to take you directly to the source of the error.
