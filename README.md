![Cube](https://github.com/user-attachments/assets/92a21d33-e13b-443e-b420-e3fed52a0f91) # 3D CubE in Blender


# Graphics-Systems-Proj-2110



A Project Created using Blender


https://github.com/user-attachments/assets/d4c0ccbb-c3a8-45c7-b390-a35a3c1d4f5a




# Blender Project Documentation

## Project Overview

This documentation outlines the key steps, methods, and settings used in the Blender project. The project focuses on creating a visually compelling scene incorporating basic modeling, material and texture assignments, animations, Python scripting, and rendering.

---

## 1. Modeling

The following basic modeling operations and transformations were employed:

1. **Scaling**: Adjusted the size of objects to fit the scene proportions. For example, the base of the table was scaled to match the tabletop dimensions.
2. **Rotation**: Oriented objects like chairs and lamps to ensure accurate placement within the scene.
3. **Extrusion**: Created depth in the table legs and window frames from basic 2D shapes.
4. **Subdivision**: Applied to the sofa and cushion models to create smooth, realistic surfaces.
5. **Boolean Operations**: Used to carve out spaces for doorways and create intersecting geometry for complex shapes.

### Key Settings

- **Units**: Metric system was used to ensure realistic proportions.
- **Origin Adjustments**: Set accurately for rotation and scaling transformations.

---

## 2. Appearance

### Materials

- **Base Color**: Assigned realistic colors to objects, such as wood textures for the table and chairs, and metallic finishes for the lamp.
    - Example: Applied a rich oak material to the table with a warm brown hue.

### Textures

- **Image Textures**: Imported high-resolution textures for the walls and floor.
- **Procedural Textures**: Generated a noise-based texture for the rug and marble surfaces for decorative objects.
- **UV Mapping**: Carefully unwrapped the sofa and cushion models to ensure textures aligned properly.

### Settings

- **Shader**: Principled BSDF was used for most materials.
- **Roughness**: Adjusted to differentiate between matte and shiny surfaces.
- **Specular**: Tuned for reflective objects like the glass vase.

---

## 3. Animation

### Timeline Keyframes

- Added keyframes to animate a pendulum motion for the wall clock and the swinging lamp.
- Keyframed object scaling and rotation for a growing plant animation.

### Follow Path Animation

- Created a circular path for a drone camera to orbit around the central table.
- Used the "Follow Path" constraint to attach the camera to the path, ensuring smooth motion.

### Physics Simulation

- Adjusted properties such as mass, friction, collision margins, and damping to simulate realistic interactions.
- Cubes were arranged dynamically in a grid and animated to interact with a rigid-body-enabled floor plane.

### Settings

- **Interpolation Mode**: Set to "Bezier" for smooth, realistic motion.
- **Frame Rate**: 24 fps for cinematic quality.

---

## 4. Scripting

### Python Automation

A custom Python script was written to automate repetitive tasks such as:

- Batch renaming of objects to maintain consistency.
- Generating cubes dynamically in a grid formation.
- Assigning rigid body physics properties to all objects.

### Script Explanation

The provided Python script automates the creation and physics setup of a 3D grid of cubes in Blender. Key features include:

1. **Cube Generation**:
    - Nested loops dynamically create cubes along the X, Y, and Z axes.
    - The `spacing` variable ensures proper separation between cubes to prevent overlap.
2. **Physics Assignment**:
    - Each cube is given active rigid body properties with defined mass and shape settings.
3. **Reusable Design**:
    - The script is parameterized to allow easy customization of the number of cubes and their spacing.

### Script Example

```
import bpy

# Parameters
num_cubes = 10  # Number of cubes per axis
spacing = 2     # Distance between cubes

# Generate cubes in a grid
for x in range(num_cubes):
    for y in range(num_cubes):
        for z in range(num_cubes):
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x * spacing, y * spacing, z * spacing))
            cube = bpy.context.object
            bpy.ops.rigidbody.object_add()
            cube.rigid_body.type = 'ACTIVE'
            cube.rigid_body.mass = 20
```

---

## 5. Rendering

### Render Settings

- **Engine**: Cycles was selected for realistic lighting and shading.
- **Samples**: Set to 512 to balance quality and performance.
- **Output Resolution**: 1920x1080 (Full HD) for a professional look.
- **Output Format**: PNG for lossless quality.

### Experience

- **Command-Line Rendering**: Automated rendering tasks via command-line for batch processing.
- **Denoising**: Enabled post-render denoising to remove grain from low-light areas.
- **Adaptive Sampling**: Used to optimize render times for complex scenes.

---

## 6. Dependencies

### Windows

1. **Blender**: Download and install the latest version from blender.org.
2. **Python**: Ensure Python 3.x is installed (included with Blender).
3. **Graphics Drivers**: Update your GPU drivers for optimal Cycles rendering performance.

### Mac

1. **Blender**: Download and install the latest version from blender.org.
2. **Python**: Ensure Python 3.x is installed (included with Blender).
3. **Metal Support**: Verify that your Mac supports Metal for GPU rendering (available on macOS 10.13 or later).

---

## 7. Using the Script to Create a New Blend File

You can use the provided script to generate a brand new `.blend` file with a grid of cubes. Follow these steps:

1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the following commands:

```
mkdir -p output
blender -b -P blender_cubes.py -- output/blender_cubes.blend
```

### Explanation:

- `mkdir -p output`: Creates an `output` directory if it doesn't exist.
- `blender -b`: Runs Blender in background mode.
- `P blender_cubes.py`: Executes the provided Python script.
- `- output/blender_cubes.blend`: Specifies the output path for the generated `.blend` file.

This command will create a new Blender file containing the grid of cubes as defined in the script.

---

## Conclusion

This project successfully integrates various Blender functionalities to create a dynamic and visually appealing scene. The scripting and animation components ensure both efficiency and realism. For detailed code and assets, refer to the project resources.

## Demo

See the Blender-proj.mp4
