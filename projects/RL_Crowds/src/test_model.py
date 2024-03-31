# Extrernal Includes
import os
import torch
import hou
from importlib import reload 

# RL Crowds Includes
import reinforce_learning_crowds
from environment import SimpleMoveEnv3D as Env
reload(reinforce_learning_crowds)

# Parameters
input_size = 1  # Adjust based on your environment's state size.
hidden_size = [128, 128, 64, 64, 32]  
output_size = 1  # Adjust based on your environment's action space size

# Load the trained model
env = Env()
reinforce = reinforce_learning_crowds.REINFORCE(input_size, hidden_size, output_size)
project_root = os.path.abspath(__file__).rsplit("/", 2)[0]
model_path = project_root + '/models/RL_Crowds.pth'
reinforce.policy_network = torch.load(model_path)
