"""Optional QA: playwright Python package, local Chrome, and axe.min.js path.
Usage: python3 scripts/browser_qa.py /path/to/axe.min.js
Serve repository at http://127.0.0.1:8765 first.
"""
from pathlib import Path
import json,sys
from playwright.sync_api import sync_playwright
ROOT=Path(__file__).resolve().parents[1]
results=[];errors=[]
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless=True)
 for width in (1440,768,390,320):
  page=browser.new_page(viewport={'width':width,'height':1000},device_scale_factor=1)
  page.on('pageerror',lambda error:errors.append(str(error)))
  for f in sorted(ROOT.glob('*.html')):
   response=page.goto('http://127.0.0.1:8765/'+f.name)
   assert response.status==200,(f.name,response.status)
   assert page.locator('h1').is_visible()
   assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(f.name,width,'horizontal overflow')
   # Detect text or controls that escape their own layout containers.
   assert page.locator('main').bounding_box()['width']<=width
   if width in (1440,390):
    page.add_script_tag(path=sys.argv[1])
    violations=page.evaluate('''async () => (await axe.run(document, {runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa']}})).violations.map(v=>({id:v.id,impact:v.impact,nodes:v.nodes.map(n=>n.target)}))''')
    if violations: errors.append({'page':f.name,'width':width,'violations':violations})
   if f.name=='index.html' and width in (1440,390):page.screenshot(path=f'/tmp/portfolio-{width}.png',full_page=True)
   results.append(f'{f.name}@{width}: OK')
  page.close()
 page=browser.new_page(viewport={'width':390,'height':844})
 page.goto('http://127.0.0.1:8765')
 menu=page.get_by_role('button',name='Menu')
 assert menu.get_attribute('aria-expanded')=='false'
 assert not page.get_by_role('link',name='Work',exact=True).is_visible()
 menu.click();assert page.get_by_role('link',name='Work',exact=True).is_visible()
 page.keyboard.press('Escape');assert menu.get_attribute('aria-expanded')=='false'
 assert menu.evaluate('el=>el===document.activeElement')
 menu.click();page.get_by_role('link',name='Work',exact=True).click();assert page.url.endswith('/work.html')
 page.goto('http://127.0.0.1:8765/case-pnc.html#impact');assert page.locator('#impact').is_visible()
 page.goto('http://127.0.0.1:8765/resume.html')
 with page.expect_download() as info:page.get_by_role('link',name='Download PDF').click()
 assert info.value.suggested_filename=='Jason-Amo-Mensah-Resume.pdf'
 page.emulate_media(reduced_motion='reduce');assert page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')=='auto'
 page.goto('http://127.0.0.1:8765/index.html');page.keyboard.press('Tab');assert page.locator('.skip-link').evaluate('el=>el===document.activeElement')
 page.keyboard.press('Enter');assert page.evaluate('document.activeElement.id')=='main'
 nojs=browser.new_context(java_script_enabled=False,viewport={'width':390,'height':844})
 tab=nojs.new_page();tab.goto('http://127.0.0.1:8765');assert tab.get_by_role('link',name='Work',exact=True).is_visible();assert tab.locator('h1').is_visible()
 nojs.close();browser.close()
assert not errors,json.dumps(errors,indent=2)
print('\n'.join(results));print('PASS: axe WCAG A/AA, mobile menu, Escape/focus, navigation, anchor, PDF download, skip link, reduced motion, and no-JS fallback.')
