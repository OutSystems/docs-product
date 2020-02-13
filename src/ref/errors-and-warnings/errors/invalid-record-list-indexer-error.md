# Invalid Record List Indexer Error

The `Invalid Record List Indexer` error is issued in the following situations:

* `'Record List' variable indexer must be an 'Integer'`
  
    You are indexing your List using a number that is not an Integer.

    Check the data type of your index because the `[]` operator expects an Integer value.

* `Only 'Record List' elements can be indexed`

    you are indexing an element that is not a List.

    Change the element data type because the `[]` operator can only be used with Lists.

Double-click on the error line to take you directly to the element where this situation was detected.
