import numpy as np
import matplotlib.pyplot as plt
import random as rnd

realValue = 2.0
maxVariance = 0.5
xnn1 = 0
xnn = 0

value = np.array([])
measures = np.array([])
filtered = np.array([])
t = np.array([])

for i in range(1, 100):
    measured = realValue + (rnd.random()*2 - 1) * maxVariance

    xnn = xnn1 + (1.0/i) * (measured - xnn1)
    xnn1 = xnn

    value = np.append(value, realValue)
    measures = np.append(measures, measured)
    filtered = np.append(filtered, xnn)
    t = np.append(t, i)

    plt.plot(t, value)
    plt.plot(t, measures, linestyle="--")
    plt.plot(t, filtered, marker = "o", markerfacecolor="g")
    plt.draw()
    plt.pause(0.005)

plt.show()
