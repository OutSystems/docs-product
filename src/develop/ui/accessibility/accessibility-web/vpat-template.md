---
summary: The purpose of the Voluntary Product Accessibility Template, or VPATTM, is to assist Federal contracting officials and other buyers in making preliminary assessments regarding the support given by OutSystems Platform to delivery of accessibility standards compliant applications.
tags: runtime-traditionalweb
locale: en-us
guid: c61481b5-bfd8-4d06-9024-e3185659b455
app_type: traditional web apps
---

# VPAT - Voluntary Product Accessibility Template

<div class="info" markdown="1">

Applies only to Traditional Web Apps

</div>

The purpose of the Voluntary Product Accessibility Template, or VPAT™, is to assist Federal contracting officials and other buyers in making preliminary assessments regarding the support given by OutSystems to delivery of accessibility standards compliant applications.

## Summary Table - Supporting Features

The scope of this VPAT includes the ability to create applications that are Section 508 compliant using OutSystems technology. This applies to the custom applications delivered by OutSystems customers and developers, not to the development toolset (e.g. the visual integrated development environment).

Considering that ultimately every application will be designed, developed and delivered by a specific OutSystems customer, all applicable standards in this VPAT are noted as Supports – meaning OutSystems, as a development platform, fully meets the letter and intent of criteria. Responsibility is left to the developer to use the required constructs, configurations, and design patterns of her/his choice, while abiding to the accessibility compliance requirements. 

| Criteria                                                        | Supporting Features | Remarks and explanations                                                                 |
|-----------------------------------------------------------------|---------------------|------------------------------------------------------------------------------------------|
| Section 1194.21 Software Applications and Operating Systems     | Supports            | OutSystems supports the development of accessible applications that follow this standard |
| Section 1194.22 Web-based Internet Information and Applications | Supports            | OutSystems supports the development of accessible applications that follow this standard |
| Section 1194.23 Telecommunications Products                     | Not Applicable      |                                                                                          |
| Section 1194.24 Video and Multimedia Products                   | Not Applicable      |                                                                                          |
| Section 1194.25 Self-Contained, Closed Products                 | Not Applicable      |                                                                                          |
| Section 1194.26 Desktop and Portable Computers                  | Not Applicable      |                                                                                          |
| Section 1194.31 Functional Performance Criteria                 | Supports            | OutSystems supports the development of accessible applications that follow this standard |
| Section 1194.41 Information, Documentation and Support          | Supports            |                                                                                          |

## Section 1194.21 Software Applications and Operating Systems

| Criteria | Supporting Features | Remarks and explanations|
|----------|---------------------|-------------------------|
| ( a ) When software is designed to run on a system that has a keyboard, product functions shall be executable from a keyboard where the function itself or the result of performing a function can be discerned textually.| Supports| See summary table for remarks |
| ( b ) Applications shall not disrupt or disable activated features of other products that are identified as accessibility features, where those features are developed and documented according to industry standards. Applications also shall not disrupt or disable activated features of any operating system that are identified as accessibility features where the application programming interface for those accessibility features has been documented by the manufacturer of the operating system and is available to the product developer. | Supports | See summary table for remarks |
| ( c ) A well-defined on-screen indication of the current focus shall be provided that moves among interactive interface elements as the input focus changes. The focus shall be programmatically exposed so that Assistive Technology can track focus and focus changes.| Supports| See summary table for remarks |
| ( d ) Sufficient information about a user interface element including the identity, operation and state of the element shall be available to Assistive Technology. When an image represents a program element, the information conveyed by the image must also be available in text.| Supports| See summary table for remarks |
| ( e ) When bitmap images are used to identify controls, status indicators, or other programmatic elements, the meaning assigned to those images shall be consistent throughout an application's performance.| Supports | See summary table for remarks |
| ( f ) Textual information shall be provided through operating system functions for displaying text. The minimum information that shall be made available is text content, text input caret location, and text attributes.| Supports| See summary table for remarks |
| ( g ) Applications shall not override user selected contrast and color selections and other individual display attributes.| Supports| See summary table for remarks |
| ( h ) When animation is displayed, the information shall be displayable in at least one non-animated presentation mode at the option of the user.| Supports| See summary table for remarks |
| ( i ) Color coding shall not be used as the only means of conveying information, indicating an action, prompting a response, or distinguishing a visual element. | Supports| See summary table for remarks |
| ( j ) When a product permits a user to adjust color and contrast settings, a variety of color selections capable of producing a range of contrast levels shall be provided.| Supports| See summary table for remarks |
| ( k ) Software shall not use flashing or blinking text, objects, or other elements having a flash or blink frequency greater than 2 Hz and lower than 55 Hz.| Supports| See summary table for remarks |
| ( l ) When electronic forms are used, the form shall allow people using Assistive Technology to access the information, field elements, and functionality required for completion and submission of the form, including all directions and cues.| Supports| See summary table for remarks |

## Section 1194.22 Web-based Internet information and applications 

The VPAT Board interprets paragraphs (a) through (k) of this section as consistent with the following priority 1 Checkpoints of the Web Content Accessibility Guidelines 1.0 (WCAG 1.0) published by the Web Accessibility Initiative of the World Wide Web Consortium.

OutSystems publishes a set of facilitators and guidelines that, even though not exhaustive or prescriptive, help OutSystems developers to understand how they can use OutSystems’s capabilities to deliver WCAG compliant applications.

The guidelines are published at [https://www.outsystems.com/goto/AccessibilityComplianceGuidelines](https://www.outsystems.com/goto/AccessibilityComplianceGuidelines)

| Criteria | Supporting Features | Remarks and explanations |
|----------|---------------------|--------------------------|
| ( a ) A text equivalent for every non-text element shall be provided (e.g., via "alt", "longdesc", or in element content).| Supports | See remarks in summary table and this section notes |
| ( b ) Equivalent alternatives for any multimedia presentation shall be synchronized with the presentation. | Supports | See remarks in summary table and this section notes |
| ( c ) Web pages shall be designed so that all information conveyed with color is also available without color, for example from context or markup.| Supports | See remarks in summary table and this section notes |
| ( d ) Documents shall be organized so they are readable without requiring an associated style sheet.| Supports | See remarks in summary table and this section notes |
| ( e ) Redundant text links shall be provided for each active region of a server-side image map. | Supports | See remarks in summary table and this section notes |
| ( f ) Client-side image maps shall be provided instead of server-side image maps except where the regions cannot be defined with an available geometric shape.| Supports| See remarks in summary table and this section notes |
| ( g ) Row and column headers shall be identified for data tables.| Supports | See remarks in summary table and this section notes |
| ( h ) Markup shall be used to associate data cells and header cells for data tables that have two or more logical levels of row or column headers.| Supports| See remarks in summary table and this section notes |
| ( i ) Frames shall be titled with text that facilitates frame identification and navigation.| Supports| See remarks in summary table and this section notes |
| ( j ) Pages shall be designed to avoid causing the screen to flicker with a frequency greater than 2 Hz and lower than 55 Hz.| Supports | See remarks in summary table and this section notes |
| ( k ) A text-only page, with equivalent information or functionality, shall be provided to make a web site comply with the provisions of this part, when compliance cannot be accomplished in any other way. The content of the text-only page shall be updated whenever the primary page changes. | Supports| See remarks in summary table and this section notes |
| ( l ) When pages utilize scripting languages to display content, or to create interface elements, the information provided by the script shall be identified with functional text that can be read by Assistive Technology.| Supports| See summary table for remarks  |
| ( m ) When a web page requires that an applet, plug-in or other application be present on the client system to interpret page content, the page must provide a link to a plug-in or applet that complies with §1194.21(a) through (l).| Supports| See remarks in summary table and this section notes |
| ( n ) When electronic forms are designed to be completed on-line, the form shall allow people using Assistive Technology to access the information, field elements, and functionality required for completion and submission of the form, including all directions and cues. | Supports| 	See summary table for remarks  |
| ( o ) A method shall be provided that permits users to skip repetitive navigation links.(p) When a timed response is required, the user shall be alerted and given sufficient time to indicate more time is required.| Supports  | 	See summary table for remarks  |
| ( p ) When a timed response is required, the user shall be alerted and given sufficient time to indicate more time is required.| Supports | 	See summary table for remarks  |

## Section 1194.31 Functional Performance Criteria

| Criteria | Supporting Features | Remarks and explanations |
|----------|---------------------|--------------------------|
| ( a ) At least one mode of operation and information retrieval that does not require user vision shall be provided, or support for Assistive Technology used by people who are blind or visually impaired shall be provided.| Supports | See summary table for remarks |
| ( b ) At least one mode of operation and information retrieval that does not require visual acuity greater than 20/70 shall be provided in audio and enlarged print output working together or independently, or support for Assistive Technology used by people who are visually impaired shall be provided. | Supports | See summary table for remarks |
| ( c ) At least one mode of operation and information retrieval that does not require user hearing shall be provided, or support for Assistive Technology used by people who are deaf or hard of hearing shall be provided.| Supports | See summary table for remarks |
| ( d ) Where audio information is important for the use of a product, at least one mode of operation and information retrieval shall be provided in an enhanced auditory fashion, or support for assistive hearing devices shall be provided.| Supports | See summary table for remarks |
| ( e ) At least one mode of operation and information retrieval that does not require user speech shall be provided, or support for Assistive Technology used by people with disabilities shall be provided.| Supports| See summary table for remarks |
| ( f ) At least one mode of operation and information retrieval that does not require fine motor control or simultaneous actions and that is operable with limited reach and strength shall be provided. | Supports | See summary table for remarks |

## Section 1194.41 Information, Documentation and Support 

| Criteria| Supporting Features | Remarks and explanations|
|---------|---------------------|-------------------------|
| ( a ) Product support documentation provided to endusers shall be made available in alternate formats upon request, at no additional charge.| Supports | End-users with disabilities can request alternative Platform documentation by opening a case through the standard Support channels. Documentation of the delivered apps is responsibility of the Platform customer.|
| ( b ) End-users shall have access to a description of the accessibility and compatibility features of products in alternate formats or alternate methods upon request, at no additional charge. | Supports| Available in the online product documentation. End-users with disabilities can request alternative documentation by opening a case through the standard Support channels. Documentation of the delivered apps is responsibility of the Platform customer. |
| ( c ) Support services for products shall accommodate the communication needs of end-users with disabilities.| Supports | Written and verbal (telephone) support channels are available.|
