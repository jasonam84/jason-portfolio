# Portfolio design and validation notes

## Current visual direction

The latest revision prioritizes readability and a traditional professional portfolio layout. Every page uses a clean system font stack, 17px body copy at approximately 1.65 line height, restrained heading sizes, and consistent margins. Article text stays within 720px; the overall site width is capped at 1040px.

Palette:

- Background: `#FAFAF8`
- Primary text: `#242424`
- Secondary text: `#626262`
- Borders: `#E5E5E1`
- Accent and links: `#365B78`

The oversized serif name, artistic type treatment, tiny labels, display numerals, tinted feature panel, and asymmetric editorial offsets were replaced. There are no gradients, shadows, decorative illustrations, pill tags, moving hover effects, or UI component libraries. Links use underlines, and dividers separate related content without enclosing everything in cards.

## Pages

- **Home:** A modest name heading and personal introduction, followed by PNC and Imageomics features with factual scope, two additional projects, experience, skills, and contact information.
- **Work:** A readable index of all four projects, with PNC and Imageomics featured first.
- **About:** Personal background and approach, with education details beside the narrative on desktop and after it on mobile.
- **Case studies:** Clear headings, role/date metadata, factual scope, article contents, readable prose, documented contributions, tools, results, and reflections. No fabricated project artifacts or process diagrams.
- **Resume:** Readable HTML resume, prominent PDF download, and embedded PDF with fallback links.
- **Contact:** Direct email and profile links in a simple directory.

On narrow screens, projects, experience, capabilities, scope summaries, and resume sections flow vertically. Mobile navigation retains a keyboard-accessible menu with Escape-to-close and focus return. Navigation also works without JavaScript.

## Accurate information and functionality

The supplied brief and existing repository remain factual sources. The Imageomics update was checked against both projects’ histories and reviews. Organizational source links, commit identifiers, and branch names are omitted from the public portfolio. PNC dates and scope, Imageomics platform details, ODOT’s approximately 25% reporting-time reduction, education, GPA, and supported skills are preserved. PNC activity figures are distinguished from conversion outcomes. Internal customer data and proprietary screenshots are omitted. The NSF HDR platform is distinguished from the separate ongoing Imageomics Institute redesign.

The previously updated one-page resume PDF is preserved. Existing page URLs, contact destinations, anchored contents, section highlighting, PDF download, readable resume fallback, skip link, reduced motion, and print styling are retained. The site remains static HTML/CSS/JavaScript, compatible with GitHub Pages without a hosting build step.

## Verification of this revision

- All nine HTML pages pass `html-validate` recommended rules.
- JavaScript syntax passes `node --check`.
- CSS parses without syntax errors with `tinycss2`.
- Local pages, assets, PDF links, fragments, IDs, landmarks, language, metadata, and content guardrails pass `scripts/check_site.py`.
- Text contrast against the background is 14.85:1 for primary text, 5.84:1 for secondary text, and 6.87:1 for the accent. Each exceeds WCAG AA’s 4.5:1 requirement for normal text.
- Responsive rules were reviewed for desktop, tablet, and mobile widths, including stacking, navigation, reading widths, and text sizes.

Earlier revisions were tested in Chrome at 1440, 768, 390, and 320px with axe and interaction checks. Those results do not verify this latest layout. The most recent requested browser run was declined; browser rendering and automated accessibility scans were not rerun for this revision. Physical devices, Safari, Firefox, and screen readers have not been tested.

## Source and deployment

Shared page composition is in `scripts/build.py`; case data is in `templates/projects.json`. All nine generated HTML files are committed for direct hosting. The local workspace contains the current output, and a separate Git checkout at `/tmp/jason-portfolio-review` holds the review branch `redesign/product-portfolio`.

No main-branch merge or Pages deployment is part of this change. The connected GitHub integration previously returned a 403 when creating a pull request. See README.md for local preview, content regeneration, and GitHub Pages deployment instructions.
