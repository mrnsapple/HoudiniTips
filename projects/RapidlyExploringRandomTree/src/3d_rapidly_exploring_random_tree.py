import numpy as np

class Node:
    """A node class for A* Pathfinding"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.parent = None

def distance(node1, node2):
    return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2 + (node1.z - node2.z)**2)

def steer(from_node, to_point, step_size):
    dist = distance(from_node, Node(to_point[0], to_point[1], to_point[2]))
    if dist < step_size:
        return Node(to_point[0], to_point[1], to_point[2])
    else:
        theta = np.arctan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
        phi = np.arccos((to_point[2] - from_node.z) / dist)
        return Node(from_node.x + step_size * np.cos(theta) * np.sin(phi),
                    from_node.y + step_size * np.sin(theta) * np.sin(phi),
                    from_node.z + step_size * np.cos(phi))

def nearest_node(nodes, random_point):
    distances = [distance(node, Node(random_point[0], random_point[1], random_point[2])) for node in nodes]
    min_index = distances.index(min(distances))
    return nodes[min_index]

def is_free_path(from_node, to_node):
    # To Implement actual collision checking with obstacles here.
    return True

def rrt(start, goal, step_size=1.0, num_iterations=3000):
    nodes = [Node(start[0], start[1], start[2])]
    for i in range(num_iterations):
        random_point = np.random.rand(3) * 200  # Assuming a 100x100x100 space
        nearest = nearest_node(nodes, random_point)
        new_node = steer(nearest, random_point, step_size)
        
        if is_free_path(nearest, new_node):
            new_node.parent = nearest
            nodes.append(new_node)
            
            if distance(new_node, Node(goal[0], goal[1], goal[2])) <= step_size:
                print("Goal reached.")
                return nodes
    return nodes

def plot(nodes, start, goal):
    geo = hou.pwd().geometry()
    for node in nodes:
        if node.parent:
            points = geo.createPoints([[node.x, node.y, node.z], [node.parent.x, node.parent.y, node.z]])
            line = geo.createPolygon()
            line.addVertex(points[0])
            line.addVertex(points[1])
       

start = (0, 0, 0)
goal = (100, 3000, 3000)
nodes = rrt(start, goal)
print(nodes, start, goal)
plot(nodes, start, goal)