import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        
        # Define the layers of the neural network
        self.fc1 = nn.Linear(3, 64)  # 3 input features, 64 output features
        self.fc2 = nn.Linear(64, 32)  # 64 input features, 32 output features
        self.fc2 = nn.Linear(32, 32)  # 64 input features, 32 output features
        self.fc2 = nn.Linear(32, 32)  # 64 input features, 32 output features
        self.fc2 = nn.Linear(32, 32)  # 64 input features, 32 output features

        self.fc3 = nn.Linear(32, 3)  # 32 input features, 10 output features (assuming 10 classes)
        self.relu = nn.ReLU()
        self.softmax = nn.Softmax(dim=1)  # Softmax activation for classification

    def forward(self, x):
        # Define the forward pass
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.fc3(x)
        x = self.softmax(x)
        return x


class ComplexNet(nn.Module):
    def __init__(self):
        super(ComplexNet, self).__init__()
        
        # Define the layers of the neural network
        self.fc1 = nn.Linear(3, 128)  # 3 input features, 128 output features
        self.fc2 = nn.Linear(128, 64)  # 128 input features, 64 output features
        #self.fc5 = nn.Linear(64, 64)  # 128 input features, 64 output features
        #self.fc6 = nn.Linear(64, 64)  # 128 input features, 64 output features

        self.fc3 = nn.Linear(64, 32)  # 64 input features, 32 output features
        self.fc4 = nn.Linear(32, 3)  # 32 input features, 10 output features (assuming 10 classes)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.5)  # Adding dropout for regularization
        #self.softmax = nn.Softmax(dim=1)  # Softmax activation for classification

    def forward(self, x):
        # Define the forward pass
        x = self.relu(self.fc1(x))
        x = self.dropout(x)  # Applying dropout after the first layer
        x = self.relu(self.fc2(x))
        x = self.dropout(x)  # Applying dropout after the second layer
        #x = self.relu(self.fc5(x))
        #x = self.dropout(x)  # Applying dropout after the second layer
        ##x = self.relu(self.fc6(x))
       # x = self.dropout(x)  # Applying dropout after the second layer
        x = self.relu(self.fc3(x))
        x = self.dropout(x)  # Applying dropout after the third layer
        x = self.fc4(x)
        #x = self.softmax(x)
        return x