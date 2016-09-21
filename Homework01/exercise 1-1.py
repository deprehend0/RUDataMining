#Exercise 1.1
import numpy as np

x = np.array([6, 7, 8, 9, 10, 11, 12])
y = np.array([3, 7, 11, 15, 19, 23, 27])
w = np.array([1, 1, 0, 0.5, 1, 1.5, 2, 0, 0])
s = np.array([100, 98.8, 97.6, 96.4, 95.2])
z = np.array([0.7, 1.0, 1.3, 1.6, 1.9, 2.2, 2.8])

#1.1.1a
v = np.multiply(3, x) + y
print('V is: {}' .format(v))

#1.1.1b
print('Dot product fo x and y is: {}' .format(np.dot(x, y)))

#1.1.1c
t = np.multiply(np.pi, (s + 4))
print('T is: {}' .format(t))

#1.1.1d
z = z - 1
print('The new z is: {}' .format(z))

#1.1.1e
x[-4] = 4
x[-3] = 4
x[-2] = 4
x[-1] = 4
print('The new x is: {}' .format(x))

#1.1.1f
r = np.multiply(2, w) -5
print('R is: {}' .format(r))

#Exercise 1.1.2
M = np.matrix('1 2 3; 6 8 4; 6 7 5')
N = np.matrix('4 6; 7 2; 5 1')
P = np.matrix('2 5; 5 5')

#1.1.2a
A = M*N + N
print('A is: {}' .format(A))

#1.1.2b
B = np.transpose(N) * M
print('B is: {}' .format(B))

#1.1.2c
C = np.linalg.inv(P) + P
print('C is: {}' .format(C))

#1.1.2d
#It isn't possible to execute operation because it isn't possible
#to multiply a (2, 2) matrix with a (2, 3) matrix (C * B). Matrix
#C should have a column more or matrix B a row less to let this
#operation be possible.
#print(np.multiply(A, (np.multiply(C, C) + np.multiply(C, B))))
#print(np.multiply(A, np.multiply(C, np.add(C, B))))

#1.1.2e
print('Eigenvalues and vectors of M: ')
print(np.linalg.eig(M))
print('Eigenvalues and vectors of N: give an error')
#The eigenvalues and vectors of N cant be computed because the
#matrix isn't square.
print('Eigenvalues and vectors of P: ')
print(np.linalg.eig(P))