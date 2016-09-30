#Exercise 2.2
from scipy.io import loadmat
import numpy as np
from pylab import *

Zip = loadmat('Data/zipdata.mat')['traindata']
X = matrix(Zip[:,1:])
y = matrix(Zip[:,0])
tmp = []

for i in range(0, len(Zip)):
    if(y.item(i) < 2 or y.item(i) > 9):
        tmp.append(X[i])
        

for i in range(0, 10):
    subplot(1,1,1);
    I = reshape(tmp[i],(16,16))
    imshow(I, extent=(0,16,0,16), cmap=cm.gray_r);
    title('Digit {} as an image' .format(i));
    show()