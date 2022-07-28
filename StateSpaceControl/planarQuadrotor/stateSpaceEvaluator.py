import stateSpaceModel as ssm
import numpy as np
from scipy.linalg import expm, sinm, cosm
import jacobianDrone as jd

np.set_printoptions(suppress=True)

def step(x, u):
    jacobianMatrix = np.array(jd.jacob(x[0, 0], x[1, 0], x[2, 0], u[0, 0], u[1, 0], u[2, 0]))

    #print(jacobianMatrix[:3, :3])
    #print(jacobianMatrix[:3, 3:])

    ssm.A[3:, :3] = jacobianMatrix[:3, :3]
    ssm.B[3:, :3] = jacobianMatrix[:3, 3:]

    tmp = np.empty ((9, 9))

    tmp[:6, :6] = ssm.A
    tmp[:6, 6:] = ssm.B

    tmp = expm(tmp * ssm.dt)

    Ad = tmp[:6, :6]
    Bd = tmp[:6, 6:]

    return Ad @ x + Bd @ u


