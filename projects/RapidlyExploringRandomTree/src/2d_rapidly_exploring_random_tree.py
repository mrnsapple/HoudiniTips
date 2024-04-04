import numpy as np
#import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def distance(node1, node2):
    return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def steer(from_node, to_point, step_size):
    dist = distance(from_node, Node(to_point[0], to_point[1]))
    if dist < step_size:
        return Node(to_point[0], to_point[1])
    else:
        theta = np.arctan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
        return Node(from_node.x + step_size * np.cos(theta), from_node.y + step_size * np.sin(theta))

def nearest_node(nodes, random_point):
    distances = [distance(node, Node(random_point[0], random_point[1])) for node in nodes]
    min_index = distances.index(min(distances))
    return nodes[min_index]import numpy as np
#import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def distance(node1, node2):
    return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def steer(from_node, to_point, step_size):
    dist = distance(from_node, Node(to_point[0], to_point[1]))
    if dist < step_size:
        return Node(to_point[0], to_point[1])
    else:
        theta = np.arctan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
        return Node(from_node.x + step_size * np.cos(theta), from_node.y + step_size * np.sin(theta))

def nearest_node(nodes, random_point):
    distances = [distance(node, Node(random_point[0], random_point[1])) for node in nodes]
    min_index = distances.index(min(distances))
    return nodes[min_index]

def is_free_path(from_node, to_node):
    # For simplicity, this example assumes there are no obstacles.
    # Implement actual collision checking with obstacles here.
    return True

def rrt(start, goal, step_size=1.0, num_iterations=1000):
    nodes = [Node(start[0], start[1])]
    for i in range(num_iterations):
        random_point = np.random.rand(2) * 100  # Assuming a 100x100 space
        nearest = nearest_node(nodes, random_point)
        new_node = steer(nearest, random_point, step_size)
        
        if is_free_path(nearest, new_node):
            new_node.parent = nearest
            nodes.append(new_node)
            
            if distance(new_node, Node(goal[0], goal[1])) <= step_size:
                print("Goal reached.")
                return nodes
    return nodes

def plot(nodes, start, goal):
    #plt.figure()
    geometry = hou.pwd().geometry()
    for node in nodes:import numpy as np
#import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def distance(node1, node2):
    return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def steer(from_node, to_point, step_size):
    dist = distance(from_node, Node(to_point[0], to_point[1]))
    if dist < step_size:
        return Node(to_point[0], to_point[1])
    else:
        theta = np.arctan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
        return Node(from_node.x + step_size * np.cos(theta), from_node.y + step_size * np.sin(theta))

def nearest_node(nodes, random_point):
    distances = [distance(node, Node(random_point[0], random_point[1])) for node in nodes]
    min_index = distances.index(min(distances))
    return nodes[min_index]

def is_free_path(from_node, to_node):
    # For simplicity, this example assumes there are no obstacles.
    # Implement actual collision checking with obstacles here.
    return True

def rrt(start, goal, step_size=1.0, num_iterations=1000):
    nodes = [Node(start[0], start[1])]
    for i in range(num_iterations):
        random_point = np.random.rand(2) * 100  # Assuming a 100x100 space
        nearest = nearest_node(nodes, random_point)
        new_node = steer(nearest, random_point, step_size)
        
        if is_free_path(nearest, new_node):
            new_node.parent = nearest
            nodes.append(new_node)
            
            if distance(new_node, Node(goal[0], goal[1])) <= step_size:
                print("Goal reached.")
                return nodes
    return nodes

def plot(nodes, start, goal):
    geo = hou.pwd().geometry()
    for node in nodes:
        if node.parent:
            points = geo.createPoints([[node.x, node.y, 0], [node.parent.x, node.parent.y, 0]])
            print(points)
            line = geo.createPolygon()
            line.addVertex(points[0])
            line.addVertex(points[1])


start = (0, 0)
goal = (90, 90)
nodes = rrt(start, goal)
print(nodes, start, goal)
plot(nodes, start, goal)

def is_free_path(from_node, to_node):
    # For simplicity, this example assumes there are no obstacles.
    # Implement actual collision checking with obstacles here.
    return True

def rrt(start, goal, step_size=1.0, num_iterations=1000):
    nodes = [Node(start[0], start[1])]
    for i in range(num_iterations):
        random_point = np.random.rand(2) * 100  # Assuming a 100x100 space
        nearest = nearest_node(nodes, random_point)
        new_node = steer(nearest, random_point, step_size)
        
        if is_free_path(nearest, new_node):
            new_node.parent = nearest
            nodes.append(new_node)
            
            if distance(new_node, Node(goal[0], goal[1])) <= step_size:
                print("Goal reached.")
                return nodes
    return nodes

def plot(nodes, start, goal):
    #plt.figure()
    geometry = hou.pwd().geometry()
    for node in nodes:import numpy as np
#import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

def distance(node1, node2):
    return np.sqrt((node1.x - node2.x)**2 + (node1.y - node2.y)**2)

def steer(from_node, to_point, step_size):
    dist = distance(from_node, Node(to_point[0], to_point[1]))
    if dist < step_size:
        return Node(to_point[0], to_point[1])
    else:
        theta = np.arctan2(to_point[1] - from_node.y, to_point[0] - from_node.x)
        return Node(from_node.x + step_size * np.cos(theta), from_node.y + step_size * np.sin(theta))

def nearest_node(nodes, random_point):
    distances = [distance(node, Node(random_point[0], random_point[1])) for node in nodes]
    min_index = distances.index(min(distances))
    return nodes[min_index]

def is_free_path(from_node, to_node):
    # For simplicity, this example assumes there are no obstacles.
    # Implement actual collision checking with obstacles here.
    return True

def rrt(start, goal, step_size=1.0, num_iterations=1000):
    nodes = [Node(start[0], start[1])]
    for i in range(num_iterations):
        random_point = np.random.rand(2) * 100  # Assuming a 100x100 space
        nearest = nearest_node(nodes, random_point)
        new_node = steer(nearest, random_point, step_size)
        
        if is_free_path(nearest, new_node):
            new_node.parent = nearest
            nodes.append(new_node)
            
            if distance(new_node, Node(goal[0], goal[1])) <= step_size:
                print("Goal reached.")
                return nodes
    return nodes

def plot(nodes, start, goal):
    geo = hou.pwd().geometry()
    for node in nodes:
        if node.parent:
            points = geo.createPoints([[node.x, node.y, 0], [node.parent.x, node.parent.y, 0]])
            print(points)
            line = geo.createPolygon()
            line.addVertex(points[0])
            line.addVertex(points[1])


start = (0, 0)
goal = (90, 90)
nodes = rrt(start, goal)
print(nodes, start, goal)
plot(nodes, start, goal)