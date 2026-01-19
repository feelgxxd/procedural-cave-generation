## Real-time Cellular Automata Playground

An algorithm-driven cave generation system focused on producing natural-looking underground layouts using tunable parameters and reproducible results.
This project explores how simple rules and noise-based processes can generate complex, game-ready environments suitable for 2D or top-down games.

## 🧠 Overview

Procedural cave generation is commonly used in games to create large, explorable spaces without handcrafted level design.

This project aims to:
- Generate organic cave structures
- Provide fine control over density, openness, and connectivity
- Produce deterministic results via seeds
- Visualize each generation step for iteration and tuning

## ✨ Core Features

- Noise-based cave generation
- Configurable parameters for shape and density
- Seed-based reproducibility
- Step-by-step visual output
- Lightweight and easy to extend

## ⚙️ How It Works

The system is built around a grid-based representation of the cave space.

1. **Initial Noise Fill**  
   The grid is initialized using random noise with a configurable fill ratio.

2. **Cellular Automata Smoothing**  
   Multiple simulation passes apply local neighborhood rules to smooth the cave structure and remove isolated artifacts.

3. **Post-Processing**  
   Optional cleanup steps improve connectivity and visual readability.

Each stage is intentionally separated to allow easy experimentation and parameter tuning.

## 🧩 Technical Highlights

- Grid-based spatial representation
- Cellular automata rules for local emergence
- Deterministic generation using random seeds
- Designed with gameplay integration in mind

## 🤔 Why I Built This

I built this project to explore how simple procedural rules can lead to rich, emergent structures that feel handcrafted while remaining fully algorithmic.

The goal was not only to generate caves, but to better understand how procedural systems can support gameplay, exploration, and replayability.

## Controls
- SPACE = Pause / Resume
- Mouse(LMB) = Carve Area(paused)
- ↑ / ↓ = Adjust birth threshold
- ← / → = Adjust survival threshold
- H = Toggle Heatmap
- R = Reset Grid

## License
MIT License - free to use, modify, and experiment with.

![1](https://github.com/user-attachments/assets/80c39a4a-3b72-495b-8aa2-f9542e1fdb3c)
![2](https://github.com/user-attachments/assets/456e0b58-2f0f-4f34-81ad-e4b7676de9c6)
![3](https://github.com/user-attachments/assets/2c42e93f-b281-41ed-882e-1654a3fe2ed1)
