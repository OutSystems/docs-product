# Supported Configurations for Import Actions from .Net Assembly

The following table lists supported configurations and limitations for the "Import Actions from .Net Assembly" wizard in the current Integration Studio version.

For the supported assembly versions please check the [System Requirements](<https://success.outsystems.com/Support/Enterprise_Customers/Installation/OutSystems_Platform_system_requirements>).  
  
<table markdown="1">  
<tr>
<th colspan="2">
Import Actions from .Net Assembly
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
– Cannot import Index Properties<br/>
– Cannot import Delegate Types<br/>
– Cannot import Structures<br/>
– Cannot import Enumerations<br/>
– Cannot import Generic Methods (although Generic Types are supported in its parameters and return value)<br/>
– Members of Generic Classes and of their inner classes are not imported<br/>
– Only static Members of Abstract Classes can be imported
</td></tr></table>
