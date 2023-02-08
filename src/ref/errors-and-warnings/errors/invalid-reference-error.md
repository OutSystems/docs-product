---
locale: en-us
guid: 786ff43e-9e5f-4aa7-bda0-bb8693a6510a
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
---

# Invalid Reference Error

The `Invalid Reference` error is issued in the following situations:

* `Action <action> from <producer> cannot be referenced. It uses entity <entity> that has the property 'Show Tenant Identifier' with a different value from the original entity definition`
  
    You have a Reference to an Action that has a Parameter in which the definition includes a Multi-tenant entity and the Show Tenant Identifier property has a different value than the Producer module.

    You should remove the reference to the action or synchronize the value of the Show Tenant Identifier property.

* `You can't use '{0}' because it navigates to a Screen outside the application.`

    You have a Block that navigates to a Screen that is not part of your application. To fix this error you can: a) remove the navigation in the Block; or b) use an external link in the Block; or c) move the module that contains the Block to your application.

* `You can't have a Screen that navigates to a Screen outside the application.`

    You have a Screen that links to a Screen that is not part of your application. To fix this error you can: a) Use an external link; or b) move the module to keep it all in the same application.


Double-click on the error line to take you directly to the element where this situation was detected.
