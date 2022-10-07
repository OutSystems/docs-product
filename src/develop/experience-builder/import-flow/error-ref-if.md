---
summary:  Experience Builder validates the flow templates module to provide a flawless experience for developers using custom flows.
locale: en-us
guid: 8c89ad30-ff41-497f-81c9-2ec418fde122
app_type: traditional web apps, mobile apps, reactive web apps
---

# Validations

During the process of importing custom flow templates, Experience Builder validates the module structure. The goal of this check is to ensure the optimal integration with features in the tool and deliver the best experience to developers using them.

Similar to Service Studio, a failed validation can result in either an **error** or a **warning**.

* **Errors** block the flow importing process and must be fixed before proceeding.

* **Warnings** are items of concern that should get analyzed and, if necessary, fixed.

## Errors

### Flows not uniquely bound to a module

Issue
:   Having multiple copies of the same flow imported to Experience Builder isn't allowed.

Possible cause
:   The module contains flows that have already been imported into another module.

Solution
:   Either delete the flows in the other module and re-import this module, or delete the flow in the current module.

### Invalid module template

Issue
:  The module template isn't valid.

Possible cause
:   The module isn't based on the Experience Builder module template.

Solution
:   Use the application provided by Experience Builder before proceeding with the importing process.

### Invalid Common flow

Issue
:   The common flow isn't valid.

Possible cause
:   Elements in the Common flow have been modified.

Solution
:   Undo any changes made to the elements in the common flow. Elements in the Common flow should never be modified. 

### Not all flows have a theme

Issue
:   The flows theme structure is invalid.

Possible cause
:   The flow theme does not inherit its definitions from the module's default theme.

Solution
:   Ensure every flow theme inherits its definitions from the module's default theme. The module must follow this proposed [Theme structure](theme-structure-if.md).

### Cannot import module

Issue
:   There are no flows to import.

Possible cause
:   Module is empty.

Solution
:   Add flows to the module before importing it.

### Module doesn't have a default theme

Issue
:   The module's theme structure is invalid.

Possible cause
:   The module has no default theme.

Solution
:   Check the module structure and set a default theme. The module must follow this proposed [Theme structure](theme-structure-if.md).

### Invalid screens layout block

Issue
:   Invalid layout blocks used in some screens.

Possible cause
:   Some screens contain invalid layout blocks.

Solution
:   Use the provided Layout or LayoutBlank blocks to build all screens. Using the same layout block on all screens allows a better integration in the tool.

## Warnings

### All screens not reachable

Issue
:   Module contains screens that can't be reached.

Possible cause
:   Imported flows contain unused code. 

Solution
:   Review the screen connections.

### Not all flows have a theme

Issue
:    Quality of the CSS in the generated apps is reduced.

Possible cause
:   Some flows don't have a default theme.  

Solution
:   Consider using a default flow theme to host flow-specific classes.

### Module doesn't have a valid default theme

Issue
:   The module's theme structure is invalid.

Possible cause
:   The module's default theme is empty. 

Solution
:    Add content to the module stylesheet.

### Module is not self-contained

Issue
:   Missing references may cause runtime errors on published apps.

Possible cause
:   The module has unknown external dependencies.

Solution
:   Check if all dependencies are installed in the target environment to prevent runtime errors.
