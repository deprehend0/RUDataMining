#Exercise 3.1
from scipy.io import loadmat
from sklearn import tree
import graphviz
import os

Wine = loadmat('Data/wine.mat')
WD = Wine['X']
y = Wine['y']
AN = Wine['attributeNames']
CN = Wine['classNames']

clf = tree.DecisionTreeClassifier(min_samples_split=100)
clf = clf.fit(WD, y)

with open('Data/wine.dot', 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

graphviz.Graph(filename='Data/wine.dot')