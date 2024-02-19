---
summary: A comprehensive guide to the process for migrating your apps from O11 to OutSystems Developer Cloud (ODC), including planning, phased migration, and the support available from documentation.
locale: en-us
guid: 0a6f2684-c594-4eca-9cbf-0780c9b3c5ae
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma: https://www.figma.com/file/daglmSUESdKw9J3HdT87a8/O11-to-ODC-migration?type=design&node-id=20%3A241&mode=design&t=IqPW9GPcaNRalD3r-1
---

# OutSystems 11 to ODC migration

Our goal is to enable you to convert your current O11 app portfolio into native ODC apps. Once converted and published on ODC, these applications can leverage all current and future ODC capabilities, such as cloud-native architecture, limitless scaling, and new AI features for businesses and developers.

OutSystems provides documentation and migration tools to ease and automate the process of migrating from O11 to ODC code and data.

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

ODC applications must be designed to take advantage of cloud-native architecture and microservices design, which promote application-independent lifecycle and ownership.

To fully benefit from all ODC capabilities, it's important to adjust the O11 app portfolio architecture to align with ODC architecture best practices. Additionally, some code patterns are implemented differently on ODC, so it's necessary to validate the suggested conversion.

To help with the O11 app portfolio assessment, OutSystems is releasing a [set of documents](../migration-to-odc/preparation/process.md). An automatic assessment tool will also be available to help you automate the O11 app portfolio assessment in a way that can be seamlessly incorporated into your regular development activities.

#### Outcomes

* Visibility over necessary code adjustments to convert O11 code to ODC-compatible code

* Guidance on how to map existing O11 code patterns into ODC constructs

* Overview of the entire factory applicational domains, understanding boundaries and domain prioritization


### Stage 2: Code preparation

After completing the O11 app portfolio assessment, adjust the current O11 app portfolio architecture and code to ensure that migrated apps benefit from all ODC advantages. Consider including necessary adjustments in sprints, prioritized according to the desired migration timelines.

#### Outcomes

* Implementation of code adjustment to be ODC-compatible

* Segregate applicational domains to be able to migrate apps independently


### Stage 3: Code migration

Once you’ve completed the O11 app portfolio assessment and the code preparation steps for your app portfolio, it’s time to start converting your O11 apps to ODC apps.

In this step, the conversion tool is used to convert all O11 apps, modules, and extensions into ODC. The tool ensures that the O11 code is mapped into ODC constructs while maintaining the same functionality. The following are some examples of the automations in place to guarantee this mapping:

* Replace System references with the ODC equivalent
* Replace Login and Logout flows
* Automatically change the Public property of some elements from **Yes** to **No**, given the [ODC rules](https://success.outsystems.com/documentation/outsystems_developer_cloud/building_apps/app_architecture/reuse_elements_across_apps/)

#### Outcomes

* Reduce manual effort required by automating O11 code mapping into ODC constructs.

* Reduce migration lead time and business impact, reducing error-prone occurrences.


### Stage 4: Data migration

Finally, after converting the code and publishing it on ODC, it's time to address the data. Data migration tools are available to ensure that O11 data is correctly migrated to ODC. These tools automatically convert data types, foreign keys, data mapping, and identity mapping as needed.

#### Outcomes

* Reduce testing and business risk by ensuring that O11 data automatically migrated to ODC.

* O11 entities are automatically mapped into ODC counterparts

Once you’ve completed the data migration step, end users can be directed to ODC apps, and O11 apps can be decommissioned.
