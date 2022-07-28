import stateSpaceEvaluator as sse
import numpy as np
import stateSpaceModel as ssm
import matplotlib.pyplot as plt

xn = ssm.x

state = np.array([[0], [0], [0], [0], [0], [0]])

X, Y = [ssm.x[0, 0]], [ssm.x[1, 0]]

for i in range(1, 100):
    xn = sse.step(xn, ssm.u)
    state = state + (xn * ssm.dt)
    X = np.append(X, state[0, 0])
    Y = np.append(Y, state[1, 0])

    plt.plot(X, Y, marker="o", markerfacecolor="r")
    plt.xlim([-15, 15])
    plt.ylim([-15, 15])
    plt.draw()
    plt.pause(0.03)


plt.show()
