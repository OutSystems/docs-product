---
locale: en-us
guid: 20338e6c-c39c-4b7a-9370-c40a6ebc5b48
---

# Scalability Suggestion Warning

Message
:   `Screen input parameters of 'Binary Data' data type should be avoided`

Cause
:   You have a Binary Data input parameter that should be avoided due to performance reasons.

Recommendation
:   You should avoid having screen input parameters of the Binary Data data type.

---

Message
:   `Screen input parameters of 'List' data type should be avoided`

Cause
:   You have a List input parameter that should be avoided due to performance reasons.

Recommendation
:   You should avoid having screen input parameters of the List data type.

---

Message
:   `Screen input parameters of 'Record' data type with Binary Data, Record, or List attributes should be avoided`

Cause
:   You have a Record input parameter that has an attribute whose data type is Binary Data, Record, or List.

Recommendation
:   You should avoid having screen input parameters whose type is Record and that has a Binary Data, Record, or List attribute.

---

Message
:   `Session variables of 'Binary Data' data type should be avoided`

Cause
:   One of the session variables that you defined is of the Binary Data data type and you should avoid this situation due to performance reasons.

Recommendation
:   You should avoid having session variables of the Binary Data data type.

---

Message
:   `Session variables of 'List' data type should be avoided`

Cause
:   One of the session variable that you defined is of the List data type and you should avoid this situation due to performance reasons.

Recommendation
:   You should avoid having session variables of the List data type.

---

Message
:   `Session variables of 'Record' data type with Binary Data, Record, or List attributes should be avoided`

Cause
:   One of the session variables that you defined is of the Record or List data type and one of its attributes is of the Binary Data, Record, or List data type.

Recommendation
:   You should avoid having a session variable of List or Record data type that has an attribute of the Binary Data, Record, or List data type.

---

Message
:   `Binary Data attributes should be placed in a separate entity`

Cause
:   You have an entity with an attribute of the Binary Data data type.

Recommendation
:   You should split the original entity into two entities, placing the Binary Data attribute in a new entity. The primary key of this new entity must be a Foreign Key to the original entity (a one to one relationship).

---

Message
:   `The <aggregate> is being calculated once for each <entity> (cross join). Consider adding a join condition involving the <entity> to improve the application performance`

Cause
:   Your data is using more than one entity and there is no join condition between them.

Recommendation
:   Open the aggregate to validate whether the join between these two entities is correct. Probably you have a cross join, while your intention was most likely to make an inner or outer join but you forgot to define this join condition.

---

Message
:   `An entity index based on the <attribute> reference attribute should be created`

Cause
:   You have an entity with a reference attribute (aka Foreign Key) and the Delete Rule associated with this attribute is set to Protect or Delete.

Recommendation
:   Due to performance reasons you should create an index on the reference attribute of the entity.

---

Message
:   `For Each 'Start Index' should be set to '<start index>' and the 'Maximum Iterations' should be set with '<maximum iterations>' to match the number of displayed records.`

Cause
:   You have a Table Records widget or List Records widget that displays a set of records different from the ones iterated in the For Each.

Recommendation
:   Check the Start Index and Maximum Iterations properties of the For Each element. Update the properties with the values suggested respectively in `<start index>` and `<maximum iterations>`, based on the properties of Table Records widget or the List Records widget: either the value of the LineCount property, if StartIndex is 0, or the value StartIndex + LineCount + 1, otherwise. In this situation, you have the guarantee that you are iterating as many records as you need to display. 
