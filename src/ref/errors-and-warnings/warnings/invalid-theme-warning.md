# Invalid Theme Warning

Message
:   `The 'Layout' layout of the '<theme_name>' theme must have placeholders named 'Title' and 'MainContent'.`

Cause
:   To set a web block as Layout of a theme, that web block needs to have two placeholders named 'Title' and 'MainContent'.

Recommendation
:   Change the web block to have the 'Title' and 'MainContent' placeholders, or change the theme Layout property to use a web block that already has these placeholders.

---

Message
:   `The '<Info Balloon/Pop-up Editor/Email>' layout of '<theme_name>' theme must have a placeholder named 'MainContent'.`

Cause
:   To set a web block as Info Balloon, Pop-up Editor, or Email layout of a theme, that web block needs to have a placeholder named 'MainContent'.

Recommendation
:   Change the web block to have the 'MainContent' placeholder, or change the theme to use a web block that already has this placeholder.

---

Message
:   `The '<web block>' is not a valid theme Menu.`

Cause
:   To set a web block as Menu layout of a theme, that web block needs to comply with the requirements outlined in the [themes documentation]( https://success.outsystems.com/Documentation/11/Developing_an_Application/Design_UI/Look_and_Feel/Themes#blocks).

Recommendation
:   Edit the web block and design it to comply with the requirements of a Menu Layout or choose another web block. Refer to the existing themes to check the necessary input parameters and entities that should be used in a Menu web block. 
