# Redesign implementation report

## Source inspection and delivery

Inspected the workspace’s seven original HTML pages, CSS, JavaScript, SVG favicon, editor configuration, and resume PDF. The workspace was an exported folder without `.git`. A separate checkout of `jasonam84/jason-portfolio` was created, based on `main` at `94a4732`, with branch `redesign/product-portfolio`. The local folder included newer wording on the homepage, About page, and Imageomics case than the remote main branch; that content and the supplied brief informed the redesign. The supplied brief controls current dates, role names, and factual corrections.

## Retained

- Static HTML/CSS/JavaScript architecture and GitHub Pages compatibility.
- All seven existing HTML URLs and `resume.pdf`.
- Existing favicon, contact email, and LinkedIn profile.
- Research platform detail supported by the original case: Google Sites-to-GitHub migration, 30+ pages, five institutes, designer collaboration, shared components, search, pagination, and legacy paths.
- Case-study in-page navigation, now consistently implemented across all four cases.

## Replaced and added

- Replaced the narrow text-heavy layout with a warm off-white, navy, and blue design system, responsive grids, project illustrations, impact metrics, and restrained hover transitions.
- Added a new PNC case, Contact page, clear five-item site navigation, accessible mobile menu, skip link, reduced-motion rules, and print styles.
- Rewrote the homepage, Work, About, Resume, and all project cases with the supplied positioning and confirmed facts.
- Added seven substantive sections to each case: overview, opportunity, responsibilities, approach, tools, results, and lessons.
- Made PNC the first project and experience, with 400+ session replays, 40+ funnels, and 3,000+ comments. These are activity/scope figures, not conversion results.
- Used an approximately 25% reporting-time reduction for ODOT, with no additional efficiency or accuracy claim.
- Added a downloadable one-page resume, PDF preview with fallback links, and full HTML text version.
- Added reusable Python page generation and centralized case-study data. Generated HTML is committed; no build process is required for hosting.
- Added local-link/content validation and optional browser QA scripts.

## Removed or superseded

- Outdated “junior” descriptions and incoming PNC status.
- Old unsupported resume outcomes, including navigation-time, approval, audit-readiness, and social-engagement percentages not confirmed by the current brief.
- Old visibility-dependent reveal effects that hid content when JavaScript failed.
- Unused progress, diagram-toggle, and roadmap-toggle code. The old source did not contain the matching controls; shared case navigation and native disclosure elements cover the useful behavior.
- Excessive case-study headings and repeated explanatory copy. Useful research implementation detail remains in a dedicated section.

No company excluded by the brief appears in the website or new PDF. No internal PNC screens, findings, customer records, or fabricated research artifacts are included. All project artwork is conceptual HTML/CSS illustration, rather than claimed screenshots. The research platform case is distinguished from the separate ongoing Imageomics Institute redesign.

## Resume decisions

The original PDF was inspected by extracting its text. It listed a 3.6 GPA and an incoming PNC role in May 2026. The new PDF and HTML resume use the brief’s 3.5 GPA, completed PNC role in June–August 2026, degree specialization, and expected May 2027 graduation. Older activities were omitted to keep the new resume focused and avoid implying unverified current participation. SQL and Tableau are supported by the original PDF; Glassbox and Qualtrics Text iQ are supported by the brief. No proficiency levels are asserted.

## Verification completed

- All nine HTML pages pass `html-validate` 9.7.1 default recommended rules, with zero errors or warnings.
- Shared JavaScript passes `node --check`.
- CSS parses with `tinycss2` without syntax errors and renders in Chrome.
- All relative document, asset, PDF, and fragment references pass the dependency-free site checker.
- Browser checks pass on all nine pages at 1440, 768, 390, and 320 pixels, with visible content and no horizontal document overflow.
- Axe WCAG 2 A/AA and 2.1 AA scans pass on every page at 1440 and 390 pixels, with zero reported violations. Two initially low-contrast illustration labels were darkened before the final passing run.
- Mobile menu opens and closes; Escape returns focus to the trigger; Work navigation succeeds.
- Skip link moves focus to main content; reduced motion disables smooth scrolling; navigation remains available with JavaScript disabled.
- Case anchors resolve, and the resume download uses `Jason-Amo-Mensah-Resume.pdf`.
- The replacement PDF extracts as one page, with confirmed dates, role information, GPA, and skills.
- Desktop and mobile homepage screenshots were visually inspected.

## Limits

Browser QA used desktop Chrome with simulated viewport widths. Safari, Firefox, physical devices, and screen readers were not tested. Axe checks do not constitute a complete accessibility audit. External mail/profile links were preserved from the source; remote destinations were not exhaustively checked. No main-branch merge or Pages deployment is performed as part of this review delivery.
