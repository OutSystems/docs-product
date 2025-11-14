---
summary: Learn how to optimize Prerender.io usage and configuration with OutSystems 11 (O11) to minimize costs and improve SEO.
tags: seo optimization, cdn configuration, lambda@edge, prerender.io, cost reduction
locale: en-us
guid: 4E680AB9-9BF6-41B2-9537-C3325FF673F5
app_type: mobile apps, reactive web apps
platform-version: o11
figma:
audience:
  - frontend developers
  - full stack developers
  - platform administrators
outsystems-tools:
  - none
coverage-type:
  - evaluate
---

# Best practices - Prerender.io usage and configuration

Prerender ensures that a cached page is served in response to the user agent's request.
Prerender.io acts like a browser, that is,  it opens the page, waits for the javascript to load, and then adds the page to the cache. Each of these occurrences is counted as a render. A re-cache (manual or automatic) replaces the previous content but is considered a new cache and is charged. To keep the cost to a minimum, limit your caches.
You can adopt the following best practices to keep your Prerender.io costs down. OutSystems recommends periodically monitoring your cache consumption using SEO tools dashboards and Prerender.io to make suitable configuration adjustments.

## Exclude unnecessary content

Exclude pages from your website not displayed in the web search results.  For example, if your website named `www.yourserver.com` has a section  `www.yourserver.com/documents` that can be excluded from the search results, then create a new behavior in your CDN that contains a path pattern `/documents/*` .
If you don’t attach the Lambda@Edge functions you created to them, it will not forward the requests to that path to prerender.io.

## Optimize the number of user agents

You can define the bots to be included in your prerender policy by modifying the Lambda@Edge function. Include only those bots that are necessary to decrease potential costs.

## Adopt cache / re-cache strategy

Since every cache is charged, you must adopt an optimal cache / re-cache strategy to minimize costs.

You can set an automatic re-cache period if your website content changes frequently.  
Use the Prerender.io [recache API](https://docs.prerender.io/docs/6-api) to instantly re-cache new and updated content without requiring additional permissions or access to external tools. With recache API, you can disable automatic cache expiration and re-cache only pages that have changed. This minimizes the number of recaches, thus enabling you to keep your cache and re-cache costs down significantly.

## Update your sitemaps

Prerender.io crawls the active sitemaps weekly and compares cached URLs with those in the sitemaps. If Prerender.io finds any new or updated URLs, it adds them to the priority queue for caching. Hence, you should periodically upload your sitemap to Prerender.io, and activate its synchronization. For more information on the Prerender.io sitemap, see [Sitemap](https://docs.prerender.io/docs/sitemap).

## Provide correct HTTP status codes

If your pages return an HTTP status code other than 200, then add **meta tags** to inform Prerender.io of the correct HTTP status code. These tags allow you to specify an alternative status code or headers for crawlers and override the default behavior of the HTML page that consistently returns a 200 status code. For more information on adding meta tags, see Prerender.io [best practices](https://docs.prerender.io/docs/11-best-practices).
For example, if a page is moved to a new URL, you can keep the old URL with a blank page and return a 301 status code. You can set the meta tags and Prerender.io return a 301 to the crawler with the page's new location.

```
<meta name="prerender-status-code" content="301">

<meta name="prerender-header" content="Location: http://www.yourserver.com">

```

To do that, you can leverage the JavaScript node in Service Studio and add the meta tag to a page if changed its location:

```

var headObject = document.getElementsByTagName("head")[0];

var metaName = "prerender-status-code";

var metaValue = "310";

var metaObject = document.getElementsByName(metaName);

if (metaObject != undefined && metaObject.length != 0) {
 metaObject.forEach((item) => { item.remove() });
}

var metaObject = document.createElement("meta");

metaObject.name = metaName;

metaObject.content = metaValue;

headObject.appendChild(metaObject);

```

Repeat this code for each meta tag you add by replacing the values of variables' metaName and metaValue.
By adding meta tags,  you can ensure that the crawler does not store 200 for a page that changed its location and that the crawler history is accurate.

For more information on Prerender.io best practices, see Prerender.io [best practices](https://docs.prerender.io/docs/11-best-practices).
