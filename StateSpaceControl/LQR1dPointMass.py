import numpy as np
from scipy.linalg import expm, sinm, cosm
import matplotlib.pyplot as plt
import scipy.linalg as LA

A = np.array([[0, 1],
              [0, 0]])

#A = np.array([[1, 1], [1, 2]])

B = np.array([[0],
              [1]])

x = np.array([[3],
              [0]])

u = np.array([[-0.5]])

r = np.array([[0],
              [0]])

Q = [[1.0, 0],
     [0, 0.15]]

R = [[0.015]]

os = np.array([3])

ss = np.array([0])


for i in range(0, 100):
    tmp = np.empty((3, 3))

    tmp[:2, :2] = A
    tmp[:2, 2:] = B

    tmp = expm(tmp*0.1)

    error = np.subtract(x, r);

    Ad = tmp[np.ix_([0, 1], [0, 1])]
    Bd = tmp[np.ix_([0, 1], [2])]

    #Start LQR
    n = 100

    P = [None] * (n+1)

    Qf = Q
    P[n] = Qf
    for i in range(n, 0, -1):
        P[i-1] = Q + Ad.T @ P[i] @ Ad - (Ad.T @ P[i] @ Bd) @ np.linalg.pinv(R + Bd.T @ P[i] @ Bd) @ (Bd.T @ P[i] @ Ad)

    K  = [None] * n
    uS = [None] * n


    for i in range(n):
        K[i] = -np.linalg.pinv(R + Bd.T @ P[i+1] @ Bd) @ Bd.T @ P[i+1] @ Ad
        uS[i] = K[i] @ error
        #print("K", K[i])
    #uS[n-1] is optimial input

    #End LQR
    x = np.add(np.matmul(Ad, x), np.matmul(Bd, uS[n-1]))
    os=np.append(os, x[0, 0])
    ss=np.append(ss, x[1, 0])


    plt.plot(ss, os, marker="o", markerfacecolor="r")
    plt.axvline(x=0, c="black", label="x=0")
    plt.axhline(y=0, c="black", label="y=0")
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])
    plt.draw()
    plt.pause(0.015)

plt.show()

