import numpy as np

#Constants
M = 1 #Mass in kg
L = 0.3 #Span
I = 1 #MOI

#state = [x, y, phi, x', y', phi']
x = np.array([[0, 0, 0, 0, 0, 0]])

#input = [u1, u2, g]
u = np.array([[0, 0, 0]])
#u1 = F1 + F2 = thrust total
#u2 = (L/2) * (F1 - F2) = moment 


#Dynamics matrix
A = np.array([[0, 0, 0, 1, 0, 0],
              [0, 0, 0, 0, 1, 0],
              [0, 0, 0, 0, 0, 1],
              [0, 0, -9.8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0]])

#Input matrix
B = np.array([[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [0, 0, 0],
              [1/m, 0, -1],
              [0, 1/I, 0]])


