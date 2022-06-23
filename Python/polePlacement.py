import numpy as np
from scipy.linalg import expm, sinm, cosm
import matplotlib.pyplot as plt
import scipy.linalg as LA

A = np.array([[0, 1],
              [-2, -0.4]])

#A = np.array([[1, 1], [1, 2]])

B = np.array([[0],
              [1]])

x = np.array([[3.14/2],
              [0]])

u = np.array([[0]])
K = np.array([[-1.5, -2.1]]) #gain matrix/controller
r = np.array([[-2, 0]]) #goal state

os = np.array([3.14/2])
ss = np.array([0])

print(LA.eigvals(A))

for i in range(0, 50):
    tmp = np.empty((3, 3))

    tmp[:2, :2] = A
    tmp[:2, 2:] = B

    tmp = expm(tmp*0.1)

    Ad = tmp[np.ix_([0, 1], [0, 1])]
    Bd = tmp[np.ix_([0, 1], [2])]

    x = np.add(np.matmul(Ad, x), np.matmul(Bd, np.matmul(K, np.subtract(x, r))))
    #x = np.add(np.matmul(Ad,  x), np.matmul(Bd, u))
    os=np.append(os, x[0, 0])
    ss=np.append(ss, x[1, 0])


    plt.plot(ss, os, marker="o", markerfacecolor="r")
    plt.axvline(x=0, c="black", label="x=0")
    plt.axhline(y=0, c="black", label="y=0")
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])
    plt.draw()
    plt.pause(0.1)

plt.show()

