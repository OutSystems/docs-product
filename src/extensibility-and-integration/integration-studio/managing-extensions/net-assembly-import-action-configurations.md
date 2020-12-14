# Supported Configurations for Import Actions from .NET Assembly

The following table lists supported configurations and limitations for the **Import Actions from .NET Assembly** wizard in the current Integration Studio version.

For the supported assembly versions please check the [System Requirements](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/OutSystems_Platform_system_requirements>).  
  
<table markdown="1">  
<tr>
<th colspan="2">
Import Actions from .NET Assembly
</th>
</tr>
<tr>
<td>
**Imported Elements**
</td>
<td>
– Non-Abstract Public Methods (Static or Instance)<br/>
– Non-Abstract Public Properties (Static or Instance)<br/>
– Public Fields (Static or Instance)<br/>
– Public Instance Constructors<br/>
– Web Service Methods
</td>
</tr>
<tr>
<td>
**Limitations**
</td>
<td>
– Can't import Index Properties<br/>
– Can't import Delegate Types<br/>
– Can't import Structures<br/>
– Can't import Enumerations<br/>
– Can't import Generic Methods (although Generic Types are supported in its parameters and return value)<br/>
– Members of Generic Classes and of their inner classes aren't imported<br/>
– Only static Members of Abstract Classes can be imported
</td></tr></table>
