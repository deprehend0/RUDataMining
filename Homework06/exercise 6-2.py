import numpy as np
import neurolab as nl
from scipy.io import loadmat
# from Scripts import decision_boundaries
from sklearn.model_selection import KFold
import matplotlib.pyplot as plt
from sklearn import tree
import pydotplus

Data=loadmat('Data/xor.mat')
X=Data['X']
y=Data['y']
# plt.scatter(X[:,0],X[:,1],c=y)
# plt.show()

kf = KFold(n_splits=10)
# for train, test in kf.split(X):
    # print train
    # print test


kTrainX = []
kTestX = []
kTrainY = []
kTestY = []


for train, test in kf.split(X, y):
    kTrainX.append(X[train])
    kTrainY.append(y[train])
    kTestX.append(X[test])
    kTestY.append(y[test])


kTrees = []
for fold in range (0, len(kTrainX)):
    kTree = []
    kclf = tree.DecisionTreeClassifier()
    kclf = kclf.fit(kTrainX[fold], kTrainY[fold])
    kTree.append(kclf)
    kTrees.append(kTree)

kTrainPerc = []
wrongs = 0
for fold in range (0, len(kTrees)):
    setPerc = []
    clf = kTrees[fold][0]
    AW = 0.0
    for i in range (0, len(kTestX[fold])):
        if clf.predict([kTestX[fold][i]]) != kTestY[fold][i]:
            AW += 1
    kTrainPerc.append(np.divide(AW, len(kTestX[fold])) * 100)
    wrongs += AW

print wrongs/len(X) * 100






net=nl.net.newff([[0,1],[0,1]],[1,1],[nl.trans.TanSig(), nl.trans.TanSig()])

err=net.train(X,y, goal=0.5)

out=net.sim(X)
plt.ylabel('error')
plt.xlabel('epoch')
plt.plot(err)
# plt.show()