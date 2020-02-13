# SQL Injection Warning

Message
:   `Avoid enabling the Expand Inline property of a SQL Query Parameter since it could make your application vulnerable to SQL injection.`

Cause
:   OutSystems uses [prepared statements](<https://en.wikipedia.org/wiki/Prepared_statement>) by default to execute the SQL queries that you define in [SQL elements](<../../../develop/data/query/sql.md>). These prepared statements contain SQL parameters or placeholders, for which you define values before executing the SQL statement. These parameters can only store a value of a given type and not arbitrary SQL fragments.

    If you enable the Expand Inline property for a Query Parameter, its value will no longer be handled as a SQL parameter value. Instead, the Query Parameter value will be included in the SQL statement without first being evaluated and turned into a literal by the SQL engine. This means that you are able to use the Query Parameter to dynamically insert SQL fragments in the full SQL statement, but it also means that your end-users may be able exploit this fact if you do not take the necessary precautions.
    
    Learn more on how the use of prepared statements can prevent SQL injection attacks in OWASP's [SQL Injection Prevention Cheat Sheet](<https://www.owasp.org/index.php/SQL_Injection_Prevention_Cheat_Sheet>). 

When is it safe to hide the warning?
:   You should **only** hide the warning when you have ensured that no values entered by end-users are being added to your SQL statement. 

## Recommendation: Avoid using Expand Inline

OutSystems will use an SQL parameter for every Query Parameter that has the Expand Inline property **disabled**. This property is disabled by default, providing you default protection against SQL injection attacks.

**Proper use of parameters being expanded inline is hard**, since you need to make sure that any user input has been properly escaped in the right way before using it in an SQL statement. If possible, avoid enabling this property altogether. 

<div class="info" markdown="1">

OutSystems provides ways of implementing common use cases without enabling this property. Check [Building dynamic SQL statements the right way](<https://success.outsystems.com/Documentation/Best_Practices/Building_dynamic_SQL_statements_the_right_way>).

</div>

If you **must** use Expand Inline, take also the following recommendations into account:

Use EncodeSql to encode string literals
:   The EncodeSql function encodes string literals to be used in SQL statements when the Expand Inline property is enabled.

    Make sure you avoid the following bad practices of using EncodeSql:

    — **Do not** use EncodeSql to encode the full contents of an SQL parameter. For example:  
    `myparameter = EncodeSql("WHERE surname = " + @myVariable1 + " OR name = " + @myVariable2)`  
    This pattern is wrong in most occasions, and thus you will get a warning if you do it.  
    Use EncodeSql only to encode **string literals**, not complete fragments of an SQL statement. 

    — **Do not** build "WHERE column IN (@values)" clauses by wrapping all the values in a EncodeSql call:  
    `values = EncodeSql(name1 + "," + name2 + "," + name)`  
    This approach will **not** protect you from SQL injection.  
    Instead, use the [BuildSafe_InClauseIntegerList](../../apis/auto/sanitization-api.final.md#BuildSafe_InClauseIntegerList) and [BuildSafe_InClauseTextList](../../apis/auto/sanitization-api.final.md#BuildSafe_InClauseTextList) functions to build "WHERE column IN (@values)" clauses.
    

Do not perform manual string encoding using the Replace
:   String literals should **only** be encoded using the EncodeSql function. Doing it manually through the Replace function is prone to errors and can introduce bugs in your application that can later be exploited by end-users of your application.
