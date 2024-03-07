node = hou.pwd()
geo = node.geometry()
import numpy as np

def tutte_embedding_3d(adj_matrix):
    # Compute degree matrix
    degrees = np.sum(adj_matrix, axis=1)
    D = np.diag(degrees)
    # Compute Laplacian matrix
    L = D - adj_matrix
    # Compute the eigenvectors corresponding to the smallest non-zero eigenvalues
    eigvals, eigvecs = np.linalg.eigh(L)
    non_zero_indices = np.where(eigvals > 1e-10)[0]
    nonzero_eigvecs = eigvecs[:, non_zero_indices]
    # Take the eigenvectors corresponding to the smallest non-zero eigenvalues
    embedding = nonzero_eigvecs[:, 1:4]  # Take the second, third, and fourth eigenvectors
    # Normalize embedding
    embedding_norm = np.linalg.norm(embedding, axis=1)
    embedding_normalized = embedding / embedding_norm[:, None]
    return embedding_normalized

def calculate_adj_matrix():
    adj_matrix = np.zeros((len(geo.points()), len(geo.points())), dtype=int)
    for point in geo.points():
        point_neighbours = point.attribValue("neighbours")
        for point_neighbour in point_neighbours:
            adj_matrix[point.number()][point_neighbour] = 1
            adj_matrix[point_neighbour][point.number()] = 1
    return adj_matrix

adj_matrix = calculate_adj_matrix()
# Perform Tutte embedding
embedding = tutte_embedding_3d(adj_matrix)
for idx, point in enumerate(geo.points()):
    point.setPosition(embedding[idx].tolist())
