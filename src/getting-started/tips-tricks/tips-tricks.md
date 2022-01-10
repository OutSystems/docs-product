---
summary: 
tags: 
---
# Service Studio Tips and Tricks

<pre class="script-css">
.mt-section h1 {
    border-bottom: solid #ddd 1px;
}
.mt-section {
    margin-bottom: 80px;
}
.mt-content-container img{
    margin-left: 2%;
    image-rendering: -moz-crisp-edges; /* Firefox */ 
    image-rendering:   -o-crisp-edges; /* Opera */ 
    image-rendering: -webkit-optimize-contrast; /* Webkit (non-standard naming) */ 
    image-rendering: crisp-edges; 
    -ms-interpolation-mode: nearest-neighbor; /* IE (non-standard property) */
}
.keyboard {
    font-size: 12px;
    color: #555;
    display: inline-block;
    padding: 0 8px;
    text-align: center;
    background-color: #eee;
    background-repeat: repeat-x;
    background-image: -webkit-gradient(linear, 0 0, 0 100%, from(#f5f5f5), to(#eee));
    background-image: -webkit-linear-gradient(#f5f5f5 0%, #eee 100%);
    background-image: -moz-linear-gradient(#f5f5f5 0%, #eee 100%);
    background-image: -o-linear-gradient(#f5f5f5 0%, #eee 100%);
    background-image: linear-gradient(#f5f5f5 0%, #eee 100%);
    border: 1px solid #ccc;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    -webkit-box-shadow: inset 0 1px 0 #fff, 0 1px 0 #ccc;
    box-shadow: inset 0 1px 0 #fff, 0 1px 0 #ccc 
}
.kbd {
    padding:0.1em 0.6em;
    border:1px solid #ccc;
    font-size:11px;
    font-family:Arial,Helvetica,sans-serif;
    background-color:#f7f7f7;
    color:#333;
    -moz-box-shadow:0 1px 0px rgba(0, 0, 0, 0.2),0 0 0 2px #ffffff inset;
    -webkit-box-shadow:0 1px 0px rgba(0, 0, 0, 0.2),0 0 0 2px #ffffff inset;
    box-shadow:0 1px 0px rgba(0, 0, 0, 0.2),0 0 0 2px #ffffff inset;
    -moz-border-radius:3px;
    -webkit-border-radius:3px;
    border-radius:3px;
    display:inline-block;
    margin:0 0.1em;
    text-shadow:0 1px 0 #fff;
    line-height:1.4;
    white-space:nowrap;
}
#title {
    max-width: 100%;
    height: auto;
    border-bottom: hidden !important;
}
.mouse {
  position: relative;
  box-sizing: border-box;
  margin: 0px 15px 0px 5px;
  top: -16px;
  display: inline-block;
  transform: scale(.35);
  -ms-transform: scale(.35);
  -moz-transform: scale(.35);
  -webkit-transform: scale(.35);
}
.butt{
  position: absolute;
  height: 30px;
  Width: 20px;
  border: 2px solid grey;
  box-sizing: border-box;
  background-color: grey;
  border-top-left-radius: 16px;
  -moz-border-top-left-radius: 16px;
  -webkit-border-top-left-radius: 16px;
}

.r.butt {
  transform: scaleX(-1);
  -ms-transform: scaleX(-1);
  -moz-transform: scaleX(-1);
  -webkit-transform: scaleX(-1);
  left: 21px;
}
.body {
  position: absolute;
  height: 71px;
  Width: 41px;
  border: 2px solid grey;
  border-radius: 20px 20px 25px 25px;
  -moz-border-radius: 20px 20px 25px 25px;
  -webkit-border-radius: 20px 20px 25px 25px; 
  box-sizing: border-box;
}
.c1, .c2, .c3{
  position: absolute;
  height: 8px;
  width: 3px;
  left: 8px;
  top: -14px;
  background-color: grey;
}
.c2 {
  transform: rotate(-45deg);
  -ms-transform: rotate(-45deg);
  -moz-transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg);
  left: -6px;
  top: -8px;
}
.c3 {
  transform: rotate(-90deg);
  -ms-transform: rotate(-90deg);
  -moz-transform: rotate(-90deg);
  -webkit-transform: rotate(-90deg);
  left: -12px;
  top: 6px;
}
td {
    background-color: transparent !important;
}
</pre>

<pre class="script-jem">
$("#title").html("&lt;img src='/@api/deki/files/13986/tt-banner.png'&gt;")
$(function() {
    $(".lclick").each(function(){
        $(this).html("&lt;div class='mouse'&gt; &lt;div class='l butt'&gt; &lt;div class='c1'&gt;&lt;/div&gt; &lt;div class='c2'&gt;&lt;/div&gt; &lt;div class='c3'&gt;&lt;/div&gt; &lt;/div&gt; &lt;div class='body'&gt;&lt;/div&gt; &lt;/div&gt;")
    });
    $(".rclick").each(function(){
        $(this).html("&lt;div class='mouse'&gt; &lt;div class='r butt'&gt; &lt;div class='c1'&gt;&lt;/div&gt; &lt;div class='c2'&gt;&lt;/div&gt; &lt;div class='c3'&gt;&lt;/div&gt; &lt;/div&gt; &lt;div class='body'&gt;&lt;/div&gt; &lt;/div&gt;")
    });
});
</pre>

# Basics

## Dark theme

You can switch Service Studio to the dark theme (or dark mode). On the **Edit** menu, chose **Preferences...** then, under **Theme** switch on **Dark theme**.

## Would you like to know more? Hit F1

You can always access relevant documentation and find more about any element/flow/tab by selecting it and pressing <span class="keyboard"> F1 </span> from within Service Studio.

## Keyboard shortcuts

You can consult the list of keyboard shortcuts in two ways:

* Use a shortcut for shortcuts: <span class="keyboard"> Cmd </span>+<span class="keyboard"> Shift </span>+<span class="keyboard"> K </span>

* Check [the shortcuts list](../../ref/lang/auto/shortcutkeys.md) in the documentation

[//]: # (* Print the shortcuts list)

## Open multiple files simultaneously

Whether you are opening files from your Environment or from a local source, you can always do it faster by selecting and opening them all at once in one of three different ways:

* Use <span class="keyboard"> Cmd </span>+<span class="lclick">Left-Click</span> to add the clicked file to your selection

* Use <span class="keyboard"> Shift </span>+<span class="lclick">Left-Click</span> to select all files between the last file you previously selected and the clicked file

* Use <span class="keyboard"> Cmd </span>+<span class="keyboard"> Shift </span>+<span class="lclick">Left-Click</span> to add to your previous selection all files from the last file you previously selected to the clicked file

## Edit the Properties of several elements in one go

Do you want to make every Screen of a Module accessible to anonymous users? Or maybe it's changing the Data Type of several Variables that you need? You'll be happy to know that you won't have to go through them one by one!

Start by selecting the elements for which you want to change the Properties and see where they share common values.

![](images/tt-bulk-edit-00.gif)

Then, you'll be able to see where their Properties differ and where they share common values. All you have to do now is adjust them according to your needs. Any change made within your current selection will be applied to all selected elements.

<<<<<<< HEAD
=======
## Closing and moving Modules

Do you have way too many Modules open? Quickly close any number of them by right-clicking a Module tab and selecting **Close**, **Close other modules**, **Close modules to the right**, or **Close all modules**.

![Close multiple modules](images/tt-close-modules-ss.gif)

If closing modules is not an option, you can rearrange them by clicking and dragging the module left or right in your list of open modules. Additionally, you can drag a module off the current Service Studio window which opens a new Service Studio window.

![Reorder modules](images/tt-reordertabs-ss.gif)
>>>>>>> master

## Open a Screen in browser

To open a Screen in a browser open the **Interface** tab, right-click that Screen and choose **Open in Browser**. There is no need to create additional Entry Points.

![](images/tt-open-in-browser-00.png)

## Expanding and collapsing trees

In any tree, you can collapse or expand all items and subitems by clicking <span class="keyboard"> Cmd </span>+<span class="lclick">Left-Click</span> in the arrow next to the item you want to expand or collapse. With just a few clicks, you can keep your development environment neat and tidy at all times.

![](images/tt-tree-02.png)

## Use the Widget Tree when designing UI

Are you having trouble placing a Widget exactly where you want it? Make your life easier by using the Widget Tree! 

With it you can confidently place or move widgets around through a hierarchical view of every widget present in a Screen or Block.
 
![](images/tt-widg-tree.gif)

The Widget Tree automatically appears whenever you drag a Widget to a Screen or Block, but you can also access it by clicking the **Widget Tree** button.

## Edit basic CSS properties with Styles Editor

No more CSS stress! Use **Styles Editor** to edit basic visual properties of widgets with the aid of a visual interface. Leave all complexity behind and use it in one of two ways:

* Select a widget and click the **Styles Editor** toggle button in the **Properties Pane**

    ![](images/tt-styles-editor-00.gif)

* Use it directly in the **Style Sheet Editor**

    ![](images/tt-styles-editor-01.png)

# Boost Performance

## Easily create Entity Diagrams

Select the target Entities and then either drag them to an open Entity Diagram canvas or right-click and select **Add to New Entity Diagram**.

![](images/tt-ent-diagram-00.gif)

When added, the **Entity Diagram** is automatically arranged. However, if an Entity is already present in the target diagram, it will not be added again.

## Guess my Attribute/Variable Data Type

Speed up your Entity/Structure creation by helping Service Studio automatically choose the correct Data Type of each Attribute or Variable. 

Name your Attribute/Variable according to the following rules and Service Studio will set the Data Type for you.

Attribute/Variable%%Data Type | Attribute/Variable%%Name | Example
---|---|---
Integer|`x`, `y`, `z`, `*Count`, `*Number`| `HeadCount`, `Number`
Date|`*Date`|`BirthDate`
DateTime|`*DateTime`, `*On`, `*Instant`|`ExitDateTime`, `CreatedOn`, `LogInstant`
Time|`*Time`|`ExitTime`
Boolean|`Is*`, `Has*`| `IsCompleted`, `HasDocument`
Email|`*Email`|`UserEmail`
PhoneNumber|`*Phone`, `*Mobile`|`HomePhone`, `WorkMobile`
Currency|`*Price`, `*Amount`|`Price`, `DollarAmount`
User Identifier|`*By`|`CreatedBy`
Entity Identifier|`<Entity>Id`|`CustomerId`
Entity Record|`<Entity>`|`Customer`
Entity Record List|`<Entity>s`,`<Entity>es`,`<Entity>ies`|`Customers`

## Quickly add a dependency in any module

Cut the search time to a minimum and quickly add dependencies by searching across all modules with no need to go through **Manage Dependencies** to check one by one.

![](images/tt-search-add-other-modules.gif)

Use <span class="keyboard"> Cmd </span>+<span class="keyboard"> F </span> to search for the desired element in the **Search** bar.

Click **Search in other Modules** in the dropdown menu to open a window that'll list all elements that match your search query across every module of the environment.

Just select the element you're looking for and click **Add Dependency**.

## Make sure you Remove Unused Dependencies

Having more dependencies increases the size of your Module and increases the duration of 1-Click Publish. 

Through the **Remove Unused Dependencies**, Service Studio will automatically remove from a Module all unnecessary dependencies.

![](images/tt-unused.gif)

# Create new elements

## Create an Aggregate from an Entity

Drag an Entity to an Action Flow to create an aggregate.

![](images/tt-drag-agg-unf-04.gif)

If you set the `Is Active Attribute` of the Entity - choose **More...** in the Entity properties, then expand **More options** - the new Aggregate is created with the filter `<Entity>.<Is Active Attribute> = True`. Otherwise, the new aggregate is created without filters.

![](images/tt-drag-agg-unf-05.png?width=500)

## Create a Button from an Action

Drag an Action and drop it to the Screen. This creates a Button and a binding to the Action.

![Demo of creating a Button from an Action](images/tt-create-button-from-action.gif?width=500) 

## Create a filtered Aggregate from an Identifier

Drag a Variable of the Identifier data type to an Action Flow to create an Aggregate filtered by that variable.

![](images/tt-drag-agg-filt.gif)

## Create an If from a Boolean

Drag a Boolean Variable to a Flow to create an If condition.

![](images/tt-drag-bool-if-03.gif)

## Create an Assignment from a Variable

In a Flow, drag a Variable to an Assign element to create an `Assignment` for that Variable.
 
![](images/tt-drag-assign-00.gif)

# Reuse elements

## Reuse logic with Extract to Action 

When you want to Extract the logic inside an Action to a different one, you can select the target flow elements, right-click and choose **Extract to Action** to create a new Action with that logic.

![](images/tt-conv-extract-04.gif)

A new action will be created with the selected logic and with all the necessary Input and Output Parameters.

# Convert Elements

## Convert Variables

You can easily change the type of a Variable. Right-click the target Variable and select **Convert to Local Variable/Input Parameter/Output Parameter**. 

![](images/tt-conv-var-00.png)

Keep in mind that not all Actions may use Output Parameters.

## Convert a Text Widget to an Expression Widget
 
Right-click the target Text Widget and select **Convert to Expression**.
    
![](images/tt-conv-text-exp-03.png)

The original text from the Text widget will be automatically included as the example of the new Expression widget.

## Convert Entities/Static Entities

Just right-click the target Entity/Static Entity and under **Advanced** select **Convert to Static Entity/Entity**.

![](images/tt-conv-ent-staent-00.png)

## Convert an Entity to a Structure 

Converting an Entity to a Structure is as easy as opening  the Data tab and dragging the target Entity to the Structure Folder.

![](images/tt-conv-str-ent-04.gif)

## Swap If Connectors

When you need to change a True branch to a False branch or a False branch to a True branch, right-click the target If and select **Swap Connectors** to swap the True/False condition branches.

![](images/tt-conv-if-02.png?width=600)
