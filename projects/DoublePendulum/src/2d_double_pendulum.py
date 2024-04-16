import numpy as np

from scipy.integrate import solve_ivp

# Constants
g = hou.pwd().parm("g").eval()  # gravitational acceleration (m/s^2)
L1 = hou.pwd().parm("l1").eval()  # length of the first pendulum (meters)
L2 = hou.pwd().parm("l2").eval()  # length of the second pendulum (meters)
m1 = hou.pwd().parm("m1").eval()  # mass of the first pendulum (kg)
m2 = hou.pwd().parm("m2").eval()  # mass of the second pendulum (kg)

# Initial conditions: [theta1, z1, theta2, z2]
# theta1, theta2 are the initial angles (radians)
# z1, z2 are the initial angular velocities (rad/s)
initial_conditions = [np.pi / 2, 0, np.pi / 2, 0]

# Time settings
t_max = 30  # total time for the simulation
dt = 0.025  # timestep

# Equations of motion for the double pendulum
def double_pendulum(t, y):
    theta1, z1, theta2, z2 = y
    c, s = np.cos(theta1-theta2), np.sin(theta1-theta2)
    
    theta1_dot = z1
    z1_dot = (m2*g*np.sin(theta2)*c - m2*s*(L1*z1**2*c + L2*z2**2) -
              (m1+m2)*g*np.sin(theta1)) / L1 / (m1 + m2*s**2)
    
    theta2_dot = z2
    z2_dot = ((m1+m2)*(L1*z1**2*s - g*np.sin(theta2) + g*np.sin(theta1)*c) +
              m2*L2*z2**2*s*c) / L2 / (m1 + m2*s**2)
    
    return [theta1_dot, z1_dot, theta2_dot, z2_dot]

# Time array
t_eval = np.arange(0, t_max, dt)

# Solving the system of differential equations
solution = solve_ivp(double_pendulum, [0, t_max], initial_conditions, t_eval=t_eval, method='RK45')

# Unpack the solution
theta1, z1, theta2, z2 = solution.y

# Calculate the positions of the pendulums
x1 = L1 * np.sin(theta1)
y1 = -L1 * np.cos(theta1)
x2 = x1 + L2 * np.sin(theta2)
y2 = y1 - L2 * np.cos(theta2)

node = hou.pwd()
geo = node.geometry()

# Create houdini geometry
line = geo.createPolygon(is_closed=False)
for idx in range(0, len(x2)):
    points = geo.createPoints([[x1[idx], y2[idx], 0]])
    line.addVertex(points[0])