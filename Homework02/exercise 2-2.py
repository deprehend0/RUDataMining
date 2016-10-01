#Exercise 2.2
from scipy.io import loadmat
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

Zip = loadmat('Data/zipdata.mat')['traindata']
X = matrix(Zip[:,1:])
y = matrix(Zip[:,0])
tmp = []

for i in range(0, len(Zip)):
    if y.item(i) < 2 or y.item(i) > 9:
        tmp.append(X[i].A[0])
    
A = matrix(np.asarray(tmp))

#for i in range(0, 10):
#    subplot(1,1,1);
#    I = reshape(A[i,:],(16,16))
#    imshow(I, extent=(0,16,0,16), cmap=cm.gray_r);
#    title('Digit {} as an image' .format(i));
#    show()
    
Y = A - np.ones((len(A),1))*A.mean(0)
SVD = np.linalg.svd(Y)
U, S, V = np.linalg.svd(Y)

V = np.transpose(V)
Z = Y*V[:,:4]
W = Z * np.transpose(V[:,0:4]) + A.mean(0)

for i in range(0, 10):
    subplot(1,1,1)
    I = reshape(W[i,:],(16,16))
    imshow(I, extent=(0,16,0,16), cmap=cm.gray_r)
    title('Digit {} as an image' .format(i));
    show()

#subplot(1,1,1)
#scatter(Z[:,0], Z[:,1])
#title("Scatter of PC1 - PC2")
#xlabel("PC1")
#ylabel("PC2")
#show()
#
#subplot(1,1,1)
#scatter(Z[:,0], Z[:,2])
#title("Scatter of PC1 - PC3")
#xlabel("PC1")
#ylabel("PC3")
#show()
#
#subplot(1,1,1)
#scatter(Z[:,0], Z[:,3])
#title("Scatter of PC1 - PC4")
#xlabel("PC1")
#ylabel("PC4")
#show()
#
#subplot(1,1,1)
#scatter(Z[:,1], Z[:,2])
#title("Scatter of PC2 - PC3")
#xlabel("PC2")
#ylabel("PC3")
#show()
#
#subplot(1,1,1)
#scatter(Z[:,1], Z[:,3])
#title("Scatter of PC2 - PC4")
#xlabel("PC2")
#ylabel("PC4")
#show()
#
#subplot(1,1,1)
#scatter(Z[:,2], Z[:,3])
#title("Scatter of PC3 - PC4")
#xlabel("PC3")
#ylabel("PC4")
#show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

sx = Z[:,0]
sy = Z[:,1]
sz = Z[:,2]

ax.scatter(sx, sy, sz)

ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

plt.show()
