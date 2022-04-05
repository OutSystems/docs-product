---
summary: Check the list of currently unsupported use cases when consuming SOAP 1.2 Web Services and how to overcome some of these situations.
---

# Unsupported SOAP Use Cases

While importing a SOAP Web Service in **Service Studio**, you get immediate feedback on any currently unsupported feature/use case identified by the development environment.

In this case, you can't import the Web Service immediately using **Service Studio**. Sometimes you can perform small changes in the WSDL describing the service so that the identified limitations no longer apply, and you can consume the Web Service in **OutSystems**.

The current list of unsupported features/use cases is the following:

* [Multidimensional arrays](<#multidimensional-arrays>)
* [Abstract types without implementation](#abstract-types-without-implementation)
* [Recursion](<#recursion>)
* [List attribute in a single list attribute](<#list-attribute-in-a-single-list-attribute>)
* Wildcards:
    * [Any inside Choices](<#wildcards-any-inside-choices>)
    * [Any attribute](<#wildcards-any-attribute>)
* Any types:
    * [AnyType](<#any-types-anytype>)
    * [No specified type](<#any-types-no-specified-type>)
    * [AnySimpleType and AnyAtomicType](<#any-types-anysimpletype-and-anyatomictype>)
* [Attribute Groups](<#attribute-groups>)
* [SOAP Action names with special characters](#special-characters)
* [Repeated SOAP structure attribute names](#repeated-attribute-names)
* [Attributes in the same SOAP structure named "&lt;attrib&gt;" and "&lt;attrib&gt;Field"](#attributes-field)
* [RPC-style Web Services with the same 'name' property in message 'part' elements](#rpc-message-part)

<div class="info" markdown="1">

**Service Studio** and the **OutSystems** platform are being **continuously improved** to support more SOAP 1.2 features and use cases and to have less unsupported scenarios that require WSDL adjustments.  
Be sure to visit this page regularly for an updated list of the current limitations.

</div>

In the following sections you can find general instructions to perform the necessary WSDL changes for working around some currently unsupported features/use cases.

To implement a workaround for an unsupported use case begin with the procedure in [Exporting SOAP definition files](#exporting).


## Multidimensional arrays

Although SOAP arrays are generally supported, the particular case of multidimensional arrays isn't currently supported in OutSystems.

Examples:

```xml
<xsd:complexType name="SummaryResultArray">
    <xsd:complexContent>
        <xsd:restriction base="soapenc:Array">
            <xsd:attribute ref="soapenc:arrayType" wsdl:arrayType="typens:SummaryResult[][]"/>
        </xsd:restriction>
    </xsd:complexContent>
</xsd:complexType>
```

```xml
<xsd:complexType name="SummaryResultArray2">
    <xsd:complexContent>
        <xsd:restriction base="soapenc:Array">
            <xsd:attribute ref="soapenc:arrayType" wsdl:arrayType="typens:SummaryResult[,]"/>
        </xsd:restriction>
    </xsd:complexContent>
</xsd:complexType>
```

```xml
<xsd:complexType name="SummaryResultArray3">
    <xsd:complexContent>
        <xsd:restriction base="soapenc:Array">
            <xsd:attribute ref="soapenc:arrayType" wsdl:arrayType="typens:SummaryResult[10,2]"/>
        </xsd:restriction>
    </xsd:complexContent>
</xsd:complexType>
```

### Use case workaround

Currently there is no generic workaround available to overcome this unsupported use case.

## Abstract types without implementation

WSDL files or included schemas might include abstract types. This means that, to actually use them, you must use a derived (non-abstract) type. When there is no non-abstract type derived from it, you can't use it.

In the following example `AbstractContract` is declared as abstract. If it's used as the type of an element but no type extends from it, this causes an error.

```xml
<xsd:complexType name="AbstractContract" abstract="true">
    <xsd:sequence>
        <xsd:element minOccurs="1" name="ContractNr" type="xsd:string" />
        <xsd:element minOccurs="1" name="StartDate" nillable="true" type="xsd:dateTime" />
        <xsd:element minOccurs="0" name="EndDate" nillable="true" type="xsd:dateTime" />
        <xsd:element minOccurs="2" maxOccurs="unbounded" name="Parties" type="tns:Party" />
    </xsd:sequence>
</xsd:complexType>
```

### Use case workaround

There are two possible workarounds, according to your specific scenario:

* If you need to **send or receive** the element (or attribute) that has the abstract type, you can try to remove the abstract indication from the type declaration.

* If you don't use the abstract type and every occurrence refers to it as optional (for example, with `minOccurs="0"`), you can remove the usage of that type and the type itself from the service definition.

## Recursion

Recursive data types are structures that reference themselves. Inside them there is a reference to another element of its own type.

This reference can be direct or indirect. For example, type **A** has an attribute of type **B** which references **C** which in turn contains an element of type **A**.

Check the following recursion example:

```xml
<xsd:complexType name="Person">
    <xsd:sequence>
        <xsd:element name="Firstname" type="xsd:string"/>
        <xsd:element name="Lastname" type="xsd:string"/>
        <xsd:element name="PhoneNumber" type="xsd:int"/>
        <xsd:element name="Address" type="s0:Address"/>
        <xsd:element name="Contacts" minOccurs="0" maxOccurs="unbounded" type="s0:Person">
    </xsd:sequence>
</xsd:complexType>
```

### Use case workaround

Follow these generic guidelines to adapt the WSDL so that the unsupported use case is no longer identified by the platform:

* "Unroll" the recursive structures up to the level you need to send or receive.  
Following the  example above, if you needed to handle two levels of recursion you would:

    1. Change type of `Contacts` in the `Person` type to be of type `s0:Person2`.
    1. Create a copy of the `Person` definition, renaming it to `Person2`.
    1. Remove the `Contacts` element from `Person2` definition.

## List attribute in a single list attribute

This use case occurs when there's a `complexType` with a single element with `maxOccurs` > 1 and that type is used as an element inside another type with `maxOccurs` > 1.

Example:

```xml
<xsd:complexType name="Organization">
    <xsd:sequence>
        <xsd:element name="Integration_ID" type="tns:External_Integration_ID" minOccurs="0" maxOccurs="unbounded" />
        <xsd:element minOccurs="0" maxOccurs="1" name="Name" type="xsd:string" />
    </xsd:sequence>
</xsd:complexType>

<xsd:complexType name="External_Integration_ID">
    <xsd:sequence>
        <xsd:element name="ID" type="tns:IDType" maxOccurs="unbounded" />
    </xsd:sequence>
</xsd:complexType>
```

In this example, the `Integration_ID` element in `Organization` is not supported, because it has `External_Integration_ID` type — composed of a single element with `maxOccurs` > 1 — and is itself a list.

### Use case workaround

Add a dummy optional element (for example, using `minOccurs="0"`) in the type containing the single list element.

Following the previous example, you would add the following element inside the `<xsd:sequence>` element belonging to `External_Integration_ID`:

```xml
<xsd:element name="dummy" type="xsd:string" minOccurs="0" />
```

## Wildcards - any inside choices

You can use the `xsd:any` construct to specify that an arbitrary element (optionally from certain namespaces) can be present in a type.  
Although this feature is generally supported in the platform, there is a specific situation that's not supported yet, when the `xsd:any` element is inside a Choice definition. In this case, Service Studio doesn't import the structure.

Example:

```xml
<xsd:element name="RelatedPerson">
    <xsd:complexType>
        <xsd:choice minOccurs="0" maxOccurs="unbounded">
            <xsd:element name="Employee" type="s0:Employee"/>
            <xsd:element name="Customer" type="s0:Customer"/>
            <xsd:any namespace="##other"/>
        </xsd:choice>
    </xsd:complexType>
</xsd:element>
```

### Use case workaround

Currently there is no generic workaround available to overcome this unsupported use case.

Although it's possible to modify the WSDL by moving the `xsd:any` element outside the Choice definition and making it optional (for example, adding a `minOccurs="0"` attribute), the obtained result isn't strictly equal to the original definition.  
Additionally, you should only perform this change for types included in requests.

## Wildcards - any attribute

You can use the `xsd:anyAttribute` construct to specify that an arbitrary attribute, optionally from certain namespaces, can be present in a type.

Example:

```xml
<xsd:complexType name="LocationWithMetadata">
    <xsd:sequence>
        <xsd:element minOccurs="1" maxOccurs="1" name="name" type="xsd:string" />
        <xsd:element minOccurs="1" maxOccurs="1" name="coordinates" type="tns:CoordsGPS" />
    </xsd:sequence>
    <xsd:anyAttribute namespace="##targetNamespace"/>
</xsd:complexType>
```

### Use case workaround

If the type that contains `xsd:anyAttribute` is being sent in a request and you know what attribute you need to send, you can replace `anyAttribute` with it.  
Otherwise, there is no generic workaround available to overcome the unsupported use case.

## Any types - AnyType

Every element present in a SOAP service definition has a type. In some special cases that type might be `xsd:anyType`. This is a special type: it's the most generic possible type and all other types derive from it. Having it in a element means that the element can have any possible type.

Example:

```xml
<xsd:complexType name="GenericInformation">
    <xsd:sequence>
        <xsd:element minOccurs="1" name="Name" type="xsd:string" />
        <xsd:element minOccurs="1" name="Type" type="tns:InformationKind" />
        <xsd:element minOccurs="1" name="IsActive" type="xsd:boolean" />
        <xsd:element name="SpecificInfo" type="xsd:anyType" />
    </xsd:sequence>
</xsd:complexType>
```

### Use case workaround

Currently there is no generic workaround available to overcome this unsupported use case.

## Any types - no specified type

An element with a `name` attribute and no `type` attribute is treated by default as `anyType` as above.

Example:

```xml
<xsd:complexType name="GenericInformation">
    <xsd:sequence>
        <xsd:element minOccurs="1" name="Name" type="xsd:string" />
        <xsd:element minOccurs="1" name="Type" type="tns:InformationKind" />
        <xsd:element minOccurs="1" name="IsActive" type="xsd:boolean" />
        <xsd:element minOccurs="1" name="SpecificInfo" /> 
    </xsd:sequence>
</xsd:complexType>
```

### Use case workaround

If the element actually represents a property of a simple type then it can always be represented as a string. In this case a possible workaround is to add a `type="xsd:string"` attribute to the element before importing. 
If the element can represent complex types then there is no generic workaround.

## Any types - AnySimpleType and AnyAtomicType

The `xsd:anySimpleType` and `xsd:anyAtomicType` types represent all simple (not composed) types. You can use them in a declaration as a placeholder. At runtime the placeholder is replaced with a value of a specific type.

Example:

```xml
<xsd:complexType name="ThirdParty">
    <xsd:attribute name="partyId" type="xsd:string" use="required"/>
    <xsd:attribute name="name" type="xsd:string" use="required"/>
    <xsd:attribute name="description" type="xsd:string"/>
    <xsd:attribute name="tags" type="xsd:anySimpleType"/>
    <xsd:attribute name="classifier" type="xsd:anyAtomicType"/>
</xsd:complexType>
```

_Notes:_  
— The `xsd:anyAtomicType` type doesn't include types defined as unions (`xsd:union`) or lists (`xsd:list`) of other types.  
— The Windows Communication Foundation (WCF) framework maps the `AnySimpleType` and `AnyAtomicType` types as strings.

### Use case workaround

Since you can use strings to represent all possible values of the above types, a possible workaround is to change the element type to the built-in string type.

## Attribute groups

`attributeGroup` elements group a set of attribute declarations that you can later incorporate as a group in complex type definitions.

Example:

```xml
 <xsd:complexType name="PersonInfo">
    <xsd:sequence>
        <xsd:element name="Forename" type="xsd:string"/>
        <xsd:element name="Surname" type="xsd:string"/>
        <xsd:element name="Dob" type="xsd:date"/>
   </xsd:sequence>
   <xsd:attributeGroup ref="ms:DateOfBirthGroup"/>
</xsd:complexType>

<xsd:attributeGroup name="DateOfBirthGroup">
    <xsd:attribute name="Day" type="xsd:string"/>
    <xsd:attribute name="Month" type="xsd:string"/>
    <xsd:attribute name="Year" type="xsd:integer"/>
</xsd:attributeGroup>
```

### Use case workaround

Since an attribute group is just a container of attributes that you can reference in complex types, a possible solution is to put all the attributes from the attribute group directly in the complex types that use it.

## SOAP Action names with special characters { #special-characters }

It's not currently possible to create Actions from some operations defined in a WSDL that contain special characters like "-".

In the example below, the `GetExtrasAndAdd-Ons` operation is not supported and Service Studio doesn't import it.

```xml
<wsdl:portType name="AccountInformationSoap">
    <wsdl:operation name="GetExtrasAndAdd-Ons">
        <wsdl:input message="tns:MethodGetExtrasSoapIn"/>
        <wsdl:output message="tns:MethodGetExtrasSoapOut"/>
    </wsdl:operation>
</wsdl:portType>
<wsdl:binding name="AccountInformationSoap" type="tns:AccountInformationSoap">
    <soap:binding transport="http://schemas.xmlsoap.org/soap/http"/>
    <wsdl:operation name="GetExtrasAndAdd-Ons">
        <soap:operation soapAction="http://example.com/AccountInformation/GetExtrasAndAddOns" style="document"/>
        <wsdl:input>
            <soap:body use="literal"/>
        </wsdl:input>
        <wsdl:output>
            <soap:body use="literal"/>
        </wsdl:output>
    </wsdl:operation>
</wsdl:binding>
```

### Use case workaround

None, for the operations whose name contains special characters.  
To import other operations from a WSDL, save the WSDL locally and edit it to remove any operations that cause this issue.

## Repeated SOAP structure attribute names { #repeated-attribute-names }

A SOAP structure can have more than one element with the same name in non-consecutive positions (lists), although this is a rare case.

Consider the following example, where the `AccountInformationType` type contains two attributes named `BranchId`.

```xml
<xsd:complexType name="AccountInformationType">
    <xsd:sequence>
        <xsd:element name="FirstName" type="xsd:string"/>
        <xsd:element name="LastName" type="xsd:string"/>
        <xsd:element name="BranchId" type="xsd:string"/>
        <xsd:element name="Email" type="xsd:string"/>
        <xsd:element name="Phone" type="xsd:string"/>
        <xsd:element name="BranchId" type="tns:BranchId"/>
    </xsd:sequence>
</xsd:complexType>
```

### Use case workaround

If you only need to send or receive one of the elements with the repeated name, edit the type definition in a local copy of the WSDL and delete the other occurrences.

## Attributes in the same SOAP structure named "&lt;attrib&gt;" and "&lt;attrib&gt;Field" { #attributes-field }

It's not currently possible to have two attributes in the same SOAP structure that have the same name except for a "Field" suffix (case sensitive).

Consider the following example, where the `ExampleType` type contains two attributes, one named `order` and another named `orderField`.

```xml
<xsd:complexType name="ExampleType">
    <xsd:sequence>
        <xsd:element name="order" type="xsd:string"/>
        <xsd:element name="orderField" type="xsd:string"/>
    </xsd:sequence>
</xsd:complexType>
```

### Use case workaround

Edit the type definition in a local copy of the WSDL and change the name of the `<attrib>Field` attribute.

## RPC-style Web Services with the same 'name' property in message 'part' elements { #rpc-message-part }

Web Services defined in Remote Procedure Call (RPC) style are services where the WSDL representation of messages exchanged for an operation contains parameters as if it were a remote procedure call.

Due to Windows Communication Foundation (WCF) limitations, OutSystems doesn't support RPC-style Web Services that use the following pattern in their `message` definitions: parts with the same `name` property, but with distinct types.

Example:

```xml
<message name="loginIn">
    <part name="request" type="tns:LoginReq"/>
</message>
<message name="logoutIn">
    <part name="request" type="tns:LogoutReq"/>
</message>
```

In the example above, the `loginIn` and `logoutIn` messages both define a part named `request` with distinct types: `tns:LoginReq` and `tns:LogoutReq`, respectively.

### Use case workaround

Currently there is no generic workaround available to overcome this unsupported use case.

## Exporting SOAP definition files  { #exporting }

To implement a workaround first use the **Export Definition Files** feature of **Service Studio** to download the definition files to a local drive so that all relevant files can be easily opened and edited by following the procedure in [Exporting definition files](https://success.outsystems.com/Documentation/11/Extensibility_and_Integration/SOAP/Consuming_SOAP_Web_Services/Export_definition_files_in_a_SOAP_web_service#Exporting_definition_files).

<div class="info" markdown="1">
During the export process the schema location is automatically changed to the relative path on the local drive. There is no need to manually change the schema location attribute in the definition files.
</div>

When the definition files have been exported continue as follows:

1. Modify definition files according to the workaround.
1. Save the file or files and return to **Service Studio**.
1. Delete the old SOAP web service. 
1. Right-click SOAP in the Logic tab, and select **Consume SOAP Web Service…** 
1. Click **Upload file**, navigate to where you saved the exported definition files, select the WSDL file in the root of the folder, and then click **Consume**.

If you do not receive another error message the SOAP web service should work as expected.
