import numpy as np
import torch
from importlib import reload
from model import *

def integrate_predicted_behavior(predicted_behavior):
    print(predicted_behavior)
    print(len(predicted_behavior))
    percentage = 1
    for idx, point in enumerate(hou.pwd().geometry().points()):
        print(predicted_behavior[idx])
        predicted_behavior[idx] = predicted_behavior[idx]*percentage + np.array(point.position())*(1-percentage)
        point.setPosition( predicted_behavior[idx].tolist())

def enhance_particle_simulation(input_params, model_path):
    model = torch.load(model_path)  # Load the trained model
    with torch.no_grad():
        inputs = torch.tensor(input_params, dtype=torch.float32)
        predicted_behavior = model(inputs).numpy()
        # Integrate predicted behavior into particle simulation
        integrate_predicted_behavior(predicted_behavior)

# Parameters
project_root = os.path.abspath(__file__).rsplit("/", 2)[0]
model_path = project_root + '/models/particle_model.pth'
node = hou.pwd()
geo = node.geometry()
new_input_parms = [[p.position().x(),p.position().y(), p.position().z()] for p in geo.points()]
enhance_particle_simulation(new_input_parms, model_path)