""" Orbital Mechanics for Engineering Students Problem 1.20
Question:
Numerically solve the second order-differential equation
    t*yDDot + t^2*yDot - 2*y = 0
for y at t = 4, if the initial conditions at t=1 are:
    - y = 0
    - yDot = 1
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from orbitutils.solvers import rkf45


# Differential equations
def Rates(t, Y):
    F = np.zeros(Y.shape)
    F[0] = Y[1]
    F[1] = 2.*Y[0]/t - t*Y[1]
    return F


# Title
print("Orbital Mechanics for Engineering Students Problem 1.20")

# Parameters
tSpan = np.array([1., 4.])
Y0 = np.array([0., 1.])

# Solve numerically
y, t = rkf45(Rates, Y0, tSpan)

# Show answer
print(f"y({t[-1]:.3f}) = {y[-1,0]:.3f}")

# Plot answer
plt.figure()
plt.plot(t, y[:, 0], label="y")
plt.plot(t, y[:, 1], label="yDot")
plt.xlabel("Time (-)")
plt.ylabel("Value (-)")
plt.legend()
plt.show()
