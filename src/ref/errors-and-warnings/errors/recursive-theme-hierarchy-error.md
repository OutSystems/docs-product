# Recursive Theme Hierarchy Error

The `Recursive Theme Hierarchy`error is issued in the following situation:

* `Your module has a circular dependency between themes`

    A typical scenario is when your module has two themes. The first theme uses the second as its Base theme, and the second uses the first as its Base theme, thus creating a circular reference in their definitions.

    Change one of the themes to stop using the other as its Base theme.
