import numpy as np
import matplotlib.pyplot as plt

def svd_LeastSquares(A, b):

    U, s, V = np.linalg.svd(A)
    
    r = [0.0, 0.0]
    r += (1/s[0]) * (U[:,0].T*b) * (V[:,0].T) 
    r += (1/s[1]) * (U[:,1].T*b) * (V[:,1].T)
    
    print '\nUnitary Matrix:'
    print U
    print '\nRectangular Diagonal Matrix:'
    print s
    print '\nConjugate transpose of the n by n unitary matrix V:'
    print V

    return r

'''
Plots the linear regression line,
Or really any array as a line
'''
def plotLinearRegression(fit):

    x = []
    y = []
    for i in range(len(fit)):
        x.append(fit[i][0])
        y.append(fit[i][1])
    plt.plot(x, y, 'g', label='Linear Regression', linewidth=2)

'''
Plots various points given an input array
'''
def plotPoints(points):
    
    x = []
    y = []
    for i in range(len(points)):
        x.append(points[i][0])
        y.append(points[i][1])

    plt.plot(x, y,'ro')

A = np.matrix([[0, 1], [1, 1], [2, 1], [3, 1],\
[4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1],\
[10, 1], [11, 1], [12, 1], [13, 1], [14, 1]])

b = np.matrix([[2.2], [2.2], [1], [3], [3], [4], [3], [6],\
[6], [7], [11], [12], [14], [10], [11]])

print "\nOriginal Matrix:\n"
print A

M = svd_LeastSquares(A, b)
print "\nSVD Matrix:\n"
print M
print ''

fit = []
for i in range(len(A)):
    fit.append([A[i, 0], A[i, 0] * M[0, 0] + M[0, 1]])

points = []
for i in range(len(A)):
    points.append([A[i, 0], b[i, 0]])

plotPoints(points)
plotLinearRegression(fit)
plt.title('Linear Regression Using SVD')
plt.show()
