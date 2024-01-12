---
helpids: 15003
locale: en-us
guid: dc811245-bcef-4579-bcee-3530a997eecd
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/eFWRZ0nZhm5J5ibmKMak49/Reference?node-id=1526:2630
summary: The article explains how to create and use a site property in an application to manage values like maximum records for an aggregate
---

# Site property

A site property is a global variable that has a constant value, or a value that doesn't change often.

By design, Site Property values have a 2000 character limit. The *usable number of characters* of a Site Property value can be lesser than 2000 characters depending on different scenarios:

* It is set as a Secure Site Property.
* The Encoding of the value.
* The Platform's database character encoding configuration.

## How to use site properties

### Example 1

In this example, there's a screen with an aggregate named **GetEmployees**. This aggregate retrieves records from an Employee entity, with a default maximum records. The maximum records is defined by a site property named MaxRecords.

1. On the **Data** tab, right-click **Site Properties** and select **Add Site Property**.

1. Set the site property's **Name** to `MaxRecords` and its **Data Type** to `Integer`. On the **Default Value** property, enter `10`.

    ![Dialog in Service Studio showing the addition of a MaxRecords site property with a data type of Integer and a default value of 10.](images/site-prop-max-records-ss.png "Adding a MaxRecords Site Property")

1. Select the **GetEmployees** aggregate and set the **Max. Records** to `Site.MaxRecords`.

    ![Service Studio interface illustrating how to set the Max. Records property of the GetEmployees aggregate to the Site.MaxRecords site property.](images/set-maxrecords-ss.png "Setting Max. Records in GetEmployees Aggregate")

1. Click the **1-Click Publish** button to publish your app, and then click **Open in browser**.

1. Open a screen that uses the **GetEmployees** aggregate. Check that the retrieved records are 10 or less.

1. In **Service Studio**, click **Module Management in Service Center...**.

    ![Service Studio option highlighted for accessing Module Management in Service Center.](images/module-management-ss.png "Module Management in Service Center")

1. In **Service Center**, make sure you're on the correct module. If you're not, click **Factory** and then **Modules**, and select your module. 

1. Click **Site Properties** and check that it lists the **MaxRecords** site property.

    ![Service Center's view of the module's Site Properties tab listing the MaxRecords site property.](images/site-prop-tab-sc.png "Site Properties Tab in Service Center")

1. Click **MaxRecords**, then change its **Effective Value** to  `5`. By doing this, you're changing the MaxRecords' value at runtime and the aggregate will now retrieve 5 records instead of the default 10.

    ![Service Center interface showing the MaxRecords site property with an option to change its Effective Value.](images/effective-value-sc.png "Editing MaxRecords Site Property")

1. Click **Apply** and then refresh your app's page. The MaxRecords displayed must adopt the new value.

### Example 2

In this example, there's an integration with an external service, where the service credentials, such as password, must be protected.

<div class="info" markdown="1">

To avail of the secret site property functionality, the following is required:
* LifeTime 11.20.1
* Platform Server 11.25.0
* Service Studio 11.54.35

</div>

1. On the **Data** tab, right-click **Site Properties** and select **Add Site Property**.

1. Set the site property's **Name** to **ServicePassword** and the **Data Type** to **String**. 

1. Set the **Is Secret** property to **Yes**.

    ![Service Studio dialog for adding a ServicePassword site property with the Is Secret property set to Yes.](images/site-prop-service-pass-ss.png "Setting Is Secret Property to Yes")

1. Use the **ServicePassword** site property in your integration logic.

1. In Service Studio, click **Module Management in Service Center....**

    ![Service Studio option highlighted for accessing Module Management in Service Center.](images/module-management-ss.png "Module Management in Service Center")

1. In Service Center, ensure you are on the correct module. If you're not, go to **Factory** -> **Modules** and select your module.

1. Click **Site Properties** and check that it lists the **ServicePassword** site property.

    ![Service Center displaying the Site Properties tab with the ServicePassword site property listed.](images/site-prop-tab-serpass-sc.png "ServicePassword Site Property in Service Center")

1. Click **ServicePassword** and change the **Effective Value** to the service password. 

    By doing this, you enforce the password value for that site property. No other users can see the value.

    ![Service Center interface showing the ServicePassword site property with an option to change its Effective Value.](images/site-prop-apply-sc.png "Applying New Effective Value to ServicePassword")

1. Click **Apply** and then test your integration implementation.

<div class="info" markdown="1">

If you change a site property from secret to non-secret or vice-versa, the effective value is cleared, and the new value must be set in Service Studio or in Service Center. 

</div>

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
<td>Identifies an element in the scope where it is defined, like a screen, action, or module</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Description">Description</td>
<td>Text that documents the element</td>
<td></td>
<td></td>
<td>Useful for documentation purposes.<br/>The maximum size of this property is 2000 characters.</td>
</tr>
<tr>
<td title="Data Type">Data Type</td>
<td>The data type of the site property</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
<tr>
<td title="Is Secret">Is Secret</td>
<td>Encrypts and protects the value</td>
<td></td>
<td>No</td>
<td>A site property with the Is Secret property enabled does not have  a default value. When a secret site property is published for the first time, its effective value is empty and must be set in Service Center.</td>
</tr>
<tr>
<td title="Default Value">Default Value</td>
<td>Initial value of this element. If undefined, the default value of the data type is used.</td>
<td></td>
<td></td>
<td>Does not apply to site properties that have the Is Secret property enabled.</td>
</tr>
<tr >
<th colspan="5">Advanced</th>
</tr>
<tr>
<td title="Is Multi-tenant">Is Multi-tenant</td>
<td>Set to Yes to enable muti-tenancy for this specific element. Overrides the multi-tenancy definitions inherited from the module.</td>
<td>Yes</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

