// MD033_INLINE_HTML
// CLI1-compatible version of markdownlint's MD033 with nested element support

// 📘 Rule: MD033_NESTED_INLINE_HTML
// Description: Extended version of MD033(no - inline - html) that allows nested element validation and differentiates between HTML and Markdown table contexts.
// This rule lets you:
// Whitelist allowed HTML tags globally.
// Define special exceptions for Markdown tables(table_allowed_elements).
// Specify what HTML elements are allowed inside specific parent tags(nested_allowed_elements).
// ⚙️ Configuration Example
// In your.markdownlint.json or.markdownlint - cli2.jsonc:
// {
//     "no-inline-or-nested-html": {
//         // ✅ Global allowed tags (always permitted)
//         "allowed_elements": [
//             "div",
//             "br",
//             "tr",
//             "th",
//             "td",
//             "table",
//             "thead",
//             "tbody"
//         ],
//         // ✅ Elements allowed only inside *Markdown* tables (| syntax), not <table>
//         "table_allowed_elements": [
//             "strong",
//             "em"
//         ],
//         // ✅ Allowed nested elements (parent -> allowed children)
//         "nested_allowed_elements": {
//             "td": ["strong", "a", "code", "b"],
//             "th": ["strong", "a", "code", "b"]
//         }
//     }
// }


"use strict";

function addErrorContext(onError, lineNumber, detail, range) {
    onError({ lineNumber, detail, range });
}

/**
 * Extract tag name and whether it's a closing tag.
 */
function getHtmlTagInfo(text) {
    const htmlTagNameRe = /^<\s*(\/?)([a-zA-Z0-9-]+)/;
    const match = htmlTagNameRe.exec(text);
    if (!match) return null;
    return { close: !!match[1], name: match[2].toLowerCase() };
}

/**
 * Returns ranges of inline code spans in a line.
 */
function getCodeSpans(line) {
    const codeSpans = [];
    const codeRe = /(`+)([\s\S]*?)(\1)/g;
    let match;
    while ((match = codeRe.exec(line)) !== null) {
        codeSpans.push([match.index, match.index + match[0].length]);
    }
    return codeSpans;
}

/**
 * Check if a given index is inside any range.
 */
function isInsideRanges(index, ranges) {
    return ranges.some(([start, end]) => index >= start && index < end);
}

module.exports = {
    names: ["MD033_INLINE_HTML", "no-inline-or-nested-html"],
    description: "Inline HTML with nested-element restrictions (extends MD033)",
    tags: ["html"],
    function: function MD033_INLINE_HTML(params, onError) {
        // Normalize allowed elements
        let allowedElements = params.config.allowed_elements;
        allowedElements = Array.isArray(allowedElements)
            ? allowedElements.map((e) => e.toLowerCase())
            : [];

        // Normalize markdown-table-specific allowed elements
        let tableAllowedElements = params.config.table_allowed_elements;
        tableAllowedElements = Array.isArray(tableAllowedElements)
            ? tableAllowedElements.map((e) => e.toLowerCase())
            : [];

        // Normalize nested allowed mapping
        const allowedNestedElements = params.config.nested_allowed_elements || {};
        const normalizedNested = {};
        for (const [parent, children] of Object.entries(allowedNestedElements)) {
            normalizedNested[parent.toLowerCase()] = (children || []).map((c) =>
                c.toLowerCase()
            );
        }

        const lines = params.lines;
        const tagStack = [];
        const htmlTagRe = /<\s*\/?\s*([a-zA-Z0-9-]+)[^>]*>/g;

        for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const lineNumber = i + 1;
            const codeSpans = getCodeSpans(line);
            let match;

            while ((match = htmlTagRe.exec(line)) !== null) {
                const fullTag = match[0];
                const tagIndex = match.index;

                // Skip HTML-like tags inside inline code spans
                if (isInsideRanges(tagIndex, codeSpans)) continue;

                const info = getHtmlTagInfo(fullTag);
                if (!info) continue;
                const { name: elementName, close } = info;

                const currentParent =
                    tagStack.length > 0 ? tagStack[tagStack.length - 1] : null;

                // Pop closing tags
                if (close) {
                    const idx = tagStack.lastIndexOf(elementName);
                    if (idx !== -1) tagStack.splice(idx, 1);
                    continue;
                }

                // If globally allowed, skip all deeper checks
                const isGloballyAllowed = allowedElements.includes(elementName);
                if (isGloballyAllowed) {
                    if (!/\/>$/.test(fullTag)) tagStack.push(elementName);
                    continue;
                }

                // Determine if we're in a Markdown table context (not HTML <table>)
                const isMarkdownTableContext =
                    params &&
                    params.configInlines &&
                    params.configInlines.inMarkdownTable === true;

                // Check if this element is allowed in a Markdown table context
                const allowedInMarkdownTable =
                    isMarkdownTableContext &&
                    tableAllowedElements.includes(elementName);

                // Check if allowed inside its parent by nested rules
                const allowedInParent =
                    currentParent &&
                    normalizedNested[currentParent] &&
                    normalizedNested[currentParent].includes(elementName);

                // In HTML tables, only nested_allowed_elements rules apply (not table_allowed_elements)
                const allowedInHTMLTable =
                    currentParent === "table" && allowedInMarkdownTable;

                if (!allowedInMarkdownTable && !allowedInParent && !allowedInHTMLTable) {
                    const detail = currentParent
                        ? `Element <${elementName}> not allowed inside <${currentParent}>`
                        : `Element <${elementName}> not allowed`;
                    const range = [tagIndex + 1, fullTag.length];
                    addErrorContext(onError, lineNumber, detail, range);
                }

                // Push non-self-closing tags
                if (!/\/>$/.test(fullTag)) {
                    tagStack.push(elementName);
                }
            }
        }
    },
};
