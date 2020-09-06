""" Orbital Mechanics for Engineering Students Problem 1.23
Question:
Using an RK solver, solve the nonlinear Lorenz Equations:
    https://journals.ametsoc.org/jas/article/20/2/130/16956/Deterministic-Nonperiodic-Flow
    xDot = sigma(y-x)
    yDot = x(rho-z)-y
    zDot = xy - beta z
with:
    - sigma = 10
    - beta = 8/3
    - rho = 28
    - x = 0, y = 1, z = 0 at t = 0
Plot the trajectory x, y, z in three dimensions to see the Lorenz attractor.
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numerical_solvers import SolveRKF45


# Differential equations
def Rates(t, Y, sigma=10., #beta=8./3., rho=28.):
    F = np.zeros(Y.shape)
    F[0] = sigma*(Y[1]-Y[0])
    F[1] = Y[0]*(rho-Y[2]) - Y[1]
    F[2] = Y[0]*Y[1] - beta*Y[2]
    return F


# Title
print("Orbital Mechanics for Engineering Students Problem 1.23")

# Parameters
tSpan = np.array([0., 20.])
Y0 = np.array([0., 1., 0.])

# Solve numerically
y, t = SolveRKF45(Rates, Y0, tSpan)

# Plot answer
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(y[:,0],y[:,1],y[:,2], label='$Y(t)$')
ax.scatter(Y0[0],Y0[1],Y0[2], color="red", label='$Y_0$')
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.set_zlabel("$z$")
ax.set_title("Lorenz attractor")
ax.legend()
plt.show()
