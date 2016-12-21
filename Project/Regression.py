import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.linear_model as lr
from statsmodels.formula.api import ols
import statsmodels.api as sm
import patsy

#Import the data and combine them into one object
from scipy import stats

with open('student/student-mat.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=';')
    sMat = list(reader)

with open('student/student-por.csv') as f:
    reader = csv.reader(f, delimiter=';')
    sPor = list(reader)

Data =[]
for i in range(1, len(sMat)):
    Data.append(sMat[i])
for i in range(1, len(sPor)):
    Data.append(sPor[i])

Data = np.asarray(Data)

#PearsonR on Alcohol consumption (X-axis) and Class failures (Y-axis)
#Alcohol consumption is Dalc (26) and Walc (27)
#Creating dummy variable for Walc and Dalc to convert them from qualitative variables to quantitative variables
df = pd.DataFrame(Data[:, [26, 27]], columns = ['Dalc', 'Walc'])
dummy_dalc = pd.get_dummies(df['Dalc'])
dummy_walc = pd.get_dummies((df['Walc']))

d1 = []
d2 = []
d3 = []
d4 = []
d5 = []
dcombined = []
for i in range(0, len(dummy_dalc)):
    d1.append(dummy_dalc.get_value(i, col='1'))
    d2.append(dummy_dalc.get_value(i, col='2'))
    d3.append(dummy_dalc.get_value(i, col='3'))
    d4.append(dummy_dalc.get_value(i, col='4'))
    d5.append(dummy_dalc.get_value(i, col='5'))

for i in range(0, len(d1)):
    dcombined.append([d1[i], d2[i], d3[i], d4[i]])

failures = []
dalcint =[]
for i in range(len(Data[:,14])):
    failures.append(int(Data[i,14]))
    dalcint.append(int(Data[i,26]))

regr=lr.LinearRegression()
regr.fit(dcombined, failures)
print regr.coef_

# print dalcint
# plt.hist(dalcint)
# # plt.hist(d2)
# # plt.hist(d3)
# # plt.hist(d4)
# # plt.hist(d5)
# plt.title('Distribution of students drinking alcohol')
# plt.xlabel('Daily Alcohol consumption (low(1) - high(5))')
# plt.ylabel('Occurences')
# plt.show()
y = failures
x = [d1, d2, d3, d4]
# print x[1:]
ones = np.ones(len(x[0]))
X = sm.add_constant(np.column_stack((d1, ones)))
for ele in x[1:]:
    X = sm.add_constant(np.column_stack((ele, X)))

results = sm.OLS(y, X).fit()
print results.summary()

# mod = ols(X, failures)
# res = mod.fit()
# print res.summary()