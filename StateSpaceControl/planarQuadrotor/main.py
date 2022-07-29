import stateSpaceEvaluator as sse
import numpy as np
import stateSpaceModel as ssm
import matplotlib.pyplot as plt

xn = ssm.x

state = np.array([[0], [0], [-np.pi/4], [0], [0], [0]])

X, Y, P = [ssm.x[0, 0]], [ssm.x[1, 0]], [ssm.x[2, 0]]
X_dots, Y_dots, P_dots = [], [], []

for i in range(1, 100):
    xn = sse.step(xn, ssm.u)
    state = state + (xn * ssm.dt)
    X = np.append(X, state[0, 0])
    Y = np.append(Y, state[1, 0])
    P = np.append(P, state[2, 0])

    X_dots.append(state[3, 0])
    Y_dots.append(state[4, 0])
    P_dots.append(state[5, 0])

    # plt.plot(X, Y, marker="o", markerfacecolor="r")

    # plt.xlim([-9, 2])
    # plt.ylim([-9, 2])
    # plt.draw()
    # plt.pause(0.02)

plt.scatter(X, Y)
plt.quiver(X, Y, -np.sin(P), np.cos(P), alpha=0.5)

fig, axs = plt.subplots(3, 1, sharex=True)
axs[0].plot(X, label='x')
axs[0].plot(Y, label='y')
axs[1].plot(P/(2*np.pi), label='rotation')
axs[2].plot(X_dots, label='x_dot')
axs[2].plot(Y_dots, label='y_dot')
for ax in axs:
    ax.legend()

plt.show()
