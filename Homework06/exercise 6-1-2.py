from sklearn.neighbors import KNeighborsClassifier as nb
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import loadmat
import sklearn.cluster
import sklearn.metrics as metrics
from xlrd import open_workbook
from sklearn.cross_validation import LeaveOneOut as loo



workbook=open_workbook('Data/iris.xls')
sheet=workbook.sheet_by_index(0)
#convert xls file into a python array and change characters into numerical values.
dataArray = []
for i in range (1, 151):
    row = sheet.row_values(i)
    dataArray.append(row)
data=np.asarray(dataArray)
for i in range(0,150):
    if data[i,4]=='Iris-setosa':
        data[i,4]=0
    if data[i,4]=='Iris-versicolor':
        data[i,4]=1
    if data[i,4]=='Iris-virginica':
        data[i,4]=2
X=[]
X=np.delete(data,4,axis=1)
Y=data[:,4]
posEuclidean=[]
errorEuclidean=[]
euclideanK=[]
loo=loo(150)
X_test=[]
Y_test=[]
X_train=[]
Y_train=[]
plt.xlabel("K")
plt.ylabel("error rate (%)")
for train, test in loo:
    X_test.append(X[test].tolist())
    Y_test.append(Y[test].tolist())
    X_train=X[train]
    Y_train=Y[train]

X_test=np.asarray(X_test)
Y_test=np.asarray(Y_test)
Y_train=np.asarray(Y_train)
X_train=np.asarray(X_train)
X_test = [l[0] for l in X_test]
Y_test = [l[0] for l in Y_test]

for k in range (1, 40):
    euclideanK.append([k])
    nbrs = nb(n_neighbors=k, metric='euclidean')
    fitted = nbrs.fit(X_train, Y_train)
    y_pred = fitted.predict(X_test)
    conf = metrics.confusion_matrix(Y_test, y_pred)
    print conf
    correct = 0
    for i in range(0,3):
        correct += conf[i][i]
    errorRate = np.multiply(np.divide((150 - correct), float(150)), 100)
    posEuclidean.append(errorRate)

plt.plot(euclideanK,posEuclidean)
plt.show()