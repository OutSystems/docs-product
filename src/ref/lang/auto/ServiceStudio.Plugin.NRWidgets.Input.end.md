## Additional Notes

### Rendering Empty Values

If a variable associated with an Input widget doesn't have a defined value, the widget will be rendered by default with no content. 

If you would like to show the default value for the associated variable type (e.g. show "0" in the widget for a variable of type Integer) when there's no defined value for the variable, add the following custom attribute to the widget in the properties editor:

* Property: **show-default-value**  
    Value: **true**
