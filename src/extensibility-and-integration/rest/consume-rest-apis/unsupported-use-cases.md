---
summary: Use cases currently unsupported when consuming REST services using "enums" and how to overcome some of these situations.
---

# Unsupported REST Enum Use Cases

Service Studio can import "enum" (enumerate) elements when consuming REST services. Service Studio represents these elements as Static Entities and each value of the "enum" corresponds to a Static Entity Record.

Importing a REST API in Service Studio can create parameters/properties with Text data type instead of the "enum" defined in the Swagger specification file describing the REST API.

Sometimes you can do some small changes to the specification file so that the identified limitations no longer apply, and you can effectively consume the REST API in OutSystems.

The current list of unsupported use cases is the following:

* ["Enums" or array of "enums" with a type other than Integer or Text](#enum-types)
* [Input Parameter specified by reference](#input-by-reference)
* [Output Parameter specified in header](#output-in-header)
* [Variable type using the oneOf keyword](#oneof)

In general, OutSystems supports "enums" in consumed REST services when they're defined inside a "schema" field or referenced using "$ref"; otherwise, they're not currently supported in OutSystems.

In the following sections you can find instructions on adjusting the Swagger specification file to work around some currently unsupported use cases.

## Enums or array of enums with a type other than Integer or Text { #enum-types }

OutSystems defines the type of an input parameter, output parameter or structure attribute based on the type defined in the "schema" field or referenced using a "$ref" field. The platform creates a Static Entity and references it correctly as the parameter type.

In OutSystems, identifiers can't have a complex type (or array element type) as data type. You can only define their data type as Integer, Long Integer, or Text. Service Studio shows you an error when there's an enum (or array of enums) in the API specification with a type other than the supported ones.

Examples of the unsupported use case:

```javascript
"parameters": [
    {
        "name": "RegionId",
        "in": "body",
        "schema": {
            "$ref": "#/definitions/Region"
        }
    }
],

"definitions": {
    "Region": {
        "description": "",
        "type": "number",
        "enum": [
            56411.0,
            23221.0,
            11222.0,
            45596.0
        ]
    }
}
```

```javascript
"responses": {
    "200": {
        "description": "Successful request",
        "schema": {
            "type": "string",
            "format": "date-time",
            "enum": [
                "2018-03-22T09:12:28Z",
                "2018-07-23T11:16:00Z",
                "2018-10-24T17:22:05Z"
            ]
        }
    }
}
```

```javascript
"responses": {
    "200": {
        "description": "Successful request",
        "schema": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Region"
            }
        }
    }
}

"definitions": {
    "Region": {
        "type": "string",
        "format": "date-time",
        "enum": [
            "2018-03-22T09:12:28Z",
            "2018-03-23T09:12:28Z",
            "2018-03-24T09:12:28Z"
        ]
    }
}
```

### Use case workaround

Change the type of the "enum" to Text since this is the type that accepts all the other allowed types. Note that you may need to explicitly convert these values back to their original type, since the OutSystems platform interprets them as Text.  
On the other hand, the consuming REST API expects these input parameters to contain integers or numbers. You need to [customize the request using an "OnBeforeRequest" callback](simple-customizations.md). Additionally, consider any default values when defining the logic that customizes the request/response.

## Input Parameter specified by reference { #input-by-reference }

Input parameters defined in the "parameters" section or referenced using a "$ref" field are created with the type defined in the "type" field and the Static Entity will not be created. When defined in body, Service Studio throws an exception.

Examples of the unsupported use case:

```javascript
"parameters": [
    {
        "$ref": "#/parameters/RegionId"
    }
]

"parameters": {
    "RegionId": {
        "name": "RegionId",
        "in": "body",
        "schema": {
            "type": "integer",
            "format": "int32",
            "enum": [
                56411,
                23221,
                11222,
                45596
            ]
        }
    }
}
```

```javascript
"parameters": [
    {
        "$ref": "#/parameters/RegionId"
    }
]

"parameters": {
    "RegionId": {
        "name": "RegionId",
        "in": "query",
        "type": "integer",
        "format": "int32",
        "enum": [
            56411,
            23221,
            11222,
            45596
        ]
    }
}
```

### Use case workaround

Define the parameter in place instead of referencing it.

## Output Parameter specified in header { #output-in-header }

Output parameters defined in a "headers" section are created with the type defined in the "type" field and the Static Entity will not be created.

Examples of the unsupported use case:

```javascript
"responses": {
    "200": {
        "description": "Successful request",
        "headers": {
            "RegionId": {
                "type": "integer",
                "format": "int64",
                "enum": [
                    56411,
                    23221,
                    11222,
                    45596
                ]
            }
        }
    }
}
```

```javascript
"responses": {
    "200": {
        "$ref": "#/responses/DefaultSuccessResponse"
    }
}

"responses": {
    "DefaultSuccessResponse": {
        "description": "Successful request",
        "headers": {
            "RegionId": {
                "type": "integer",
                "format": "int32",
                "enum": [
                    56411,
                    23221,
                    11222,
                    45596
                ]
            }
        }
    }
}
```

### Use case workaround

Currently there is no generic workaround to overcome this unsupported use case.

## Variable type using the oneOf keyword { #oneof }

Having elements of a specification whose definition allows for more than one type using the `oneOf` keyword is currently not supported. In this case, OutSystems determines a specific type for the element according to the following rules:

* If the `oneOf` definition has only one Object (complex type) entry, OutSystems selects that Object for the type.
* If there are multiple or no Objects, OutSystems searches for a `string` entry. If it finds one or more entries, OutSystems uses the first found `string` entry for the type.
* If none of the above rules applies, OutSystems uses the first entry of the `oneOf` definition for the type.

The type is automatically set according to the rules above. However, you can change the type later, after importing the REST service.

### Use case workaround

Besides customizing the type defined automatically by the platform when importing the service, there is no generic workaround to overcome this unsupported use case.
