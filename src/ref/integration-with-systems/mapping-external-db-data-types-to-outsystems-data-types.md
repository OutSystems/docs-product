---
tags: support-application_development; support-Database; support-Integrations_Extensions
locale: en-us
guid: 310843b2-84da-4461-99e8-c2dc6be41778
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
---

# Mapping External DB Data Types to OutSystems Data Types

When [connecting to external databases](../../integration-with-systems/external-database/connect-external-db.md), OutSystems maps the external DB Data Types into OutSystems Data Types as follows:

SQL Server  |  Oracle Data Type  |  MySQL Data Type  | PostgreSQL Data Type |  DB2 Data Type  | OutSystems Data Type  
---|---|---|---|---|---  
Char <br/>Varchar <br/>Text <br/>Nchar <br/>Nvarchar <br/>Ntext <br/>Xml <br/>Decimal(Any,> 8) <br/>Numeric(Any,> 8) <br/>Real <br/>Float <br/>UniqueIdentifier <br/>Time <br/>Datetimeoffset  |  Char <br/>Varchar <br/>Varchar2 <br/>Clob <br/>Long <br/>Nchar <br/>NVarchar2 <br/>Nclob <br/>Number(Any,> 8) <br/>Float <br/>Binary\_float <br/>Binary\_double <br/>RowId URowId <br/>XmlType  |  Varchar <br/>Char <br/>Longtext <br/>Mediumtext <br/>Tinytext <br/>Text <br/>Enum <br/>Set <br/>Decimal(> 28,Any) <br/>Decimal(Any,> 8) <br/>Numeric(> 28,Any) <br/>Numeric(Any,> 8) <br/>Double <br/>Real <br/>Float <br/>Time  |  Character <br/>Character Varying <br/>Varchar <br/>Vhar <br/>Uuid <br/>xml <br/>Public.citext <br/>Citext <br/>Text <br/>Real <br/>Double Precision <br/>Decimal (> 28, Any) <br/>Decimal (Any, > 8) <br/>Numeric (> 28, Any) <br/>Numeric (Any, > 8)  | Character <br/>Varchar <br/>Clob <br/>DbClob <br/>Xml <br/>Decimal(> 28,Any) <br/>Decimal(Any,> 8) <br/>Numeric(> 28,Any) <br/>Numeric(Any,> 8) <br/>Float <br/>Real <br/>DecFloat <br/>Double <br/>Time <br/>Nchar <br/>Nvarchar <br/>NClob  |  Text  
Tinyint <br/>Smallint <br/>Int <br/>Decimal(1-9,0) <br/>Numeric(1-9,0)  |  Number(2-9,0)  |  Tinyint(> 1) <br/>Smallint <br/>Mediumint <br/>Int <br/>Decimal(1-9,0) <br/>Numeric(1-9,0)  |  Integer <br/>Int <br/>Int4 <br/>Smallint <br/>Int2 <br/>Serial <br/>Serial4 <br/>Decimal(1-9,0) <br/>Numeric(1-9,0)  |  Integer <br/>Smallint <br/>Decimal(1-9,0) <br/>Numeric(1-9,0)  |  Integer  
Bigint <br/>Decimal(10-18,0) <br/>Numeric(10-18,0)  |  Number(10-18,0)  |  Bigint <br/>Unsigned Int <br/>Bit(2-64) <br/>Decimal(10-18,0) <br/>Numeric(10-18,0)  |  Bigint <br/>Int8 <br/>Bigserial <br/>Serial8 <br/>Decimal(10-18,0) <br/>Numeric(10-18,0) |  Bigint <br/>Decimal(10-18,0) <br/>Numeric(10-18,0)  |  Long Integer  
Decimal(19-28,0-8) <br/>Decimal(1-18,>1-8) <br/>Numeric(19-28,0-8) <br/>Numeric(1-18,>1-8) <br/>Money <br/>Smallmoney  |  Number(19-28,0-8) <br/>Number(1-18,1-8)  |  Unsigned Bigint <br/>Decimal(19-28,0-8) <br/>Decimal(1-18,1-8) <br/>Numeric(19-28,0-8) <br/>Numeric(1-18,1-8)  |  Money <br/>Decimal(19-28,0) <br/>Decimal(1-18,1-8) <br/>Numeric(19-28,0)  <br/>Numeric(1-28,1-8)  |  Decimal(1-18,1-8) <br/>Decimal(19-28,0-8) <br/>Numeric(1-18,1-8) <br/>Numeric(19-28,0-8)  |  Decimal  
Bit  |  Number(1,0)  |  Bit(1) <br/>Tinyint(1)  |  Bit <br/>Boolean <br/>Bool  |  SmallInt* <br/>Integer* <br/>Bigint* <br/>* with constraint in (0,1)  |  Boolean   
Date  |  |  Date  |  Date  |  Date  |  Date  
Datetime <br/>DateTime2 <br/>Smalldatetime  |  Date <br/>Timestamp  |  Datetime <br/>Timestamp  |  Timestamp  |  Timestamp  |  DateTime  
Image <br/>Binary <br/>Varbinary  |  Bfile <br/>Blob <br/>Raw <br/>Long Raw  |  Blob <br/>Longblob <br/>Tinyblob <br/>Mediumblob <br/>Binary <br/>Varbinary  |  Bytea  |  Binary <br/>Blob <br/>Char(Bit) <br/>VarChar(Bit) <br/>VarBinary  |  Binary Data  
Sql_variant <br/>Geometry <br/>HierarchyId <br/>Geography <br/>Rowversion <br/>Timestamp  |  Interval day to second <br/>Interval year to month  |  Polygon <br/>Point <br/>Multipoint <br/>MultiPolygon <br/>LineString <br/>MultiLineString <br/>Geometry <br/>GeometryCollection <br/>Year  |  Box <br/>Cidr <br/>Circle <br/>Inet <br/>Line <br/>Lseg <br/>Macaddr <br/>Path <br/>Point <br/>Polygon <br/>Tsquery <br/>Tsvector <br/>Txid_snapshot <br/>Bit varying <br/>ARRAY <br/>USER-DEFINED <br/>Interval  |  Datalink <br/>Graphic <br/>Vargraphic <br/>RowId  |  No mapping available. <br/>The attribute will be marked as "Ignored" in Integration Studio.  
  
_For Decimal(M,D) or similar, M is the maximum number of digits (the precision) and D is the number of digits to the right of the decimal point (the scale)._