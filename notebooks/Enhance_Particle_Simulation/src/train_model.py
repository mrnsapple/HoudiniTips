import numpy as np
import pandas as pd
import torch
import ast
from model import ComplexNet
# Define a simple neural network model


# Train the machine learning model
def train_model(x, y):
    model = ComplexNet()
    criterion = torch.nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    for epoch in range(num_epochs):
        inputs = torch.tensor(x, dtype=torch.float32)
        targets = torch.tensor(y, dtype=torch.float32)
        
        optimizer.zero_grad()
        outputs = model(inputs)
        #print(targets.shape)
        #print(outputs.shape)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')
    return model

# Integrate machine learning-driven behaviors into particle simulation
def enhance_particle_simulation(input_params, model_path):
    model = torch.load(model_path)  # Load the trained model
    with torch.no_grad():
        inputs = torch.tensor(input_params, dtype=torch.float32)
        predicted_behavior = model(inputs).numpy()
        # Integrate predicted behavior into particle simulation
        integrate_predicted_behavior(predicted_behavior)

# Mock function to integrate predicted behavior into particle simulation
def integrate_predicted_behavior(predicted_behavior):
    print("Integrating predicted behavior into particle simulation...")
    # Placeholder function for integrating predicted behavior into particle simulation

def generate_syntetic_data(num_input_params, num_output_param, num_samples):
    # Generate synthetic particle data for training
    input_params = np.random.rand(num_samples, num_input_params)
    simulated_behavior = np.random.rand(num_samples, num_output_params)
    return input_params, simulated_behavior

def retrieve_particles(points_data_csv):
    df = pd.read_csv(points_data_csv)
    x = np.array([])
    y = np.array([])
    for index, row in df.iterrows():
        points_position = [ast.literal_eval(row["Points Position"])]
        next_frame_points_position = df[df["Frame"] == row["Frame"] + 1]
        if next_frame_points_position.empty:
            continue
        next_frame_points_position = [ast.literal_eval(next_frame_points_position.iloc[0]["Points Position"])  ]  
        if np.size(x) <= 0:
            x = points_position
            y = next_frame_points_position
        else:
            x = np.concatenate((x, points_position))
            y = np.concatenate((y, next_frame_points_position))
    print(np.shape(x))
    print(np.shape(y))#(121, 2500, 3)
    return x, y
# Parameters
num_input_params = 3  # Number of input parameters affecting particle behavior
num_output_params = 3  # Number of output parameters representing particle behavior
num_samples = 1000  # Number of training samples
num_epochs = 400
model_path = '/home/oriol/tools/DailyTips/notebooks/Enhance_Particle_Simulation/models/particle_model.pth'
points_data_csv = '/home/oriol/tools/DailyTips/notebooks/Enhance_Particle_Simulation/data/test.csv'
x, y = retrieve_particles(points_data_csv)
#input_params, simulated_behavior = generate_syntetic_data(num_input_params, num_output_params, num_samples)
# Train the machine learning model
model = train_model(x, y)
# Save the trained model
torch.save(model, model_path)