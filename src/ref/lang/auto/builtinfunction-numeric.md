---
locale: en-us
guid: aace68aa-c3bc-4e37-85f1-ad8b6f204bf7
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Numeric

| Name | Description |
|---|---|
| [Max](#Max)(​Decimal, Decimal) | Returns the largest number of 'n' and 'm'. |
| [Min](#Min)(​Decimal, Decimal) | Returns the smallest number of 'n' and 'm'. |
| [Sign](#Sign)(​Decimal) | Returns -1 if 'n' is negative; 1 if 'n' is positive; 0 if 'n' is 0. |

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

