"""python tests/test_preview.py [official HTML] [preview HTML]; requires Playwright."""
import asyncio,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
root=Path(__file__).resolve().parents[1]
old=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root/'index.html'
new=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else root/'test/index.html'
results=[]
def check(name,ok):
 results.append({'test':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
async def main():
 before=old.read_bytes();a=before.decode();b=new.read_text(encoding='utf-8')
 check('Release entspricht freigegebener Vorschau bis auf Versionskennzeichnung',a==b.replace('1.2.1-rc.1','1.2.1'))
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True)
  page=await browser.new_page(viewport={'width':390,'height':844},has_touch=True)
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto(new.as_uri());await page.evaluate('paused=true;clearWorld(true);select(STONE)')
  async def verify(name,js):check(name,await page.evaluate(js))
  await verify('Hinweis entfernt, linke Anleitung bleibt','!document.getElementById("hint")&&document.querySelectorAll("#gameHelp h3").length===4')
  await verify('Testversion sichtbar','VERSION==="1.2.1-rc.1"&&document.querySelector(".version").textContent.includes("1.2.1-rc.1")')
  r=await page.locator('#game').bounding_box();x=r['x']+r['width']*.5;y=r['y']+r['height']*.4
  await page.mouse.click(x,y);await verify('Maus malt','particleCount>996')
  await page.locator('#eraseMode').click();await page.mouse.click(x,y)
  await verify('Maus radiert','particleCount===996')
  await page.locator('#paintMode').tap();await page.touchscreen.tap(x,y)
  await verify('Touch malt','particleCount>996')
  await page.locator('#eraseMode').tap();await page.touchscreen.tap(x,y)
  await verify('Touch radiert','particleCount===996')
  for w,h in [(390,844),(844,390),(1280,720)]:
   await page.set_viewport_size({'width':w,'height':h})
   await verify('Layout %dx%d'%(w,h),'(()=>{fitCanvas();let c=canvas.getBoundingClientRect(),s=document.getElementById("stage").getBoundingClientRect();return c.left>=s.left&&c.right<=s.right+1&&c.top>=s.top&&c.bottom<=s.bottom+1})()')
  check('Keine JavaScript-Fehler',not errors)
  await browser.close()
 check('Offizielle Datei durch Test nicht verändert',old.read_bytes()==before)
 print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':asyncio.run(main())
