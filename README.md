# Documentation

This repository holds the source files of the [OutSystems product documentation](https://success.outsystems.com/Documentation). 

Check [how you can contribute](CONTRIBUTING.md).

## Writing

All documentation present in this repository should be written in Markdown (check [here](https://daringfireball.net/projects/markdown/syntax) for the basic syntax).

The Markdown-to-HTML conversion process is done through the Python Markdown package. The following Markdown extensions are currently being used in the conversion step:

Extension | Description
----------|------------
[markdown.extensions.extra](https://python-markdown.github.io/extensions/extra/) | Meta-extension adding support to a series of smaller extensions (check documentation). Currently supports the definition lists syntax.
[markdown.extensions.meta](https://python-markdown.github.io/extensions/meta_data/) | Read metadata from each Markdown front-matter section (discarded in HTML output). Can be used for specifying custom page titles, for example (not used by the default template).
[markdown.extensions.toc](https://python-markdown.github.io/extensions/toc/) | Only used to get automatic bookmarks in headings.
[markdown.blankline](https://github.com/ribalba/markdown.blankline) | Adds Markdown syntax so it is possible to add a blank line (by writing `%%`). Currently used inside table cells.
[markdown-include](https://github.com/cmacmackin/markdown-include) | Include other Markdown files in a given file. [Currently not used]

## Editor settings

Before editing any Markdown document that you wish to push to this repository, you should configure your preferred editor with the following generic settings:

* When the tab key is pressed, insert **4 spaces** instead of a `Tab` character (`.editorconfig` file available for configuring several editors automatically);
* Use soft-wrapping, if available, avoiding carriage returns inside paragraphs.

The 4-spaces setting follows the R&D development recommendations for configuring Visual Studio.

## Recommended editors

### Visual Studio Code

Very powerful and extensible editor. Get it from [here](https://code.visualstudio.com/).

Has Markdown support out-of-the-box, with preview capabilities (just press `Control+K, V` when editing a **saved** `.md` file).

#### Settings

Install [EditorConfig for VS Code](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) extension for handling common editor settings (4 spaces instead of tabs).

**Set up soft-wrapping**

In the same pane (**User Settings**), make sure the following settings are defined:

    {
        (...)            
        "editor.wordWrapColumn": 80,
        "editor.wordWrap": "bounded"
    }

*Note:* For some reason, Markdown documents do not automatically assume these settings. You will have to define a `[markdown]` language definition section with the same settings:

    {
        (These are the 2 settings described above. Mind the new trailing comma after "bounded"!)

        "editor.wordWrapColumn": 80,
        "editor.wordWrap": "bounded",
        "[markdown]": {
            "editor.wordWrapColumn": 80,
            "editor.wordWrap": "bounded"
        }
    }

**Install a spell checker**

1. Open *View > Extensions*.
2. Search and install the offline spell checker by Michael Vernier, called SpellChecker.
3. Reload the window.

### Visual Studio 2017 (with Markdown Editor extension)

If you already use Visual Studio, you can install the [Markdown Editor](https://marketplace.visualstudio.com/items?itemName=MadsKristensen.MarkdownEditor) extension and keep using the same IDE for editing Markdown documents.

#### Settings

Visual Studio 2017 supports EditorConfig out of the box.

### Notepad++

Check the [markdown_npp](https://github.com/Edditoria/markdown_npp) language definition. There's no preview available.

*Note:* it has a few syntax highlighting limitations, when compared with more powerful implementations.

#### Settings

Install the [EditorConfig Notepad++ plugin](https://github.com/editorconfig/editorconfig-notepad-plus-plus) to set up your workspace settings while editing Markdown files in this repository.

### Vim (with `vim-markdown` plugin)

If you use Vim, install the [vim-markdown](https://github.com/plasticboy/vim-markdown) plugin and get a load of new features related to Markdown editing.

*Note:* Mentioning Vim here just for completeness. :)


