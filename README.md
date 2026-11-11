# Jason Amo-Mensah — Portfolio

A readable, understated portfolio for product analytics, digital strategy, information systems, and frontend work. A clean system font, 17px body text, restrained headings, neutral colors, and simple dividers keep the focus on the content. The production site is plain HTML, CSS, JavaScript, and a downloadable resume PDF. There are no runtime packages, external fonts, trackers, or API keys.

## Preview

From the repository root:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open <http://127.0.0.1:8765>. Every page also works as static files. Email opens the visitor’s mail application; LinkedIn and GitHub links open the corresponding public profiles.

## Content and shared components

- `scripts/build.py` contains the shared page shell, navigation, footer, and page composition.
- `templates/projects.json` holds project summaries, roles, dates, responsibilities, methods, and outcomes.
- `templates/case-imageomics.html` contains the detailed HDR/Imageomics case. It describes contributions without displaying or linking to organizational source code.
- `assets/css/style.css` defines readable typography, consistent spacing, responsive layouts, focus states, reduced motion, and print styles.
- `assets/js/main.js` progressively enhances mobile navigation and case-study section highlighting.
- The nine committed HTML files are the deployable output. They include complete content and navigation without JavaScript.

After changing content or shared components:

```sh
python3 scripts/build.py
python3 scripts/check_site.py
```

Do not edit generated HTML alone; rebuilds will replace those edits. Keep any resume changes consistent with the readable text version on `resume.html`.

## Resume PDF

`resume.pdf` was rebuilt using facts in the supplied redesign brief and confirmed case-study content. It replaces an older PDF that listed PNC as incoming and showed a different GPA. The new PDF uses the completed June–August 2026 PNC role, May 2027 expected graduation, and 3.5 GPA. It omits older numerical claims not confirmed by the brief.

To regenerate the PDF, install the optional authoring tool in your own Python environment:

```sh
python3 -m pip install 'reportlab>=4,<5'
python3 scripts/build_resume.py
```

ReportLab is an authoring dependency only. Visitors and GitHub Pages do not need it. For future updates, confirm the source facts before rebuilding. The HTML resume includes a complete readable text version and direct PDF links for browsers without an embedded PDF viewer.

## Validation

```sh
python3 scripts/check_site.py
node --check assets/js/main.js
```

Additional optional checks used for this redesign:

- HTML: `html-validate` 9.7.1, default recommended rules, across all nine HTML files.
- CSS: `tinycss2` syntax parsing, plus rendering in Chrome.
- Browser: Python Playwright with the locally installed Google Chrome; all nine pages at 1440, 768, 390, and 320 CSS pixels.
- Accessibility: `axe-core` WCAG 2 A/AA and 2.1 AA rules, all nine pages at desktop and mobile sizes.

To reproduce browser QA, install Playwright and axe-core in an isolated tooling environment, start the preview server, and run:

```sh
python3 scripts/browser_qa.py /absolute/path/to/axe-core/axe.min.js
```

The browser script currently points to the macOS Google Chrome installation. Adjust `executable_path` for another system. It verifies responsive overflow, page loading, mobile navigation, Escape/focus behavior, skip links, case anchors, PDF download, reduced motion, and navigation without JavaScript. Automated checks supplement a manual review; they do not replace assistive-technology testing.

See [the redesign report](docs/REDESIGN.md) for scope, source decisions, and validation details.

## Deploy through GitHub Pages

1. Review and merge the redesign pull request into `main`.
2. In the GitHub repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select `main` and `/(root)`, then save.
5. Wait for GitHub’s Pages deployment to finish and open the URL shown in Settings.

The conventional project-site address is `https://jasonam84.github.io/jason-portfolio/`; use the URL GitHub actually reports, especially if a custom domain is configured. Relative asset and page links support this repository subpath. `.nojekyll` keeps publishing static. No build command or dependency installation is needed for deployment. If the repository already uses a custom Pages workflow, keep its settings and publish the repository root as the artifact.

The redesign branch is for review. Opening the pull request does not deploy or merge it. To roll back after a merge, revert the merge commit and let Pages republish the previous version.
