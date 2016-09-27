#Exercise 2.1.1
from pylab import *
from scipy.io import loadmat
from scipy import stats

W = loadmat('Data/wine.mat')['X']

#W0 = stats.zscore(W[:,0])
#subplot(2, 1, 1)
#boxplot(W0)
#title('Boxplot fixed acidity (tartaric)')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W0)
#title('Histogram fixed acidity (tartaric)')
#xlabel('g/dm3')
#ylabel('occurences')

#W1 = stats.zscore(W[:,1])
#subplot(2, 1, 1)
#boxplot(W1)
#title('Boxplot volatile acidity (acetic)')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W1)
#title('Histogram volatile acidity (acetic)')
#xlabel('g/dm3')
#ylabel('occurences')

#W2 = stats.zscore(W[:,2])
#subplot(2, 1, 1)
#boxplot(W2)
#title('Boxplot citric acid')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W2)
#title('Histogram citric acid')
#xlabel('g/dm3')
#ylabel('occurences')

#W3 = stats.zscore(W[:,3])
#subplot(2, 1, 1)
#boxplot(W3)
#title('Boxplot residual sugar')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W3)
#title('Histogram residual sugar')
#xlabel('g/dm3')
#ylabel('occurences')

#W4 = stats.zscore(W[:,4])
#subplot(2, 1, 1)
#boxplot(W4)
#title('Boxplot chlorides')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W4)
#title('Histogram chlorides')
#xlabel('g/dm3')
#ylabel('occurences')

#W5 = stats.zscore(W[:,5])
#subplot(2, 1, 1)
#boxplot(W5)
#title('Boxplot free sulfur dioxide')
#ylabel('mg/dm3')
#
#subplot(2, 1, 2)
#hist(W5)
#title('Histogram free sulfur dioxide')
#xlabel('mg/dm3')
#ylabel('occurences')

#W6 = stats.zscore(W[:,6])
#subplot(2, 1, 1)
#boxplot(W6)
#title('Boxplot total sulfur dioxide')
#ylabel('mg/dm3')
#
#subplot(2, 1, 2)
#hist(W6)
#title('Histogram total sulfur dioxide')
#xlabel('mg/dm3')
#ylabel('occurences')

#W7 = stats.zscore(W[:,7])
#subplot(2, 1, 1)
#boxplot(W7)
#title('Boxplot density')
#ylabel('g/cm3')
#
#subplot(2, 1, 2)
#hist(W[:,7])
#title('Histogram density')
#xlabel('g/cm3')
#ylabel('occurences')

#W8 = stats.zscore(W[:,8])
#subplot(2, 1, 1)
#boxplot(W8)
#title('Boxplot pH')
#ylabel('pH')
#
#subplot(2, 1, 2)
#hist(W8)
#title('Histogram pH')
#xlabel('pH')
#ylabel('occurences')

#W9 = stats.zscore(W[:,9])
#subplot(2, 1, 1)
#boxplot(W9)
#title('Boxplot sulphates')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W9)
#title('Histogram sulphates')
#xlabel('g/dm3')
#ylabel('occurences')

#W10 = stats.zscore(W[:,10])
#subplot(2, 1, 1)
#boxplot(W10)
#title('Boxplot alcohol')
#ylabel('% vol.')
#
#subplot(2, 1, 2)
#hist(W[:,10])
#title('Histogram aclohol')
#xlabel('% vol.')
#ylabel('occurences')

W11 = stats.zscore(W[:,11])
subplot(2, 1, 1)
boxplot(W[:,11])
title('Boxplot alcohol')
ylabel('% vol.')

subplot(2, 1, 2)
hist(W11)
title('Histogram aclohol')
xlabel('% vol.')
ylabel('occurences')