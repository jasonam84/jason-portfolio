"""Dependency-free structural, factual guardrail, and local-link checks."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self,path):
  super().__init__(convert_charrefs=True);self.path=path;self.ids=[];self.links=[];self.h1=0;self.main=0;self.nav=0;self.lang=False;self.description=False;self.feed(path.read_text())
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for k in ('href','src','data'):
   if k in a:self.links.append(a[k])
  if tag=='h1':self.h1+=1
  if tag=='main':self.main+=1
  if tag=='nav':self.nav+=1
  if tag=='html':self.lang=a.get('lang')=='en'
  if tag=='meta' and a.get('name')=='description':self.description=bool(a.get('content'))
pages={p.name:Page(p) for p in ROOT.glob('*.html')}
errors=[]
for name,page in pages.items():
 for test,msg in [(page.h1==1,'expected one h1'),(page.main==1 and page.nav>=1,'missing main or navigation landmark'),(page.lang,'missing language'),(page.description,'missing description'),(len(page.ids)==len(set(page.ids)),'duplicate ids')]:
  if not test:errors.append(f'{name}: {msg}')
 text=page.path.read_text()
 if re.search(r'wells\s+fargo|\bjunior\b',text,re.I):errors.append(f'{name}: prohibited or outdated copy')
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  target=(page.path.parent/unquote(u.path)).resolve() if u.path else page.path
  if not target.is_file():errors.append(f'{name}: missing {link}')
  if u.fragment and target.name in pages and u.fragment not in pages[target.name].ids:errors.append(f'{name}: missing fragment {link}')
assert len(pages)==10,f'Expected 10 pages, found {len(pages)}'
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages; local links, fragments, metadata, landmarks, unique ids, and content guardrails.')
