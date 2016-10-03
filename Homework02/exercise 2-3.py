#Exercise 2.3
import numpy as np
import itertools as itt
from pylab import *

Appendages  = [2, 3, 6, 8, 11, 18]

M = np.mean(Appendages)
SD = np.std(Appendages)
print("The mean is: {}" .format(M))

print("The standard deviation is: {}" .format(SD))

C2 = [list(x) for x in itt.combinations(Appendages, 2)]
C2M = []

print("All combinations for 2 aliens without replacement are: {}" .format(C2) )

for i in range(0, len(C2)):
    mean = np.mean(C2[i])
    print("The mean for {} is: {}" .format(C2[i], mean))
    C2M.append(mean)

C4 = [list(x) for x in itt.combinations(Appendages, 4)]
C4M = []

print("All combinations for 4 aliens without replacement are: {}" .format(C4) )

for i in range(0, len(C4)):
    mean = np.mean(C4[i])
    print("The mean for {} is: {}" .format(C4[i], np.mean(C4[i])))
    C4M.append(mean)
    
C4SD = np.std(C4M)
C2SD = np.std(C2M)
print("The mean of the means of all 2 alien combinations without replacement is: {}" 
        .format(np.mean(C2M)))
print("The standard deviation of the means of all 2 alien combinations without replacement is: {}"
        .format(C2SD))
print("The mean of the means of all 4 alien combinations without replacement is: {}" 
        .format(np.mean(C4M)))
print("The standard deviation of the means of all 4 alien combinations without replacement is: {}"
        .format(C4SD))
        
print(SD / np.sqrt(4))
RPop = np.sqrt(np.divide((6 - 4), (6 - 1), dtype=float))
print(np.multiply((SD / np.sqrt(4)), RPop))

print(SD / np.sqrt(2))
print(np.multiply((SD / np.sqrt(2)), RPop))

subplot(1,1,1)
title('Histogram of distribution of the population')
xlabel('Appendages')
ylabel('Occurence')
plt.hist(Appendages, bins=(2,4,6,8,10,12,14,16,18))
show()

subplot(1,1,1)
title('Histogram of distribution of the sample population N=2')
xlabel('Appendages')
ylabel('Occurence')
plt.hist(C2M,bins=(2,4,6,8,10,12,14,16,18))
plt.show()

subplot(1,1,1)
title('Histogram of distribution of the sample population N=4')
xlabel('Appendages')
ylabel('Occurence')
plt.hist(C4M,bins=(2,4,6,8,10,12,14,16,18))
plt.show()