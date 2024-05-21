
<details>
<summary>Error details</summary>
<br />

Each visual asset is classified according to the list below:

* **Delete** - No export defined in Figma, and not used in the corresponding Markdown file. Might be used elsewhere.

* **Missing in Figma** - Used in markdown, and exists in the repository, but there is no asset with an export defined in Figma. Confirm if the Figma link is correct, it should direct to the page (canvas) rather than the image (frame).

* **Not used** - Export defined in Figma but the asset is not used in the corresponding Markdown file.

* **Not at top-level** - The export defined in Figma is from an element defined inside another one.

* **Duplicated** - There are multiple elements with the same name. Only one allowed.

* **Hidden** - Element has exports defined but it is hidden.

* **Similarity @ NN %** - Visual mismatch between Figma and the current file in the repository.

</details>
