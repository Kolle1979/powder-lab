"""python tests/test_fire.py [preview HTML] [official HTML]; requires Playwright."""
import asyncio,json,sys
from pathlib import Path
from playwright.async_api import async_playwright
root=Path(__file__).resolve().parents[1]
new=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root/'test/index.html'
old=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else root/'index.html'
results=[]
def check(name,ok):
 results.append({'test':name,'passed':bool(ok)})
 if not ok:raise AssertionError(name)
async def main():
 before=old.read_bytes()
 async with async_playwright() as p:
  browser=await p.chromium.launch(headless=True)
  page=await browser.new_page(viewport={'width':1280,'height':800},has_touch=True)
  errors=[];requests=[]
  page.on('pageerror',lambda e:errors.append(str(e)))
  async def network(route):
   if route.request.url.startswith(('http:','https:')):
    requests.append(route.request.url);await route.abort()
   else:await route.continue_()
  await page.route('**/*',network)
  await page.goto(new.as_uri());await page.evaluate('paused=true')
  async def case(name,js):check(name,await page.evaluate('(()=>{clearWorld(true);select(FIRE);brush=1;'+js+'})()'))
  await case('Kurzer Funke','paint(100,70,false);simulate();return cells.includes(FIRE);')
  await case('Nach sechs Ticks weg ohne Rauch','paint(100,70,false);for(let t=0;t<6;t++)simulate();return !cells.includes(FIRE)&&!cells.includes(SMOKE);')
  for fuel in ['WOOD','OIL']:
   await case(fuel+' brennt weiter',f'const rng=Math.random;Math.random=()=>.999;try{{put(100,100,{fuel});paint(100,99,false);for(let t=0;t<12;t++)simulate();for(let i=0;i<N;i++)if(cells[i]===FIRE&&life[i]<PAINT_FIRE_FLAG)return true;return false;}}finally{{Math.random=rng;}}')
  await case('Brennendes Feuer nicht verkürzen','put(100,70,FIRE,80);paint(100,70,false);return life[70*W+100]===80;')
  await case('Explosionsfeuer unverändert','put(100,70,FIRE,80);for(let t=0;t<10;t++)simulate();return cells.includes(FIRE);')
  await case('Pause erhält Funken','paint(100,70,false);const n=life[70*W+100];render();return n===life[70*W+100];')
  await case('Bomben zünden mit kurzem Funken','put(100,100,BOMB);paint(99,100,false);simulate();return !cells.includes(BOMB);')
  await page.evaluate('clearWorld(true);select(FIRE);brush=1')
  r=await page.locator('#game').bounding_box();x=r['x']+r['width']*.5;y=r['y']+r['height']*.4
  await page.mouse.click(x,y)
  check('Maus setzt kurzen Funken',await page.evaluate('cells.includes(FIRE)&&life.some(v=>v>PAINT_FIRE_FLAG)'))
  await page.evaluate('for(let t=0;t<6;t++)simulate()')
  check('Maus-Funke verschwindet',await page.evaluate('!cells.includes(FIRE)'))
  await page.touchscreen.tap(x,y)
  check('Touch setzt kurzen Funken',await page.evaluate('cells.includes(FIRE)&&life.some(v=>v>PAINT_FIRE_FLAG)'))
  await page.evaluate('for(let t=0;t<6;t++)simulate()')
  check('Touch-Funke verschwindet',await page.evaluate('!cells.includes(FIRE)'))
  check('Keine Netzverbindungen',not requests)
  check('Keine Laufzeitfehler',not errors)
  await browser.close()
 check('Offizielle Datei unverändert',before==old.read_bytes())
 print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':asyncio.run(main())
