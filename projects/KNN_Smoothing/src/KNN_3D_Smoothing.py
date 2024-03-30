import numpy as np
from sklearn.neighbors import NearestNeighbors

def smooth_point_cloud(point_cloud, k=4, smoothing_factor=1):
    """
    Smooth a 3D point cloud using KNN-based smoothing.

    Parameters:
    - point_cloud (ndarray): Nx3 array representing the 3D point cloud.
    - k (int): Number of nearest neighbors to consider for smoothing.
    - smoothing_factor (float): Weighting factor for smoothing.

    Returns:
    - smoothed_point_cloud (ndarray): Nx3 array representing the smoothed 3D point cloud.
    """

    # Initialize nearest neighbors model
    nn_model = NearestNeighbors(n_neighbors=k+1)  # Include the point itself
    nn_model.fit(point_cloud)
    smoothed_point_cloud = np.zeros_like(point_cloud)
    # Iterate over each point in the point cloud
    for i, point in enumerate(point_cloud):
        # Find indices of k nearest neighbors (including the point itself)
        distances, indices = nn_model.kneighbors([point])
        indices = indices.squeeze()

        # Calculate centroid of k nearest neighbors
        centroid = np.mean(point_cloud[indices], axis=0)
        
        # Update the position of the point based on the centroid
        smoothed_point_cloud[i] = point * (1 - smoothing_factor) + centroid * smoothing_factor

    return smoothed_point_cloud


node = hou.pwd()
geo = node.geometry()

#point_cloud = np.random.rand(num_points, 3)  # Replace this with your own point cloud data
point_cloud = np.array([point.position() for point in geo.points()])
# Smooth the point cloud
smoothed_point_cloud = smooth_point_cloud(point_cloud, k=10, smoothing_factor=0.5)
for idx, point in enumerate(geo.points()):
    point.setPosition(smoothed_point_cloud[idx])