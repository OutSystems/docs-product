---
summary: Learn how to search encrypted searchable attributes.
locale: en-us
guid: f1e59367-c1a5-4ef1-bb4e-ea265d5100e2
---

# Search encrypted data

You can enable the search of encrypted data for [encrypted searchable attributes](encrypt-data-hipaa.md#encrypt-no-search), by encrypting the search string before querying the database. This isn't possible with unsearchable attributes.

## Prerequisites

To enable the search of an attribute ensure that:

* The attribute is searchable, and you know the **IndexType** used for the encryption of the attribute.

* In the module with the entity you want to search, the [EncryptSearchableAttribute](encrypt-data-hipaa.md#encrypt-search) has the **Public** property set to **Yes**.

* In the module where you are doing the search, you added the [EncryptSearchableAttribute](encrypt-data-hipaa.md#encrypt-search) action and the entity with the attribute as a dependency.

## Search an encrypted attribute

To search an encrypted searchable attribute do the following:

1. In the module where you are doing the search, open the search action, and add the **EncryptSearchableAttribute** action before searching the data.

1. Set the **EncryptSearchableAttribute** inputs as follows:

    * Set **Text** as `<search-text>`, replacing `<search-text>` with the variable that holds the text you want to search for.
    * Set **IndexType** as `<index-type>`, replacing `<index-type>` with the same string used during the encryption of the attribute. For example, `BloodType`.

1. After **EncryptSearchableAttribute**, add an **Assign** and assign the **EncryptedText** output of the **EncryptSearchableAttribute** action to the variable used for the database query.

1. Publish the module.
