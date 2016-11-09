#Exercise 3.2
import pydotplus
from scipy.io import loadmat
import sklearn.model_selection as ms
from sklearn import tree
import numpy as np
from pylab import *
import matplotlib.pyplot as plt

Wine = loadmat('Data/wine.mat')
WD = Wine['X']
y = Wine['y']
AN = Wine['attributeNames'][0]
CN = Wine['classNames'][0]

X_train, X_test, y_train, y_test = ms.train_test_split(WD, y, test_size=0.1)

# clfs = [],[]
# for i in range (2, 21):
#     clf = tree.DecisionTreeClassifier(min_samples_split=100, max_depth=i)
#     clfs[0].append(clf.fit(X_train, y_train))
#     clfs[1].append(i)
#
# train = []
# for i in range(0, len(clfs[0])):
#     AW = 0.0
#     clf = clfs[0][i]
#     for j in range(0, len(X_train)):
#         if(clf.predict([X_train[j]]) != y_train[j]):
#             AW += 1;
#     train.append(np.divide(AW, len(X_train)) * 100)
#
# test = []
# for i in range(0, len(clfs[0])):
#     AW = 0.0
#     clf = clfs[0][i]
#     for j in range(0, len(X_test)):
#         if (clf.predict([X_test[j]]) != y_test[j]):
#             AW += 1;
#     test.append(np.divide(AW, len(X_test)) * 100)
#
#
# TestError, = plot(clfs[1], test, 'b-', label='test error')
# TrainingError, = plot(clfs[1], train, 'r-', label='training error')
# plt.legend((TestError, TrainingError), ('Test error', 'Training error'))
# xlabel('Depth')
# ylabel('Misclassification percentage')
# show()

# kf = ms.KFold(n_splits=100)
# kTrainX = []
# kTestX = []
# kTrainY = []
# kTestY = []
#
#
# for train_index, test_index in kf.split(WD, y):
#     kTrainX.append(WD[train_index])
#     kTrainY.append(y[train_index])
#     kTestX.append(WD[test_index])
#     kTestY.append(y[test_index])
#
# kclf = tree.DecisionTreeClassifier(min_samples_split=100)
# kclf = kclf.fit(kTrainX[0], kTrainY[0])
#
# dot_data = tree.export_graphviz(kclf, out_file=None, feature_names=AN, class_names=['red', 'white'])
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('Data/kclf0.pdf')
#
# kTrees = []
# for fold in range (0, len(kTrainX)):
#     kTree = []
#     for depth in range (2, 21):
#         kclf = tree.DecisionTreeClassifier(min_samples_split=100, max_depth=depth)
#         kclf = kclf.fit(kTrainX[0], kTrainY[0])
#         kTree.append(kclf)
#     kTrees.append(kTree)
#
# kTrainPerc = []
# for fold in range (0, len(kTrees)):
#     print 'set:', fold
#     setPerc = []
#     for kTree in range (0, len(kTrees[fold])):
#         clf = kTrees[fold][kTree]
#         AW = 0.0
#         for i in range (0, len(kTrainX[fold])):
#             if clf.predict([kTrainX[fold][i]]) != kTrainY[fold][i]:
#                 AW += 1
#         setPerc.append(np.divide(AW, len(kTrainX[fold])) * 100)
#     kTrainPerc.append(setPerc)
#
# #Still need to fix that x axis is the proper depth
# plot(kTrainPerc[0], 'b-')
# plot(kTrainPerc[1], 'r-')
# plot(kTrainPerc[2], 'g-')
# plot(kTrainPerc[3], 'b--')
# plot(kTrainPerc[4], 'r--')
# plot(kTrainPerc[5], 'g--')
# plot(kTrainPerc[6], 'y-')
# plot(kTrainPerc[7], 'y--')
# plot(kTrainPerc[8], 'c-')
# plot(kTrainPerc[9], 'c--')
# ylabel('Miscalculation percentage')
# xlabel('Depth (+2)')
# show()