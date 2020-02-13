# Grid Dimensions Overflow Warning

Message
:   `The sum of the 'Width' and 'Margin Left' properties of the widget must be set within the grid boundaries`

Cause
:   The widget has its Width and Margin Left properties set using 'col' and the sum of the two is exceeding the number of columns defined in the theme's grid.

Recommendation
:   Change Width or Margin Left properties of the element so that they fit within the grid, or change the Grid property of the Theme to increase the number of columns of the grid.
