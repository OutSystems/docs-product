---
kinds: ServiceStudio.Model.Variables+ClientVariable+Kind
helpids: 30206
---

# Client Variable

Holds data that is persisted client-side and can be used to save information during the end user interaction.  

Create a Client Variables in Data tab

Client Variables shall be bound to a widget to allow changing its value, for example, an input widget (set the input Variable as Client.MovieSearchKeyword, for example)

When the input value is changed by the user, its value is stored in the browser's cache with the name of the Client Variable (Client.MovieSearchKeyword, for example)

Later, if the user didn't close the session, when the user comes back to the page/session, the Client Variable is restored.

If the Client Variable is used in an aggregate filter, lets say an aggregate called GetMovies that fetches Movies from an Entity Movie, the filter 
Movie.Title like "%" +Client.MovieSearchKeyword+ "%" will search only the Titles accordingly to the query shown and retrieved from the browser's cache. 

## Properties

<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
<th>Mandatory</th>
<th>Default value</th>
<th>Observations</th>
</tr>
</thead>
<tbody>
<tr>
<td title="Name">Name</td>
<td>Identifies an element in the scope where it is defined, like a screen, action, or module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element.</td>
<td></td>
<td></td>
<td>Useful for documentation purpose.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>The variable data type.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td>The default value of a session variable must be a literal.</td>
</tr>
</tbody>
</table>

