# Originaler Startprompt

Das folgende englische Briefing ist der ursprüngliche Nutzerauftrag. Es wird als Herkunfts- und Anforderungsdokument archiviert, nicht als Bestätigung, dass v1.1.0 jede Anforderung vollständig erfüllt. Abweichungen stehen in ARCHITEKTUR.md und TESTS.md. Sonstige private Chat-Inhalte sind nicht enthalten.

---

Create a smooth, performant 2D sandbox game inspired by Powder Game and Powder Box: All Ages.

Goal:
The player spawns elements and watches them interact with realistic physics. The game should feel like a creative physics laboratory, not a platformer.

Core requirements:
- Use HTML, CSS, and JavaScript in a single self-contained HTML file.
- Use a canvas-based falling-sand physics engine.
- The simulation area should be at least 1280x720 pixels and scale correctly to the browser window.
- Target 60 FPS on a normal laptop.
- Optimize the simulation with typed arrays, spatial partitioning, dirty rectangles or chunk updates, and minimal object allocation.
- Do not simulate every pixel every frame if it is unnecessary.
- Add a pause button and a clear/reset button.

Elements to include:
- Sand: falls, piles up, can be pushed by water.
- Water: flows, spreads, extinguishes fire, turns lava into stone.
- Stone: static solid block.
- Dirt: falls like sand and can grow plants.
- Wood: static, burns when touched by fire.
- Fire: spreads to wood, oil, plants and gunpowder; extinguished by water.
- Smoke: rises and disappears after some time.
- Steam: rises, condenses back into water after a while.
- Lava: flows slowly, burns flammable materials, turns into stone when touching water.
- Oil: flows like water but is flammable.
- Gunpowder: falls like sand and explodes when ignited.
- Acid: dissolves stone, dirt, wood and plants, but not glass.
- Glass: static, transparent, acid-proof.
- Plant: grows slowly on dirt, burns easily.
- Ice: static, melts into water near fire or lava.
- Metal: static, conducts heat slowly.
- Bomb: explodes when ignited, destroys nearby blocks.
- Wall: indestructible static block for building containers.

Physics rules:
- Each element has weight, flammability, conductivity, melting point and interaction rules.
- Sand sinks in water.
- Water flows around obstacles and fills containers.
- Lava melts ice and ignites flammable materials.
- Acid dissolves most materials but stops at glass.
- Explosions create pressure, destroy blocks and spawn smoke and fire.
- Elements should not pass through solid blocks.

Gameplay features:
- Left mouse button: place the selected element.
- Right mouse button: erase elements.
- Mouse wheel: change brush size.
- Number keys 1 to 9: quickly select elements.
- A sidebar with all elements, grouped by category.
- A small preview of the currently selected element.
- A brush-size slider.
- A simulation-speed slider.
- A clear button and a reset-world button.

Visual style:
- Clean, colorful pixel-art look.
- Clear outlines for walls and containers.
- Smooth animations for water, fire, smoke and explosions.
- A dark UI so the colorful elements stand out.
- Show FPS in the corner.

Performance requirements:
- Use typed arrays for the world grid.
- Update active elements using an activity map or chunk system.
- Avoid creating new objects inside the main loop.
- Use requestAnimationFrame for rendering.
- Keep the code modular: world, elements, physics, rendering and input should be separate sections.

After creating the game:
- Explain how to open and play it.
- List all elements and their interactions.
- Suggest 5 fun experiments the player can try, for example making a volcano, a water container, a fire spread test or a bomb explosion.
