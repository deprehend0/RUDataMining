#Exercise 4.1
from scipy.io import loadmat
from sklearn.cluster import k_means
from Toolbox import clusterPlot
from Toolbox import clusterVal
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# S1 = loadmat('Data/synth1.mat')
# X1 = S1['X']
# y1 = S1['y']
# S2 = loadmat('Data/synth2.mat')
# X2 = S2['X']
# y2 = S2['y']
# S3 = loadmat('Data/synth3.mat')
# X3 = S3['X']
# y3 = S3['y']
# S4 = loadmat('Data/synth4.mat')
# X4 = S4['X']
# y4 = S4['y']
#
# clusters = 4
# K1 = k_means(X1, n_clusters=clusters)
# K2 = k_means(X2, n_clusters=clusters)
# K3 = k_means(X3, n_clusters=clusters)
# K4 = k_means(X4, n_clusters=clusters)

# clusterPlot.clusterPlot(X1, K1[1], centroids=K1[0], y=y1)
# plt.xlabel('Attribute A')
# plt.ylabel('Attribute B')
# plt.show()
# clusterPlot.clusterPlot(X2, K2[1], centroids=K2[0], y=y2)
# plt.xlabel('Attribute A')
# plt.ylabel('Attribute B')
# plt.show()
# clusterPlot.clusterPlot(X3, K3[1], centroids=K3[0], y=y3)
# plt.xlabel('Attribute A')
# plt.ylabel('Attribute B')
# plt.show()
# clusterPlot.clusterPlot(X4, K4[1], centroids=K4[0], y=y4)
# plt.xlabel('Attribute A')
# plt.ylabel('Attribute B')
# plt.show()

# 4.1.2
# kmeansArray = []
# for i in range(1, 11):
#     km1 = k_means(X1, n_clusters=i)
#     kmeansArray.append(km1)
#
# for i in range(0, 10):
#     clusterPlot.clusterPlot(X1,kmeansArray[i][1])
    # plt.show()

# cluster = []
# for i in range(0, 10):
#     cluster.append(clusterVal.clusterVal(y1, kmeansArray[i][1]))
# entropy1 = []
# purity1 = []
# rand1 = []
# jaccard1 = []
#
# for i in range(0, 10):
#     entropy1.append(cluster[i][0])
#     purity1.append(cluster[i][1])
#     rand1.append(cluster[i][2])
#     jaccard1.append(cluster[i][3])
#
# k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# plt.plot(k, cluster, k, purity1, k, rand1, k, jaccard1)
# plt.show()

# kmeansArray2 = []
# for i in range(1, 11):
#     km2 = k_means(X2, n_clusters=i)
#     kmeansArray2.append(km2)
#
# for i in range(0, 10):
#     clusterPlot.clusterPlot(X2,kmeansArray2[i][1])
    # plt.show()

# cluster2 = []
# for i in range(0, 10):
#     cluster2.append(clusterVal.clusterVal(y2, kmeansArray2[i][1]))
# entropy2 = []
# purity2 = []
# rand2 = []
# jaccard2 = []
#
# for i in range(0, 10):
#     entropy2.append(cluster2[i][0])
#     purity2.append(cluster2[i][1])
#     rand2.append(cluster2[i][2])
#     jaccard2.append(cluster2[i][3])
#
# plt.plot(k, cluster2, k, purity2, k, rand2, k, jaccard2)
# plt.show()

# kmeansArray3 = []
# for i in range(1, 11):
#     km3 = k_means(X3, n_clusters=i)
#     kmeansArray3.append(km3)
#
# for i in range(0, 10):
#     clusterPlot.clusterPlot(X3,kmeansArray3[i][1])
    # plt.show()

# cluster3 = []
# for i in range(0, 10):
#     cluster3.append(clusterVal.clusterVal(y3, kmeansArray3[i][1]))
# entropy3 = []
# purity3 = []
# rand3 = []
# jaccard3 = []
#
# for i in range(0, 10):
#     entropy3.append(cluster3[i][0])
#     purity3.append(cluster3[i][1])
#     rand3.append(cluster3[i][2])
#     jaccard3.append(cluster3[i][3])
#
# plt.plot(k, cluster3, k, purity3, k, rand3, k, jaccard3)
# plt.show()

# kmeansArray4 = []
# for i in range(1, 11):
#     km4 = k_means(X4, n_clusters=i)
#     kmeansArray4.append(km4)
#
# for i in range(0, 10):
#     clusterPlot.clusterPlot(X4,kmeansArray2[i][1])
    # plt.show()

# cluster4 = []
# for i in range(0, 10):
#     cluster4.append(clusterVal.clusterVal(y4, kmeansArray4[i][1]))
# entropy4 = []
# purity4 = []
# rand4 = []
# jaccard4 = []
#
# for i in range(0, 10):
#     entropy4.append(cluster4[i][0])
#     purity4.append(cluster4[i][1])
#     rand4.append(cluster4[i][2])
#     jaccard4.append(cluster4[i][3])
#
# plt.plot(k, cluster4, k, purity4, k, rand4, k, jaccard4)
# plt.show()

#exercise 4.1.3
# Fclusters = 2
# WF = loadmat('Data/wildfaces.mat')['X']
# WFkmeans = k_means(WF, n_clusters=Fclusters)
# clusterPlot.clusterPlot(WF, WFkmeans[1], centroids=WFkmeans[0])
# plt.xlabel('Attribute A')
# plt.ylabel('Attribute B')
# plt.show()

# for i in range(0, 10):
#     plt.imshow(np.reshape(WF[i,:], (3, 40, 40)).T)
#     plt.show()

# for i in range(0, Fclusters):
#     plt.imshow(np.reshape(WFkmeans[0][i,:], (3, 40, 40)).T)
#     plt.show()

#exercise 4.1.4
D = loadmat('Data/digits.mat')
DX = D['X']
Dy = D['y']

Dnclusters = 20
Dkmeans = k_means(DX, n_clusters=Dnclusters)
Dcluster = Dkmeans[0]
# clusterPlot.clusterPlot(DX, Dkmeans[1], centroids=Dkmeans[0], y=Dy)
# plt.show()

for i in range(0, Dnclusters):
    plt.imshow(np.reshape(Dkmeans[0][i,:], (16, 16)), cmap=cm.binary)
    plt.show()