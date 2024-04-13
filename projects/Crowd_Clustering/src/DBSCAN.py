from numpy import unique, where
import numpy as np
from sklearn.datasets import make_classification
from sklearn.cluster import DBSCAN

node = hou.pwd()
geo = node.geometry()
points = geo.points()

# initialize the data set we'll work with
training_data = np.array([[point.position().x(), point.position().z()] for point in points])
# define the model
dbscan_model = DBSCAN(eps=node.parm("eps").eval(), min_samples=node.parm("min_samples").eval())
# train the model
dbscan_model.fit(training_data)
labels = dbscan_model.labels_
# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

for idx, point in enumerate(points):
    point.setAttribValue("cluster", int(labels[idx]))
geo.setGlobalAttribValue("n_clusters", n_clusters_)
geo.setGlobalAttribValue("n_noise", n_noise_)

print("Estimated number of clusters: %d" % n_clusters_)
print("Estimated number of noise points: %d" % n_noise_)
