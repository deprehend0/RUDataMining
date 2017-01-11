import xlrd as xl
import pydotplus
import numpy as np

from sklearn import tree

workbook_mat = xl.open_workbook('student/student-mat.xls')
sheet_mat = workbook_mat.sheet_by_index(0)

workbook_por = xl.open_workbook('student/student-por.xls')
sheet_por = workbook_por.sheet_by_index(0)

col14_mat = sheet_mat.col(14)
print col14_mat[0].value

porFailures = sheet_por.col_values(14, 1)
porX = []


for i in range(0, sheet_por.row_len(0)):
    if (i != 14):
        porX.append(sheet_por.col_values(i, 1))

#yes/no columns
yn = [15, 16, 17, 18, 19, 20, 21, 22, 23]
for i in range (0, len(porX)):
    a = np.array(porX[i])
    if (i == 0):
        b = np.where(a=="GP", 1, 0)
        porX[i] = b.tolist()
    elif (i == 1):
        b = np.where(a=="F", 1, 0)
        porX[i] = b.tolist()
    elif (i == 3):
        b = np.where(a=="U", 1, 0)
        porX[i] = b.tolist()
    elif (i == 4):
        b = np.where(a=="LE3", 1, 0)
        porX[i] = b.tolist()
    elif (i == 5):
        b = np.where(a=="T", 1, 0)
        porX[i] = b.tolist()
    elif (i == 8 or i == 9):
        tmp = []
        for j in range(0, len(porX[i])):
            if (porX[i][j] == "teacher"):
                porX[i][j] = 0
            elif (porX[i][j] == "health"):
                porX[i][j] = 1
            elif (porX[i][j] == "services"):
                porX[i][j] = 2
            elif (porX[i][j] == "at_home"):
                porX[i][j] = 3
            elif (porX[i][j] == "other"):
                porX[i][j] = 4
    elif (i == 10):
        tmp = []
        for j in range(0, len(porX[i])):
            if (porX[i][j] == "home"):
                porX[i][j] = 0
            elif (porX[i][j] == "reputation"):
                porX[i][j] = 1
            elif (porX[i][j] == "course"):
                porX[i][j] = 2
            elif (porX[i][j] == "other"):
                porX[i][j] = 3
    elif (i == 11):
        for j in range(0, len(porX[i])):
            if (porX[i][j] == "mother"):
                porX[i][j] = 0
            elif (porX[i][j] == "father"):
                porX[i][j] = 1
            elif (porX[i][j] == "other"):
                porX[i][j] = 2
    elif (i == 14 or i == 15 or i == 16 or i == 17 or i == 18 or i == 19 or i == 20 or i == 21):
        b = np.where(a=="yes", 1, 0)
        porX[i] = b.tolist()

print len(porX)

porX2=[]
for i in range(0,len(porX[0])):
    tmp=[]
    for j in range(0,31):
        tmp.append(porX[j][i])
    porX2.append(tmp)
print(porX2)

clf = tree.DecisionTreeClassifier(min_samples_split=100)
clf = clf.fit(porX2, porFailures)

dot_data = tree.export_graphviz(clf, out_file=None)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('Images/porDTGraph.pdf')