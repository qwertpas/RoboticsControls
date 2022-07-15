import numpy as np
import matplotlib.pyplot as plt
import random as rnd

pos = 0
velo = 2

maxVariance = 2

alpha = 0.2
beta = 0.1

xnn1 = 0
xnn = 0

xnn_dot = 0
xnn1_dot = 0

value = np.array([]) #position real
measures = np.array([]) #measure distance
filtered = np.array([]) #estimated distance
t = np.array([]) #time

for i in range(1, 30):
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
