import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sklearn.linear_model as lr
from statsmodels.formula.api import ols
import statsmodels.api as sm
import patsy

# Import the data and combine them into one object
from scipy import stats

with open('student/student-mat.csv') as f:
    reader = csv.reader(f, delimiter=';')
    sMat = list(reader)

with open('student/student-por.csv') as f:
    reader = csv.reader(f, delimiter=';')
    sPor = list(reader)

Data = []
for i in range(1, len(sMat)):
    Data.append(sMat[i])
for i in range(1, len(sPor)):
    Data.append(sPor[i])

Data = np.asarray(Data)

failures = []
Dalc = []
Walc = []
alc = []
for i in range(len(Data[:, 14])):
    failures.append(int(Data[i, 14]))
    Dalc.append(int(Data[i, 26]))
    Walc.append(int(Data[i, 27]))

print("below are Dalc and Walc r coefficients:")
print(stats.pearsonr(Dalc, failures)[0])
print(stats.pearsonr(Walc, failures)[0])
plt.title("alcohol cons during weekend days")
plt.hist(Walc)
plt.xlabel("alcohol consumption 1(low) to 5(high)")
plt.ylabel("number of students")
plt.show()
# divide boys from girls
boys = []
girls = []

for i in range(0, 1044):
    if Data[i, 1] == 'F':
        girls.append(Data[i])
    else:
        boys.append(Data[i])
boys = np.asarray(boys)
girls = np.asarray(girls)
boysDalc = []
boysWalc = []
boysFailures = []
for i in range(0, 453):
    boysFailures.append(int(boys[i, 14]))
    boysDalc.append(int(boys[i, 26]))
    boysWalc.append(int(boys[i, 27]))
print("below are boys Dalc and Walc coefficients:")
print(stats.pearsonr(boysDalc, boysFailures)[0])
print(stats.pearsonr(boysWalc, boysFailures)[0])

girlsDalc = []
girlsWalc = []
girlsFailures = []
for i in range(0, 453):
    girlsFailures.append(int(girls[i, 14]))
    girlsDalc.append(int(girls[i, 26]))
    girlsWalc.append(int(girls[i, 27]))
print("below are girls Dalc and Walc coefficients")
print(stats.pearsonr(girlsDalc, girlsFailures)[0])
print(stats.pearsonr(girlsWalc, girlsFailures)[0])
