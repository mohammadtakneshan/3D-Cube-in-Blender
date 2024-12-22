# Import necessary modules
import bpy  # Blender's Python API
import sys  # For handling command-line arguments

# Clear all existing objects and physics bakes in the scene
bpy.ops.ptcache.free_bake_all()  # Free all physics cache
bpy.ops.object.select_all(action='SELECT')  # Select all objects
bpy.ops.object.delete(use_global=False)  # Delete all selected objects

# Set the world background to black
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)

# Create a large plane to act as the ground
bpy.ops.mesh.primitive_plane_add(size=100, enter_editmode=False, location=(0, 0, -40))

# Add physics properties to the plane
bpy.ops.rigidbody.object_add()  # Add a rigid body to the plane
bpy.context.object.rigid_body.type = 'PASSIVE'  # Set plane as passive (static)
bpy.context.object.rigid_body.collision_shape = 'MESH'  # Use mesh collision
bpy.context.object.rigid_body.collision_margin = 0  # No extra collision margin

# Add a Sun light source to the scene
bpy.ops.object.light_add(type='SUN', radius=2, location=(0, 0, 0), rotation=(0, 1, 5))
bpy.context.object.data.energy = 2  # Set light energy/intensity

# Add a camera to the scene
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(40, -9.18, -19),
                          rotation=(1.14494, 1.01332e-07, 1.17286))
bpy.context.object.data.lens = 30  # Set camera lens focal length in mm
bpy.context.scene.camera = bpy.context.object  # Set this camera as the active camera

# Create a material using material nodes
material = bpy.data.materials.new(name="Diffuse")  # Create a new material
material.use_nodes = True  # Enable material nodes
material_output = material.node_tree.nodes.get('Material Output')  # Get the material output node
diffuse = material.node_tree.nodes.new('ShaderNodeBsdfDiffuse')  # Create a diffuse shader node
diffuse.inputs['Color'].default_value = (0.27, 0.18, 0.8, 1)  # Set diffuse color (RGBA)
material.node_tree.links.new(material_output.inputs[0], diffuse.outputs[0])  # Connect nodes

# Parameters for creating a 3D grid of cubes
n_x = 4  # Number of cubes along the x-axis
n_y = 4  # Number of cubes along the y-axis
n_z = 4  # Number of cubes along the z-axis
step_size = 2  # Distance between cube centers
epsilon = 0.005  # Small gap to prevent overlapping
obj_size = step_size - epsilon  # Effective cube size

# Generate the grid of cubes
x_count = 0
for x in range(0, n_x):
    x_count += step_size
    y_count = 0
    for y in range(0, n_y):
        y_count += step_size
        z_count = 0
        for z in range(0, n_z):
            # Add a cube at the calculated location
            bpy.ops.mesh.primitive_cube_add(size=obj_size, location=(x_count, y_count, z_count))
            z_count += step_size

            # Add rigid body physics to the cube
            bpy.ops.rigidbody.object_add()
            bpy.context.object.rigid_body.mass = 20  # Set mass of the cube
            bpy.context.object.rigid_body.collision_shape = 'BOX'  # Use box collision
            bpy.context.object.rigid_body.friction = 1  # Set surface friction
            bpy.context.object.rigid_body.restitution = 0.2  # Set bounciness
            bpy.context.object.rigid_body.use_margin = True  # Enable collision margin
            bpy.context.object.rigid_body.collision_margin = 0  # No extra margin
            bpy.context.object.rigid_body.linear_damping = 0.35  # Reduce linear velocity over time
            bpy.context.object.rigid_body.angular_damping = 0.6  # Reduce angular velocity over time

            # Assign the created material to the cube
            bpy.context.object.active_material = material

# Bake all physics simulations
bpy.ops.ptcache.bake_all(bake=True)

# Save the Blender file if executed from the command line
if __name__ == "__main__":
    OUTPUT_BLEND_FILE = sys.argv[-1]  # Get output file name from command-line arguments
    print(OUTPUT_BLEND_FILE)  # Print the file name for confirmation
    bpy.ops.wm.save_mainfile(filepath=OUTPUT_BLEND_FILE)  # Save the .blend file