---
summary: Enter the metadata when creating Screen Templates, to enable the developers to choose the best Screen Template for the Screen they are creating.
locale: en-us
guid: e888ea09-ae0e-4632-9631-5b9abfd1acaf
app_type: traditional web apps, mobile apps, reactive web apps
---

# Metadata reference

Enter the information about the Screen Template, so the developers who want to create Screens know what's its purpose. Set the preview image to showcase the visual elements.

## Preview image

When developers are browsing the Screen Templates in the **New Screen** window they see the preview images, which help them decide whether to use a Screen Template. Scroll down to the metadata section of the Screen Template and select **Change image** in the **Preview** field.

We recommend you use:

* Format: PNG
* Resolution: 1000 x 625 pixels
* Maximum size: 100 KB

Here are some additional notes:

* You can download [these preview image templates](<https://www.outsystems.com/Downloads/ScreenDetails.aspx?MajorVersion=1&ReleaseId=19347>) for web and mobile to create the previews for your Screen Templates.
* Use a mobile frame in the images for better visibility.
* Capture a representative part of the Screen Template and the main content areas.
* Have important interactions like a sidebar or modal captured in the open state.

## Metadata values

Use the values in the fields to enable the developers to browse and find the templates in the **New Screen** window. Enter the values in the **Metadata** section of the Properties Pane.

Property | Description | Value | Notes  
---|---|---|---  
Title | The Screen Template name | Has no specific syntax. For better readability use camel case with separated words. | The title of the template in the **New Screen** window. Mention the main feature of the Screen Template. For example, join information about the data the Screen Template shows and a hint about the UI - like Directory List.  
Tags | The Screen Template tags | Separate by commas, no spaces, and in lowercase. Example: `graph,finance,cash,eating` | The tags help developers find the Screen Template when they search in the **New Screen** window.  
Category | The Screen Template categories | Separate by commas and use no spaces. For better readability use the camel case. Example: `Dashboards,Lists` | The categories are automatically populated in the sidebar of the **New Screen** window.
Description | The Screen Template description| Has no specific syntax. Aim for a short, clear description. | Used when developers search for a Screen Template in **New Screen** window. Include information about the general purpose of the Screen Template, the UI / UX and the logic.
Preview | Preview image | Select **Default image** to use the generic image or **Change image** to upload a new image. | We recommend that you set a preview image for all Screen Templates you design.
