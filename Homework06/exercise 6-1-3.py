from scipy.io import loadmat
from sklearn.neighbors import KNeighborsClassifier as nb
from pylab import *
import math as m

import numpy as np

Wine = loadmat('Data/wine.mat')
X = Wine['X']
NAA = np.delete(X,10,axis=1) #NonAlcoholAttritutes
AP = X[:,10] #AlcoholPercentage

#Convert the alcoholPercentages form float to long. Otherwise we get a "type is continuous"-error
APT = []
for i in range(len(AP)):
    APT.append(long(AP[i]))


# knn = nb(n_neighbors=4, metric='euclidean')
# knn.fit(NAA, APT)
#
# nbr = knn.kneighbors([NAA[5]], n_neighbors=7)
# print nbr[1][0]
xaxis = []
predError = []
for k in range(1, 40):
    xaxis.append(k)
    print k
    predAP = []
    knn = nb(n_neighbors=k, metric='euclidean')
    knn.fit(NAA, APT)
    for i in range(len(AP)):
        nbr = knn.kneighbors([NAA[i]], n_neighbors=k+1)
        sumAP = 0.0
        for n in range(len(nbr[1][0])):
            if (nbr[1][0][n] != i):
                sumAP += AP[nbr[1][0][n]]
        predAP.append(np.divide(sumAP, k))
    error = 0.0
    for p in range(len(predAP)):
        error += m.pow((predAP[p] - AP[p]), 2)
    predError.append(np.divide(error, len(predAP)))

print predError

plt.plot(xaxis, predError)
plt.title('Mean Squared Error with k neighbors')
plt.xlabel('neighbors (k)')
plt.ylabel('Mean Squared Error')
plt.show()