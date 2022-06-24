import numpy as np
from scipy.linalg import expm, sinm, cosm
import matplotlib.pyplot as plt

#Pendulum
A = np.array([[0, 1],
              [-2, -0.4]])

#A = np.array([[1, 1], [1, 2]])

B = np.array([[0],
              [1]])

x = np.array([[3.14/2],
              [0]])

u = np.array([[0]])

os = np.array([3.14/2])
ss = np.array([0])


for i in range(0, 150):
    tmp = np.empty((3, 3))

    tmp[:2, :2] = A
    tmp[:2, 2:] = B

    tmp = expm(tmp*0.1)

    Ad = tmp[np.ix_([0, 1], [0, 1])]
    Bd = tmp[np.ix_([0, 1], [2])]

    x = np.add(np.matmul(Ad, x), np.matmul(Bd, u))
    os=np.append(os, x[0, 0])
    ss=np.append(ss, x[1, 0])


    plt.plot(ss, os, marker="o", markerfacecolor="r")
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])
    plt.draw()
    plt.pause(0.1)

plt.show()

