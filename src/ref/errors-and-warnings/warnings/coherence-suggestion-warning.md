---
locale: en-us
guid: b50e7c6e-1f6a-4ae5-bd3d-5c621d1bd899
app_type: traditional web apps, mobile apps, reactive web apps
---

# Coherence Suggestion Warning

Message
:   `'Input' is declared as non-mandatory but <attribute> is mandatory`

Cause
:   You have an Input widget that handles an attribute value and the Mandatory property of the widget and attribute do not match. This occurs when, for example, you have an Edit Record widget used to edit an entity record and one of the entity attributes is declared as mandatory while the corresponding Input widget has False explicitly typed in the Mandatory property expression.

Recommendation
:   Either the Input widget Mandatory property should be explicitly True or an expression (evaluated only at runtime), or the attribute should be non-mandatory. Check which is more suitable for your module and fix the corresponding property.

---

Message
:   `'InputPassword' is declared as non-mandatory but <attribute> is mandatory`

Cause
:   You have an Input Password widget that handles an attribute value and the Mandatory property of the widget and attribute do not match. This occurs when, for example, you have an Edit Record widget used to edit an entity record and one of the entity attributes is declared as mandatory while the corresponding Input Password widget has False explicitly typed in the Mandatory property expression.

Recommendation
:    the Input Password widget Mandatory property should be explicitly True or an expression (evaluated only in runtime), or the attribute should be non-mandatory. Check which is more suitable for your module and fix the corresponding property.

---

Message
:   `'Max. Length' of Input (<size>) and <attribute> 'Length' (<size>) values should match`

Cause
:   You have an Input widget that handles an attribute value and the length does not match with the size of that attribute. This occurs when, for example, you have and Edit Record widget used to edit an entity record and one of the entity attributes has a Length different from the Max. Length property of the corresponding Input widget.

Recommendation
:   Either the Max. Length of the Input widget should be updated or the Length property of the attribute should be updated. Check which is more suitable for your module and fix the corresponding property.

---

Message
:   `'Max. Length' of Input Password (<size>) and <attribute> 'Length' (<size>) values should match`

Cause
:   You have an Input Password widget that handles an attribute value and the length does not match the size of that attribute. This occurs when, for example, you have an Edit Record widget used to edit an entity record and one of the entity attributes has a Length different from the Max. Length property of the corresponding Input Password widget.

Recommendation
:   Either the Max. Length of the Input Password widget or the Length property of the attribute should be updated. Check which is more suitable for your module and fix the corresponding property.

---

Message
:   `You should use an attribute from ‘<table | list records name>’ current record for the <input widget> ‘<input name>’ variable`

Cause
:   You have an input widget (Input, Input Password, Select, etc), inside a Table Records or List Records widget, that handles a variable that is not bound to the List runtime property of the list with records being displayed. In this situation, the attribute associated with this variable will have the same value in all the records and this value corresponds to the last value provided by the end user.

Recommendation
:   If you want to update a set of records correctly, in a Table Records widget or a List Records widget, the Variable property of the input widget should be obtained through the List runtime property. For example: `TableRecords1.List.Current.Customer.Name`

---

Message
:   `<query> 'Max. Records' should be set to '<number>' to match the number of records presented by <widget>`

Cause
:   You have a Table Records widget or List Records widget that presents a set of records different from the ones fetched by the associated query.

Recommendation
:   Check the Max. Records property of your aggregate or SQL query and update this property with the value suggested in `<number>`, based on the properties of Table Records widget or the List Records widget: either the value of the LineCount property, if StartIndex is 0, or the value StartIndex + LineCount + 1, otherwise. In this situation, you have the guarantee that you are fetching as many records as you need to display.

---

Message
:   `'Special Variable' will always be empty because 'Special List' is not specified`

Cause
:   You have a Combo Box widget that is not populated with generic values but the Special Variable property is set. This property is only necessary to gather the end user input when generic values are displayed, i.e. the Special List property is set.

Recommendation
:   Edit this Combo Box widget and delete the variable associated with the Special Variable property because this variable is ignored by Service Studio.

---

<a id="helpid-30142"></a>

Message
:   `'<OnInitialize action | OnReady action>' accesses Aggregates or Data Actions, but the data might not be available at this time. To avoid inconsistencies, use the OnAfterFetch of the Aggregate or Data Action instead.`

Cause
:   When the OnInitialize event occurs, the Aggregates and Data Actions of screens and blocks have not started to fetch data yet. Also, the OnReady event occurs right after the screen is ready and does not wait for the data to be fetched. Accessing Aggregates or Data Actions in OnInitialize or OnReady actions may cause inconsistencies, since the data may not be available by this time.

Recommendation
:   Move the logic that accesses the fetched data to the [OnAfterFetch](../../../develop/logic/screen-block-lifecycle-events.md#on-after-fetch) action of the Aggregate or Data Action. The OnAfterFetch of an Aggregate or Data Action is executed right after the data is fetched.

---

<a id="helpid-30143"></a>

Message
:   `There are Aggregates or Data Actions that use variables assigned in '<OnReady action| OnRender action>', which runs after the data is fetched. To avoid inconsistencies, move the assign of those variables to the OnInitalize event.`

Cause
:   Aggregates and Data Actions start to fetch data before the OnReady or the OnRender event occurs. If you assign the variables used in Aggregates and Data Actions in the OnReady or the OnRender actions, their value may not be the expected by the time the data is fetched, which will affect the resulting data.

Recommendation
:   Execute the Assign of the variables used in Aggregates or Data Actions in the [OnInitialize](../../../develop/logic/screen-block-lifecycle-events.md#on-initialize) action. This way you assure the variables are assigned with their values when the data is fetched.
