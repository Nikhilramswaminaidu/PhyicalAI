import pybullet
import pybullet_data

import pybullet as p
import time

# Connect to the physics server
physicsClient = p.connect(p.GUI)

import pybullet_data

# Set the gravity
p.setGravity(0, 0, -9.81)

# Add a path for loading assets
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load the ground plane
planeId = p.loadURDF("plane.urdf")

# Load an object (e.g., a cube)
startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
r2d2Id = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# A more interactive simulation loop
for i in range(10000):
    p.stepSimulation()

    # Every 240 steps (once per second), print the position
    if i % 240 == 0:
        r2d2Pos, r2d2Orn = p.getBasePositionAndOrientation(r2d2Id)
        print(f"R2-D2 Position: {r2d2Pos}")

    time.sleep(1./240.)

# Disconnect from the physics server
p.disconnect()
# Save the simulation state
p.saveState("sine_simulation.bullet")

# Load the simulation state
p.loadState("sine_simulation.bullet")

# Run the simulation    
