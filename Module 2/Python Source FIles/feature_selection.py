import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

#Load the dataset test.csv and assign the number of components.
data = pd.read_csv('test.csv')
X=data.values
print len(X)
X = scale(X)
pca = PCA(n_components=23)
pca.fit(X)

var= pca.explained_variance_ratio_

var1=np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

print var1

#plt.plot(var1) Plot the corresponding Graph if required.
pca = PCA(n_components=100)
pca.fit(X)
X1=pca.fit_transform(X)

print len(X1)
np.savetxt('extract.csv',X1,'%.3f',delimiter=',')