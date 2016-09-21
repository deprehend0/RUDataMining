#Exercise 1.2
import xlrd as xl
import numpy as np
from pylab import *

#1.2.1a
workbook = xl.open_workbook('Data/nanonose.xls')
sheet = workbook.sheet_by_index(0)
#first relevant row values
#rowX = sheet.row_values(2, 3, 11)
#first relevant column values
#colX = sheet.col_values(3, 2, 92)
#print(rowX)

dataArray = np.zeros((90, 8))
for i in range (2, 92):
    for j in range (0, 8):
        row = sheet.row_values(i, 3, 11)
        dataArray[i-2,j] = row[j]

X = np.asmatrix(dataArray)
#print(X)

#1.2.1b
sensorA = X[:,0]
sensorB = X[:,1]
sensorC = X[:,2]
sensorD = X[:,3]
sensorE = X[:,4]
sensorF = X[:,5]
sensorG = X[:,6]
sensorH = X[:,7]

scatter(sensorA, sensorB)
scatter(sensorE, sensorH)
scatter(sensorD, sensorF)
scatter(sensorC, sensorG)

#Exercise 1.2.2

#Exercise 1.2.2a
#pca can be used to diminish the dimensionality of data in your matrix, while
#keeping most of the information. PCA uses orthogonal transformation to transform 
#a set of possibly correlated variables into linearly uncorrelated ones called
#principal components. The first principal component has the greatest variance.
#PCA is sensitive to the relative scaling of the starting variables

#PCA is a way to reduce the data. Not the actual data only the discription. By calculating the eigenvectors and the covariance matrix it is 
#possible to "replace" the coordinate system in such a way that the line in which the biggest variation is the new X-axis becomes and the line
#with the second biggest variation the Y-axis. With this method you can (re)determine what the most important variation is, so it'll be easier to
#focus on that variation

#Exercise 1.2.2b
#The relation between SVD and EVD is that they both change the base of a matrix. EVD works on NxN matrices where SVD also works on MxN matrices.

#Exercise 1.2.2c
#Y = X - Il
Y = X - np.ones((90,1))*X.mean(0)
SVD = np.linalg.svd(Y)
U, S, W = np.linalg.svd(Y)
#print(S)
V = np.transpose(W)
Variances=(S*S)/(sum(S*S))
plot(Variances)
#print(Variances[0])
#print(Variances[1])
#print(Variances[2])
#print(Variances[0] + Variances[1] + Variances[2])

#0.76347901 + 0.11497144 + 0.04899809 = 92,744854 percent of the variance can be explained 
#by the first three principal components

#Exercise 1.2.2d
#Z1 = np.multiply(Y, V[0, :])
#Z2 = np.multiply(Y, V[1, :])
Z1 = Y * (W[0,:].T)
Z2 = Y * (W[1,:].T)
scatter(Z1, Z2)

#The given projection by PCA makes that the data is normalized and we get less distracted by variances
#we don't want to focus on. If you just plot the dimensions against each other that noice will still be there.
