#Exercise 3.1
from scipy.io import loadmat
from sklearn import tree
import pydotplus
import numpy as np
import graphviz as gv

Wine = loadmat('Data/wine.mat')
WD = Wine['X']
y = Wine['y']
AN = Wine['attributeNames'][0]
CN = Wine['classNames'][0]

clf = tree.DecisionTreeClassifier(min_samples_split=100)
clf = clf.fit(WD, y)

dot_data = tree.export_graphviz(clf, out_file=None, feature_names=AN, class_names=['red', 'white'])
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('Data/wine.pdf')

AW = 0.0
for i in range (0, len(WD)):
    if(clf.predict([WD[i]]) != y[i]):
        AW += 1

# print AW

PerC = np.divide((len(WD) - AW), len(WD)) * 100

print "{}%" .format(PerC)