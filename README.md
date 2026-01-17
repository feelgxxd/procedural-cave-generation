## Real-time Cellular Automata Playground
An interactive, real-time procedural cave generation simulation built with
cellular automata.

This project is designed as a playground, not a one-click generator:
rules can be modified live, reactions are visualized, and cave structures
emerge step by step.

## Simulation Model
- Grid-based cellular automata
- Each cell is either wall or floor
- Neighbor counts determine survival and birth
- Rules are adjustable in real time
- The focus is on emergent behavior, not fixed outcomes.

## Controls
- SPACE = Pause / Resume
- Mouse(LMB) = Carve Area(paused)
- ↑ / ↓ = Adjust birth threshold
- ← / → = Adjust survival threshold
- H = Toggle Heatmap
- R = Reset Grid

## Visualization
- Smooth state transitions
- Birth / death reaction highlighting
- Debug-friendly rendering

The algorithm remains readable while running.

## License
MIT License - free to use, modify, and experiment with.
