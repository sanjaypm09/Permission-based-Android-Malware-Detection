import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")
from sklearn.cluster import KMeans

from numpy import genfromtxt


my_data = np.loadtxt('extract.csv', delimiter=',')
print my_data




kmeans = KMeans(n_clusters=2)
kmeans.fit(my_data)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
colors = ["g.","r.","c.","y."]

for i in range(len(my_data)):
    #print("coordinate:",my_data[i], "label:", labels[i])
    plt.plot(my_data[i][0], my_data[i][1], colors[labels[i]], markersize = 10)


plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)
print(centroids[0],centroids[1])

plt.show()