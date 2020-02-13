# Invalid Column Reference Error

The `Invalid Column Reference` error is issued in the following situations:

* `The <column1> column cannot use <column2> in its formula since <column2> depends on the definition of <column1>'. Change <column1> or <column2> columns to stop them from depending on one another`

    You have two columns that depend on one another, creating a circular dependency.

* `The <column> column cannot be sorted since its formula only contains constants or functions that always return the same result. Stop sorting this column, or change its formula to use values from other columns`

    The column you are sorting only contains constant values or functions that always return the same value.  
  
    You must stop sorting the column causing the error, or change its formula to use entity attributes.

* `The columns '{0}' and '{1}' cannot be sorted at the same time since they have the same formula. Remove the sort from one of the columns, or make their formulas different from one another`

    Cannot sort at the same time columns with the same formula.  
  
    You must stop sorting one of the columns, or change their formulas.

    Edit the columns to stop the circular dependency.

Double-click on the error line to take you directly to the source of the error.
