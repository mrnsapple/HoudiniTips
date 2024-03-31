# External Includes
import sys
from importlib import reload
import numpy as np
sys.path.append("/home/oriol/tools/DailyTips/projects/RL_Crowds/src")

# Rl Crowd Includes
import test_model
reload(test_model)

# Set new velocity for each agent
step = 2
node = hou.pwd()
geo = node.geometry()
for point in geo.points():
    # Retrieve the point position, which correspond to the state of the reinforce learning algorith
    state = point.attribValue("P")
    # Retrieve the point velocity
    velocity = point.attribValue("v")
    # Get the action based in the state
    print(state)
    action = test_model.reinforce.select_action(np.array(state))
    calculated_velocity = test_model.env.action_space[action]
    velocity = velocity + calculated_velocity * step
    point.setAttribValue("v", velocity)