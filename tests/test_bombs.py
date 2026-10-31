"""python tests/test_bombs.py [preview HTML] [official HTML]; requires Playwright."""
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
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  await page.goto(new.as_uri());await page.evaluate('paused=true')
  async def case(name,js):check(name,await page.evaluate('(()=>{clearWorld(true);'+js+'})()'))
  for name,js in [
   ('Fest','put(100,30,BOMB);for(let t=0;t<30;t++)simulate();return get(100,30)===BOMB&&state[BOMB]===SOLID;'),
   ('Pulver fällt','put(100,30,GUNPOWDER);simulate();return get(100,31)===GUNPOWDER;'),
   ('1600 Bomben ein Tick','for(let y=30;y<70;y++)for(let x=80;x<120;x++)put(x,y,BOMB);put(79,50,FIRE);simulate();return !cells.includes(BOMB)&&queueRead===queueWrite;'),
   ('Diagonal','for(let k=0;k<50;k++)put(80+k,30+k,BOMB);put(79,30,LAVA);simulate();return !cells.includes(BOMB);'),
   ('Keine Nachzünder','for(let x=100;x<110;x++)put(x,50,BOMB);put(99,50,FIRE);for(let t=0;t<100;t++)simulate();return !cells.includes(BOMB)&&queueRead===queueWrite;'),
   ('Entfernte Bombe','put(50,50,BOMB);put(250,100,BOMB);put(49,50,FIRE);simulate();return get(250,100)===BOMB&&cells.filter(e=>e===BOMB).length===1;'),
   ('Im Radius','put(50,50,BOMB);put(60,50,BOMB);put(49,50,FIRE);simulate();return !cells.includes(BOMB);'),
   ('Wasser','put(100,50,BOMB);put(101,50,WATER);simulate();return get(100,50)===BOMB;'),
   ('Wand','put(100,50,BOMB);put(101,50,WALL);put(99,50,FIRE);simulate();return get(101,50)===WALL;'),
   ('Pulverqueue','put(100,50,GUNPOWDER);ignite(100,50);return queueWrite===1&&explodeRadius[0]===5;'),
   ('Pulver durch Bombe','put(100,50,BOMB);put(105,50,GUNPOWDER);ignite(100,50);return !cells.includes(BOMB)&&queueWrite===1;'),
   ('Zähler','for(let x=90;x<110;x++)put(x,50,BOMB);ignite(90,50);let n=0;for(let i=0;i<N;i++)if(cells[i]!==AIR)n++;return n===particleCount;'),
   ('Wiederholung','for(let n=0;n<3;n++){clearWorld(true);put(100,50,BOMB);ignite(100,50);if(cells.includes(BOMB))return false;}return true;'),
   ('Rand','put(1,1,BOMB);put(2,1,LAVA);simulate();return !cells.includes(BOMB)&&get(0,0)===WALL;')]:await case(name,js)
  for hot in ['FIRE','LAVA']:
   for dx,dy in [(0,-1),(0,1),(-1,0),(1,0),(1,1)]:
    await case(hot+str((dx,dy)),f'const rng=Math.random;Math.random=()=>.999;try{{put(100,50,BOMB);put({100+dx},{50+dy},{hot});simulate();return !cells.includes(BOMB);}}finally{{Math.random=rng;}}')
  await page.evaluate('clearWorld(true);select(BOMB)')
  r=await page.locator('#game').bounding_box();x=r['x']+r['width']*.5;y=r['y']+r['height']*.4
  await page.mouse.click(x,y);check('Maus malen',await page.evaluate('cells.includes(BOMB)'))
  await page.locator('#eraseMode').click();await page.mouse.click(x,y);check('Maus radieren',await page.evaluate('!cells.includes(BOMB)'))
  await page.locator('#paintMode').tap();await page.touchscreen.tap(x,y);check('Touch malen',await page.evaluate('cells.includes(BOMB)'))
  await page.locator('#eraseMode').tap();await page.touchscreen.tap(x,y);check('Touch radieren',await page.evaluate('!cells.includes(BOMB)'))
  for w,h in [(390,844),(844,390),(1280,720)]:
   await page.set_viewport_size({'width':w,'height':h})
   check('Layout '+str((w,h)),await page.evaluate('(()=>{fitCanvas();const c=canvas.getBoundingClientRect(),s=document.getElementById("stage").getBoundingClientRect();return c.right<=s.right+1&&c.bottom<=s.bottom+1})()'))
  signature="(()=>{paused=true;let seed=123456;Math.random=()=>{seed=(Math.imul(seed,1664525)+1013904223)>>>0;return seed/4294967296};clearWorld(true);for(let y=30;y<45;y++)for(let x=70;x<120;x++)put(x,y,[SAND,WATER,OIL,DIRT,ACID,WOOD,ICE,STONE,FIRE,GUNPOWDER][(x+y)%10]);for(let t=0;t<60;t++)simulate();let hash=2166136261;for(const array of [cells,life,heat]){const bytes=new Uint8Array(array.buffer);for(let i=0;i<bytes.length;i++)hash=Math.imul(hash^bytes[i],16777619)>>>0;}return hash})()"
  a=await page.evaluate(signature)
  original=await browser.new_page();await original.goto(old.as_uri())
  check('Physik ohne Bomben unverändert',a==await original.evaluate(signature))
  check('Keine Laufzeitfehler',not errors)
  await browser.close()
 check('Offizielle Datei unverändert',before==old.read_bytes())
 print(json.dumps(results,ensure_ascii=False,indent=2))
if __name__=='__main__':asyncio.run(main())
