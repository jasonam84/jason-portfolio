"""Generate complete static pages with shared navigation; no runtime dependencies."""
from pathlib import Path
from html import escape as e
import json
import re
ROOT = Path(__file__).resolve().parents[1]
PROJECTS = json.loads((ROOT / 'templates/projects.json').read_text())
NAV = [('Home','index.html'),('Work','work.html'),('About','about.html'),('Resume','resume.html'),('Contact','contact.html')]

def page(file, title, description, body, active=None):
    active = active or file
    nav = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url == active else '')+f'>{label}</a>' for label,url in NAV)
    output = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(title)} | Jason Amo-Mensah</title>
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#f7f7f2">
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
<a class="brand" href="index.html"><span class="monogram" aria-hidden="true">ja<span>.</span></span><span>Jason Amo-Mensah</span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="nav-links" hidden>Menu <span aria-hidden="true">＋</span></button>
<div class="nav-links" id="nav-links">{nav}</div>
</nav></header>
<main id="main" class="wrap" tabindex="-1">{body}</main>
<footer class="footer"><div class="wrap footer-inner"><a class="brand" href="index.html">Jason Amo-Mensah<span class="blue">.</span></a><p>Thoughtful products. Clearer experiences.</p><div><a href="mailto:jasonam84@gmail.com">Email ↗</a><a href="https://www.linkedin.com/in/jasonamomensah">LinkedIn ↗</a><a href="https://github.com/jasonam84">GitHub ↗</a></div><small>© <span id="year">2026</span> Jason Amo-Mensah</small></div></footer>
</body>
</html>
'''
    # Encode literal ampersands while retaining entities already escaped above.
    output = re.sub(r'&(?!#?\w+;)', '&amp;', output)
    output = re.sub(r'(?<=>)(?=<(?:section|/section|article|/article|aside|/aside|nav|/nav|header|/header|footer|/footer|div|/div|h[1-3]|p|dl|ol|ul|li|details|summary)\b)', '\n', output)
    (ROOT / file).write_text(output)

def metrics(items):
    return '<dl class="metrics">'+''.join(f'<div><dt>{e(a)}</dt><dd>{e(b)}</dd></div>' for a,b in items)+'</dl>'

def visual(p, large=False):
    theme = p['theme']
    if theme == 'banking':
        inside='''<div class="insight-label"><span class="status-dot"></span> CUSTOMER EXPERIENCE</div><div class="signal-row"><span>Customer behavior</span><span>01</span></div><div class="signal-lines"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div><div class="signal-row"><span>Customer feedback</span><span>02</span></div><div class="topic-pills"><span>Observe</span><span>Understand</span><span>Prioritize</span></div><div class="insight-result">Evidence → Product recommendations <span>↗</span></div>'''
    elif theme == 'research':
        inside='''<div class="browser-top"><i></i><i></i><i></i><span>NSF HDR · Structure illustration</span></div><div class="research-title">A shared home<br>for discovery<span>.</span></div><div class="research-map"><b>Institutes</b><b>Resources</b><b>Publications</b><b>Events</b></div><div class="tiny-label">30+ PAGES · ONE CONNECTED PLATFORM</div>'''
    elif theme == 'operations':
        inside='''<div class="tiny-label">OPERATIONAL REPORTING</div><div class="time-stat">≈25%<span>less reporting time</span></div><div class="time-bars"><span>Before</span><i></i><span>After</span><i></i></div>'''
    else:
        inside='''<div class="tiny-label">FROM ANALYSIS TO ACTION</div><div class="strategy-path"><span>Data</span><b>→</b><span>Context</span><b>→</b><span>Decision</span></div><div class="strategy-note">A clear question.<br>A useful takeaway.</div>'''
    return f'<div class="project-visual {theme}{" visual-large" if large else ""}" aria-hidden="true">{inside}</div>'

def cards():
    return '<div class="project-grid">'+''.join(f'''<a class="project-card" href="{p['slug']}">{visual(p)}<div class="card-copy"><div class="card-meta"><span>{e(p['category'])}</span><span>0{i+1} / 202{'6' if i==0 else '5'}</span></div><h3>{e(p['name'])}<span aria-hidden="true">↗</span></h3><p>{e(p['desc'])}</p><span class="text-link">Read case study <span aria-hidden="true">→</span></span></div></a>''' for i,p in enumerate(PROJECTS))+'</div>'

def contact():
    return '''<section class="contact-band"><div><p class="eyebrow">LET’S CONNECT</p><h2>Good experiences<br>start with a conversation.</h2><p>I’m interested in opportunities in product management, business analytics, and digital strategy.</p></div><div class="contact-actions"><a class="button" href="mailto:jasonam84@gmail.com">Say hello <span aria-hidden="true">↗</span></a><a href="https://www.linkedin.com/in/jasonamomensah">Connect on LinkedIn ↗</a></div></section>'''

def skills():
    groups=[('Product & strategy',['Product Analytics','Customer Experience','Voice of Customer','Funnel Analysis','Stakeholder Communication','Process Improvement']),('Data & analytics',['SQL','Excel','Tableau','Qualtrics Text iQ','Glassbox']),('Technology',['HTML','CSS','JavaScript','GitHub','Website Development'])]
    return '<div class="skills-grid">'+''.join(f'<div><span class="section-number">0{i+1}</span><h3>{name}</h3><ul class="skill-list">'+''.join(f'<li>{s}</li>' for s in vals)+'</ul></div>' for i,(name,vals) in enumerate(groups))+'</div>'

def experience():
    return '<div class="experience-list">'+''.join(f'''<article class="experience-row"><p class="experience-date">{e(p['date'])}</p><div><h3>{e(p['org'])}</h3><p class="role">{e(p['role'])}</p><p>{e(p['desc'])}</p></div><a href="{p['slug']}" aria-label="Read {e(p['name'])}">↗</a></article>''' for p in PROJECTS)+'</div>'

page('index.html','Product, insights & digital experiences','Jason Amo-Mensah is an Ohio State MIS student working across digital product analytics, web development, and process improvement.',f'''
<section class="hero"><div class="hero-copy"><p class="eyebrow"><span class="status-dot"></span> PRODUCT THINKING. HUMAN PERSPECTIVE.</p><h1>Turning customer<br>insights into <span>better<br>digital experiences.</span></h1><p class="lede">I’m Jason, a Management Information Systems student at Ohio State with experience in digital product analytics, web development, and process improvement. I enjoy understanding where technology creates friction and finding practical ways to make it better.</p><div class="button-row"><a class="button" href="work.html">Explore my work <span aria-hidden="true">↗</span></a><a class="button button-quiet" href="about.html">A little about me <span aria-hidden="true">→</span></a></div><p class="hero-footnote">THE OHIO STATE UNIVERSITY <span>BSBA · MIS · MAY 2027</span></p></div><aside class="hero-aside"><p class="tiny-label">MY APPROACH / 01—03</p><div class="orbit" aria-hidden="true"><div class="orbit-center">People<span>×</span>Product</div><span class="orbit-node node-one"></span><span class="orbit-node node-two"></span><span class="orbit-node node-three"></span></div><ol class="approach-list"><li><span>01</span> Listen to people</li><li><span>02</span> Follow the evidence</li><li><span>03</span> Make it clearer</li></ol></aside></section>
<section class="impact-strip" aria-label="Selected impact">{metrics([('400+','PNC session replays analyzed'),('3,000+','customer comments classified'),('30+','research platform pages'),('≈25%','less ODOT reporting time')])}</section>
<section class="section" id="selected-work"><div class="section-heading"><div><p class="eyebrow">SELECTED WORK / 2024—2026</p><h2>Different challenges.<br>A common curiosity.</h2></div><p>Understanding people, making sense of data,<br>and building something useful.</p></div>{cards()}</section>
<section class="section experience-section"><div class="section-heading"><div><p class="eyebrow">EXPERIENCE</p><h2>Learning through real work.</h2></div><a class="text-link" href="resume.html">View my resume ↗</a></div>{experience()}</section>
<section class="section"><div class="section-heading"><div><p class="eyebrow">CAPABILITIES</p><h2>From insight to implementation.</h2></div><p>A mix of analytical methods, product thinking,<br>and hands-on frontend development.</p></div>{skills()}</section>{contact()}''')

page('work.html','Selected work','Four case studies in digital banking analytics, research platform development, operational reporting, and digital strategy.',f'''<section class="page-intro"><p class="eyebrow">WORK / 2024—2026</p><h1>Questions explored.<br><span>Ideas put to work.</span></h1><p class="lede">From understanding a digital banking journey to rebuilding a research platform, these projects reflect how I connect people, data, and technology.</p></section><section class="work-section" aria-label="Project case studies">{cards()}<p class="visual-caption">Project visuals illustrate methods and scope. They are not screenshots of internal systems or customer data.</p></section>{contact()}''')

page('about.html','About','Meet Jason Amo-Mensah, an Ohio State Fisher College of Business student interested in product management, technology, and customer experience.',f'''<section class="page-intro about-intro"><div><p class="eyebrow">ABOUT ME</p><h1>Curious about people.<br><span>Practical about technology.</span></h1></div><div class="initials-art" aria-hidden="true">ja<span>.</span><small>JASON AMO-MENSAH</small></div></section><section class="about-layout section"><div class="prose"><h2>I like figuring out why<br>something feels harder than it should.</h2><p>I’m Jason, a Management Information Systems student at The Ohio State University’s Fisher College of Business. I’m interested in how people interact with technology, and how research, data, and careful product decisions can make those interactions better.</p><p>At PNC, I explored that question through digital banking behavior and customer feedback. Watching session replays and organizing customer comments taught me to look beyond a metric and ask what the experience felt like to the person using it.</p><p>At Imageomics, I’ve approached the same question through building: helping redesign and migrate a research platform, implementing navigation and search, and working with designers and research stakeholders. At ODOT, the focus was on practical reporting improvements in a setting where documentation and accuracy matter.</p><h2>How I work</h2><p>I start by listening and understanding the task someone is trying to complete. Then I look at the evidence, write down the tradeoffs, and work toward a clear next step. I care about solutions that a team can understand, maintain, and improve after the first version.</p><p>That combination of customer understanding, analysis, and implementation is what draws me to product management and digital strategy. I want to help teams make thoughtful decisions about what to build and why.</p></div><aside class="education-card"><p class="eyebrow">EDUCATION</p><h3>The Ohio State University</h3><p>Fisher College of Business</p><hr><p>Bachelor of Science in Business Administration</p><dl><dt>Specialization</dt><dd>Management Information Systems</dd><dt>Expected graduation</dt><dd>May 2027</dd><dt>GPA</dt><dd>3.5</dd></dl><a class="text-link" href="resume.html">View my resume ↗</a></aside></section><section class="section"><p class="eyebrow">MY TOOLKIT</p><h2>Analytical and hands-on.</h2>{skills()}</section>{contact()}''')

page('contact.html','Contact','Contact Jason Amo-Mensah about product management, business analytics, digital strategy, and technology opportunities.','''<section class="page-intro contact-intro"><p class="eyebrow">CONTACT</p><h1>Let’s make<br><span>something clearer.</span></h1><p class="lede">Have a role, a project, or a question in mind? I’d be glad to hear from you.</p></section><section class="contact-grid" aria-label="Ways to connect"><a class="contact-card" href="mailto:jasonam84@gmail.com"><span class="eyebrow">EMAIL</span><h2>Start a conversation <span aria-hidden="true">↗</span></h2><p>jasonam84@gmail.com</p></a><a class="contact-card" href="https://www.linkedin.com/in/jasonamomensah"><span class="eyebrow">LINKEDIN</span><h2>Let’s connect <span aria-hidden="true">↗</span></h2><p>Jason Amo-Mensah</p></a></section><section class="contact-note"><p class="eyebrow">LOOKING AHEAD</p><p>I’m interested in product management, digital product strategy, business analytics, and technology roles. I’m completing my BSBA in Management Information Systems at Ohio State, with expected graduation in May 2027.</p><a class="text-link" href="resume.html">Get to know my experience →</a></section>''')

for i,p in enumerate(PROJECTS):
    toc=[('overview','Overview'),('problem','The opportunity'),('role','My responsibilities'),('approach','Approach & process'),('tools','Tools & methods'),('impact','Results & impact'),('reflection','Lessons learned')]
    sections=f'''<section id="overview"><p class="eyebrow">01 / PROJECT OVERVIEW</p><h2>{e(p['short'])}</h2><p>{e(p['desc'])}</p>{metrics(p['metrics'])}</section><section id="problem"><p class="eyebrow">02 / THE OPPORTUNITY</p><h2>The question behind the work.</h2><p>{e(p['problem'])}</p></section><section id="role"><p class="eyebrow">03 / MY RESPONSIBILITIES</p><h2>Where I contributed.</h2><ul class="responsibility-list">{''.join('<li>'+e(t)+'</li>' for t in p['responsibilities'])}</ul></section><section id="approach"><p class="eyebrow">04 / APPROACH & PROCESS</p><h2>From understanding to action.</h2><ol class="process-list">{''.join(f'<li><span class="process-number">0{j+1}</span><div><h3>{e(a)}</h3><p>{e(b)}</p></div></li>' for j,(a,b) in enumerate(p['steps']))}</ol></section><section id="tools"><p class="eyebrow">05 / TOOLS & METHODS</p><h2>The working toolkit.</h2><ul class="tool-list">{''.join('<li>'+e(t)+'</li>' for t in p['tools'])}</ul></section><section id="impact"><p class="eyebrow">06 / RESULTS & IMPACT</p><h2>What the work contributed.</h2><p>{e(p['results'])}</p></section><section id="reflection"><p class="eyebrow">07 / LESSONS LEARNED</p><h2>What I’m taking forward.</h2><p>{e(p['lesson'])}</p></section>'''
    # Preserve meaningful legacy section fragments alongside the retained page URLs.
    if p['theme']=='research':
        sections += '''<section id="architecture"><p class="eyebrow">IMPLEMENTATION DETAIL</p><h2>A structure built to be maintained.</h2><div class="structure-comparison"><div><h3>Legacy platform</h3><p>Google Sites, content spread across sections, and navigation shaped by program history.</p></div><div><h3>Rebuilt platform</h3><p>GitHub-hosted HTML, CSS, and JavaScript; shared navigation and footer; searchable pages and clearer routes to resources.</p></div></div><p>Implementation included client-side search indexing, event and news pagination, challenge status logic, and redirect pages for important legacy paths. The designer led UX direction; I focused on frontend implementation and content migration.</p><details><summary>Publishing and handoff</summary><p>The designer shared the update, I implemented the frontend, and stakeholders reviewed content accuracy before publication. Future work on the NSF HDR platform centers on maintenance and content updates.</p></details></section>'''
    nxt=PROJECTS[(i+1)%len(PROJECTS)]
    page(p['slug'],p['name'],p['desc'],f'''<div class="case-back"><a class="text-link" href="work.html">← All work</a><span class="tiny-label">CASE STUDY / 0{i+1}</span></div><section class="case-hero"><p class="eyebrow">{e(p['category'])}</p><h1>{e(p['name'])}<span class="blue">.</span></h1><p class="lede">{e(p['desc'])}</p><dl class="case-facts"><div><dt>ORGANIZATION</dt><dd>{e(p['org'])}</dd></div><div><dt>ROLE</dt><dd>{e(p['role'])}</dd></div><div><dt>TIMEFRAME</dt><dd>{e(p['date'])}</dd></div></dl></section>{visual(p,True)}<p class="visual-caption">Conceptual illustration of the project’s methods and scope.</p>{f'<p class="case-note">{e(p["note"])}</p>' if p.get('note') else ''}<div class="case-layout"><aside class="case-nav"><nav aria-label="On this page"><p class="eyebrow">IN THIS CASE</p>{''.join(f'<a href="#{id}">{name}</a>' for id,name in toc)}</nav></aside><article class="case-content">{sections}</article></div><a class="next-case" href="{nxt['slug']}"><span class="eyebrow">NEXT CASE STUDY</span><h2>{e(nxt['name'])} <span aria-hidden="true">→</span></h2></a>''',active='work.html')

resume_experience=''.join(f'<section class="resume-role"><h3>{e(p["org"])}</h3><p><strong>{e(p["role"])}</strong><br>{e(p["date"])}</p><ul>'+''.join(f'<li>{e(t)}</li>' for t in p['responsibilities'])+'</ul></section>' for p in PROJECTS)
page('resume.html','Resume','Read and download Jason Amo-Mensah’s resume: Ohio State MIS, digital product analytics, website development, and process improvement.',f'''<section class="page-intro"><p class="eyebrow">RESUME</p><h1>The experience<br><span>behind the work.</span></h1><p class="lede">Education, experience, and capabilities in one place.</p><div class="button-row"><a class="button" href="resume.pdf" download="Jason-Amo-Mensah-Resume.pdf">Download PDF <span aria-hidden="true">↓</span></a><a class="button button-quiet" href="resume.pdf">Open PDF ↗</a></div></section><section class="resume-preview" aria-label="Resume PDF preview"><div class="document-bar"><span>JASON AMO-MENSAH / RESUME</span><span>PDF · Updated November 2026</span></div><object data="resume.pdf" type="application/pdf" title="Jason Amo-Mensah resume PDF"><p>Your browser cannot preview this PDF. <a href="resume.pdf">Open or download the resume</a>, or read the text below.</p></object></section><section class="resume-text section"><p class="eyebrow">TEXT VERSION</p><h2>Jason Amo-Mensah</h2><p><a href="mailto:jasonam84@gmail.com">jasonam84@gmail.com</a> · <a href="https://www.linkedin.com/in/jasonamomensah">LinkedIn</a></p><h3>Education</h3><p>The Ohio State University, Fisher College of Business<br>Bachelor of Science in Business Administration<br>Management Information Systems · Expected May 2027 · GPA 3.5</p><h2>Experience</h2>{resume_experience}<h2>Skills</h2>{skills()}</section>{contact()}''')
print('Generated 9 static HTML pages.')
