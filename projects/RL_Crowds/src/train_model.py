# External Modules
import os
import numpy as np
import torch

# RL Crowds modules
from reinforce_learning_crowds import REINFORCE
from environment import SimpleMoveEnv3D as Env

def train(env, reinforce, num_episodes):
    for episode in range(num_episodes):
        state = env.reset()
        for t in range(1, 1000):  # Replace 10000 with the actual max timestep
            action = reinforce.select_action(state)
            state, reward, done, _ = env.step(action)
            reinforce.rewards.append(reward)
            if done:
                break
        reinforce.update_policy()
        print("Action:{}, State:{},reward:{}, done:{}".format(action, state, reward, done))
        print("Episode {} finished after {} timesteps".format(episode + 1, t + 1))

# Params
env = Env(target=np.array([-200, 0, 300]))
input_size = env.state_size  # Adjust based on your environment's state size.
hidden_size = 128
output_size = env.action_space_size  # Adjust based on your environment's action space size

# Train the machine learning model
reinforce = REINFORCE(input_size, hidden_size, output_size)
train(env, reinforce, num_episodes=300)

# Save the trained model
project_root = os.path.abspath(__file__).rsplit("/", 2)[0]
model_path = project_root + '/models/RL_Crowds.pth'
torch.save(reinforce.policy_network, model_path)