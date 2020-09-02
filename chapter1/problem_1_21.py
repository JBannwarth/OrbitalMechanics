""" Orbital Mechanics for Engineering Students Problem 1.21
Question:
Numerically solve the system
    xDot + 0.5*y - z = 0
    -0.5*x + yDot + 1/sqrt(2)*z = 0
    0.5*x - 1/sqrt(2)*y + zDot = 0
for x, y, and z at t = 20, if the initial conditions at t=0 are:
    - x = 1
    - y = z = 0
Note: the answer in the book is likely wrong, I cannot see anything wrong
with my working yet it yields a different answer.
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from numerical_solvers import SolveRKF45, SolveRK14


# Differential equations
def Rates(t, Y):
    F = np.zeros(Y.shape)
    F[0] = -0.5*Y[1] + Y[2]
    F[1] = 0.5*Y[0] - Y[2]/np.sqrt(2.)
    F[2] = -0.5*Y[0] + Y[1]/np.sqrt(2.)
    return F


# Title
print("Orbital Mechanics for Engineering Students Problem 1.21")

# Parameters
tSpan = np.array([0., 20.])
Y0 = np.array([1., 0., 0.])

# Solve numerically
y, t = SolveRKF45(Rates, Y0, tSpan)
y, t = SolveRK14(Rates, Y0, tMax=20, h=1e-4)

# Show answer
print(f"x({t[-1]:.3f}) = {y[-1,0]:.3f}")
print(f"y({t[-1]:.3f}) = {y[-1,1]:.3f}")
print(f"z({t[-1]:.3f}) = {y[-1,2]:.3f}")

# Plot answer
plt.figure()
plt.plot(t, y[:, 0], label="x")
plt.plot(t, y[:, 1], label="y")
plt.plot(t, y[:, 2], label="z")
plt.xlabel("Time (-)")
plt.ylabel("Value (-)")
plt.legend()
plt.show()
