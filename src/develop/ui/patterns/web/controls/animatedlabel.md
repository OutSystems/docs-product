---
tags: runtime-traditionalweb; 
summary: The Animated Label animates a label when there is user input.
---

# Animated Label

You can use the Animated Label UI Pattern to animate a label when there is a user input.

 ![](<images/animatedlabel-10-ss.png>)

**How to use the Animated Label UI Pattern**

1. In Service Studio, in the Toolbox, search for `Animated Label`.

    The Animated Label widget is displayed.

    ![](<images/animatedlabel-7-ss.png>)

1. From the Toolbox, drag the Animated Label widget into the Main Content area of your application's screen.

    ![](<images/animatedlabel-8-ss.png>)

    By default, the Animated Label widget contains Label and Input placeholders.

1. Enter the relevant text in the Label placeholder. In this example, we enter `Name`.

   ![](<images/animatedlabel-9-ss.png>)

1. Create a new local variable for the Input widget by selecting the Input widget and on the **Properties** tab, and from the **Variable** drop-down, and select **New Local Variable**. 
    
    ![](<images/animatedlabel-1-ss.png>)

1. Enter a name for the new local variable. In this example, we enter `UserInput`.
    
    ![](<images/animatedlabel-2-ss.png>)

1. On the **Properties** tab, you can change the look and feel of the Animated Label by setting the (optional) properties.

    ![](<images/animatedlabel-3-ss.png>)

After following these steps and publishing the module, you can test the pattern in your app. 
    
## Properties

| **Property** |  **Description** |  
|---|---|
| IsInline (Boolean): Optional |  If False, the the Animated Input is displayed in a white input box. If True, there is no white input box. This is the default. | 
| ExtendedClass (Text): Optional  |  Add custom style classes to the Animated Label UI Pattern. You define your [custom style classes](../../../../../../develop/ui/look-feel/css.md) in your application using CSS.<br/><br/>Examples<br/><br/> <ul><li>_Blank_ - No custom styles are added (default value).</li><li>_"myclass"_ - Adds the _myclass_ style to the Animated Label UI styles being applied.</li><li>_"myclass1" "myclass2"_ - Adds the _myclass1_ and _myclass2_ styles to the Animated Label UI styles being applied.</li></ul> |