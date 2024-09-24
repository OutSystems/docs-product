---
summary: Search engine optimization (SEO) is the process of improving a website’s content and technical configuration to increase its ranking in search engine results pages (SERPs).
tags: runtime-traditionalweb
locale: en-us
guid: C07BCA11-7DB2-49FD-B01B-97EBFBDCF36F
app_type: traditional web apps, reactive web apps
platform-version: o11
figma:
---

# Search engine optimization in apps

Search engine optimization (SEO) is the process of improving a website’s content and technical configuration to increase its ranking in search engine results pages (SERPs). Because search is one of the main ways in which people discover content online, ranking higher in search engines can lead to an increase in traffic to a website. SEO makes your website more visible to people who are looking for solutions that your brand, product, or service can provide via search engines. 

![Diagram illustrating the search engine optimization process for OutSystems apps](images/seo-process-diag.png "SEO Process Diagram")  

## SEO benefits

The following are some benefits of SEO for websites that want to increase visibility and provide value to their users:
* Increased organic (unpaid) discovery 

    Organic visibility leads to increased traffic.

* Improved credibility and trust 

    Ranking on the first page of a search engine boosts credibility among users.

* Optimized user experience

    User experience is a critical component of SEO and a significant ranking factor. 

For developers that want to take their application to production, and have it be widely available and easily findable by new users, implementing SEO strategies allows them to:

* Improve traffic analytics for customer applications

    Implementing SEO strategies brings more users to applications. This improves the app’s data statistics that relate to the number of impressions (how often a user sees a link to your app) and how users discover the app.

* Identify improvements to application structure (duplicated content, pages returning 404 errors - missing content)

* Drive and improve traffic between different applications

    Redirecting traffic between different applications can be achieved using SEO rules. This improves application behavior as it allows integration of old and new applications.

## Limitations

Check the current limitations in the following sections.

### Performance degradation while ISAPIFilter synchronizes SEO Rules

<div class="info" markdown="1">

Applies to Reactive and Traditional Web apps.

</div>

Having a high number (more than 1000) of SEO Rules configured in Service Center (Page Rules, Path Rules, Site Rules, and Redirect Rules combined) may result in performance degradation after performing one of the following operations:

* Change the SEO URL Rules (Page, Path, Site, and Redirect): Create / Edit / Delete
* Publish a module (via Service Center or Service Studio)
* Perform the **Update Status** step when deploying a solution
* Upload an OutSystems license  

This performance degradation occurs while the ISAPIFilter synchronizes the SEO Rules, after performing one of the operations above.
