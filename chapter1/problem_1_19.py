""" Orbital Mechanics for Engineering Students Problem 1.19
Question:
Numerically solve the forth order-differential equation
    d^4y/dt^4 + 3*d^2y/dt^2 - 4*dy/dt - 12*y = 0
for y at t = 20, if the initial conditions at t=0 are:
    - y = 0
    - dy/dt = d^2y/dt^2 = 0
Note: the question has a typo, and gives
    3*d^3y/dt^3
instead of
    3*d^2y/dt^2
Written by: J.X.J. Bannwarth
"""
import numpy as np
from orbitutils.solvers import rkf45


# Differential equations
def rates(t, Y):
    F = np.zeros(Y.shape)
    F[0] = Y[1]
    F[1] = Y[2]
    F[2] = - 3.*Y[2] + 4.*Y[1] + 12*Y[0] + t*np.exp(2.*t)
    return F


# Title
print("Orbital Mechanics for Engineering Students Problem 1.19")

# Parameters
tSpan = np.array([0., 3.])
Y0 = np.array([0., 0., 0., 0.])

# Solve numerically
y, t = rkf45(rates, Y0, tSpan)

# Show answer
print(f"y({t[-1]:.3f}) = {y[-1,0]:.3f}")
