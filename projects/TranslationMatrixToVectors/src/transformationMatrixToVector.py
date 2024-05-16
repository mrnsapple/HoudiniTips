import numpy as np

node = hou.pwd()
geo = node.geometry()
point = geo.points()[0]
# Use drop down menu to select examples.
T = np.array(point.attribValue("transform"))
# Example 4x4 matrix containing rotation, scaling, and translation
T = T.reshape(-1, 4).T
# Extract translation
translation = T[0:3, 3]
# Extract the 3x3 matrix
R_s = T[0:3, 0:3]
# Use SVD to decompose the 3x3 matrix
U, S, Vt = np.linalg.svd(R_s)
# Assuming no shearing, the rotation matrix can be approximated by
R = np.dot(U, Vt)
yaw = np.arctan2(R[1, 0], R[0, 0]) 
pitch = np.arctan2(-R[2, 0], np.sqrt(R[2, 1]**2 + R[2, 2]**2))
roll = np.arctan2(R[2, 1], R[2, 2])
# Convert from radians to degrees, if preferred 
yaw_deg = np.degrees(yaw) 
pitch_deg = np.degrees(pitch) 
roll_deg = np.degrees(roll)
rotation = [roll_deg, pitch_deg, yaw_deg]
# The scale components are the singular values, under the assumption of no shearing
scale = S
# Set the houdini attributes
point.setAttribValue("translation", translation)
point.setAttribValue("rotation", rotation)
point.setAttribValue("scale", scale)