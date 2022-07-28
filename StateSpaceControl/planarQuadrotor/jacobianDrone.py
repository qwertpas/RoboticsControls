import casadi as ca
import numpy as np
import stateSpaceModel as ssm

x = ca.MX.sym('x')
y = ca.MX.sym('y')
p = ca.MX.sym('p')
u1 = ca.MX.sym('u1')
u2 = ca.MX.sym('u2')
g = ca.MX.sym('g')

m = ssm.M
I = ssm.I

f = ca.Function('f',
                    [x, y, p, u1, u2, g],
                    [
                        -u1 * ca.sin(p) / m,
                        u1 * ca.cos(p) / m - g,
                        u2/I
                    ],
                    ['x', 'y', 'p', 'u1', 'u2', 'g'],
                    ['xdd', 'ydd', 'pdd']
                )

jac = f.jacobian()

def jacob(x, y, p, u1, u2, g):
    return jac(x, y, p, u1, u2, g, 0, 0, 0)
