"""Historical filename; tests official 1.2.2. Run: python tests/test_v120.py [HTML]."""
import asyncio,hashlib,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
path=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'index.html'
results=[]
def check(name,ok):
 results.append({'test':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
async def main():
 text=path.read_text(encoding='utf-8');a='// ==================== ELEMENTS';b='// ==================== INPUT / UI'
 check('Freigegebene Bomben-Engine',hashlib.sha256(text[text.index(a):text.index(b)].encode()).hexdigest()=='149994a8983c06765ea258e246706c9b832d252713d0014cea4288746531d50e')
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True)
  page=await browser.new_page(viewport={'width':1280,'height':800},has_touch=True)
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto(path.as_uri());await page.evaluate('paused=true;clearWorld(true);select(STONE)')
  async def verify(name,js):check(name,await page.evaluate(js))
  await verify('Bombe bleibt fest','(()=>{put(100,30,BOMB);for(let t=0;t<30;t++)simulate();return get(100,30)===BOMB})()')
  await verify('Feuer zündet Fläche in einem Tick','(()=>{clearWorld(true);for(let y=30;y<70;y++)for(let x=80;x<120;x++)put(x,y,BOMB);put(79,50,FIRE);simulate();return !cells.includes(BOMB)&&queueRead===queueWrite})()')
  await verify('Lava zündet sofort','(()=>{clearWorld(true);put(100,50,BOMB);put(99,50,LAVA);simulate();return !cells.includes(BOMB)})()')
  await verify('Keine Bombenreste','(()=>{for(let t=0;t<60;t++)simulate();return !cells.includes(BOMB)&&queueRead===queueWrite})()')
  await page.evaluate('clearWorld(true)')
  r=await page.locator('#game').bounding_box();x=r['x']+r['width']*.5;y=r['y']+r['height']*.4
  await verify('Version','VERSION==="1.2.2"')
  await page.mouse.click(x,y);await verify('Maus malt','particleCount>996')
  await page.locator('#eraseMode').click();await page.mouse.click(x,y)
  await verify('Radieren per Linksklick','particleCount===996')
  await page.mouse.move(x,y);await page.mouse.down();await page.wait_for_timeout(100)
  await page.mouse.move(x+25,y,steps=4);await page.mouse.up()
  await verify('Radieren beim Ziehen malt nicht','particleCount===996&&down===0')
  await verify('Werkzeugstatus','document.getElementById("toolStatus").textContent==="Aktiv: Radieren"')
  await page.locator('#paintMode').click();await page.mouse.click(x,y)
  await verify('Rückwechsel Malen','particleCount>996')
  await page.mouse.click(x,y,button='right');await verify('Rechtsklick löscht','particleCount===996')
  await page.touchscreen.tap(x,y);await verify('Touch malt','particleCount>996')
  await page.locator('#eraseMode').tap();await page.touchscreen.tap(x,y)
  await verify('Touch radiert','particleCount===996')
  await page.locator('#clearBtn').click();await verify('Leeren','particleCount===0')
  await page.locator('#resetBtn').click();await verify('Reset','particleCount===996')
  await verify('Anleitung','getComputedStyle(document.getElementById("gameHelp")).fontSize==="13px"&&document.querySelectorAll("#gameHelp h3").length===4')
  for w,h in [(1280,720),(390,844),(844,390)]:
   await page.set_viewport_size({'width':w,'height':h})
   await verify('Layout %dx%d'%(w,h),'(()=>{fitCanvas();const c=canvas.getBoundingClientRect(),s=document.getElementById("stage").getBoundingClientRect();return c.left>=s.left&&c.right<=s.right+1&&c.top>=s.top&&c.bottom<=s.bottom+1})()')
  check('Keine Laufzeitfehler',not errors)
  await browser.close()
 print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':asyncio.run(main())
