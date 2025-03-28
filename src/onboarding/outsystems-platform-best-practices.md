---
summary: Explore best practices for developing applications with OutSystems 11 (O11), covering coding conventions, database management, UI design, and more.
guid: 463d263b-5aba-4881-857e-2465a046c24d
locale: en-us
app_type: traditional web apps, mobile apps, reactive web apps
platform-version: o11
figma:
tags: database optimization, ui design best practices, code reusability, javascript best practices, css best practices
audience:
  - mobile developers
  - frontend developers
  - full stack developers
outsystems-tools:
  - service studio
coverage-type:
  - evaluate
topic:
  - scale-development-strategy
---

# OutSystems Platform Best Practices

This article aggregates a collection of best practices and conventions that you can apply when developing your OutSystems applications. These are only recommendations and you should adapt them to each environment and to each development style.

## Naming and coding conventions

### Standard language

* Use English for code and comments.

### Naming conventions

* Meaningful names (for example, "Customer" instead of "Cstr").
* Use PascalCase.
* Suffix foreign keys with “Id” (for example, "CustomerId").
* Include the Entity's Name in the Record's name (for example, "Customer" instead of "record").
* Group Screens with a prefix (for example, "Customer_Edit" and "Customer_Show").
* Prefix actions invoked by Timers with "Timer_".
* Set the Name property of ShowRecords, EditRecords and TableRecords.

### Coding conventions

* Avoid empty labels and descriptions.
* Comment unclear or complex logic.
* Set the example string of Expressions.
* Keep Action Flows vertical and tidy.
* Use Static Entities instead of hard-coded values.

### Reusability

* Reuse logic with Server Actions.
* Reuse screen parts with Blocks.
* Encapsulate data formatting with User Functions.
* Use RefreshQuery to rerun a Query.

## JavaScript, CSS and HTML

* Comment your JavaScript.
* Use cross-browser JavaScript.
* Avoid duplicate CSS styles.
* Minify JavaScript and CSS whenever possible.

## Database

* Avoid having hundreds of attributes in one Entity
* Avoid large attributes (e.g. text attributes with length above 2000)
* Check the Delete Rule of Foreign Keys to an Entity.
* Remember to set the Is Mandatory property.
* Add descriptions at least to the Entities.

## Aggregates and Advanced Queries

### Queries

* Use Aggregates: they’re optimized and database independent!
* Avoid using indexes ([i]) when iterating a Query output.
* Minimize the number of Queries you need to execute.
* Avoid type casts in Aggregates.

### Advanced Queries

* Use Advanced Queries only when absolutely necessary.
* Use Parameters instead of hard-coded values in the SQL.
* Indent SQL code consistently.
* Use comments and inline comments in your SQL.
* Use Advanced Queries for bulk operations.
* Don't put business logic in the SQL.
* Use the EncodeSQL built-in function for Inline Parameters.
* Keep in mind that Advanced Queries are database specific.

## Building for change

* Favor Aggregates over SQL Queries.
* Keep in mind that SQL Queries are harder to maintain.
* Avoid creating custom HTML/JavaScript.
* Split functionality in different Web Screens.
* Don’t use Extensions to implement business logic.

## User Interface

* Find out what needs improvement by observing your users.
* Reduce the size of the images in your module.

## Architecture

Use a 3 layers approach:

* Business Processes: a service available for use by users or business processes.
* Core Entities: logical grouping of operations per responsibility.
* Connectors: extensions or integration with other systems.

Also:

* Wrap Extensions in modules.
* Avoid circular references between modules.
* Clearly define the responsibilities of each module.
* Remove unused references.
* Encapsulate business logic in Server Actions.
* Create user story driven interfaces.
* Don't isolate the data model in one module. Modules should be functional units instead of architectural units.
* Use asynchronous logic when possible.

## Teamwork

* Know the recommended project team for your project (see [The Talent Playbooks](https://www.outsystems.com/1/talent-playbook/)).
* Use a single user for each team member.
* Everyone in the team should use the same Service Studio version.
* Use LifeTime to perform application versioning.
* Avoid publishing single modules: use LifeTime.
* Avoid applying a hotfix without testing it first (see [Apply a Hotfix](https://success.outsystems.com/Documentation/11/Managing_the_Applications_Lifecycle/Deploy_Applications/Apply_a_Hotfix)).
* Avoid working on the same elements at the same time.
* Avoid deploying to Production during business hours.
* Create team processes for active log monitoring.
* Create team processes for manual deployment procedures such as data update scripts.
* Define what "done" means and include testing.

## Logic and development

* Remove unused or duplicate code.
* A module with a size larger than 4 MB could indicate poor architecture (see [How to reduce the size of my modules](https://success.outsystems.com/documentation/how_to_guides/development/how_to_reduce_the_size_of_my_modules/)).
* Set at least one default button in your Web Screens.
* Avoid changing Site Properties values in your logic.
* Be careful about infinite recursion.
* Hide warnings only for a good reason.
* More than 20 site properties in one module normally means bad design.
* Avoid using Extensions solely for Web Service consumption.
* Disable auditing of Extensions in Production.

## Security

* Set the Screen's Roles.
* Be aware of sensitive data exchange.
* **Don't** send sensitive information in screen parameters.
* Remember: In Traditional Web, Screen's variables or Preparation outputs might be exposed in the URL or Viewstate.
* When applicable, use SSL for sensitive information.
* **Don't** rely on the Screen widgets interface to control permissions.
* Validate user’s Roles before executing Screen Actions.
* Use encrypted passwords in the database.
* Use Internal Access Only for UI Flows and Web Services.
* Check the Reactive web specific [security best practices](https://success.outsystems.com/documentation/best_practices/security/reactive_web_security_best_practices/).

## Performance

### Data model

* Index your Entities.
* Isolate large Text and Binary Data in another entity.
* Beware of Large Excel Files Performance.
* Make good use of the Delete Rules in Entities.
* Archive old data in separate Entities.

### Infrastructure

* Setup database maintenance plans.
* Configure Web server memory settings.
* Backup database transaction logs often.
* Tune database file growth.
* Apply virtual memory and system settings.
* Use a dedicated server for Timers.
* Prefer 64-bit architectures.
* Plan and monitor timers schedule so there are no conflicting schedules.

### Logic

* Look into Service Center reports.
* Avoid long-running Timers and batch jobs.
* In Traditional Web, simplify screen Preparations.
* Place as little information as possible in Session Variables.
* Avoid using isolated Aggregates in Server Actions.
* In traditional web, avoid using queries inside If branches in Preparation.
* Avoid chained Web Service calls. Return as much as possible in a single call.

### Queries

* Don’t perform joins over linked servers.
* Minimize the number of fields fetched from the database.
* Keep Max Records consistent with your needs.
* Iterate over queries once and avoid using indexes ([i]).
* Minimize the number of executed queries.

### References

* **Never** create circular references between modules.
* Choose wisely between Local Web Services or Public Actions.
* Use Connection Pooling.

### User Interface

* In Traditional Web, avoid using Preparation data in screen actions.
* Use multiple Screens instead of creating complex ones.
* Cache, baby, cache!
* Minimize Screen Parameters.
* Import JavaScript files as resources.
* Move JavaScript Blocks that aren't needed at loading time to the bottom.
* Use CSS Sprite Images.

## Common patterns and examples

Here’s a quick list of several open apps you can use or refer to for examples:

* Hierarchical tree example: [Directory](https://www.outsystems.com/forge/component-overview/614/directory)
* Tags implementation example: [Documents](https://www.outsystems.com/forge/component-overview/612/documents)
* Storing files (binary data) example: [Documents](https://www.outsystems.com/forge/component-overview/612/documents)
* Yearly Calendar: [Time Sheets](https://www.outsystems.com/forge/component-overview/613/time-sheets)
* Charts: [Sales](https://www.outsystems.com/forge/component-overview/582/sales)
* Using Email POP: [Cases](https://www.outsystems.com/forge/component-overview/584/cases)

For downloading components to speed up your development time, check out the [Forge](https://www.outsystems.com/forge/).

For more learning resources, check the [OutSystems Training area](https://www.outsystems.com/learn/).
