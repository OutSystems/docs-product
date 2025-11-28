// CLI1-compatible MD025_PAGE_BREAKS

function addErrorContext(onError, lineNumber, text) {
    onError({ lineNumber, detail: text });
}

function getFrontMatterTitle(lines) {
    if (lines[0] === '---') {
        let title = '';
        for (let i = 1; i < lines.length; i++) {
            const line = lines[i];
            if (/^title\s*:\s*(.+)/i.test(line)) {
                title = line.replace(/^title\s*:\s*/i, '').trim();
            }
            if (lines[i] === '---') break;
        }
        return title;
    }
    return '';
}

module.exports = {
    names: ["MD025_PAGE_BREAKS", "single-title-page-breaks", "single-h1-page-breaks"],
    description: "Allow multiple headings of configurable level if separated by page breaks",
    tags: ["headings", "page-breaks"],

    function: function MD025_PAGE_BREAKS(params, onError) {
        const lines = params.lines;
        const level = Number(params.config.level || 1); // configurable heading level

        let sectionHeadings = [];
        let inTabBlock = false;
        let inFencedBlock = false;

        const frontMatterTitle = params.config.front_matter_title === '' ? getFrontMatterTitle(lines) : '';
        if (frontMatterTitle && level === 1) {
            sectionHeadings.push({ lineNumber: 1, text: frontMatterTitle });
        }

        for (let i = 0; i < lines.length; i++) {
            const lineNumber = i + 1;
            const rawLine = lines[i];
            const line = rawLine.trim();

            // DocFX tab blocks
            if (/^:::/.test(line)) {
                inTabBlock = !inTabBlock;
                continue;
            }
            if (inTabBlock) continue;

            // Detect start/end of fenced code blocks (``` or ~~~)
            if (/^\s*(```|~~~)/.test(rawLine)) {
                inFencedBlock = !inFencedBlock;
                continue;
            }

            // Skip all content inside code fences
            if (inFencedBlock) continue;

            // Skip HTML comments
            if (/^<!--.*-->$/.test(line)) continue;

            // Skip non-content lines
            if (/^\s*$/.test(line)) continue;

            // Page break detection
            const isPageBreak =
                /^\s*---\s*$/.test(line) ||
                /^\s*<!--\s*PAGE BREAK\s*-->\s*$/.test(line);

            if (isPageBreak) {
                if (sectionHeadings.length > 1) {
                    sectionHeadings.slice(1).forEach(h =>
                        addErrorContext(onError, h.lineNumber, h.text)
                    );
                }
                sectionHeadings = [];
                continue;
            }

            // ATX heading detection
            const atxMatch = new RegExp(`^#{${level}}\\s+(.*)`).exec(line);
            if (atxMatch) {
                const headingText = atxMatch[1].trim();
                sectionHeadings.push({ lineNumber, text: headingText });
                if (sectionHeadings.length > 1) {
                    addErrorContext(onError, lineNumber, headingText);
                }
                continue;
            }

            // Setext heading detection
            if (i + 1 < lines.length) {
                if (level === 1 && /^=+$/.test(lines[i + 1].trim())) {
                    const headingText = line;
                    sectionHeadings.push({ lineNumber, text: headingText });
                    if (sectionHeadings.length > 1) {
                        addErrorContext(onError, lineNumber, headingText);
                    }
                    i++;
                    continue;
                } else if (level === 2 && /^-+$/.test(lines[i + 1].trim())) {
                    const headingText = line;
                    sectionHeadings.push({ lineNumber, text: headingText });
                    if (sectionHeadings.length > 1) {
                        addErrorContext(onError, lineNumber, headingText);
                    }
                    i++;
                    continue;
                }
            }
        }
    }
};
