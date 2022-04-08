---
locale: en-us
guid: f9c4bf6c-a906-4df6-9272-a29b3d26466e
---

# Invalid Excel Import Error

The `Invalid Excel Import` error is issued in the following situations:

* `No Worksheet with data was found in the Excel file`
  
    The Excel file you chose contains no data. The Excel file should contain a first row with the column headers and the following rows should have the data to be loaded.

    Check your Excel file and make sure it contains at least one worksheet with column headers and rows with data to be loaded.

* `Definition of columns headers must start at the A1 cell in the '<worksheet>' Worksheet`
  
    The column headers definition must start at the A1 cell of the Excel worksheet.

    Edit your Excel file and move the column headers and their data to have the first column header starting at the A1 cell.

* `The specified Excel file is encrypted`

    The Excel file must be unencrypted to be imported.

    Import an unencrypted version of the Excel file.

    ![](images/invalid-excel-import.png)
