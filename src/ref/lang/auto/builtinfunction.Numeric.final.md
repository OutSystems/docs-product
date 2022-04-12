---
locale: en-us
guid: aace68aa-c3bc-4e37-85f1-ad8b6f204bf7
---

# Numeric


<table markdown="1">
<thead>
<tr>
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="#Max">Max</a>(&#8203;Decimal, Decimal)</td>
<td>Returns the largest number of 'n' and 'm'.</td>
</tr>
<tr>
<td><a href="#Min">Min</a>(&#8203;Decimal, Decimal)</td>
<td>Returns the smallest number of 'n' and 'm'.</td>
</tr>
<tr>
<td><a href="#Sign">Sign</a>(&#8203;Decimal)</td>
<td>Returns -1 if 'n' is negative; 1 if 'n' is positive; 0 if 'n' is 0.</td>
</tr>
</tbody>
</table>

## Max { #Max }

Returns the largest number of 'n' and 'm'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  


m
:    Type: Decimal. Mandatory.  


### Output

Type: Decimal  

### Examples

```
Max(-10.89, -2.3) = -2.3
Max(10.89, 2.3) = 10.89
```

## Min { #Min }

Returns the smallest number of 'n' and 'm'.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  


m
:    Type: Decimal. Mandatory.  


### Output

Type: Decimal  

### Examples

```
Min(-10.89, -2.3) = -10.89
Min(10.89, 2.3) = 2.3
```

## Sign { #Sign }

Returns -1 if 'n' is negative; 1 if 'n' is positive; 0 if 'n' is 0.  

Available in:  

  * Server-side logic: Yes
  * Client-side logic: Yes
  * Database: Function is evaluated before the aggregate is executed.
  * Local Storage: Function is evaluated before the aggregate is executed.

### Parameters

n
:    Type: Decimal. Mandatory.  
The number from which to calculate the sign value.

### Output

Type: Integer  

### Examples

```
Sign(-10.89) = -1
Sign(2.3) = 1
Sign(0.0) = 0
```

