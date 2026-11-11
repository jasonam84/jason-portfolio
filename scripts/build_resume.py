"""Regenerate resume.pdf from the same verified content as the website.
Optional authoring tool: python3 -m pip install reportlab. Not needed to serve site.
"""
from pathlib import Path
from html import escape
import json
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
ROOT = Path(__file__).resolve().parents[1]
projects = json.loads((ROOT / 'templates/projects.json').read_text())
styles = {
 'name': ParagraphStyle('name',fontName='Helvetica-Bold',fontSize=23,leading=28,textColor=HexColor('#192b40'),spaceAfter=6),
 'contact': ParagraphStyle('contact',fontName='Helvetica',fontSize=9,leading=13,spaceAfter=12),
 'section': ParagraphStyle('section',fontName='Helvetica-Bold',fontSize=10,leading=15,textColor=HexColor('#255ed2'),spaceBefore=12,spaceAfter=6),
 'org': ParagraphStyle('org',fontName='Helvetica-Bold',fontSize=9,leading=13,spaceBefore=7,spaceAfter=2),
 'body': ParagraphStyle('body',fontName='Helvetica',fontSize=8.7,leading=12,spaceAfter=3),
 'bullet': ParagraphStyle('bullet',fontName='Helvetica',fontSize=8.7,leading=12,leftIndent=10,firstLineIndent=-8,spaceAfter=3),
}
story=[]
def p(text,style='body'): return Paragraph(text,styles[style])
story += [p('JASON AMO-MENSAH','name'), p('<link href="mailto:jasonam84@gmail.com">jasonam84@gmail.com</link> | <link href="https://www.linkedin.com/in/jasonamomensah">LinkedIn</link>','contact'),p('EDUCATION','section'),p('The Ohio State University, Fisher College of Business','org'),p('Bachelor of Science in Business Administration | Expected May 2027'),p('Specialization: Management Information Systems | GPA: 3.5'),p('EXPERIENCE','section')]
for item in projects:
 role=escape(item['role']).replace('&amp;','&amp;')
 block=[p(escape(item['org']),'org'),p('<b>'+role+'</b> | '+escape(item['date'].replace('–','-')))]
 for bullet in item['responsibilities']: block.append(p('- '+escape(bullet),'bullet'))
 story.append(KeepTogether(block))
story += [p('SKILLS','section'),p('<b>Product &amp; Strategy:</b> Product Analytics, Customer Experience, Voice of Customer, Funnel Analysis, Stakeholder Communication, Process Improvement'),p('<b>Data &amp; Analytics:</b> SQL, Excel, Tableau, Qualtrics Text iQ, Glassbox'),p('<b>Technology:</b> HTML, CSS, JavaScript, GitHub, Website Development')]
doc=SimpleDocTemplate(str(ROOT/'resume.pdf'),pagesize=(612,792),leftMargin=40,rightMargin=40,topMargin=32,bottomMargin=32,title='Jason Amo-Mensah | Resume',author='Jason Amo-Mensah')
doc.build(story)
print('Generated resume.pdf from confirmed portfolio facts.')
