import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import statsmodels.api as sm

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
samen=[]
Dalc = []
Walc = []
alc = []
for i in range(len(Data[:, 14])):
    failures.append(int(Data[i, 14]))
    Dalc.append(int(Data[i, 26]))
    Walc.append(int(Data[i, 27]))

samen.append(Dalc)
samen.append(Walc)
print("below are Dalc and Walc r coefficients:")
print(stats.pearsonr(Dalc, failures)[0])
print(stats.pearsonr(Walc, failures)[0])

#Printing histograms for alcohol consumption for girls, boys and both
df = pd.read_csv(filepath_or_buffer="student/student.csv", delimiter=";")

dalc = pd.DataFrame({'cats': [1, 2, 3, 4, 5], 'dalc': df.Dalc.value_counts()})
walc = pd.DataFrame({'cats': [1, 2, 3, 4, 5], 'walc': df.Walc.value_counts()})
frame = pd.merge(dalc, walc, how='outer')
frame[['cats', 'dalc', 'walc']].plot(kind='bar', x='cats', rot=0, title='Alcohol consumption boys and girls')
plt.ylabel("number of students")
plt.xlabel("alcohol consumption 1(low) to 5(high)")
plt.show()

pdBoys = df.loc[df['sex'] == "M"]
bdalc = pd.DataFrame({'cats': [1, 2, 3, 4, 5], 'dalc': pdBoys.Dalc.value_counts()})
bwalc = pd.DataFrame({'cats': [1, 2, 3, 4, 5], 'walc': pdBoys.Walc.value_counts()})
bframe = pd.merge(bdalc, bwalc, how='outer')
bframe[['cats', 'dalc', 'walc']].plot(kind='bar', x='cats', rot=0, title='Alcohol consumption boys')
plt.ylabel("number of students")
plt.xlabel("alcohol consumption 1(low) to 5(high)")
plt.show()

pdGirls = df.loc[df['sex'] == "F"]
fdalc = pd.DataFrame({'cats': [1, 2, 3, 4, 5], 'dalc': pdGirls.Dalc.value_counts()})
fwalc = pd.DataFrame({'cats': [1, 2, 3, 4, 5], 'walc': pdGirls.Walc.value_counts()})
fFrame = pd.merge(fdalc, fwalc, how='outer')
fFrame[['cats', 'dalc', 'walc']].plot(kind='bar', x='cats', rot=0, title='Alcohol consumption girls')
plt.ylabel("number of students")
plt.xlabel("alcohol consumption 1(low) to 5(high)")
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

jongens = []
jongens.append(boysDalc)
jongens.append(boysWalc)
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

meisjes = []
meisjes.append(girlsDalc)
meisjes.append(girlsWalc)
print("below are girls Dalc and Walc coefficients")
print(stats.pearsonr(girlsDalc, girlsFailures)[0])
print(stats.pearsonr(girlsWalc, girlsFailures)[0])

def reg_m(y,x):
    ones=np.ones(len(x[0]))
    X=sm.add_constant(np.column_stack((x[0],ones)))
    for ele in x[1:]:
        X=sm.add_constant(np.column_stack((ele,X)))
    results=sm.OLS(y,X).fit()
    return results
#
# print("-------Samen--------")
# print(reg_m(failures,samen).summary())
# print("-------Meisjes--------")
# print(reg_m(girlsFailures,meisjes).summary())
# print("-------Jongens--------")
# print(reg_m(boysFailures,jongens).summary())
