""" Orbital Mechanics for Engineering Students Example 1.19
Question:
Solve
    xDDot + 2*zeta*omegaN*xDot + omegaN**2*x = F0/m*sin(omega*t)
numerically using Heun's method. Use two different time steps, h = 1s and
h = 0.1 s and compare the results.
Parameter values:
    - m = 1 kg
    - omegaN = 1 rad/s
    - zeta = 0.03
    - F0 = 1 N
    - omega = 0.4 rad/s
Initial conditions:
    x = xDot = 0
Written by: J.X.J. Bannwarth
"""
import numpy as np
import matplotlib.pyplot as plt
from orbitutils.solvers import heun
from example_1_18 import Rates, CartSystemExactResponse

# Title
print("Orbital Mechanics for Engineering Students Example 1.19")

# Set-up
Y0 = np.array([0., 0.])
h = [1., 0.1]
tMax = 110.

# Solve equation
y1,  t1 = heun(Rates, Y0, tMax, h[0])
y01, t01 = heun(Rates, Y0, tMax, h[1])
xExact = CartSystemExactResponse(t01)

# Plot results
fig = plt.figure()
plt.grid()
plt.plot(t1, y1[:, 0], color="red", label=f"h = {h[0]}")
plt.plot(t01, y01[:, 0], color="black", label=f"h = {h[1]}")
plt.plot(t01, xExact, "--", color="green", label=f"Analytical")
plt.xlabel("Time (s)")
plt.ylabel("$x$ (m)")
plt.legend()
plt.xlim((0, 110))
plt.ylim((-2, 2))
plt.tight_layout()
plt.show()
