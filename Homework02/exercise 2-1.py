#Exercise 2.1.1
from pylab import *
from scipy.io import loadmat
from scipy import stats
import numpy as np

W = loadmat('Data/wine.mat')['X']

#W0 = stats.zscore(W[:,0])
#subplot(2, 1, 1)
#boxplot(W0)
#title('Boxplot fixed acidity (tartaric)')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(W[:,0])
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
#hist(W[:,1])
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
#hist(W[:,2])
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
#hist(W[:,3])
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
#hist(W[:,4])
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
#hist(W[:,5])
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
#hist(W[:,6])
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
#hist(W[:,8])
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
#hist(W[:,9])
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

#W11 = stats.zscore(W[:,11])
#subplot(2, 1, 1)
#boxplot(W[:,11])
#title('Boxplot quality score')
#ylabel('0-10')
#
#subplot(2, 1, 2)
#hist(W[:,11])
#title('Histogram quality score')
#xlabel('0-10')
#ylabel('occurences')
#
#Alcohol = W[:,10]
#Acidity = W[:,2]
#Density = W[:,8]
#Rating = W[:,11]
#tmpAlc = [],[]
#tmpAci = [],[]
#tmpDen = [],[]
#
#for i in range (0, len(Alcohol)):
#    if(Alcohol[i] < 200 and Alcohol[i] > 0.5):
#        tmpAlc[0].append(Alcohol[i])
#        tmpAlc[1].append(Rating[i])
#    if(Acidity[i] > 0 and Acidity[i] < 20):
#        tmpAci[0].append(Acidity[i])
#        tmpAci[1].append(Rating[i])
#    if(Density[i] > 0.1 and Density[i] < 10):
#        tmpDen[0].append(Density[i])
#        tmpDen[1].append(Rating[i])
#        
#CAlc = stats.zscore(tmpAlc[:,0])
#subplot(2, 1, 1)
#boxplot(CAlc)
#title('Boxplot cleaned Alcohol')
#ylabel('% vol.')
#
#subplot(2, 1, 2)
#hist(tmpAlc[:,0])
#title('Histogram cleaned Alcohol')
#xlabel('% vol.')
#ylabel('occurences')
#      
#CAci = stats.zscore(tmpAci[:,0])
#subplot(2, 1, 1)
#boxplot(CAci)
#title('Boxplot cleaned volatide acidity')
#ylabel('g/dm3')
#
#subplot(2, 1, 2)
#hist(tmpAci[:,0])
#title('Histogram cleaned volatide acidity')
#xlabel('g/dm3')
#ylabel('occurences')
#        
#CDen = stats.zscore(tmpDen[:,0])
#subplot(2, 1, 1)
#boxplot(CDen)
#title('Boxplot cleaned density')
#ylabel('% vol.')
#
#subplot(2, 1, 2)
#hist(tmpDen[:,0])
#title('Histogram cleaned density')
#xlabel('g/cm3')
#ylabel('occurences')

#scatter(W[:,0], W[:,11])
#xlabel('Volatide acidity (g/dm3)')
#ylabel('Quality score (0-10)')
#
#print(stats.pearsonr(W[:,0], W[:,11]))

scatter(tmpAci[0], tmpAci[1])
xlabel('Volatile acidity (acetic) (g/dm3)')
ylabel('Quality score (0-10)')

print(stats.pearsonr(tmpAci[0], tmpAci[1]))