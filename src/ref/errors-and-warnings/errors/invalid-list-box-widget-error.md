# Invalid List Box Widget Error

The `Invalid List Box` widget error is issued in the following situations:

* `'Selection Attribute' must be filled in with a Boolean attribute in <List Box> widget`
  
    You have a List Box widget and it won't be possible to determine which values are selected or not because the Selection Attribute property is not properly set.

    Edit the List Box widget and change the Selection Attribute property to have an attribute with Boolean data type.

* `'Source Attribute' must be filled in with an appropriate attribute in <List Box> widget`
  
    You have a List Box widget and the property that indicates which attribute is to be displayed is not correct. This situation occurs, for example, when you delete a Record Attribute that is being used as Source Attribute, or when an Attribute is of Binary Data data type.

    Edit the List Box widget and set the Source Attribute property with a suitable attribute.

Double-click on the error line to take you directly to the invalid List Box widget.
