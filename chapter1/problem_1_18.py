""" Orbital Mechanics for Engineering Students Problem 1.18
Question:
Numerically solve the forth order-differential equation
    d^4y/dt^4 + 2d^2y/dt^2 + y = 0
for y at t = 20, if the initial conditions at t=0 are:
    - y = 1
    - dy/dt = d^2y/dt^2 = d^3y/dt^3 = 0
Written by: J.X.J. Bannwarth
"""
import numpy as np
from numerical_solvers import SolveRKF45, SolveRK14


# Differential equations
def Rates(t, Y):
    F = np.zeros(Y.shape)
    F[0:3] = Y[1:]
    F[3] = - 2.*Y[2] - Y[0]
    return F


# Title
print("Orbital Mechanics for Engineering Students Problem 1.18")

# Parameters
tSpan = np.array([0., 20.])
Y0 = np.array([1., 0., 0., 0.])

# Solve numerically
y, t = SolveRKF45(Rates, Y0, tSpan)

# Show answer
print(f"y({t[-1]:.3f}) = {y[-1,0]:.3f}")