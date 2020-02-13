A Theme defines the look and feel of the application, including what layouts are used for the screens, the global stylesheet used, and also the grid definitions used to position and size elements on the screen. 

## Exposed Theme

A Theme cannot be exposed when:

* It has a Web Block with a parameter that is defined using an Entity/Structure that is not exposed.
* It has a Web Block with a parameter that is defined using an Entity/Structure that is reused from another module.
* It contains a Link widget, Button widget, or a consumed Web Screen with arguments of Binary Data, Record, or List data types.
