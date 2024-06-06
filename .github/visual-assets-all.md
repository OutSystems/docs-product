Validate each of the visual assets in this Pull Request.
If **ALL** changed files are valid, approve and **merge** the pull request, then delete the branch.
A new execution of the workflow will be executed afterwards.

Otherwise, if at least one of the files is **NOT** valid then:

1. If the issue can be fixed in Figma, open the corresponding Figma file and fix it.

After all issues are fixed, add a comment to this pull request with 'Update'. This will trigger a new execution of the workflow.

On the next execution of this workflow, the updated visuals will be exported from Figma and the Pull Request will be created/updated.

---

Each visual asset is identified with a tag.

* **Delete** - No export defined in Figma, and not used in the corresponding Markdown file. Might be used elsewhere.

* **Missing in Figma** - Used in markdown, and exists in the repository, but there is no asset with an export defined in Figma. Confirm if the Figma link is correct, it should direct to the page (canvas) rather than the image (frame).

* **Not used** - Export defined in Figma but the asset is not used in the corresponding Markdown file.

* **Not at top-level** - The export defined in Figma is from an element defined inside another one.

* **Duplicated** - There are multiple elements with the same name. Only one allowed.

* **Hidden** - Element has exports defined but it is hidden.

* **Similarity @ NN %** - Visual mismatch between Figma and the current file in the repository.

Below is a report of the changes in this Pull Request.

---
