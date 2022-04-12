---
locale: en-us
guid: 286230b7-c011-42bd-9923-7b3ef0a4abbc
---

# Invalid Image Error

The `Invalid Image` error is issued in the following situations:

* `'Attribute' must be of 'Binary Data' data type in <Image>`
  
    The attribute that handles Image is not of the binary Data data type.

    Edit the Image widget and change the type of the Attribute property to Binary Data.

* `In <Image>, 'Id' must be set to an '<Entity> Identifier' value`
  
    You have a Database Image and its Id attribute does not have the correct data type.

    Edit the Image widget and change the type of the Id attribute to be an Entity Identifier data type.

* `'Id' must be set in <Image>`
  
    The Identifier of the image is not defined or is incorrect.

    Edit the Image widget and set the Id property to an Entity attribute that identifies the image. Note that this property must be of the type Entity Identifier.

* `'Attribute' must be set in <Image>`
  
    The attribute that handles the Image widget is not defined or is incorrect.

    Edit the Image widget and set the Attribute property to the Binary Data attribute/variable that contains the image content.

* `'File Name' must be set in <Image>`
  
    You have a Database Image with an image file name that is not defined or is incorrect.

    Edit the Image widget and set the File name property to a suitable file name.

* `'URL' must be set in <Image>`
  
    You have an external image with no defined URL address.

    Edit the Image widget and set the URL property with a suitable URL address.

Double-click on the error line to take you directly to the invalid image widget.
