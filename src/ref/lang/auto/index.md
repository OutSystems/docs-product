---
locale: en-us
guid: 90fdddea-a0af-4d39-a56d-dda1bd58ed12
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=1:89
summary: Explore the comprehensive guide to built-in functions, widgets, and plugins in OutSystems 11 (O11).
tags: outsystems 11, widgets guide, built-in functions, ide usage, reactive web apps
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - remember
---

# OutSystems Language

## Index

[Built-in Functions](<builtinfunctions.md>) | [Glossary](<glossary.md>) | [Error Messages](<errors.md>) | [Warning Messages](<warnings.md>)

  * ![](../images/ServiceStudio.Framework/Images/DataSet.ico) [Aggregate](<Class.Aggregate.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/AjaxRefresh.ico) [Ajax Refresh](<Class.Ajax%20Refresh.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Assign.ico) [Assign](<Class.Assign.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/AttachEmailContent.ico) [Attach File](<Class.Attach%20File.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ProcessAutomaticActivity.ico) [Automatic Activity](<Class.Automatic%20Activity.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/WebBlock.ico) [Block](<Class.Block.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/WebBlock.ico) [Block Widget](<Class.Block%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Button.ico) [Button Widget](<Class.Button%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Cell.ico) [Cell Widget](<Class.Cell%20Widget.md>) `10`
  * ![](../images/ServiceStudio.Framework/Images/CheckBox.ico) [Check Box Widget](<Class.Check%20Box%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ClientAction.ico) [Client Action](<Class.Client%20Action.md>) `3`
  * ![](../images/ServiceStudio.Framework/Images/ClientVariable.ico) [Client Variable](<Class.Client%20Variable.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ComboBox.ico) [Combo Box Widget](<Class.Combo%20Box%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Comment.ico) [Comment](<Class.Comment.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Comment.ico) [Comment Widget](<Class.Comment%20Widget.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ProcessConditionalStart.ico) [Conditional Start](<Class.Conditional%20Start.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Container.ico) [Container Widget](<Class.Container%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/DataAction.ico) [Data Action](<Class.Data%20Action.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/If.ico) [Decision](<Class.Decision.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ProcessDecisionOutcome.ico) [Decision Outcome](<Class.Decision%20Outcome.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/WebLink.ico) [Destination](<Class.Destination.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/DownloadWidget.ico) [Download](<Class.Download.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/EditRecord.ico) [Edit Record Widget](<Class.Edit%20Record%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/EmailScreen.ico) [Email](<Class.Email.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/End.ico) [End](<Class.End.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Entity.ico) [Entity](<Class.Entity.md>) `3`
  * ![](../images/ServiceStudio.Framework/Images/EntityAttribute.ico) [Entity Attribute](<Class.Entity%20Attribute.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/EntityDiagram.ico) [Entity Diagram](<Class.Entity%20Diagram.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Entry.ico) [Entry](<Class.Entry.md>) `1`
  * ![](../images/empty.png) [Event](<Class.Event.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ExcelToRecordList.ico) [Excel To Record List](<Class.Excel%20To%20Record%20List.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ExceptionHandler.ico) [Exception Handler](<Class.Exception%20Handler.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Process.ico) [Execute Process](<Class.Execute%20Process.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Expression.ico) [Expression Widget](<Class.Expression%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ExternalSite.ico) [External Site](<Class.External%20Site.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ForEach.ico) [For Each](<Class.For%20Each.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/WebLink.ico) [Go To Destination](<Class.Go%20To%20Destination.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Row.ico) [Header Row Widget](<Class.Header%20Row%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ProcessHumanActivity.ico) [Human Activity](<Class.Human%20Activity.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/If.ico) [If](<Class.If.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/If.ico) [If Widget](<Class.If%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/Image.ico) [Image](<Class.Image.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Image.ico) [Image Widget](<Class.Image%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter](<Class.Input%20Parameter.md>) `11`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (Deprecated SOAP)](<Class.Input%20Parameter%20(Deprecated%20SOAP).md>) `11`
  * ![](../images/ServiceStudio.Framework/Images/InputPassword.ico) [Input Password Widget](<Class.Input%20Password%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Input.ico) [Input Widget](<Class.Input%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/JavascriptNode.ico) [JavaScript](<Class.JavaScript.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/DeserializeJSON.ico) [JSON Deserialize](<Class.JSON%20Deserialize.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/SerializeJSON.ico) [JSON Serialize](<Class.JSON%20Serialize.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Link.ico) [Link Widget](<Class.Link%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/ListBox.ico) [List Box Widget](<Class.List%20Box%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ListRecords.ico) [List Records Widget](<Class.List%20Records%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/LocalVariable.ico) [Local Variable](<Class.Local%20Variable.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/LocalizedImage.ico) [Localized Image](<Class.Localized%20Image.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/MessageInfo.ico) [Message](<Class.Message.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/OutSystems.ico) [Mobile Module](<Class.Mobile%20Module.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Theme.ico) [Mobile Theme](<Class.Mobile%20Theme.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/OutSystems.ico) [Module](<Class.Module.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ClientEvent.ico) [On Application Ready](<Class.On%20Application%20Ready.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ClientEvent.ico) [On Application Resume](<Class.On%20Application%20Resume.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/SystemEvent.ico) [On Begin Web Request](<Class.On%20Begin%20Web%20Request.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/SystemEvent.ico) [On Session Start](<Class.On%20Session%20Start.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter](<Class.Output%20Parameter.md>) `10`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (Deprecated SOAP)](<Class.Output%20Parameter%20(Deprecated%20SOAP).md>) `10`
  * ![](../images/ServiceStudio.Framework/Images/PlaceholderArgument.ico) [Placeholder Content Widget](<Class.Placeholder%20Content%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/Placeholder.ico) [Placeholder Widget](<Class.Placeholder%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/Process.ico) [Process](<Class.Process.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/End.ico) [Process End](<Class.Process%20End.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Start.ico) [Process Start](<Class.Process%20Start.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Query Parameter](<Class.Query%20Parameter.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/RadioButton.ico) [Radio Button Widget](<Class.Radio%20Button%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/RaiseException.ico) [Raise Exception](<Class.Raise%20Exception.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/RecordListToExcel.ico) [Record List To Excel](<Class.Record%20List%20To%20Excel.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/OutSystems.ico) [Reference](<Class.Reference.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ClientEvent.ico) [ReferenceFlowExceptionHandlingFlow](<Class.ReferenceFlowExceptionHandlingFlow.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/DataSetRefresh.ico) [Refresh Data](<Class.Refresh%20Data.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Resource.ico) [Resource](<Class.Resource.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Role.ico) [Role](<Class.Role.md>) `3`
  * ![](../images/ServiceStudio.Framework/Images/Exception.ico) [Role Exception](<Class.Role%20Exception.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Row.ico) [Row Widget](<Class.Row%20Widget.md>) `8`
  * ![](../images/ServiceStudio.Framework/Images/ClientAction.ico) [Run Client Action](<Class.Run%20Client%20Action.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [Run Server Action](<Class.Run%20Server%20Action.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/RuntimeProperty.ico) [Runtime Property](<Class.Runtime%20Property.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Screen_Mobile.ico) [Screen](<Class.Screen.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [Screen Action](<Class.Screen%20Action.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/JavaScript.png) [Script](<Class.Script.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/SendEmail.ico) [Send Email](<Class.Send%20Email.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [Server Action](<Class.Server%20Action.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/ServiceAPIMethod.ico) [Service Action](<Class.Service%20Action.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/SessionVariable.ico) [Session Variable](<Class.Session%20Variable.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ShowRecord.ico) [Show Record SMS Widget](<Class.Show%20Record%20SMS%20Widget.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/SiteProperty.ico) [Site Property](<Class.Site%20Property.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/WebService.ico) [SOAP Web Service](<Class.SOAP%20Web%20Service.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/WebReference.ico) [SOAP Web Service (Deprecated)](<Class.SOAP%20Web%20Service%20(Deprecated).md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/AdvancedQuery.ico) [SQL](<Class.SQL.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/Start.ico) [Start](<Class.Start.md>) `2`
  * ![](../images/StaticEntity.ico) [Static Entity](<Class.Static%20Entity.md>) `3`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure](<Class.Structure.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure (Deprecated SOAP)](<Class.Structure%20(Deprecated%20SOAP).md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute](<Class.Structure%20Attribute.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute (Deprecated SOAP)](<Class.Structure%20Attribute%20(Deprecated%20SOAP).md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/CSS.ico) [Style Sheet](<Class.Style%20Sheet.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Switch.ico) [Switch](<Class.Switch.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/TableRecords.ico) [Table Records Widget](<Class.Table%20Records%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Table.ico) [Table Widget](<Class.Table%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Text.ico) [Text Widget](<Class.Text%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/Theme.ico) [Theme](<Class.Theme.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/Timer.ico) [Timer](<Class.Timer.md>) `1`
  * ![](../images/empty.png) [Trigger Event](<Class.Trigger%20Event.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/WebFlow.ico) [UI Flow](<Class.UI%20Flow.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/InputFilename.ico) [Upload Widget](<Class.Upload%20Widget.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Exception.ico) [User Exception](<Class.User%20Exception.md>) `1`
  * ![](../images/ServiceStudio.Framework/Images/ProcessWait.ico) [Wait](<Class.Wait.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/WebBlock.ico) [Web Block](<Class.Web%20Block.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/WebBlock.ico) [Web Block Widget](<Class.Web%20Block%20Widget.md>) `4`
  * ![](../images/ServiceStudio.Framework/Images/WebScreen.ico) [Web Screen](<Class.Web%20Screen.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [Web Service Method](<Class.Web%20Service%20Method.md>) `2`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [Web Service Method (Deprecated SOAP)](<Class.Web%20Service%20Method%20(Deprecated%20SOAP).md>) `2`

### Plugins

  * <img width="16" height="16" src="../images/Plugins/NRWidgets/AdvancedHtml.ico"/> [HTML Element](<ServiceStudio.Plugin.NRWidgets.AdvancedHtml.md>) `NRWidgets.AdvancedHtml`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Button.ico"/> [Button](<ServiceStudio.Plugin.NRWidgets.Button.md>) `NRWidgets.Button`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/ButtonGroup.ico"/> [Button Group](<ServiceStudio.Plugin.NRWidgets.ButtonGroup.md>) `NRWidgets.ButtonGroup`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/ButtonGroupItem.ico"/> [Button Group Item](<ServiceStudio.Plugin.NRWidgets.ButtonGroupItem.md>) `NRWidgets.ButtonGroupItem`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Checkbox.ico"/> [Checkbox](<ServiceStudio.Plugin.NRWidgets.Checkbox.md>) `NRWidgets.Checkbox`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Container.ico"/> [Container](<ServiceStudio.Plugin.NRWidgets.Container.md>) `NRWidgets.Container`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Dropdown.ico"/> [Dropdown](<ServiceStudio.Plugin.NRWidgets.Dropdown.md>) `NRWidgets.Dropdown`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Expression.ico"/> [Expression](<ServiceStudio.Plugin.NRWidgets.Expression.md>) `NRWidgets.Expression`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Form.ico"/> [Form](<ServiceStudio.Plugin.NRWidgets.Form.md>) `NRWidgets.Form`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Icon.ico"/> [Icon](<ServiceStudio.Plugin.NRWidgets.Icon.md>) `NRWidgets.Icon`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Image.ico"/> [Image](<ServiceStudio.Plugin.NRWidgets.Image.md>) `NRWidgets.Image`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Input.ico"/> [Input](<ServiceStudio.Plugin.NRWidgets.Input.md>) `NRWidgets.Input`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Label.ico"/> [Label](<ServiceStudio.Plugin.NRWidgets.Label.md>) `NRWidgets.Label`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Link.ico"/> [Link](<ServiceStudio.Plugin.NRWidgets.Link.md>) `NRWidgets.Link`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/List.ico"/> [List](<ServiceStudio.Plugin.NRWidgets.List.md>) `NRWidgets.List`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/ListItem.ico"/> [List Item](<ServiceStudio.Plugin.NRWidgets.ListItem.md>) `NRWidgets.ListItem`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/ListSwipeLeft.ico"/> [List Action](<ServiceStudio.Plugin.NRWidgets.ListItemAction.md>) `NRWidgets.ListItemAction`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Popover.ico"/> [Popover Menu](<ServiceStudio.Plugin.NRWidgets.Popover.md>) `NRWidgets.Popover`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Popup.ico"/> [Popup](<ServiceStudio.Plugin.NRWidgets.Popup.md>) `NRWidgets.Popup`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/RadioButton.ico"/> [Radio Button](<ServiceStudio.Plugin.NRWidgets.RadioButton.md>) `NRWidgets.RadioButton`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/RadioGroup.ico"/> [Radio Group](<ServiceStudio.Plugin.NRWidgets.RadioGroup.md>) `NRWidgets.RadioGroup`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Switch.ico"/> [Switch](<ServiceStudio.Plugin.NRWidgets.Switch.md>) `NRWidgets.Switch`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/TableRecords.ico"/> [Table](<ServiceStudio.Plugin.NRWidgets.TableRecords.md>) `NRWidgets.TableRecords`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/TextArea.ico"/> [Text Area](<ServiceStudio.Plugin.NRWidgets.TextArea.md>) `NRWidgets.TextArea`
  * <img width="16" height="16" src="../images/Plugins/NRWidgets/Upload.ico"/> [Upload](<ServiceStudio.Plugin.NRWidgets.Upload.md>) `NRWidgets.Upload`
  * <img width="16" height="16" src="../images/Plugins/REST/rest-consume.ico"/> [REST API](<ServiceStudio.Plugin.REST.RestClient.md>) `REST.RestClient`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [REST API Method](<ServiceStudio.Plugin.REST.RestAction.md>) `REST.RestAction`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (REST API Method)](<ServiceStudio.Plugin.REST.RestActionInput.md>) `REST.RestActionInput`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (REST API Method)](<ServiceStudio.Plugin.REST.RestActionOutput.md>) `REST.RestActionOutput`
  * <img width="16" height="16" src="../images/Plugins/REST/Callback.ico"/> [REST API Callback](<ServiceStudio.Plugin.REST.RestCallbackActionFlow.md>) `REST.RestCallbackActionFlow`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (REST API Callback)](<ServiceStudio.Plugin.REST.RestCallbackActionFlowInput.md>) `REST.RestCallbackActionFlowInput`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (REST API Callback)](<ServiceStudio.Plugin.REST.RestCallbackActionFlowOutput.md>) `REST.RestCallbackActionFlowOutput`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure (REST API Callback)](<ServiceStudio.Plugin.REST.RestCallbackStructure.md>) `REST.RestCallbackStructure`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute (REST API Callback)](<ServiceStudio.Plugin.REST.RestCallbackStructureAttribute.md>) `REST.RestCallbackStructureAttribute`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure (REST API Method)](<ServiceStudio.Plugin.REST.RestStructure.md>) `REST.RestStructure`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute (REST API Method)](<ServiceStudio.Plugin.REST.RestStructureAttribute.md>) `REST.RestStructureAttribute`
  * <img width="16" height="16" src="../images/Plugins/RESTService/rest-expose.ico"/> [REST API](<ServiceStudio.Plugin.RESTService.RestService.md>) `RESTService.RestService`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [REST API Method](<ServiceStudio.Plugin.RESTService.RestServiceAction.md>) `RESTService.RestServiceAction`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (REST API Method)](<ServiceStudio.Plugin.RESTService.RestServiceActionInput.md>) `RESTService.RestServiceActionInput`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (REST API Method)](<ServiceStudio.Plugin.RESTService.RestServiceActionOutput.md>) `RESTService.RestServiceActionOutput`
  * <img width="16" height="16" src="../images/Plugins/RESTService/Callback.ico"/> [REST API Callback (Authentication)](<ServiceStudio.Plugin.RESTService.RestServiceAuthenticationFlow.md>) `RESTService.RestServiceAuthenticationFlow`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (REST Authentication)](<ServiceStudio.Plugin.RESTService.RestServiceAuthenticationFlowInput.md>) `RESTService.RestServiceAuthenticationFlowInput`
  * <img width="16" height="16" src="../images/Plugins/RESTService/Callback.ico"/> [REST API Callback](<ServiceStudio.Plugin.RESTService.RestServiceCallbackActionFlow.md>) `RESTService.RestServiceCallbackActionFlow`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (REST Service API Callback)](<ServiceStudio.Plugin.RESTService.RestServiceCallbackActionFlowInput.md>) `RESTService.RestServiceCallbackActionFlowInput`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (REST Service API Callback)](<ServiceStudio.Plugin.RESTService.RestServiceCallbackActionFlowOutput.md>) `RESTService.RestServiceCallbackActionFlowOutput`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure (REST Service API Callback)](<ServiceStudio.Plugin.RESTService.RestServiceCallbackStructure.md>) `RESTService.RestServiceCallbackStructure`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute (REST Service API Callback)](<ServiceStudio.Plugin.RESTService.RestServiceCallbackStructureAttribute.md>) `RESTService.RestServiceCallbackStructureAttribute`
  * <img width="16" height="16" src="../images/Plugins/SAP/SAP.ico"/> [SAP Connection](<ServiceStudio.Plugin.SAP.SapClient.md>) `SAP.SapClient`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [SAP Remote Function](<ServiceStudio.Plugin.SAP.SapAction.md>) `SAP.SapAction`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (SAP Remote Function)](<ServiceStudio.Plugin.SAP.SapActionInput.md>) `SAP.SapActionInput`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (SAP Remote Function)](<ServiceStudio.Plugin.SAP.SapActionOutput.md>) `SAP.SapActionOutput`
  * <img width="16" height="16" src="../images/Plugins/SAP/Callback.ico"/> [SAP Callback](<ServiceStudio.Plugin.SAP.SapCallbackActionFlow.md>) `SAP.SapCallbackActionFlow`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (SAP Callback)](<ServiceStudio.Plugin.SAP.SapCallbackActionFlowInput.md>) `SAP.SapCallbackActionFlowInput`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure (SAP Remote Function)](<ServiceStudio.Plugin.SAP.SapStructure.md>) `SAP.SapStructure`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute (SAP Remote Function)](<ServiceStudio.Plugin.SAP.SapStructureAttribute.md>) `SAP.SapStructureAttribute`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (SAP Username)](<ServiceStudio.Plugin.SAP.SapDynamicLoginInput.md>) `SAP.SapDynamicLoginInput`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (SAP Password)](<ServiceStudio.Plugin.SAP.SapDynamicPasswordInput.md>) `SAP.SapDynamicPasswordInput`
  * <img width="16" height="16" src="../images/Plugins/SOAP/SOAPConsume.ico"/> [SOAP Web Service (Consumed)](<ServiceStudio.Plugin.SOAP.SOAPClient.md>) `SOAP.SOAPClient`
  * ![](../images/ServiceStudio.Framework/Images/Action.ico) [Web Service Method (Consumed)](<ServiceStudio.Plugin.SOAP.SOAPAction.md>) `SOAP.SOAPAction`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Input Parameter (Consumed SOAP Method)](<ServiceStudio.Plugin.SOAP.SOAPActionInput.md>) `SOAP.SOAPActionInput`
  * ![](../images/ServiceStudio.Framework/Images/OutputParameter.ico) [Output Parameter (Consumed SOAP Method)](<ServiceStudio.Plugin.SOAP.SOAPActionOutput.md>) `SOAP.SOAPActionOutput`
  * <img width="16" height="16" src="../images/Plugins/SOAP/Callback.ico"/> [SOAP Callback (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPCallbackActionFlow.md>) `SOAP.SOAPCallbackActionFlow`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Password Input Parameter (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPDynamicPasswordInput.md>) `SOAP.SOAPDynamicPasswordInput`
  * ![](../images/ServiceStudio.Framework/Images/InputParameter.ico) [Username Input Parameter (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPDynamicUsernameInput.md>) `SOAP.SOAPDynamicUsernameInput`
  * ![](../images/ServiceStudio.Framework/Images/Entity.ico) [Static Entity (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPStaticEntity.md>) `SOAP.SOAPStaticEntity`
  * ![](../images/ServiceStudio.Framework/Images/EntityAttribute.ico) [Static Entity Attribute (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPStaticEntityAttribute.md>) `SOAP.SOAPStaticEntityAttribute`
  * ![](../images/ServiceStudio.Framework/Images/Structure.ico) [Structure (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPStructure.md>) `SOAP.SOAPStructure`
  * ![](../images/ServiceStudio.Framework/Images/StructureAttribute.ico) [Structure Attribute (Consumed SOAP)](<ServiceStudio.Plugin.SOAP.SOAPStructureAttribute.md>) `SOAP.SOAPStructureAttribute`
  * <img width="16" height="16" src="../images/Plugins/Widgets/EditableTable.ico"/> [Editable Table Widget](<ServiceStudio.Plugin.Widgets.EditableTable.md>) `Widgets.EditableTable`
  * <img width="16" height="16" src="../images/Plugins/Widgets/EditableTableCell.ico"/> [Cell Widget](<ServiceStudio.Plugin.Widgets.EditableTableCell.md>) `Widgets.EditableTableCell`
  * <img width="16" height="16" src="../images/Plugins/Widgets/Form.ico"/> [Form Widget](<ServiceStudio.Plugin.Widgets.Form.md>) `Widgets.Form`
  * <img width="16" height="16" src="../images/Plugins/Widgets/Label.ico"/> [Label Widget](<ServiceStudio.Plugin.Widgets.Label.md>) `Widgets.Label`

