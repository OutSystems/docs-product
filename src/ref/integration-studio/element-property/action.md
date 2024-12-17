---
locale: en-us
guid: b5a2987a-129b-4bc7-953d-13a6f8ffc2ca
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/design/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=3066-140&t=0cuQUgeosMV2m0Kw-1
summary: OutSystems 11 (O11) action properties include mandatory and optional settings, defaults, and customization options.
tags: ide usage, reactive web apps, tutorials for beginners, extension management, action definition
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
  - integration studio
coverage-type:
  - remember
---

# Action Properties

The next table presents the properties of the [action](<../../../integration-with-systems/integration-studio/managing-extensions/action-define.md>) element.  

|Property|Description|Optionality|Default value|Obs.|
|--- |--- |--- |--- |--- |
|Name|Name of the action.|Mandatory|`Action `|See [rules for naming elements](<../element-naming.md>).|
|Icon|Icon associated with the action. This icon will be used in Service Studio to graphically identify this action.||By default, Integration Studio associates an icon with the extension action. If the action was initially created in this tool, then the icon associated is ![Default icon representing an action in Service Studio](images/action-icon.png "Default Action Icon") `(Default)`. If the action was imported from a .NET assembly, then the default icon associated is ![Icon for an action imported from a .NET assembly in Service Studio](images/imported-action-icon.png "Imported Action Icon").|See how to [change the action icon](<../editor/action.md>).|
|Description|Free text that describes the action.|Optional||Useful for documentation and knowledge transfer purposes.<br/>The maximum size of this property is 255 characters.|
|Function|Indicates whether this action can be used as a user function in expressions, in Service Studio.|Mandatory|No||
|Import Details...|Presents information about the import operation.|Optional||Only available when the action was added during the Import Actions from .NET Assembly wizard. For more information, see [Action editor](<../editor/action.md#import-details>).|
