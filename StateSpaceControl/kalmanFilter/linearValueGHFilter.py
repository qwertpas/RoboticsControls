import numpy as np
import matplotlib.pyplot as plt
import random as rnd

pos = 10
velo = 4

maxVariance = 4

alpha = 0.2
beta = 0.1

xnn1 = 14
xnn = 0

xnn_dot = 0
xnn1_dot = 4

value = np.array([]) #position real
measures = np.array([]) #measure distance
filtered = np.array([]) #estimated distance
t = np.array([]) #time

for i in range(1, 10):
    pos = pos + velo
    measured = pos + (rnd.random()*2 -1)*maxVariance

    xnn = xnn1 + alpha * (measured - xnn1)
    xnn_dot = xnn1_dot + beta * ((measured - xnn1)/1)
    xnn1 = xnn + xnn_dot
    xnn1_dot = xnn_dot


    value = np.append(value, pos)
    measures = np.append(measures, measured)
    filtered = np.append(filtered, xnn)
    t = np.append(t, i)

    plt.plot(t, value)
    plt.plot(t, measures, linestyle="--")
    plt.plot(t, filtered, marker = "o", markerfacecolor="g")
    plt.draw()
    plt.pause(0.001)

plt.show()
