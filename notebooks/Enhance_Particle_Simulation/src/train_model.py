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
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {loss.item()}')
    return model

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
    return x, y

# Parameters
num_epochs = 400
model_path = '/home/oriol/tools/DailyTips/notebooks/Enhance_Particle_Simulation/models/particle_model.pth'
points_data_csv = '/home/oriol/tools/DailyTips/notebooks/Enhance_Particle_Simulation/data/test.csv'
x, y = retrieve_particles(points_data_csv)
#input_params, simulated_behavior = generate_syntetic_data(3, 3, 1000)
# Train the machine learning model
model = train_model(x, y)
# Save the trained model
torch.save(model, model_path)