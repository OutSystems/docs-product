---
summary: How to deploy sitemap.xml and robots.txt.  
tags:
locale: en-us
guid: 7ea79b34-6e91-4e4d-8c94-1318b03f7e22
app_type: traditional web apps, mobile apps, reactive web apps
---

# Sitemap.xml and robots.txt

The **sitemap.xml** and **robots.txt** files let you control website crawlers and indexing the public pages in your apps. Check information in this document and the [sample app](#sample-app) to generate and deploy the files.

<div class="info" markdown="1">

When adding static files to a module, [create a Site Rule](intro.md#managing-site-rules) so that the module is the root app of the domain.

</div>


## Sitemap.xml

Generating the **sitemap.xml** file in the technical preview is a semi-automated task. To add **sitemap.xml** to your module, follow these steps in Service Studio:

1. Create a REST endpoint that lists URLs in your app. See: [Generating the list of URLs](#generating-the-list-of-urls)
1. Add the REST endpoint to your **sitemap.xml**. See: [Sample sitemap.xml](#sample-sitemapxml) 
1. Deploy the **sitemap.xml** as a static file.
1. [Create a Site Rule](intro.md#managing-site-rules) and make the module the root app of the domain.

### Sample sitemap.xml

Here is a sample **sitemap.xml** you can use. Replace the sample URL **https://example.com/rest/Sitemap/GetSitemap** with the REST method URL in your app that lists the URLs.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
        <sitemap>
        <loc>https://example.com/rest/Sitemap/GetSitemap</loc>
        </sitemap>
</sitemapindex>
```

The example shows how to use a sitemap index with one sitemap, where the sitemap contains text with one URL per line. For more information see [Sitemaps XML format](https://www.sitemaps.org/protocol.html) at Sitemaps.org.

## Robots.txt

To add **robots.txt** to your module, follow these steps in Service Studio:

1. Create your **robots.txt** file.
1. Deploy **robots.txt** as a static file. See: [Deploying a static file](#deploying-a-static-file).
1. [Create a Site Rule](intro.md#managing-site-rules) and make the module the root app of the domain.

### Sample robots.txt

Here is a sample **robots.txt** file:

    Sitemap: https://example.com/sitemap.xml

    User-agent:*
    Allow: /

    User-agent: Adsbot-Google
    Allow: /store

    User-agent: Googlebot
    Allow: /
    Disallow: /profile

See [Robots.txt Specification](https://developers.google.com/search/docs/advanced/robots/robots_txt) by Google for more information. 

## Deploying a static file

To deploy a static file, follow these steps in Service Studio:

1. Go to the **Data** tab and locate the **Resources** folder.
1. Right-click the **Resources** folder and select **Import Resource**. In the dialog that opens, select your file. 
1. In the Resource properties for the file, in **Deploy Action** select **Deploy to Target Directory**.
1. Publish your module. 
1. [Create a Site Rule](intro.md#managing-site-rules) and make the module the root app of the domain.
 
## Generating the list of URLs

To generate the list of URLs, create a REST endpoint that outputs the list as text. You need to add the hostname and the list of static screens, but you can generate the subpages by looping over the data in Aggregates.

[Download and install the sample app](#sample-app) and open it in Service Studio. Check the logic in **Logic** > **Integrations** > **REST** > **Sitemap**. The logic shows how to generate links for your content. To see the list or URLs the method generates, right-click **Sitemap** and select **Open Documentation**.


## Sample app

You can [download the sample app](files/sitemap-and-robots.oap), install it in your environment, and open it in Service Studio. The app contains examples of how to deploy and generate **sitemap.xml** and **robots.txt**.

When working with the sample app, keep in mind the following:

* You need to activate the technical preview **SEO-friendly URLs for Reactive Web Apps**. See [the prerequisites](intro.md#prerequisites).
* You can't install the sample app in a Personal Environment, only OutSystems Cloud subscriptions or properly configured self-managed installations.
* The app uses sample data from the OutSystems UI, a default component in OutSystems installations.
* You have some feedback? Great! Use the feedback box in the page to send us a message.

![REST logic to generate the URLs](images/rest-sitemap-ss.png?width=800)
