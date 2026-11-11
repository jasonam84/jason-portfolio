"""Build the readable professional portfolio. Generated pages need no runtime dependencies."""
from pathlib import Path
from html import escape as e
import json
import re
ROOT = Path(__file__).resolve().parents[1]
PROJECTS = json.loads((ROOT / 'templates/projects.json').read_text())
NAV = [('Home', 'index.html'), ('Work', 'work.html'), ('About', 'about.html'), ('Resume', 'resume.html'), ('Contact', 'contact.html')]


def page(file, title, description, body, active=None):
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url == (active or file) else '')+f'>{label}</a>' for label, url in NAV)
    output = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)} | Jason Amo-Mensah</title>
<meta name="description" content="{e(description)}">
<meta name="theme-color" content="#FAFAF8">
<meta property="og:title" content="{e(title)} | Jason Amo-Mensah">
<meta property="og:description" content="{e(description)}">
<meta property="og:type" content="website">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="stylesheet" href="assets/css/style.css">
<script src="assets/js/main.js" defer></script>
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="header"><nav class="nav wrap" aria-label="Main navigation">
<a class="brand" href="index.html">Jason Amo-Mensah</a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" hidden>Menu</button>
<div class="nav-links" id="nav-links">{nav}</div>
</nav></header>
<main id="main" class="wrap" tabindex="-1">{body}</main>
<footer class="footer wrap"><p>Jason Amo-Mensah<br><span>Ohio State · Class of 2027</span></p><div><a href="mailto:jasonam84@gmail.com">Email</a><a href="https://www.linkedin.com/in/jasonamomensah">LinkedIn</a><a href="https://github.com/jasonam84">GitHub</a></div><small>© <span id="year">2026</span></small></footer>
</body>
</html>'''
    output = re.sub(r'&(?!#?\w+;)', '&amp;', output)
    output = re.sub(r'(?<=>)(?=<(?:section|/section|article|/article|aside|/aside|nav|/nav|header|/header|footer|/footer|div|/div|h[1-3]|p|dl|ol|ul|li|details|summary)\b)', '\n', output)
    (ROOT / file).write_text(output + '\n')


def metrics(items):
    return '<dl class="metrics">' + ''.join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a, b in items) + '</dl>'


def contact():
    return '''<section class="closing"><h2>Get in touch</h2><p>I’m interested in opportunities in product management, business analytics, and digital strategy.</p><a class="email-link" href="mailto:jasonam84@gmail.com">jasonam84@gmail.com</a><p><a href="contact.html">Other ways to connect</a></p></section>'''


def skills():
    groups = [('Product & strategy', 'Product Analytics, Customer Experience, Voice of Customer, Funnel Analysis, Stakeholder Communication, Process Improvement'), ('Data & analytics', 'SQL, Excel, Tableau, Qualtrics Text iQ, Glassbox'), ('Technology', 'HTML, CSS, JavaScript, GitHub, Website Development')]
    return '<dl class="capabilities">' + ''.join(f'<div><dt>{e(name)}</dt><dd>{e(items)}</dd></div>' for name, items in groups) + '</dl>'


def experience():
    return '<div class="experience-list">' + ''.join(f'''<article class="experience-row"><p class="experience-date">{e(p['date'])}</p><div><h3><a href="{p['slug']}">{e(p['org'])}</a></h3><p>{e(p['role'])}</p>{f'<p class="experience-summary">{e(p["experience_summary"])}</p>' if p.get('experience_summary') else ''}</div></article>''' for p in PROJECTS) + '</div>'


def featured_work():
    return '''<article class="feature feature-pnc"><div class="feature-index"><span>PNC Financial Services</span><span>Summer 2026</span></div><div class="feature-main"><div><p class="label">Digital product · Insights & optimization</p><h3><a href="case-pnc.html">Digital banking experience analysis</a></h3><p>Where do customers get stuck? I used session replays, funnel analysis, and customer feedback to help digital product teams understand the friction.</p><a class="read-link" href="case-pnc.html">Read the PNC case study <span aria-hidden="true">↗</span></a></div><aside class="scope-note" aria-label="PNC analysis scope"><p class="label">The scope of the work</p>''' + metrics(PROJECTS[0]['metrics']) + '''<p class="note">Analysis volume, rather than measured changes in conversion.</p></aside></div></article>
<article class="feature feature-hdr"><div class="feature-index"><span>Ohio State · Imageomics Institute</span><span>2025–Present</span></div><div class="hdr-layout"><aside class="platform-scope" aria-label="Research platform scope"><h4>Project scope</h4><dl class="metrics"><div><dt>30+ pages</dt><dd>rebuilt and migrated</dd></div><div><dt>5 institutes</dt><dd>served by one research platform</dd></div></dl><p>Google Sites to GitHub migration</p></aside><div class="hdr-story"><p class="label">Website & platform development</p><h3><a href="case-imageomics.html">NSF HDR platform development & redesign</a></h3><p>I implemented frontend pages and features for the HDR research community, then continued improving search, event listings, mobile layouts, and links. I also contribute to the separate Imageomics Institute website.</p><a class="read-link" href="case-imageomics.html">Read the NSF HDR case study <span aria-hidden="true">↗</span></a></div></div></article>'''


def other_work():
    return '''<div class="other-work"><p class="label">Other projects</p><div><article><span class="work-year">2025</span><h3><a href="case-asphalt-qcqa.html">ODOT operational reporting improvements</a></h3><p>Ohio Department of Transportation · Excel reporting improvements that reduced reporting time by approximately 25%.</p><a class="read-link" href="case-asphalt-qcqa.html">Read the case study ↗</a></article><article><span class="work-year">2024–2025</span><h3><a href="case-digital-strategy.html">Ohio State digital strategy & analytics</a></h3><p>Ohio State, Education and Human Ecology · Engagement analysis and practical recommendations for nontechnical teams.</p><a class="read-link" href="case-digital-strategy.html">Read the case study ↗</a></article></div></div>'''


page('index.html', 'Product, analytics & information systems', 'Jason Amo-Mensah’s portfolio. Ohio State MIS student with experience in digital product analytics at PNC and research platform development at Imageomics.', f'''
<section class="introduction"><p class="label">Product, analytics & information systems</p><h1>Jason Amo-Mensah</h1><p class="intro-text">I’m a Management Information Systems student at Ohio State, interested in how people use technology and how to make their experiences better.</p><p class="intro-detail">My experience includes digital product analytics at PNC, research website development at Imageomics, and operational reporting at ODOT. I enjoy understanding a problem, looking at the evidence, and finding practical improvements.</p><div class="intro-links"><a href="work.html">View my work</a><a href="about.html">More about me</a><a href="resume.html">Resume</a></div></section>
<section class="selected-work" id="selected-work"><div class="section-heading"><h2>Selected work</h2><p>Projects and contributions from my internships.</p></div>{featured_work()}{other_work()}</section>
<section class="background"><div><p class="label">Experience</p><h2>Professional experience</h2><a class="read-link" href="resume.html">View my resume ↗</a></div>{experience()}</section>
<section class="toolkit"><p class="label">Capabilities</p><div><h2>Skills & tools</h2>{skills()}</div></section>{contact()}''')

page('work.html', 'Selected work', 'Case studies in digital banking analytics, research platform development, operational reporting, and digital strategy.', f'''<section class="page-intro"><p class="label">Selected work</p><h1>Projects & experience</h1><p class="page-lede">A closer look at my work in digital banking, research platforms, operational reporting, and digital strategy.</p></section><section class="work-index" aria-label="Project case studies">{featured_work()}{other_work()}</section>{contact()}''')

page('about.html', 'About', 'About Jason Amo-Mensah, an Ohio State Fisher College of Business student interested in product management, technology, and customer experience.', f'''<section class="page-intro about-heading"><p class="label">About</p><h1>About me</h1><p class="page-lede">I’m interested in understanding how people use technology and finding practical ways to improve it.</p></section><div class="about-layout"><aside class="education"><p class="label">Currently</p><h2>The Ohio State<br>University</h2><p>Fisher College of Business</p><dl><dt>Degree</dt><dd>Bachelor of Science in Business Administration</dd><dt>Specialization</dt><dd>Management Information Systems</dd><dt>Expected graduation</dt><dd>May 2027</dd><dt>GPA</dt><dd>3.5</dd></dl></aside><article class="prose"><p class="opening-paragraph">My interest in product work comes from a fairly simple question: what makes a piece of technology useful to the person using it?</p><p>At Ohio State, I’m studying Management Information Systems at the Fisher College of Business. I’m interested in how research and data can inform decisions, and in the practical work of turning those decisions into something people can use.</p><h2>What I’ve learned through my work</h2><p>At PNC, I spent time with digital banking session replays, funnels, and customer feedback. That work taught me to look beyond a metric and ask what the experience felt like to the person behind it.</p><p>At Imageomics, I’ve worked on both the NSF HDR platform and the institute’s own website. Building features and then maintaining them has made me more attentive to the details that outlast a redesign: content accuracy, broken links, search behavior, and small-screen usability. I work with designer direction and stakeholder feedback rather than treating the code as a solo project.</p><p>My time at ODOT added another perspective: a small reporting improvement can be useful without introducing a new system. In a setting shaped by quality standards, the details matter.</p><h2>How I approach problems</h2><p>I start by listening. I write things down, ask what the evidence actually supports, and make tradeoffs clear. I care about leaving work understandable for the next person who picks it up.</p><p>That mix of customer understanding, analysis, and implementation is what draws me toward product management and digital strategy.</p><a class="read-link" href="work.html">See that approach in the work ↗</a></article></div><section class="toolkit"><p class="label">Capabilities</p><div><h2>Skills & tools</h2>{skills()}</div></section>{contact()}''')

page('contact.html', 'Contact', 'Get in touch with Jason Amo-Mensah about product, analytics, digital strategy, and technology opportunities.', '''<section class="page-intro"><p class="label">Contact</p><h1>Contact</h1><p class="page-lede">Have a role, a project, or a question in mind? I’d be glad to hear from you.</p></section><div class="contact-page"><p>I’m completing my BSBA in Management Information Systems at Ohio State, with expected graduation in May 2027. I’m interested in opportunities in product management, digital strategy, business analytics, and technology.</p><dl class="contact-directory"><div><dt>Email</dt><dd><a href="mailto:jasonam84@gmail.com">jasonam84@gmail.com <span aria-hidden="true">↗</span></a></dd></div><div><dt>LinkedIn</dt><dd><a href="https://www.linkedin.com/in/jasonamomensah">Jason Amo-Mensah <span aria-hidden="true">↗</span></a></dd></div><div><dt>Elsewhere</dt><dd><a href="https://github.com/jasonam84">GitHub <span aria-hidden="true">↗</span></a></dd></div></dl><a class="read-link" href="resume.html">Read my resume ↗</a></div>''')

# Case-specific headings keep the articles grounded in their actual subject matter.
HEADINGS = [
    ('Understanding friction in digital banking', 'What behavior and feedback could explain', 'My contribution', 'Reading the experience from several angles', 'Recommendations, with limits', 'What this changed about how I think'),
    ('One platform for a research community', 'Finding information across a growing site', 'Frontend implementation & content migration', 'Rebuilding without losing the content', 'A shared, searchable reference point', 'The work behind a reliable migration'),
    ('Reporting within a regulated workflow', 'The cost of repeated manual work', 'Testing, documentation & reporting', 'Improving the workflow already in place', 'Approximately 25% less reporting time', 'Small improvements need to hold up'),
    ('Helping teams understand digital performance', 'A metric needs context', 'Analysis & stakeholder communication', 'From performance patterns to a useful report', 'Clearer recommendations for the team', 'The next decision matters')
]


def evidence(index):
    if index == 0:
        return '''<aside class="evidence-note" aria-label="Work contributions"><h3>What the work produced</h3><dl class="evidence-list"><div><dt>Glassbox</dt><dd>Observations from 400+ session replays and evaluation of 40+ digital funnels.</dd></div><div><dt>Qualtrics Text iQ</dt><dd>Topic structures and keyword strategies to classify 3,000+ customer comments.</dd></div><div><dt>Product recommendations</dt><dd>Customer behavior and Voice of Customer insights translated for digital product teams.</dd></div></dl><p class="note">These are descriptions of my contributions. Customer records, internal screens, and proprietary findings are not published here.</p></aside>'''
    if index == 1:
        return '''<aside class="evidence-note" id="architecture" aria-label="Implementation evidence"><h3>Implementation notes</h3><dl class="evidence-list"><div><dt>Shared structure</dt><dd>Reusable headers and footers across 30+ HTML pages, including path handling between directories.</dd></div><div><dt>Finding content</dt><dd>Client-side search indexing, query normalization, and pagination for events and news.</dd></div><div><dt>Migration continuity</dt><dd>Content review with research stakeholders and redirect pages to retain important legacy paths.</dd></div></dl><details><summary>Publishing and handoff</summary><p>The designer shared the update, I implemented the frontend, and stakeholders reviewed content accuracy before publication. The ongoing Imageomics Institute redesign is separate from this NSF HDR platform work.</p></details></aside>'''
    return ''


for i, p in enumerate(PROJECTS):
    overview, problem, role, approach, impact, reflection = HEADINGS[i]
    toc = [('overview', 'Overview'), ('problem', 'The problem'), ('role', 'My role'), ('approach', 'The work'), ('tools', 'Tools'), ('impact', 'Results'), ('reflection', 'Reflection')]
    # Text-based account of the actual work; no invented artifacts or process graphics.
    process = ''.join(f'<div class="approach-entry"><h3>{e(a)}</h3><p>{e(b)}</p></div>' for a, b in p['steps'])
    article = f'''<section id="overview"><h2>{e(overview)}</h2><p>{e(p['desc'])}</p></section><section id="problem"><h2>{e(problem)}</h2><p>{e(p['problem'])}</p></section><section id="role"><h2>{e(role)}</h2><ul class="responsibility-list">{''.join('<li>'+e(t)+'</li>' for t in p['responsibilities'])}</ul></section><section id="approach"><h2>{e(approach)}</h2>{process}{evidence(i)}</section><section id="tools" class="methods"><h2>Tools & methods</h2><p>{e(' · '.join(p['tools']))}</p></section><section id="impact"><h2>{e(impact)}</h2><p>{e(p['results'])}</p></section><section id="reflection" class="reflection"><p class="label">Lessons learned</p><h2>{e(reflection)}</h2><p>{e(p['lesson'])}</p></section>'''
    if p['theme'] == 'research':
        article = (ROOT / 'templates/case-imageomics.html').read_text()
        toc = [('overview', 'Overview'), ('problem', 'Migration'), ('role', 'My role & the team'), ('approach', 'Implementation'), ('architecture', 'Decisions & tradeoffs'), ('tools', 'Tools'), ('impact', 'Outcomes'), ('maintenance', 'Ongoing work'), ('reflection', 'Reflection')]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    page(p['slug'], p['name'], p['desc'], f'''<div class="case-back"><a href="work.html">← All work</a><span>{e(p['category'])}</span></div><header class="case-heading"><p class="label">{e(p['org'])}</p><h1>{e(p['name'])}</h1><p class="page-lede">{e(p['desc'])}</p><dl class="case-facts"><div><dt>My role</dt><dd>{e(p['role'])}</dd></div><div><dt>Timeframe</dt><dd>{e(p['date'])}</dd></div></dl></header><section class="case-scope" aria-label="Project scope">{metrics(p['metrics'])}</section>{f'<p class="case-note">{e(p["note"])}</p>' if p.get('note') else ''}<div class="case-layout"><aside class="case-nav" aria-label="Article contents"><nav aria-label="On this page"><p class="label">In this article</p>{''.join(f'<a href="#{id}">{name}</a>' for id, name in toc)}</nav></aside><article class="case-content">{article}</article></div><a class="next-case" href="{nxt['slug']}"><span class="label">Read next</span><h2>{e(nxt['name'])} <span aria-hidden="true">↗</span></h2></a>''', active='work.html')

resume_experience = ''.join(f'<section class="resume-role"><div><h3>{e(p["org"])}</h3><p class="resume-date">{e(p["date"])}</p></div><p class="resume-role-title">{e(p["role"])}</p><ul>'+''.join(f'<li>{e(t)}</li>' for t in p['responsibilities'])+'</ul></section>' for p in PROJECTS)
page('resume.html', 'Resume', 'Read and download Jason Amo-Mensah’s resume: Ohio State MIS, digital product analytics, website development, and process improvement.', f'''<section class="page-intro resume-heading"><div><p class="label">Resume</p><h1>Resume</h1></div><div><a class="download-link" href="resume.pdf" download="Jason-Amo-Mensah-Resume.pdf">Download PDF <span aria-hidden="true">↓</span></a><p class="note">Updated November 2026</p></div></section><section class="resume-text"><div class="resume-identity"><h2>Jason Amo-Mensah</h2><p><a href="mailto:jasonam84@gmail.com">jasonam84@gmail.com</a> · <a href="https://www.linkedin.com/in/jasonamomensah">LinkedIn</a></p></div><div class="resume-section"><h2>Education</h2><div><h3>The Ohio State University, Fisher College of Business</h3><p>Bachelor of Science in Business Administration<br>Management Information Systems · Expected May 2027 · GPA 3.5</p></div></div><div class="resume-section"><h2>Experience</h2><div>{resume_experience}</div></div><div class="resume-section"><h2>Skills</h2>{skills()}</div></section><section class="resume-preview" aria-label="Resume PDF preview"><div class="document-bar"><h2>The PDF version</h2><a href="resume.pdf">Open PDF ↗</a></div><object data="resume.pdf" type="application/pdf" title="Jason Amo-Mensah resume PDF"><p>Your browser cannot preview this PDF. <a href="resume.pdf">Open or download the resume</a>, or read the text above.</p></object></section>''')
print('Generated 9 portfolio pages.')
