---
summary: A comprehensive guide to the process for migrating your apps from O11 to OutSystems Developer Cloud (ODC), including planning, phased migration, and the support available from documentation.
locale: en-us
guid: 0a6f2684-c594-4eca-9cbf-0780c9b3c5ae
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?type=design&node-id=20%3A241&mode=design&t=IqPW9GPcaNRalD3r-1
---

# OutSystems 11 to ODC migration

For over 20 years, OutSystems has been committed to ensuring that you, our customers, have access to the latest and greatest capabilities for software delivery. When we built our product, it was because we wanted to make innovation easier so that you can always be at the forefront of it. It is for this same reason that we released OutSystems Developer Cloud (ODC).

In keeping with this commitment, OutSystems also wants to ensure that you can take your existing O11 app portfolio and modernize it for native ODC apps. This means that even older apps can take advantage of all existing and future ODC capabilities, for example, cloud-native architecture, scaling without limits, and new AI capabilities for businesses and developers.

![Diagram illustrating the conversion process from OutSystems 11 apps to OutSystems Developer Cloud apps](images/app-conversion-diag.png "O11 to ODC App Conversion Diagram")

To make this opportunity for modernization as easy as possible, OutSystems fully supports you in the migration journey by providing documentation and migration tools to ease and automate a significant part of the work.

![Graphic representation of the supporting materials provided by OutSystems for the migration from O11 to ODC](images/o11-odc-migration-kit-diag.png "O11 to ODC Migration Support Material")

With that in mind, the following topics will help you understand the migration process.

## How to plan for migration

OutSystems is committed to making sure that you have an easy migration process and one that fits smoothly into your development team's schedule. You can migrate on a timeline that takes into account your app portfolio and business demand.

Depending on the size of your app portfolio, you may follow different migration journeys. 

* **One-shot migration** is suitable for smaller app portfolios (infrastructures with less than 2 business apps) with up to 300 application objects. You can choose to migrate the entire portfolio at once and have it ported to ODC in a short timeframe.

    ![Diagram showing the one-shot migration process for small app portfolios from O11 to ODC](images/one-shot-migration-diag.png "One-Shot Migration Diagram")

* **Coexistence**  is suitable for larger app portfolios (infrastructures with more than 2 apps) where it is essential to continue providing business value and, at the same time, work on the migration activities. With this migration journey, new apps can be created in ODC while you independently migrate apps from O11.

    * **Start using ODC**: ODC tenant for new apps, ability to leverage existing O11 components such as integrations and master data.

    * **Prepare and progressively migrate O11 apps**: Assess and migrate O11 apps that will benefit most from ODC capabilities.

    * **Complete migration of all apps**: Assess and migrate more complex O11 apps.

    ![Diagram depicting the phased approach for migrating larger app portfolios from O11 to ODC](images/migration-phased-approach-diag.png "Phased Approach to Migration Diagram")

## How migration capabilities will be delivered

Migration capabilities will be delivered incrementally, addressing the most common use cases first, then progressing to more complex ones, and finally aligning with all ODC capabilities. 

![Timeline showing the incremental delivery of migration capabilities from O11 to ODC](images/migration-toolkit-value.png "Migration Capabilities Delivery Timeline")

## Migration stages

![Comprehensive diagram outlining the stages of the migration process from O11 to ODC](images/migration-process-diag.png "Overall Migration Process Diagram")

### Stage 1: O11 app portfolio assessment

![Diagram highlighting the outcomes of the O11 app portfolio assessment stage in the migration process](images/migration-process-step-1-diag.png "O11 App Portfolio Assessment Outcomes")

ODC was designed to bring your apps into the cloud-native future. This means that ODC apps must be architected in a way that allows you to reap the benefits of cloud-native architecture and microservices design, fostering application-independent lifecycle and ownership. In summary, ODC enables businesses to be agile and helps them meet the [DevOps Research and Assessment (DORA) metrics standards](https://dora.dev/).

Once O11 apps are ported over to ODC, for them to truly benefit from all ODC capabilities, it's important to adjust the O11 app portfolio-architecture to align with ODC architecture best practices.  Also, some code patterns are not fully compatible with ODC and must be adjusted accordingly on the O11 side before migration.

To help with the O11 app portfolio assessment, OutSystems is releasing a [set of documents](../migration-to-odc/preparation/process.md). An automatic assessment tool will also be available to help you automate the O11 app portfolio assessment in a way that can be worked seamlessly into your development activities.

#### Outcomes

* Visibility over necessary code adjustments to convert O11 code to ODC-compatible code

* Guidance on how to map existing O11 code patterns into ODC constructs

* Overview of the entire factory applicational domains, understanding boundaries and domain prioritization

### Stage 2: Code preparation

![Diagram illustrating the outcomes of the code preparation stage in the O11 to ODC migration process](images/migration-process-step-2-diag.png "Code Preparation Outcomes")

Once you’ve completed your O11 app portfolio assessment, you must adjust your current O11 app portfolio architecture and code to ensure that migrated apps benefit from all ODC benefits. 

Once the O11 app portfolio assessment (stage 1 of migration) is completed, teams will understand what tasks must be addressed before migrating to ODC and can build these steps into sprints, prioritized according to the desired migration timelines.

#### Outcomes

* Implementation of code adjustment to be ODC-compatible

* Segregate applicational domains to be able to migrate apps independently

### Stage 3: Code migration

![Diagram detailing the outcomes of the code migration stage from O11 to ODC](images/migration-process-step-3-diag.png "Code Migration Outcomes")

Once you’ve completed the O11 app portfolio assessment and the code preparation steps for your app portfolio, it’s time to start converting your O11 apps to ODC apps.

During this step, all O11 apps, modules, and extensions are converted into ODC using the conversion tool. The following are some examples of automations that are in place to guarantee that O11 code is mapped into ODC constructs, keeping the same functionality.

* Replace System references with the ODC equivalent
* Replace Login and Logout flows
* Automatically change the Public property of some elements from **Yes** to **No**, given the [ODC rules](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/app_architecture/reuse_elements_across_apps/)

#### Outcomes

* Reduce manual effort required by automating O11 code mapping into ODC constructs.

* Reduce migration lead time and business impact, reducing error-prone occurrences.

### Stage 4: Data migration

![Diagram showing the outcomes of the data migration stage in the transition from O11 to ODC](images/migration-process-step-4-diag.png "Data Migration Outcomes")

Finally, once the code is converted and published on ODC, it’s time to look at data. Data migration tools will be available to ensure that O11 data is correctly migrated to ODC. These tools help you convert data types, foreign keys, data mapping, and identity mapping.

#### Outcomes

* Reduce testing and business risk by ensuring that O11 data automatically migrated to ODC.

* O11 entities are automatically mapped into ODC counterparts

Once you’ve completed the data migration step, end users can be directed to ODC apps, and O11 apps can be decommissioned.
