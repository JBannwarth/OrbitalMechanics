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

# Title
print("Orbital Mechanics for Engineering Students Example 1.19")
