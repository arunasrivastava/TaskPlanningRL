from ai2thor.controller import Controller
import time

# Initialize the controller with a specific scene
controller = Controller(scene="FloorPlan10")

# Function to print agent's state
def print_agent_state(event, action_name):
    metadata = event.metadata
    print(f"Action: {action_name}")
    print("Agent position:", metadata['agent']['position'])
    print("Agent rotation:", metadata['agent']['rotation'])
    print("Visible objects:", [obj['objectId'] for obj in metadata['objects'] if obj['visible']])
    print("-" * 50)

# Perform a series of RotateRight actions slowly
for i in range(5):  # Adjust the range for more or fewer rotations
    event = controller.step(action="RotateRight")
    print_agent_state(event, "RotateRight")
    time.sleep(1)  # Adding delay to simulate slow rotation

# Turn off the simulation
controller.stop()
print("Simulation stopped.")