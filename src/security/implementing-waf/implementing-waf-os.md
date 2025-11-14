---
summary: Explore how OutSystems 11 (O11) integrates with a Web Application firewall.
tags: web application security, waf configuration, api protection, http/https traffic monitoring, compliance standards
locale: en-us
guid: 453F8846-CBCE-412D-8E59-2F12C1A5E489
app_type: traditional web apps, reactive web apps
platform-version: o11
figma:
audience:
  - platform administrators
  - full stack developers
  - backend developers
  - tech leads
  - infrastructure managers
outsystems-tools:
  - none
coverage-type:
  - understand
---

# Web Application Firewall in OutSystems

A Web Application Firewall (WAF) is a security system that monitors, filters, and blocks HTTP/HTTPS traffic to and from a web application.
Its primary purpose is to protect web applications from various threats and vulnerabilities, such as:

* SQL Injection. An attack where malicious SQL statements are inserted into an entry field for execution.
* Cross-Site Scripting (XSS). An attack where malicious scripts are injected into otherwise benign and trusted websites.
* Cross-Site Request Forgery (CSRF). An attack that tricks the user into executing unwanted actions on a web application in which they are authenticated.
* File Inclusion. Attacks that allow an attacker to include a file on the web server through the web browser.

A WAF operates by applying a set of rules to an HTTP conversation. These rules cover common attacks such as cross-site scripting (XSS) and SQL injection.
By customizing these rules, a WAF can provide protection tailored to a specific web application.

## Key features of a WAF

* Filtering and Monitoring. WAFs analyze the incoming and outgoing traffic between the web application and the internet.
* Rule-Based Protection. They operate based on predefined security rules to identify and block malicious traffic.
* Real-Time Protection. WAFs provide real-time monitoring and response to security threats.
* Compliance. WAFs help in meeting compliance requirements for data protection and privacy standards.
* Logging and Reporting. WAFs log malicious traffic and provide reports for further analysis.

## Types of WAF

* Network-Based WAF. Installed on a network, providing high-speed security, but requiring hardware.
* Host-Based WAF. Integrated into the application itself, providing more granular control but consuming local server resources.
* Cloud-Based WAF. Provided as a service by third-party vendors, easy to deploy, and manage with no hardware requirements.

WAFs are an essential component in a layered defense strategy, providing specialized protection for web applications against a wide range of attacks.

## Understanding and keeping up with OWASP Top 10

Open Worldwide Application Security Project (OWASP) is a nonprofit foundation that works to improve the security of software.
The OWASP Top 10 is a standard awareness document for developers and web application security. It represents a broad consensus about the most critical security risks to web applications.
Every few years the OWASP foundation releases the Top 10 attack vectors in Web Applications.
Keeping up with these attacks is paramount to understanding what kind of attacks we want to protect our applications with WAF rules.
You can find more about this in [OWASP](https://owasp.org/www-project-top-ten/).
