#Exercise 6.1
from scipy.io import loadmat
from sklearn import cross_validation as cv
from pylab import *
from sklearn import neighbors

import xlrd as xl

S1 = loadmat('Data/synth1.mat')
S1attributes = S1['attributeNames']
S1classes = S1['classNames']
S1X = S1['X']
S1Y = S1['y']
S1Xtest = S1['X_test']
S1Ytest = S1['y_test']
S1Xtrain = S1['X_train']
S1Ytrain = S1['y_train']

# scatter(S1X[:,0], S1X[:,1])
# title('Synth1.mat Scatterplot')
# xlabel(S1attributes[0][0][0])
# ylabel(S1attributes[1][0][0])
# show()

S2 = loadmat('Data/synth2.mat')
S2attributes = S2['attributeNames']
S2classes = S2['classNames']
S2X = S2['X']
S2Xtest = S2['X_test']
S2Ytest = S2['y_test']
S2Xtrain = S2['X_train']
S2Ytrain = S2['y_train']

# scatter(S2X[:,0], S2X[:,1])
# title('Synth2.mat Scatterplot')
# xlabel(S2attributes[0][0][0])
# ylabel(S2attributes[1][0][0])
# show()

S3 = loadmat('Data/synth3.mat')
S3attributes = S3['attributeNames']
S3classes = S3['classNames']
S3X = S3['X']
S3Xtest = S3['X_test']
S3Ytest = S3['y_test']
S3Xtrain = S3['X_train']
S3Ytrain = S3['y_train']

# scatter(S3X[:,0], S3X[:,1])
# title('Synth3.mat Scatterplot')
# xlabel(S3attributes[0][0][0])
# ylabel(S3attributes[1][0][0])
# show()

S4 = loadmat('Data/synth4.mat')
S4attributes = S4['attributeNames']
S4classes = S4['classNames']
S4X = S4['X']
S4Xtest = S4['X_test']
S4Ytest = S4['y_test']
S4Xtrain = S4['X_train']
S4Ytrain = S4['y_train']

# scatter(S4X[:,0], S4X[:,1])
# title('Synth4.mat Scatterplot')
# xlabel(S4attributes[0][0][0])
# ylabel(S4attributes[1][0][0])
# show()

#Synth1
S1euc = []
S1man = []
xaxis = []
trainSize = np.divide(np.size(S1Xtrain), 2)
for i in range(1, trainSize):
    xaxis.append(i)
    euc = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
    ef = euc.fit(S1Xtrain, S1Ytrain.ravel())
    eucScore = 100 - np.multiply(ef.score(S1Xtest, S1Ytest), 100)
    S1euc.append(eucScore)
    man = neighbors.KNeighborsClassifier(n_neighbors=i, metric='manhattan')
    mf = man.fit(S1Xtrain, S1Ytrain.ravel())
    manScore = 100 - np.multiply(mf.score(S1Xtest, S1Ytest), 100)
    S1man.append(manScore)

plotE, = plot(xaxis, S1euc)
plotM, = plot(xaxis, S1man)
title('Synth1 Euclidean vs Manhattan')
xlabel('Amount of neighbors')
ylabel('Error rate')
plt.legend([plotE, plotM], ['Euclidean', 'Manhattan'], loc=4)
show()

#Synth2
S2euc = []
S2man = []
xaxis = []
trainSize = np.divide(np.size(S2Xtrain), 2)
for i in range(1, trainSize):
    xaxis.append(i)
    euc = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
    ef = euc.fit(S2Xtrain, S2Ytrain.ravel())
    eucScore = 100 - np.multiply(ef.score(S2Xtest, S2Ytest), 100)
    S2euc.append(eucScore)
    man = neighbors.KNeighborsClassifier(n_neighbors=i, metric='manhattan')
    mf = man.fit(S2Xtrain, S2Ytrain.ravel())
    manScore = 100 - np.multiply(mf.score(S2Xtest, S2Ytest), 100)
    S2man.append(manScore)

plotE, = plot(xaxis, S2euc)
plotM, = plot(xaxis, S2man)
title('Synth2 Euclidean vs Manhattan')
xlabel('Amount of neighbors')
ylabel('Error rate')
plt.legend([plotE, plotM], ['Euclidean', 'Manhattan'], loc=4)
show()

#Synth3
S3euc = []
S3man = []
xaxis = []
trainSize = np.divide(np.size(S3Xtrain), 2)
for i in range(1, trainSize):
    xaxis.append(i)
    euc = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
    ef = euc.fit(S3Xtrain, S3Ytrain.ravel())
    eucScore = 100 - np.multiply(ef.score(S3Xtest, S3Ytest), 100)
    S3euc.append(eucScore)
    man = neighbors.KNeighborsClassifier(n_neighbors=i, metric='manhattan')
    mf = man.fit(S3Xtrain, S3Ytrain.ravel())
    manScore = 100 - np.multiply(mf.score(S3Xtest, S3Ytest), 100)
    S3man.append(manScore)

plotE, = plot(xaxis, S3euc)
plotM, = plot(xaxis, S3man)
title('Synth3 Euclidean vs Manhattan')
xlabel('Amount of neighbors')
ylabel('Error rate')
plt.legend([plotE, plotM], ['Euclidean', 'Manhattan'], loc=4)
show()

#Synth4
# S4euc = []
# S4man = []
# xaxis = []
# trainSize = np.divide(np.size(S4Xtrain), 2)
# for i in range(1, trainSize):
#     xaxis.append(i)
#     euc = neighbors.KNeighborsClassifier(n_neighbors=i, metric='euclidean')
#     ef = euc.fit(S4Xtrain, S4Ytrain.ravel())
#     eucScore = 100 - np.multiply(ef.score(S4Xtest, S4Ytest), 100)
#     S4euc.append(eucScore)
#     man = neighbors.KNeighborsClassifier(n_neighbors=i, metric='manhattan')
#     mf = man.fit(S4Xtrain, S4Ytrain.ravel())
#     manScore = 100 - np.multiply(mf.score(S3Xtest, S3Ytest), 100)
#     S4man.append(manScore)

# plotE, = plot(xaxis, S4euc)
# plotM, = plot(xaxis, S4man)
# title('Synth4 Euclidean vs Manhattan')
# xlabel('Amount of neighbors')
# ylabel('Error rate')
# plt.legend([plotE, plotM], ['Euclidean', 'Manhattan'], loc=4)
# show()