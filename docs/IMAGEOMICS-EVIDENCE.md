# Imageomics and HDR case-study evidence

Reviewed November 10, 2026. Source code and full Git histories were read from both public repositories. GitHub connector searches were used to locate Jason’s PRs, then local diffs, blame, branch containment, and reviews were checked to separate attribution from merge status.

## Separate projects

- [HDR Ecosystem](https://github.com/HDR-Ecosystem/hdr-website): the NSF community platform, with five institutes and existing challenge content preceding Jason’s redesign. Reviewed main at `d049831450870bcb6904ee87b394ca19b1c41d54`.
- [Imageomics Institute](https://github.com/Imageomics/imageomics.github.io): a separate website. Its README explicitly credits HDR’s header, footer, and search as the starting point. Reviewed main at `c4842d7edbb264a32f42f329b43b2e0dfab9b699` and development branches, including mobile-fixes at `c9889e063728ea07532abdb548ced21cbb2f2376`.

Main-branch containment establishes that a change is included in the reviewed default branch. It is not independent verification of the current deployed website.

## Evidence used

| Claim | Evidence | Attribution/status |
| --- | --- | --- |
| Initial HTML/CSS/JS frontend implementation | [August 2025 page-build commit](https://github.com/HDR-Ecosystem/hdr-website/commit/e9bf68fe7682d364522f856a0330883aa6e29afb), [redesign PR #4](https://github.com/HDR-Ecosystem/hdr-website/pull/4) | Jason; included in HDR main |
| Event search, institute/type filters, pagination | [Initial events implementation](https://github.com/HDR-Ecosystem/hdr-website/commit/30b38adb024491a6d0a4d72d183171efbc226e15) | Jason; included in HDR main |
| Search URL resolution and results handling | [December fixes](https://github.com/HDR-Ecosystem/hdr-website/commit/db173e871eaae189a38537bb36d7190358a09961) | Jason; included in HDR main |
| Search normalization, page discovery, dynamic event indexing | `git blame` of HDR `js/script.js` attributes these functions to Jason’s February 15 commit `e1c519d8` | Jason; included in HDR main |
| Header/search initialization fixes | [February fixes](https://github.com/HDR-Ecosystem/hdr-website/commit/f3e744d241800b25481bae4d15b8a553a064c101) | Jason; included in HDR main |
| Initial modular loader | [PR #63](https://github.com/HDR-Ecosystem/hdr-website/pull/63), commits `bb9460c`, `769f52f` | Authored by copilot-swe-agent, merged by Jason; not credited as Jason’s original implementation |
| Dynamic homepage event selection | [Homepage/event update](https://github.com/HDR-Ecosystem/hdr-website/commit/d8f56dc8b44733846d9519b1b97d6cb3fb3bc193) | Jason; included in HDR main |
| Mobile event/news page sizes and reduced button list | [Mobile fixes](https://github.com/HDR-Ecosystem/hdr-website/commit/dcc4292976e366ab9a8d7636359a3c84656472a7), [PR #102](https://github.com/HDR-Ecosystem/hdr-website/pull/102) | Jason; included in HDR main; review approval from egrace479 |
| Year 2 leaderboard/winners website work | [PR #100](https://github.com/HDR-Ecosystem/hdr-website/pull/100) | Jason’s website work; no claim to research or competition results |
| Removing confusing challenge controls | [Maintainer change](https://github.com/HDR-Ecosystem/hdr-website/commit/83f7faf8298542a1572b703f096b910137ffb87d) | egrace479; explicitly presented as a team decision, not Jason’s implementation |
| Later link maintenance | [PR #107](https://github.com/HDR-Ecosystem/hdr-website/pull/107), [PR #108](https://github.com/HDR-Ecosystem/hdr-website/pull/108) | Jason; included in HDR main |
| Imageomics redesign/content work | [PR #1](https://github.com/Imageomics/imageomics.github.io/pull/1), [PR #3](https://github.com/Imageomics/imageomics.github.io/pull/3) | Jason-authored work in main; stakeholder review thread on news wording was resolved by Jason |
| Imageomics news/events pagination correction | [July fix](https://github.com/Imageomics/imageomics.github.io/commit/de93fd6d1bd391157127d45285fa05329ea24aae) | Jason; included in Imageomics main |
| Search upgrades and indexing tools | Commits `7f5c3ab`, `66abb54`; [post-release PR #9](https://github.com/Imageomics/imageomics.github.io/pull/9) | Jason; present on post-release-1/mobile-fixes, absent from reviewed Imageomics main |
| Mobile image, focus, and carousel work | Commits `31f105f`, `bf91673`, `4dab610`, `c9889e0`; [PR #13](https://github.com/Imageomics/imageomics.github.io/pull/13) | Jason; development-branch work, not described as shipped |

## Claims that need context beyond Git

The original brief and existing portfolio supply the Google Sites migration background, designer collaboration, employment title, and June 2025 start date. Git alone cannot establish user pain, usability improvement, employment dates, or authorship of every design decision. Those facts were retained conservatively from the supplied material rather than treated as discoveries from commit messages.

The current HDR tree contains 36 HTML files including supporting files; the portfolio retains the existing conservative “30+ page platform” scope instead of presenting a newly invented page-count achievement. Five institutes are named in the HDR README. Neither number is a measured outcome.

No quantitative claims about traffic, conversion, task time, approval speed, or usability were added. No claim of sole authorship, ownership of the research, or completion of every Imageomics branch was added. The source repositories were not modified.

## Portfolio implementation

- `templates/case-imageomics.html` holds the dedicated technical case study and public evidence links.
- `templates/projects.json` supplies the concise internship/resume responsibilities and experience summary.
- Home and Work introduce the project briefly; the case gives the implementation details and tradeoffs.
- The About paragraph and both HTML/PDF resumes remain consistent with the two-project scope.
- Current typography and layout remain unchanged apart from spacing for the added experience summary.

Verification: all nine generated pages pass HTML validation and the local-link/content checker. The updated PDF remains one page and contains the new responsibilities. Browser testing was not rerun for this content change.
