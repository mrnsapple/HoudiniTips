import numpy as np

class SimpleMoveEnv3D:
    def __init__(self, target=np.array([5.0, 5.0, 5.0]), start_position=np.array([0.0, 0.0, 0.0]), step_size=1.0):
        """
        Initialize the environment.

        :param target: The target position in 3D space as a numpy array.
        :param start_position: The starting position of the agent in 3D space.
        :param step_size: The magnitude of each step in any direction.
        """
        self.target = target
        self.position = start_position
        self.step_size = step_size
        self.action_space = np.array([
            [-1, 0, 0],  # Left
            [1, 0, 0],   # Right
            [0, -1, 0],  # Down
            [0, 1, 0],   # Up
            [0, 0, -1],  # Back
            [0, 0, 1],   # Forward
            [0.0, 0.0, 0.0] # Not Move
        ])
        self.action_space_size = len(self.action_space)
        self.state_size = 3 # The current velocity of the agent.

    def reset(self):
        """
        Reset the environment to the starting state.

        :return: The initial state of the agent.
        """
        self.position = np.array([0.0, 0.0, 0.0])
        return self.position.copy()

    def step(self, action):
        """
        Apply an action and update the environment state.

        :param action: An integer representing the action to be taken.
        :return: A tuple containing the new state, reward, and done flag.
        """
        # Ensure action is valid
        if action < 0 or action >= len(self.action_space):
            raise ValueError("Invalid action.")

        # Calculate new position
        direction = self.action_space[action]
        new_position = self.position + direction * self.step_size
        #print("pos", self.position, direction, self.step_size, new_position)
        # Calculate reward based on the change in distance to the target
        distance_before = np.linalg.norm(self.target - self.position)
        distance_after = np.linalg.norm(self.target - new_position)
        reward = distance_before - distance_after  # Positive reward for getting closer

        # Update the state
        self.position = new_position
        done = np.array_equal(self.position, self.target)

        return self.position.copy(), reward, done, {}

    def render(self, mode='human'):
        """
        Render the environment state for visualization.

        :param mode: The mode for rendering.
        """
        print(f"Position: {self.position}")
