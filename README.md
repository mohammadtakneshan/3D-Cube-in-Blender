![Cube](https://github.com/user-attachments/assets/92a21d33-e13b-443e-b420-e3fed52a0f91)

# 3D Cube in Blender

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Running the Script](#running-the-script)
- [Features](#features)
  - [Modeling](#modeling)
  - [Appearance](#appearance)
  - [Animation](#animation)
  - [Scripting](#scripting)
  - [Rendering](#rendering)
- [Resources](#resources)

## Overview

This project offers a foundational introduction to Blender's core features, making it ideal for beginners in 3D modeling and animation. The focus is on creating and animating a 3D cube using Blender's tools.

## Getting Started

To explore or recreate this project, ensure you have the following:

1. **Blender**: Download the latest version from [blender.org](https://www.blender.org).
2. **Python**: Download Python 3.x from python.org (included with Blender but available separately if needed).

### Running the Script

Use the provided Python script to generate a grid of cubes and apply physics:

```bash
mkdir -p output
blender -b -P blender_cubes.py -- output/blender_cubes.blend
```

This will create a new `.blend` file with the dynamic cube setup.


## Features

### Modeling
- Utilizes scaling, rotation, extrusion, and subdivision for creating realistic objects.

### Texturing
- Assigns base colors and procedural textures for enhanced visuals.

### Animation
- Keyframed object motions and used follow-path animations.

### Scripting
- Automates repetitive tasks, including object generation and physics assignment.

### Rendering
- Configured Cycles engine for high-quality outputs with denoising and adaptive sampling.


## Resources

- [Blender Documentation](https://docs.blender.org)
