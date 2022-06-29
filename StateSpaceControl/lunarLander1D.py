import numpy as np
from scipy.linalg import expm, sinm, cosm
import matplotlib.pyplot as plt

#Pendulum
A = np.array([[0, 1],
              [0, 0]])

#A = np.array([[1, 1], [1, 2]])

B = np.array([[0],
              [1]])

x = np.array([[3],
              [0]])

u = np.array([[-1]])

os = np.array([3])
ss = np.array([0])

r = np.array([[0], [0]])

Q = [[1.0, 0], [0, 1.0]]

R = [[0.2]]


for i in range(0, 50):
    tmp = np.empty((3, 3))

    tmp[:2, :2] = A
    tmp[:2, 2:] = B

    tmp = expm(tmp*0.1)

    error = np.subtract(r, x);

    Ad = tmp[np.ix_([0, 1], [0, 1])]
    Bd = tmp[np.ix_([0, 1], [2])]

    x = np.add(np.matmul(Ad, x), np.matmul(Bd, u))
    os=np.append(os, x[0, 0])
    ss=np.append(ss, x[1, 0])


    plt.plot(ss, os, marker="o", markerfacecolor="r")
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])
    plt.draw()
    plt.pause(0.03)

plt.show()

