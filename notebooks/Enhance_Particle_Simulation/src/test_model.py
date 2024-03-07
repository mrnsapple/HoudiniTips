import numpy as np
import torch
from train_model import ParticleModel

# Define a simple neural network model
#class ParticleModel(torch.nn.Module):
#    def __init__(self, num_input_params, num_output_params):
#        super(ParticleModel, self).__init__()
#        self.fc1 = torch.nn.Linear(num_input_params, 64)
#        self.fc2 = torch.nn.Linear(64, 64)
#        self.fc3 = torch.nn.Linear(64, num_output_params)
        
#    def forward(self, x):
#        x = torch.relu(self.fc1(x))
#        x = torch.relu(self.fc2(x))
#        x = self.fc3(x)
#        return x

def integrate_predicted_behavior(predicted_behavior):
    print(predicted_behavior)

def enhance_particle_simulation(input_params, model_path):
    model = torch.load(model_path)  # Load the trained model
    with torch.no_grad():
        inputs = torch.tensor(input_params, dtype=torch.float32)
        predicted_behavior = model(inputs).numpy()
        # Integrate predicted behavior into particle simulation
        integrate_predicted_behavior(predicted_behavior)


# Parameters
num_input_params = 3 
model_path = '/home/oriol/tools/DailyTips/notebooks/Enhance_Particle_Simulation/models/particle_model.pth'

# Use the trained model to enhance particle simulation
new_input_params = np.random.rand(1, num_input_params)  # New input parameters for simulation
enhance_particle_simulation(new_input_params, model_path)