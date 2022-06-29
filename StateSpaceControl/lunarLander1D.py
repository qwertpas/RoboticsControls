import numpy as np
from scipy.linalg import expm, sinm, cosm
import matplotlib.pyplot as plt
import scipy.linalg as LA

#Pendulum
A = np.array([[0, 1],
              [0, 0]])

#A = np.array([[1, 1], [1, 2]])

B = np.array([[0],
              [1]])

x = np.array([[3],
              [0]])

u = np.array([[-0.5]])

os = np.array([3])

ss = np.array([0])

r = np.array([[0],
              [0]])

Q = [[1.0, 0],
     [0, 0.2]]

R = [[0.0]]


for i in range(0, 100):
    tmp = np.empty((3, 3))

    tmp[:2, :2] = A
    tmp[:2, 2:] = B

    tmp = expm(tmp*0.1)

    error = np.subtract(x, r);

    #Start LQR
    n = 50

    P = [None] * (n+1)

    Qf = Q
    P[n] = Qf

    for i in range(n, 0, -1):
        P[i-1] = Q + A.T @ P[i] @ A - (A.T @ P[i] @ B) @ np.linalg.pinv(R + B.T @ P[i] @ B) @ (B.T @ P[i] @ A)
        #print(P[i-1], "\n")
        #P[i-1] = LA.solve_discrete_are(A, B, Q, R, s=P[i])

    K  = [None] * n
    uS = [None] * n


    for i in range(n):
        K[i] = -np.linalg.pinv(R + B.T @ P[i+1] @ B) @ B.T @ P[i+1] @ A
        print("P", P[i+1])
        uS[i] = K[i] @ error
    #uS[n-1] is optimial input

    #End LQR

    Ad = tmp[np.ix_([0, 1], [0, 1])]
    Bd = tmp[np.ix_([0, 1], [2])]

    x = np.add(np.matmul(Ad, x), np.matmul(Bd, uS[n-1]))
    os=np.append(os, x[0, 0])
    ss=np.append(ss, x[1, 0])


    plt.plot(ss, os, marker="o", markerfacecolor="r")
    plt.xlim([-4, 4])
    plt.ylim([-4, 4])
    plt.draw()
    plt.pause(0.03)

plt.show()

