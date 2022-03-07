---
tags: support-application_development; support-Database; support-Integrations_Extensions
---

# Mapping External DB Data Types to OutSystems Data Types

When [connecting to external databases](../../extensibility-and-integration/external-database/connect-external-db.md), OutSystems maps the external DB Data Types into OutSystems Data Types as follows:

SQL Server  |  Oracle Data Type  |  MySQL Data Type  | PostgreSQL Data Type |  DB2 Data Type  | OutSystems Data Type  
---|---|---|---|---|---  
Char %%Varchar %%Text %%Nchar %%Nvarchar %%Ntext %%Xml %%Decimal(Any,> 8) %%Numeric(Any,> 8) %%Real %%Float %%UniqueIdentifier %%Time %%Datetimeoffset  |  Char %%Varchar %%Varchar2 %%Clob %%Long %%Nchar %%NVarchar2 %%Nclob %%Number(Any,> 8) %%Float %%Binary\_float %%Binary\_double %%RowId URowId %%XmlType  |  Varchar %%Char %%Longtext %%Mediumtext %%Tinytext %%Text %%Enum %%Set %%Decimal(> 28,Any) %%Decimal(Any,> 8) %%Numeric(> 28,Any) %%Numeric(Any,> 8) %%Double %%Real %%Float %%Time  |  Character %%Character Varying %%Varchar %%Vhar %%Uuid %%xml %%Public.citext %%Citext %%Text %%Real %%Double Precision %%Decimal (> 28, Any) %%Decimal (Any, > 8) %%Numeric (> 28, Any) %%Numeric (Any, > 8)  | Character %%Varchar %%Clob %%DbClob %%Xml %%Decimal(> 28,Any) %%Decimal(Any,> 8) %%Numeric(> 28,Any) %%Numeric(Any,> 8) %%Float %%Real %%DecFloat %%Double %%Time %%Nchar %%Nvarchar %%NClob  |  Text  
Tinyint %%Smallint %%Int %%Decimal(1-9,0) %%Numeric(1-9,0)  |  Number(2-9,0)  |  Tinyint(> 1) %%Smallint %%Mediumint %%Int %%Decimal(1-9,0) %%Numeric(1-9,0)  |  Integer %%Int %%Int4 %%Smallint %%Int2 %%Serial %%Serial4 %%Decimal(1-9,0) %%Numeric(1-9,0)  |  Integer %%Smallint %%Decimal(1-9,0) %%Numeric(1-9,0)  |  Integer  
Bigint %%Decimal(10-18,0) %%Numeric(10-18,0)  |  Number(10-18,0)  |  Bigint %%Unsigned Int %%Bit(2-64) %%Decimal(10-18,0) %%Numeric(10-18,0)  |  Bigint %%Int8 %%Bigserial %%Serial8 %%Decimal(10-18,0) %%Numeric(10-18,0) |  Bigint %%Decimal(10-18,0) %%Numeric(10-18,0)  |  Long Integer  
Decimal(19-28,0-8) %%Decimal(1-18,>1-8) %%Numeric(19-28,0-8) %%Numeric(1-18,>1-8) %%Money %%Smallmoney  |  Number(19-28,0-8) %%Number(1-18,1-8)  |  Unsigned Bigint %%Decimal(19-28,0-8) %%Decimal(1-18,1-8) %%Numeric(19-28,0-8) %%Numeric(1-18,1-8)  |  Money %%Decimal(19-28,0) %%Decimal(1-18,1-8) %%Numeric(19-28,0)  %%Numeric(1-28,1-8)  |  Decimal(1-18,1-8) %%Decimal(19-28,0-8) %%Numeric(1-18,1-8) %%Numeric(19-28,0-8)  |  Decimal  
Bit  |  Number(1,0)  |  Bit(1) %%Tinyint(1)  |  Bit %%Boolean %%Bool  |  SmallInt* %%Integer* %%Bigint* %%* with constraint in (0,1)  |  Boolean   
Date  |  |  Date  |  Date  |  Date  |  Date  
Datetime %%DateTime2 %%Smalldatetime  |  Date %%Timestamp  |  Datetime %%Timestamp  |  Timestamp  |  Timestamp  |  DateTime  
Image %%Binary %%Varbinary  |  Bfile %%Blob %%Raw %%Long Raw  |  Blob %%Longblob %%Tinyblob %%Mediumblob %%Binary %%Varbinary  |  Bytea  |  Binary %%Blob %%Char(Bit) %%VarChar(Bit) %%VarBinary  |  Binary Data  
Sql_variant %%Geometry %%HierarchyId %%Geography %%Rowversion %%Timestamp  |  Interval day to second %%Interval year to month  |  Polygon %%Point %%Multipoint %%MultiPolygon %%LineString %%MultiLineString %%Geometry %%GeometryCollection %%Year  |  Box %%Cidr %%Circle %%Inet %%Line %%Lseg %%Macaddr %%Path %%Point %%Polygon %%Tsquery %%Tsvector %%Txid_snapshot %%Bit varying %%ARRAY %%USER-DEFINED %%Interval  |  Datalink %%Graphic %%Vargraphic %%RowId  |  No mapping available. %%The attribute will be marked as "Ignored" in Integration Studio.  
  
_For Decimal(M,D) or similar, M is the maximum number of digits (the precision) and D is the number of digits to the right of the decimal point (the scale)._