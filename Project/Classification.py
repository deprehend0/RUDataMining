import xlrd as xl
import pydotplus
import numpy as np

from sklearn import tree

workbook_mat = xl.open_workbook('student/student-mat.xls')
sheet_mat = workbook_mat.sheet_by_index(0)

workbook_por = xl.open_workbook('student/student-por.xls')
sheet_por = workbook_por.sheet_by_index(0)

col14_mat = sheet_mat.col(14)

porRowZero = sheet_por.row_values(0)
labels = []
for i in range(0, sheet_por.row_len(0)):
    if (i != 14):
        labels.append(sheet_por.cell_value(0, i).decode('ascii')) # Both .csv-files have the same labelnames


#Make one big array of all values from both por and mat. We choose to add first the por list and afterwards the mat list
X = []
Failures = []
for i in range(0, sheet_por.row_len(0)):
    if (i != 14):
        X.append(sheet_por.col_values(i, 1))
    else:
        Failures.append(sheet_por.col_values(i, 1))

for i in range(0, sheet_mat.row_len(0)):
    if (i < 14):
        for j in range(1, len(sheet_mat.col_values(i, 1))):
            X[i].append(sheet_mat.cell_value(j, i))
    if (i == 14):
        for j in range(1, len(sheet_mat.col_values(i, 1))):
            Failures[0].append(sheet_mat.cell_value(j, i))
    if (i > 14):
        for j in range(1, len(sheet_mat.col_values(i, 1))):
            X[i-1].append(sheet_mat.cell_value(j, i))

Failures = Failures[0]

#yes/no columns [15, 16, 17, 18, 19, 20, 21, 22, 23]

#Transition from strings to ints
for i in range (0, len(X)):
    a = np.array(X[i])
    if (i == 0):
        b = np.where(a=="GP", 1, 0)
        X[i] = b.tolist()
    elif (i == 1):
        b = np.where(a=="F", 1, 0)
        X[i] = b.tolist()
    elif (i == 3):
        b = np.where(a=="U", 1, 0)
        X[i] = b.tolist()
    elif (i == 4):
        b = np.where(a=="LE3", 1, 0)
        X[i] = b.tolist()
    elif (i == 5):
        b = np.where(a=="T", 1, 0)
        X[i] = b.tolist()
    elif (i == 8 or i == 9):
        tmp = []
        for j in range(0, len(X[i])):
            if (X[i][j] == "teacher"):
                X[i][j] = 0
            elif (X[i][j] == "health"):
                X[i][j] = 1
            elif (X[i][j] == "services"):
                X[i][j] = 2
            elif (X[i][j] == "at_home"):
                X[i][j] = 3
            elif (X[i][j] == "other"):
                X[i][j] = 4
    elif (i == 10):
        tmp = []
        for j in range(0, len(X[i])):
            if (X[i][j] == "home"):
                X[i][j] = 0
            elif (X[i][j] == "reputation"):
                X[i][j] = 1
            elif (X[i][j] == "course"):
                X[i][j] = 2
            elif (X[i][j] == "other"):
                X[i][j] = 3
    elif (i == 11):
        for j in range(0, len(X[i])):
            if (X[i][j] == "mother"):
                X[i][j] = 0
            elif (X[i][j] == "father"):
                X[i][j] = 1
            elif (X[i][j] == "other"):
                X[i][j] = 2
    elif (i == 14 or i == 15 or i == 16 or i == 17 or i == 18 or i == 19 or i == 20 or i == 21):
        b = np.where(a=="yes", 1, 0)
        X[i] = b.tolist()

X2=[]
for i in range(0,len(X[0])):
    tmp=[]
    for j in range(0,31):
        tmp.append(X[j][i])
    X2.append(tmp)

clf = tree.DecisionTreeClassifier(min_samples_split=100)
clf = clf.fit(X2, Failures)

dot_data = tree.export_graphviz(clf, out_file="tree.dot")
# graph = pydotplus.graph_from_dot_data(dot_data)
# graph.write_pdf('Images/porDTGraph.pdf')